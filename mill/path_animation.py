import pymel.core as pm
import millrigger.utils.name as mname
import millrigger.utils.matrix as mmtrx
import millrigger.utils.nodes.constraints as mcon
import millrigger.utils.nodes.matrixrivet as mrvt
import millrigger.objects.controls.control as mctrl

CTRL_NAME_LIST = ["C_head_CTRL",
                  "C_chest_ik_CTRL",
                  "C_hip_ik_CTRL",
                  "C_spine_ik_CTRL",
                  "?_hand_ik_CTRL",
                  "?_foot_ik_CTRL"]


class PathAnimation(object):
    def __init__(self, rig, path_crv, ctrl_names=CTRL_NAME_LIST, flow=True):
        self.rig = rig.root()
        self.path_crv = path_crv
        self.path_shape = path_crv.getShape()
        self.namespace = mname.get_namespace(self.rig.name())[0]
        self.global_ctrl = pm.ls(self.namespace + "C_global_CTRL")[0]
        self.main_ctrl = pm.ls(self.namespace + "C_main_CTRL")[0]
        self.main_ofs = pm.ls(self.namespace + "C_main_CTRL_OFS")[0]
        self.body_zero = pm.ls(self.namespace + "C_body_CTRL_ZERO")[0]

        self.ctrls = pm.ls([self.namespace + ctrl_name for ctrl_name in ctrl_names])
        self.nrb_list = []
        self.bake_set = pm.sets(self.ctrls, name=self.namespace + "bake_SET")
        self.path_set = pm.sets([], name=self.namespace + "path_SET")

        self.ctrl_grp = self.create_node("transform",
                                         name=self.namespace + "C_path_CTRLS",
                                         parent=self.namespace + "control_GRP")

        self.parts_grp = self.create_node("transform",
                                          name=self.namespace + "C_path_PARTS",
                                          parent=self.namespace + "parts_GRP")
        self.nurbs_grp = self.create_node("transform",
                                          name=self.namespace + "C_nurbs_PARTS",
                                          parent=self.parts_grp)

        self.mpath = None
        self.ffd = None
        self.ltc = None
        self.ltcb = None
        self.flow = None

        self.build(flow)

    def build(self, flow=True):
        self._cleanup_maincontrol()

        for ctrl in self.ctrls:
            # create nurbsSurface and rivet the ofs or the custom-space to it
            namer = mname.Name(ctrl.name())
            ofs = self._find_ofs(namer)
            bank_matrix = None

            # create "bank" controls for head, chest and hip
            if namer.part in ["head", "chest", "spine", "hip"]:
                ctrl_obj = self._create_bank_control(namer)
                bank_matrix = ctrl_obj.obj.matrix
                self.nrb_list.append(ctrl_obj.nurbs)

            self._create_offset_multmatrix(ctrl,
                                           ofs,
                                           bank_matrix)

            # switch to custom space if necessary
            if pm.objExists(ctrl.name() + "_SPC"):
                self._switch_space(ctrl)

        # create latice for nurbs and deform it along path
        self._create_lattice()

        # create and connect motionPath
        self._create_motionpath()

        # make lattice a "flow" object
        if flow:
            self._create_flow()

        # drive motionPath
        self._connect_to_motionpath(flow=flow)

    def create_node(self, *args, **kwargs):
        # little wrapper to add each newly created node into the "path_set"
        node = pm.createNode(*args, **kwargs)
        self.path_set.add(node)
        return node

    def _create_offset_multmatrix(self,
                                  ctrl,
                                  ofs,
                                  bank_matrix=None):
        namer = mname.Name(ctrl)
        local_space = ofs.getParent()
        rot_space = local_space
        pos_space = local_space
        has_space = pm.attributeQuery("world", n=ctrl, exists=True)
        has_split_space = pm.attributeQuery("worldRotate", n=ctrl, exists=True)
        rot_local = True
        pos_local = True

        if has_space or has_split_space:
            space_name = namer.replace(add_to_tags="world",
                                       suffix="SPACE")
            space_name2 = namer.replace(add_to_tags=["ik", "world"],
                                        suffix="SPACE")
            global_space = pm.ls(space_name, space_name2)[0]

            if has_space and ctrl.world.get() == 1:
                    rot_space = global_space
                    pos_space = global_space
                    rot_local = False
                    pos_local = False

            if pm.attributeQuery("worldRotate", n=ctrl, exists=True):
                if ctrl.worldRotate.get() == 1:
                    rot_space = global_space
                    rot_local = True

            if pm.attributeQuery("worldTranslate", n=ctrl, exists=True):
                if ctrl.worldTranslate.get() == 1:
                    pos_space = global_space
                    pos_local = True

        mdcp = self._create_matrix_rivet(ofs,
                                         rot_space,
                                         bank_matrix=bank_matrix,
                                         tags=None,
                                         namer=namer,
                                         local=rot_local)

        mdcp.outputRotate >> ofs.r

        if not has_space or not has_split_space:
            mdcp.outputTranslate >> ofs.t
            return

        pos_mdcp = self._create_matrix_rivet(ofs,
                                             pos_space,
                                             bank_matrix=bank_matrix,
                                             tags="pos",
                                             local=pos_local)
        pos_mdcp.outputTranslate >> ofs.t

    def _create_matrix_rivet(self,
                             ofs,
                             par,
                             namer=None,
                             bank_matrix=None,
                             tags=None,
                             local=True):
        namer = namer or mname.Name(ofs, tags=tags)
        # create "deformable" matrix
        nrb, nrb_mmlt = self._create_nurbs_matrix(namer, bank_matrix)

        par_mmlt = self.create_node("multMatrix",
                                    name=namer.replace(add_to_tags="parent",
                                                       suffix="multMatrix")
                                    )

        par_mdcp = self.create_node("decomposeMatrix",
                                    name=namer.replace(add_to_tags="parent",
                                                       suffix="decomposeMatrix")
                                    )
        par_mmlt.matrixSum >> par_mdcp.inputMatrix
        par_mdcp.outputTranslate >> nrb.t
        par_mdcp.outputRotate >> nrb.r
        par.worldMatrix >> par_mmlt.matrixIn[0]
        self.main_ctrl.worldInverseMatrix >> par_mmlt.matrixIn[1]

        minv = self.create_node("inverseMatrix",
                                name=namer.replace(suffix="MINV")
                                )
        mmlt = self.create_node("multMatrix",
                                name=namer.replace(suffix="multMatrix")
                                )
        mdcp = self.create_node("decomposeMatrix",
                                name=namer.replace(suffix="decomposeMatrix")
                                )

        nrb_mmlt.matrixSum >> mmlt.matrixIn[0]
        par_mmlt.matrixSum >> minv.inputMatrix
        minv.outputMatrix >> mmlt.matrixIn[1]
        mmlt.matrixSum >> mdcp.inputMatrix

        if local is False:
            par.matrix >> mmlt.matrixIn[2]

        return mdcp

    def _find_ofs(self, namer):
        # check type of control
        ofs_name = namer.replace(add_to_tags="custom",
                                 suffix="SPACE")

        if not pm.objExists(ofs_name):
            ofs_name = namer.replace(add_to_tags=["ik", "custom"],
                                     suffix="SPACE")

        if not pm.objExists(ofs_name):
            ofs_name = namer.replace(add_to_suffix="OFS")

        if not pm.objExists(ofs_name):
            raise RuntimeError("%s does not exist!" % ofs_name)

        return pm.PyNode(ofs_name)

    def _switch_space(self, ctrl):
        if pm.attributeQuery("world", n=ctrl, exists=True):
            pm.cutKey(ctrl, at="custom", cl=True)
            pm.cutKey(ctrl, at="world", cl=True)
            ctrl.world.set(0)
            ctrl.custom.set(1)
        if pm.attributeQuery("worldTranslate", n=ctrl, exists=True):
            pm.cutKey(ctrl, at="worldTranslate", cl=True)
            pm.cutKey(ctrl, at="customTranslate", cl=True)
            ctrl.worldTranslate.set(0)
            ctrl.customTranslate.set(1)
        if pm.attributeQuery("worldRotate", n=ctrl, exists=True):
            pm.cutKey(ctrl, at="worldRotate", cl=True)
            pm.cutKey(ctrl, at="customRotate", cl=True)
            ctrl.worldRotate.set(0)
            ctrl.customRotate.set(1)

    def _create_bank_control(self, namer):

        zero = pm.ls(namer.replace(suffix="CTRL_ZERO"))[0]

        full_path = zero.fullPath()
        top_zero = self.body_zero.name()
        full_path = full_path.rsplit(top_zero, 1)[1]
        hierarchy = [item for item in full_path.split("|") if item[-4:] in ["ZERO", "ROOT"]]
        hierarchy.insert(0, top_zero)
        pos_matrix = mmtrx.MMatrix()
        for item in hierarchy:
            new_matrix = mmtrx.get_matrix(pm.PyNode(item), ws=False)
            pos_matrix *= new_matrix

        # create control that follows the rig along path
        ctrl_obj = mctrl.Control(name=namer.replace(add_to_tags="bank"),
                                 matrix=None,
                                 parent=self.ctrl_grp,
                                 shape_type="pinDiamond",
                                 create_ofs=False,
                                 shape_aim="+y",
                                 shape_up="+x",
                                 size=2 * pos_matrix[13],
                                 color=21,
                                 lock_scl="xyz")

        # create nurbsSurface and rivet the control to it
        nrb = pm.nurbsPlane(name=namer.replace(tags=None, suffix="CTRL_NRB"),
                            axis=(0, 0, 1),
                            d=1,
                            lengthRatio=1,
                            patchesU=1,
                            patchesV=1,
                            width=0.1,
                            ch=False
                            )[0]
        nrb.t.set(0, 0, pos_matrix[14])
        nrb.setParent(self.nurbs_grp)

        # use a simple matrix construct instead of a rivet
        mrvt.MatrixRivet(nurbs=nrb, target=ctrl_obj.zero)

        ctrl_obj.nurbs = nrb

        return ctrl_obj

    def _create_nurbs_matrix(self, namer, bank_matrix=None):
        nrb = pm.nurbsPlane(name=namer.replace(suffix="NRB"),
                            axis=(0, 0, 1),
                            d=1,
                            lengthRatio=1,
                            patchesU=1,
                            patchesV=1,
                            width=0.01,
                            ch=False
                            )[0]
        self.nrb_list.append(nrb)
        nrb.setParent(self.nurbs_grp)

        # get info of point on nurbsSurface
        poci = self.create_node("pointOnSurfaceInfo",
                                name=namer.replace(suffix="pointOnSurfaceInfo")
                                )
        nrb.getShape().worldSpace >> poci.inputSurface
        poci.u.set(0.5)
        poci.v.set(0.5)

        # convert the info into a matrix
        mfbf = self.create_node("fourByFourMatrix",
                                name=namer.replace(suffix="fourByFourMatrix")
                                )

        for plug, row in zip(["nu", "nv", "nn", "p"], range(4)):
            for i, axis in enumerate("xyz"):
                poci.attr(plug + axis) >> mfbf.attr("i%d%d" % (row, i))

        nrb_mmlt = self.create_node("multMatrix",
                                    name=namer.replace(add_to_tags="nurbs",
                                                       suffix="multMatrix")
                                    )

        mfbf.output >> nrb_mmlt.matrixIn[0]
        self.main_ctrl.worldInverseMatrix >> nrb_mmlt.matrixIn[1]
        if bank_matrix:
            bank_matrix >> nrb_mmlt.matrixIn[2]

        return nrb, nrb_mmlt

    def _create_lattice(self):
        # create lattice for nurbs
        self.ffd, self.ltc, self.ltcb = pm.lattice(self.nrb_list,
                                                   dv=(2, 2, 10),
                                                   ldv=(4, 4, 4),
                                                   name=self.rig.name() + "_FFD",
                                                   oc=False,
                                                   pos=(0, 0, 0),
                                                   ol=1)
        self.ltc.s.set(3, 6, 6)
        self.ltcb.s.set(3, 6, 6)
        self.main_ctrl.ro >> self.ltc.ro

        # cleanup
        self.ffd.rename(self.rig.name() + "_FFD")
        self.ltc.rename(self.rig.name() + "_LTC")
        self.ltcb.rename(self.rig.name() + "_LTCB")
        self.ltc.setParent(self.parts_grp)
        self.ltcb.setParent(self.parts_grp)

    def _create_motionpath(self):
        self.mpath = self.create_node("motionPath", name=self.rig.name() + "_MPATH")
        self.mpath.follow.set(True)
        self.mpath.frontAxis.set(2)
        self.mpath.upAxis.set(1)
        self.mpath.worldUpType.set(0)
        # self.mpath.fractionMode(0)  # percentage not parameter
        self.main_ctrl.ro >> self.mpath.ro

        self.path_shape.worldSpace >> self.mpath.geometryPath
        self.mpath.fractionMode.set(1)
        self.mpath.allCoordinates >> self.ltc.t
        self.mpath.r >> self.ltc.r

        # cleanup
        self.mpath.rename(self.rig.name() + "_MPATH")

    def _create_flow(self):
        # create and clean up the flow-object
        flow = pm.flow(self.ltc,
                       divisions=[2, 2, 10],
                       localCompute=True,
                       localDivisions=[4, 4, 4],
                       objectCentered=True
                       )
        self.flow = flow[0]
        self.flow_ffd = flow[1]
        self.flow_ltc = flow[2]
        self.flow_ltcb = flow[3]

        # cleanup
        self.flow.rename(self.rig.name() + "_FLOW")
        self.flow_ffd.rename(self.rig.name() + "_FLOW_FFD")
        self.flow_ltc.rename(self.rig.name() + "_FLOW_LTC")
        self.flow_ltcb.rename(self.rig.name() + "_FLOW_LTCB")
        self.flow_ltc.setParent(self.parts_grp)
        self.flow_ltcb.setParent(self.parts_grp)

    def _connect_to_motionpath(self, flow=True):
        # convert main-control z-translation into percentage value on path
        info_crv = self.create_node("curveInfo", name=self.rig.name() + "_CRV_INFO")
        self.path_shape.worldSpace >> info_crv.inputCurve

        div = self.create_node("multiplyDivide", name=self.rig.name() + "_CRV_DIV")
        div.operation.set(2)  # divide

        self.main_ctrl.tz >> div.i1z
        info_crv.arcLength >> div.i2z
        div.oz >> self.mpath.uValue

        # use multMatrix-node to drive the ofs
        path_srt = self.create_node("transform",
                                    name=self.rig.name() + "_PATH_SRT",
                                    parent=self.parts_grp)
        path_neg = self.create_node("transform",
                                    name=self.rig.name() + "_PATH_NEG",
                                    parent=path_srt)

        # counter animation of z-translation
        mdl = self.create_node("multDoubleLinear", name=self.rig.name() + "_MDL")
        self.main_ctrl.tz >> mdl.i1
        mdl.i2.set(-1)
        mdl.o >> path_neg.tz

        # connect to motionpath
        self.mpath.allCoordinates >> path_srt.t

        if flow:
            self.mpath.r >> path_srt.r
        else:
            angl = pm.createNode("angleBetween", name=self.rig.name() + "_PATH_ANGL")
            mvec = pm.createNode("vectorProduct", name=self.rig.name() + "_PATH_MVEC")
            mvec.operation.set(3)
            mvec.normalizeOutput.set(1)
            self.mpath.orientMatrix >> mvec.matrix
            mvec.input1.set(0, 0, 1)
            mvec.ox >> angl.v2x
            mvec.oz >> angl.v2z
            angl.v2y.set(0)
            angl.v1.set(0, 0, 1)
            angl.euler >> path_srt.r
            angl.euler >> self.ltc.r

        con = mcon.create_simple_constraint(path_neg, self.main_ofs, snap=True, connect="rt")
        self.path_set.add(con)

    def _cleanup_maincontrol(self):
        # remove animation from main_ctrl and reset values
        pm.cutKey(self.main_ctrl, at=["tx", "ty", "rx", "ry", "rz"], cl=True)
        self.main_ctrl.tx.set(0)
        self.main_ctrl.ty.set(0)
        self.main_ctrl.r.set(0, 0, 0)


