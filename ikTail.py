import maya.cmds as cmds


def createJointChain(selected, *args):
    cmds.select(d=True)
    jntList = []
    i = 1
    for obj in selected:
        jnt = cmds.joint(n='ikTail_jnt{}'.format(i))
        cmds.delete(cmds.parentConstraint(obj, jnt))
        jntList.append(jnt)
        cmds.setAttr('{}.v'.format(jnt), 0)
        i += 1

    return jntList


def createCurve(objects, n='ikTail_curve1', d=3, *args):
    # 1 == Linear / 3 == Curve
    pointList = []
    for obj in objects:
        if type(obj) == str or type(obj) == unicode:
            var = cmds.xform(obj, q=True, ws=True, rp=True)
        elif type(obj) == list:
            var = obj
        pointList.append(var)
    curve = cmds.curve(n=n, d=d, p=pointList)

    shape = cmds.listRelatives(curve, shapes=True)
    cmds.rename(shape, '{}Shape'.format(curve))
    cmds.setAttr('{}.v'.format(curve), 0)

    return curve


def clusterCurve(curve, n='cluster', *args):
    clusterList = []
    curveCVs = cmds.ls('{0}.cv[:]'.format(curve), fl=True)
    i = 1
    for cv in curveCVs:
        clusterList.append(cmds.cluster(cv, n='{0}_{1}'.format(n, i))[1])
        i += 1

    for c in clusterList:
        cmds.setAttr('{}.v'.format(c), 0)

    return clusterList


def createControl(selected, *args):
    ctlList = []
    i = 1
    for obj in selected:
        ctl = cmds.circle(n='ikTail_ctl{}'.format(i), ch=False, r=.5, nr=[0, 0, 0])[0]
        cmds.delete(cmds.parentConstraint(obj, ctl))
        ctlList.append(ctl)
        i += 1
    return ctlList


def createSpline(start, end, curve, *args):
    ik = cmds.ikHandle(n='ikTail_spline', sj=start, ee=end, c=curve, sol='ikSplineSolver', ccv=False, rootOnCurve=True,
                       parentCurve=False)[0]
    cmds.setAttr('{}.v'.format(ik), 0)
    return ik


def bakeAnimation():
    pass


def createRig(parent=None, *args):
    selected = cmds.ls(sl=True)
    if selected:
        joints = createJointChain(selected)
        curve = createCurve(joints)
        controls = createControl(joints)
        clusters = clusterCurve(curve)
        spline = createSpline(joints[0], joints[-1], curve)

        controlGrp = cmds.group(controls, n='ikTail_control_grp')

        if parent:
            cmds.parentConstraint(parent, controlGrp, mo=True)

        cmds.group(joints[0], curve, controlGrp, spline, n='ikTail_grp')

        for obj in selected:
            i = selected.index(obj)
            cmds.parent(clusters[i], controls[i])
            cmds.orientConstraint(joints[i], obj, mo=True)