def bake_pathanim(obj):
    ns = mname.get_namespace(obj)[0]
    attr_list = ["tx", "ty", "tz", "rx", "ry", "rz"]
    bake_set = pm.ls(ns + "bake_SET")[0]
    path_set = pm.ls(ns + "path_SET")[0]
    ctrls = [ctrl for ctrl in bake_set]
    ctrls.append(pm.ls(ns + "C_main_CTRL")[0])
    ofs = pm.ls(ns + "C_main_CTRL_OFS")[0]
    con = ofs.inputs(type="millSimpleConstraint")

    bake_srts = []
    constr_list = []
    for ctrl in ctrls:
        srt = pm.spaceLocator(name=ctrl.name() + "_BAKE")

        constr_list.append(pm.parentConstraint(ctrl, srt, mo=False))
        bake_srts.append(srt)

    anim_start_frame = pm.playbackOptions(q=True, ast=True)
    anim_end_frame = pm.playbackOptions(q=True, aet=True)

    pm.bakeResults(bake_srts, at=attr_list, t=(anim_start_frame, anim_end_frame), simulation=True)
    pm.delete(constr_list)
    pm.cutKey(ctrls, at=attr_list, cl=True)
    pm.delete(pm.sets(path_set, q=True), con)

    # space to worldspace
    for ctrl, srt in zip(ctrls, bake_srts):
        if ctrl.hasAttr("world"):
            ctrl.world.set(1)
            ctrl.custom.set(0)
            if ctrl.hasAttr("worldTranslate"):
                ctrl.worldTranslate.set(1)
                ctrl.customTranslate.set(0)
        pm.parentConstraint(srt, ctrl, mo=False)

    pm.bakeResults(ctrls, at=attr_list, t=(anim_start_frame, anim_end_frame), simulation=True)
    pm.delete(bake_srts, bake_set)


# FIXED

# def reset_bank_controls():
#     """
#     --- Fixer in case an animator has moved their global control ---
#
#     loops through the ctrl nubs for the head, hips and ctrl and works out the difference
#     in pos z between that and the main_ctrl, then moves the nrbs patch to the right place
#
#     This should move the bank controls to the same place as the head/chest/hips ctrls
#
#     :return:
#     """
#     ctrl_nrb_names = ["C_head_CTRL_NRB", "C_chest_CTRL_NRB", "C_hip_CTRL_NRB"]
#
#     # get every ctrl_nerb from each rig
#     for ctrl_nrb_name in ctrl_nrb_names:
#         for ctrl_nrb in pm.ls("*:" + ctrl_nrb_name):
#             # get the control it drives and the main control for the namespace
#             ctrl = pm.PyNode(ctrl_nrb.name().replace("_NRB", ""))
#             main_ctrl = pm.PyNode(ctrl.namespace() + "C_main_CTRL")
#
#             # get the relative position along z
#             matrix = mmtrx.get_matrix(ctrl) * mmtrx.get_matrix(main_ctrl).inverse()
#             z_pos = matrix[-2]
#
#             # set the ctrl nrb to that at the root of the scene
#             mmtrx.set_matrix(ctrl_nrb, mmtrx.get_position_matrix(z=z_pos))
#


