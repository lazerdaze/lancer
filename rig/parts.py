# LANCER.RIG.PARTS
#
#
#
#
#

# Lancer Modules
import ults
import control
import network
import skeleton

reload(ults)
reload(control)
reload(network)
reload(skeleton)

# Maya Modules
from maya import cmds, mel

########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################

GlobalCharacterAttr = 'character'
GlobalRigRootAttr = 'rigNetworkRoot'
GlobalRigAttr = 'rigNetwork'


########################################################################################################################
#
#
#	CONTROL CLASSES
#
#
########################################################################################################################


class CONTROL(object):
	def __init__(self,
	             name='control',
	             typ=None,
	             scale=1,
	             axis=None,
	             translate=False,
	             rotate=False,
	             child=None,
	             parent=None,
	             index=0,
	             side=None,
	             label=None,
	             color=None,
	             ):
		'''
		Base Control class to be used in all parts classes.
		Created as a joint with nurbs shape node and default attributes.

		:param name:        Name of the control.
		:param typ:         Preset wire type.
		:param scale:       Scale of control. Default is 1.
		:param axis:        Forward axis of the control.
		:param translate:   Snap the position of the control to the child.
		:param rotate:      Snap the rotation of the control to the child.
		:param child:       Object that is parented to the control.
		:param parent:      Object that the control is parented to.
		:param index:       Used to determined rig priority.
		:param side:        Side of the controls origin.
		:param label:       Label of the control to determine rig type.
		:param color:       Color of control.
		'''

		self.name = name
		self.typ = typ
		self.scale = scale
		self.axis = axis if axis else [1, 0, 0]
		self.translate = translate
		self.rotate = rotate
		self.child = child
		self.parent = parent
		self.index = index
		self.side = side
		self.label = label
		self.color = color

		self.transform = None
		self.shape = None
		self.group = None

		self.create()

	def create(self):
		ctl = control.create(name=self.name,
		                     shape=self.typ,
		                     axis=self.axis,
		                     scale=self.scale,
		                     )
		self.transform = ctl[0]
		self.shape = ctl[1]
		self.setAttributes(self.transform)
		self.setLabel()
		self.setColor()
		self.createGroup()
		return

	def setAttributes(self, selected):
		for attr in ['character', 'skeletonNetwork', 'rigNetwork']:
			cmds.addAttr(selected, ln=attr, at='message')

		cmds.addAttr(selected, ln='index', at='long', dv=self.index)
		return

	def setColor(self):
		if type(self.color) is str:
			ults.presetWireColor(self.transform, self.color)
		return

	def createGroup(self):
		self.group = cmds.group(self.transform, name='{}_grp'.format(self.transform))
		if self.child:
			ults.snap(self.child, self.group, t=True, r=True)
		self.setAttributes(self.group)
		return

	def setLabel(self):
		if self.side and self.label:
			skeleton.setJointLabel(self.transform, side=self.side, typ=self.label)


class FKCONTROL(CONTROL):
	def __init__(self,
	             name='fk_control',
	             scale=1,
	             child=None,
	             parent=None,
	             index=0,
	             side=None,
	             label=None,
	             axis=None,
	             ):
		CONTROL.__init__(self,
		                 name=name,
		                 typ=control.component.circle,
		                 scale=scale,
		                 child=child,
		                 parent=parent,
		                 index=index,
		                 side=side,
		                 label=label,
		                 color=ults.component.fk,
		                 axis=axis,
		                 )


class IKCONTROL(CONTROL):
	def __init__(self,
	             name='ik_control',
	             scale=1,
	             child=None,
	             parent=None,
	             index=0,
	             side=None,
	             label=None,
	             axis=None,
	             ):
		CONTROL.__init__(self,
		                 name=name,
		                 typ=control.component.square,
		                 scale=scale,
		                 child=child,
		                 parent=parent,
		                 index=index,
		                 side=side,
		                 label=label,
		                 color=ults.component.ik,
		                 axis=axis,
		                 )


class ATTRCONTROL(CONTROL):
	def __init__(self,
	             name='attr_control',
	             scale=1,
	             child=None,
	             parent=None,
	             index=0,
	             side=None,
	             label=None,
	             axis=None,
	             ):
		CONTROL.__init__(self,
		                 name=name,
		                 typ=control.component.lollipop,
		                 scale=scale,
		                 child=child,
		                 parent=parent,
		                 index=index,
		                 side=side,
		                 label=label,
		                 color=ults.component.attr,
		                 axis=axis,
		                 )


class DETAILCONTROL(CONTROL):
	def __init__(self,
	             name='detail_control',
	             scale=1,
	             child=None,
	             parent=None,
	             index=0,
	             side=None,
	             label=None,
	             axis=None,
	             ):
		CONTROL.__init__(self,
		                 name=name,
		                 typ=control.component.locator,
		                 scale=scale,
		                 child=child,
		                 parent=parent,
		                 index=index,
		                 side=side,
		                 label=label,
		                 color=[0, 0, 1],
		                 axis=axis,
		                 )


########################################################################################################################
#
#
#	RIG COMPONENTS
#
#
########################################################################################################################


def createJointChain(objects, name='jnt'):
	jointList = []
	cmds.select(d=True)

	for obj in objects:
		jntName = '{}_{}'.format(ults.removeJointStr(str(obj)), name)
		jnt = cmds.joint(n=jntName)
		cmds.setAttr('{}.drawStyle'.format(jnt), 2)

		ults.snap(obj, jnt, t=True, r=True)

		if cmds.objectType(obj, isType='joint'):
			radius = cmds.getAttr('{0}.radius'.format(obj))
			cmds.setAttr('{}.radius'.format(jnt), radius)

		jointList.append(jnt)
		cmds.select(d=True)

	for jnt in jointList:

		i = jointList.index(jnt)
		ults.freezeTransform(jnt)

		if i != 0:
			cmds.parent(jnt, jointList[i - 1])

	return jointList


class CHAIN(object):
	def __init__(self,
	             objects,
	             controlClass,
	             name='rig_chain',
	             scale=1,
	             index=0,
	             axis=None,
	             side=None
	             ):
		self.name = name
		self.objects = objects
		self.controlClass = controlClass
		self.scale = scale
		self.index = index
		self.axis = axis
		self.side = side
		self.control = None
		self.group = None
		self.parent = None
		self.joint = None
		self.stretchGroup = None
		self.ikHandle = None
		self.ikPoleVector = None

	def create(self):

		controlList = []
		groupList = []

		for obj in self.objects:
			objectLabel = skeleton.getJointLabel(obj)
			objectSide = objectLabel[0]
			objectType = objectLabel[1]
			objectIndex = skeleton.getJointIndex(obj)

			ctl = self.controlClass(name='{}_{}'.format(ults.removeJointStr(obj), self.name),
			                        child=obj,
			                        scale=self.scale,
			                        side=objectSide,
			                        label=objectType,
			                        index=self.index if self.index else objectIndex,
			                        axis=self.axis,
			                        )
			controlList.append(ctl.transform)
			groupList.append(ctl.group)

		self.control = controlList
		self.group = groupList
		return

	def setUpGroupHierarchy(self):
		groupList = self.group
		for x in groupList:
			i = groupList.index(x)
			if i != 0:
				cmds.parent(x, self.control[i - 1])
		return

	def createParent(self):
		self.parent = ults.createGroup(self.group[0], n='{}_grp'.format(self.name))
		return

	def lockGroups(self):
		for grp in self.group:
			ults.lockAttributes(grp, hide=True)


class FKCHAIN(CHAIN):
	def __init__(self,
	             objects,
	             name=ults.component.fk,
	             scale=1,
	             axis=None,
	             side=None,
	             ):
		CHAIN.__init__(self,
		               objects=objects,
		               name=name,
		               scale=scale,
		               axis=axis,
		               controlClass=FKCONTROL,
		               side=side,
		               )
		self.create()
		self.setUpGroupHierarchy()
		self.createParent()
		self.setUpStretch()
		self.lockGroups()

	def setUpStretch(self):
		stretchGroup = []
		cmds.addAttr(self.parent, ln='stretch', m=True, at='double', k=True)
		for ctl in self.control:
			i = self.control.index(ctl)
			grp = ults.createGroup(ctl, n='{}_stretch_grp'.format(ctl))
			cmds.connectAttr('{}.stretch[{}]'.format(self.parent, i), '{}.tx'.format(grp))
			ults.lockAttributes(grp, hide=True)
			stretchGroup.append(grp)

		self.stretchGroup = stretchGroup


class IKCHAIN(CHAIN):
	def __init__(self,
	             objects,
	             name=ults.component.ik,
	             scale=1,
	             axis=None,
	             side=None,
	             ):
		CHAIN.__init__(self,
		               objects=objects,
		               controlClass=IKCONTROL,
		               name=name,
		               scale=scale,
		               axis=axis,
		               side=side,
		               )

		self.create()
		self.resetRotations()
		self.createParent()
		self.createJointChain()
		self.createIK()

	def createJointChain(self):
		self.joint = createJointChain(self.objects, name='ik_chain_jnt')
		cmds.parent(self.joint[0], self.control[0])
		return

	def resetRotations(self):
		for grp in self.group:
			for axis in ['x', 'y', 'z']:
				cmds.setAttr('{}.r{}'.format(grp, axis), 0)
		return

	def createIK(self):
		# IK Handle
		start = self.joint[0]
		mid = self.joint[1]
		end = self.joint[2]
		self.ikHandle = cmds.ikHandle(name='{}_ikHandle'.format(self.name),
		                              sj=start,
		                              ee=end,
		                              sol='ikRPsolver')[0]

		cmds.parent(self.ikHandle, self.control[-1])
		cmds.orientConstraint(self.ikHandle, end, mo=True)
		cmds.setAttr('{}.v'.format(self.ikHandle), 0)

		# Pole Vector
		pvPos = ults.getPoleVectorPosition(start, mid, end)
		cmds.xform(self.control[1], ws=True, t=pvPos)
		poleVector = ults.createPoleVector(self.ikHandle, self.control[1], mid)
		poleVectorCurve = poleVector.curve
		cmds.parent(poleVectorCurve, self.parent)
		ults.zeroAttrs(poleVectorCurve)
		return

	def createStretch(self):
		return


class RIBBONCHAIN(CHAIN):
	def __init__(self):
		pass


########################################################################################################################
#
#
#	BASE CLASS
#
#
########################################################################################################################


class BASE(object):
	def __init__(self,
	             start=None,
	             mid=None,
	             end=None,
	             name='base',
	             fkName=ults.component.fk,
	             ikName=ults.component.ik,
	             scale=1,
	             axis=None,
	             side=None,
	             index=0,
	             networkRoot=None,
	             ):
		'''
		:param start:
		:param mid:
		:param end:
		:param name:
		:param fkName:
		:param ikName:
		:param scale:
		:param axis:
		:param side:
		:param index:
		:param networkRoot:
		'''
		self.start = start
		self.mid = mid
		self.end = end
		self.objects = [start, mid, end]
		self.name = name
		self.fkName = fkName
		self.ikName = ikName
		self.scale = scale
		self.axis = axis
		self.side = side
		self.index = index

		self.fkControl = None
		self.fkGroup = None
		self.fkPoleVector = None
		self.fkParent = None

		self.ikJoint = None
		self.ikControl = None
		self.ikGroup = None
		self.ikHandle = None
		self.ikPoleVector = None
		self.ikParent = None

		self.attrControl = None
		self.attrGroup = None

		self.parent = None
		self.network = None
		self.networkRoot = networkRoot
		self.set = None

	def __str__(self):
		print ''
		for x in sorted(vars(self).iterkeys()):
			print '{}: {}'.format(x, vars(self)[x])
		return str()

	def createFKChain(self):
		fk = FKCHAIN(self.objects,
		             name=self.fkName,
		             scale=self.scale,
		             axis=self.axis,
		             side=self.side,
		             )

		self.fkControl = fk.control
		self.fkGroup = fk.group
		self.fkParent = fk.parent
		return

	def createIKChain(self):
		ik = IKCHAIN(self.objects,
		             name=self.ikName,
		             scale=self.scale,
		             axis=self.axis,
		             side=self.side,
		             )

		self.ikJoint = ik.joint
		self.ikControl = ik.control
		self.ikGroup = ik.group
		self.ikHandle = ik.ikHandle
		self.ikPoleVector = ik.ikPoleVector
		self.ikParent = ik.parent
		return

	def createFKPoleVector(self):
		fkPoleVector = cmds.group(n=self.createName('_FKPoleVector_null'), em=True)
		ults.snap(self.ikControl[1], fkPoleVector, t=True, r=True)
		cmds.parent(fkPoleVector, self.fkControl[1])
		self.fkPoleVector = fkPoleVector
		return

	def createAttrControl(self):
		ctl = ATTRCONTROL(name='{}_attr_ctl'.format(self.name),
		                  child=self.end,
		                  scale=self.scale,
		                  side=self.side,
		                  axis=self.axis,
		                  )

		self.attrControl = ctl.transform
		self.attrGroup = ctl.group
		cmds.parent(self.attrGroup, self.end)
		ults.lockAttributes(self.attrControl, hide=True)
		return

	def createFKIKChain(self):
		self.createFKChain()
		self.createIKChain()
		self.createFKPoleVector()
		self.createAttrControl()
		self.createFKIKConnections()
		self.createParent()
		self.createSet(self.fkControl + self.ikControl + [self.attrControl])
		return

	def createParent(self):
		self.parent = cmds.group(n='{}_grp'.format(self.name), em=True)
		ults.snap(self.start, self.parent, t=True, r=True)
		return

	def createFKIKConnections(self):
		attrName = 'fkik'
		fkik = ults.createFKIK(obj=self.objects,
		                       fk=self.fkControl,
		                       ik=self.ikJoint,
		                       ctl=self.attrControl,
		                       n=attrName,
		                       )

		for grp in self.fkGroup:
			i = self.fkGroup.index(grp)
			cmds.setAttr('{}.v'.format(grp), lock=False)
			cmds.connectAttr('{}.outputX'.format(fkik[1][i]), '{}.v'.format(grp), f=True)

		for grp in self.ikGroup:
			cmds.setAttr('{}.v'.format(grp), lock=False)
			cmds.connectAttr('{}.{}'.format(self.attrControl, attrName), '{}.v'.format(grp), f=True)
		return

	def createNetwork(self, typ):
		node = cmds.createNode('network', n='{}_network'.format(self.name))
		cmds.addAttr(node, ln='type', dt='string')
		ults.addSideAttr(node)
		cmds.addAttr(node, ln='index', at='long')
		cmds.setAttr('{}.type'.format(node), typ, type='string', lock=True)
		cmds.setAttr('{}.index'.format(node), self.index)
		ults.setEnumByString(node, 'side', self.side)
		cmds.addAttr(node, ln='children', dt='string')
		self.connectToRoot(node)
		self.network = node
		return

	def createSet(self, objs):
		self.set = ults.createSet(objs,
		                          n='{}_control_set'.format(self.name))
		return

	def connectToNetwork(self, obj, name):
		network = self.network
		attrName = GlobalRigAttr
		objAttr = '{}.{}'.format(obj, attrName)
		networkAttr = '{}.{}'.format(network, name)

		if not cmds.attributeQuery(attrName, node=obj, ex=True):
			cmds.addAttr(obj, ln=attrName, at='message')

		if cmds.attributeQuery(name, node=network, ex=True):
			if cmds.attributeQuery(name, node=network, m=True):
				mList = cmds.listAttr('{}.{}'.format(network, name), m=True)
				if mList:
					i = mList.index(mList[-1]) + 1
				else:
					i = 0

				ults.addIndexValue(obj, i)
				networkAttr = '{}.{}[{}]'.format(network, name, i)
		else:
			cmds.addAttr(network, ln=name, at='message')

		cmds.connectAttr(networkAttr, objAttr, force=True)
		self.connectToRoot(obj)
		return

	def connectToRoot(self, obj):
		attrName = GlobalRigRootAttr
		if self.networkRoot:
			if not cmds.attributeQuery(attrName, node=obj, ex=True):
				cmds.addAttr(obj, ln=attrName, at='message')
			if not network.getConnectedObj(obj, attrName):
				cmds.connectAttr('{}.children'.format(self.networkRoot), '{}.{}'.format(obj, attrName), f=True)
		return

	def multiConnectToNetwork(self, objects, name):
		attrName = GlobalRigAttr
		network = self.network

		if not cmds.attributeQuery(name, node=network, ex=True):
			cmds.addAttr(network, ln=name, dt='string', m=True)
			i = 0
		else:
			if cmds.listAttr('{}.{}'.format(network, name), m=True):
				i = int(cmds.listAttr('{}.{}'.format(network, name), m=True)[-1].split('[')[-1].split(']')[0])
			else:
				i = 0

		objects = ults.listCheck(objects)

		for x in objects:
			self.connectToRoot(x)

			if not cmds.attributeQuery(attrName, node=x, ex=True):
				cmds.addAttr(x, ln=attrName, at='message')

			cmds.connectAttr('{}.{}[{}]'.format(network, name, i), '{}.{}'.format(x, attrName), f=True)
			ults.addIndexValue(x, i)
			i += 1

		return

	def createNetworkConnections(self):
		# Parent
		if self.parent:
			self.connectToNetwork(self.parent, 'parentGroup')

		# Attr Control
		if self.attrControl:
			self.connectToNetwork(self.attrControl, 'attrControl')

		# Set
		if self.set:
			self.connectToNetwork(self.set, 'set')

		# FK
		if self.fkParent:
			self.connectToNetwork(self.fkParent, 'fkParent')

		if self.fkPoleVector:
			self.connectToNetwork(self.fkPoleVector, 'fkPoleVector')

		# IK
		if self.ikParent:
			self.connectToNetwork(self.fkParent, 'ikParent')

		if self.ikPoleVector:
			self.connectToNetwork(self.fkPoleVector, 'ikPoleVector')

		if self.ikHandle:
			self.connectToNetwork(self.fkPoleVector, 'ikHandle')

		# Skeleton
		if self.objects:
			self.multiConnectToNetwork(self.objects, 'skeleton')

		# FK Control
		if self.fkControl:
			self.multiConnectToNetwork(self.fkControl, 'fkControl')

		# IK Control
		if self.ikControl:
			self.multiConnectToNetwork(self.ikControl, 'ikControl')

		return

	def cleanUp(self):
		return


########################################################################################################################
#
#
#	RIG PARTS CLASSES
#
#
########################################################################################################################


class FKIK(BASE):
	def __init__(self,
	             start,
	             mid,
	             end,
	             name='fkik',
	             ):
		BASE.__init__(self,
		              start=start,
		              mid=mid,
		              end=end,
		              name=name,
		              )

		self.createFKIKChain()
		self.createNetwork('fkik')
		self.createNetworkConnections()


class ROOT(BASE):
	def __init__(self,
	             start,
	             name='charater',
	             ):
		BASE.__init__(self,
		              start=start,
		              name=name,
		              side='Center',
		              )
		self.objects = [start]
		self.determineScale()
		self.createControls()
		self.setupGlobalScale()
		self.createParent()
		self.createSet(self.fkControl)
		self.createNetwork(typ='character')
		self.createNetworkConnections()

	def determineScale(self):
		posList = []
		children = cmds.listRelatives(self.start, ad=True)

		if children:
			for child in children:
				if cmds.objectType(child, isType='joint'):
					pos = cmds.xform(child, q=True, ws=True, rp=True)
					posList.append(pos[1])
		if posList:
			self.scale = int(max(posList) / 2)


		return

	def createControls(self):

		ctl = CONTROL(name='{}_ctl'.format(self.name),
		              typ='root',
		              scale=self.scale + 2,
		              axis=[0,0,0],
		              )

		offset = CONTROL(name='{}_offset_ctl'.format(self.name),
		              typ='center',
		              scale=self.scale,
		              axis=[0,0,0],
		              )

		rootOffset = CONTROL(name='{}_root_offset_ctl'.format(self.name),
		                 typ='circle',
		                 scale=self.scale - .8,
		                 axis=[0, 0, 0],
		                 )

		ults.presetWireColor([ctl.transform, offset.transform, rootOffset.transform], typ=ults.component.center)
		cmds.parent(rootOffset.group, offset.transform)
		cmds.parent(offset.group, ctl.transform)
		self.fkControl = [ctl.transform, offset.transform, rootOffset.transform]
		self.fkGroup = [ctl.group, offset.group, rootOffset.group]
		return

	def setupGlobalScale(self):
		globalNode = self.fkControl[0]
		attrName = 'globalScale'

		cmds.addAttr(globalNode, ln=attrName, dv=1)
		cmds.setAttr('{}.globalScale'.format(globalNode), k=False, channelBox=True)

		for axis in ['x', 'y', 'z']:
			cmds.connectAttr('{}.{}'.format(globalNode, attrName), '{}.s{}'.format(globalNode, axis))
			cmds.connectAttr('{}.{}'.format(globalNode, attrName), '{}.s{}'.format(self.objects[0], axis))
			cmds.setAttr('{}.s{}'.format(globalNode, axis), k=False, channelBox=False, lock=True)

	def createParent(self):
		self.parent = cmds.group(self.fkGroup[0], n='{}_global'.format(self.name))
		return



class COG(BASE):

	def __init__(self, selected=None, name='cog', scale=1, *args):
		super(COG, self).__init__(selected=selected, name=name, scale=scale, typ=ults.component.cog)

		if self.selected:
			self.createControls()
			self.updateNetwork()

	def determineControlScale(self):
		self.scale = cmds.xform(self.selected[0], q=True, ws=True, rp=True)[1] / 4 + 1

	def createControls(self):
		self.determineControlScale()
		self.createBindJoints()

		ctl = control(self.bindJoint, n='cog_ctl', typ='center', r=False, parent=False, scale=self.scale, nest=True)
		presetWireColor(ctl, typ=ults.component.center)

		self.fkControl = ctl
		self.control.append(ctl[0])

	def updateNetwork(self):
		self.createSet()

		if self.rootQuery.network:
			connectToNetwork(self.network, self.rootQuery.network, ults.component.cog)
			rootCtl = getConnectedObj(self.rootQuery.network, 'control[0]')
			cmds.parent(self.fkControl[1], rootCtl)

		multiConnectToNetwork(self.control, self.network, 'control')
		multiConnectToNetwork(self.bindJoint, self.network, 'bindJoint')


class HIP(BASE):

	def __init__(self, selected=None, name='hip', scale=1, *args):
		super(HIP, self).__init__(selected=selected, name=name, scale=scale, typ=ults.component.hip)

		if self.selected:
			self.createControls()
			self.updateNetwork()

	def determineControlScale(self):
		self.scale = cmds.xform(self.selected[0], q=True, ws=True, rp=True)[1] / 4

	def createControls(self):
		self.determineControlScale()
		self.createBindJoints()

		ctl = control(self.bindJoint, n='hip_ctl', typ='circle', r=False, parent=False, scale=self.scale, nest=True)
		presetWireColor(ctl, typ=ults.component.center)

		self.fkControl = ctl
		self.control.append(ctl[0])

	def updateNetwork(self):
		self.createSet()

		if self.rootQuery.network:
			connectToNetwork(self.network, self.rootQuery.network, ults.component.hip)

		if self.rootQuery.cog:
			cog = getConnectedObj(self.rootQuery.cog, 'control[0]')

			if cog:
				cmds.parent(self.fkControl[1], cog)

		multiConnectToNetwork(self.control, self.network, 'control')
		multiConnectToNetwork(self.bindJoint, self.network, 'bindJoint')


class SPINE(BASE):
	def __init__(self, selected=None, name='spine', scale=1, *args):
		super(SPINE, self).__init__(selected=selected, name=name, scale=scale, typ=ults.component.spine)

		if self.selected:
			self.createControls()
			self.updateNetwork()

	def determineControlScale(self):
		bound = estimateBoundsByJoint(self.selected[0])
		if bound:
			self.scale = bound.maxX[0]

	def createControls(self):
		self.determineControlScale()
		self.createBindJoints()
		self.createFK(self.bindJoint)

		i = 0
		for jnt in self.fkJoint:
			cmds.parentConstraint(jnt, self.bindJoint[i], mo=True)
			i += 1

	def updateNetwork(self):
		self.createSet()
		self.createFKIKNetwork()

		if self.rootQuery.network:
			connectToNetwork(self.network, self.rootQuery.network, ults.component.spine)

		if self.rootQuery.cog:
			cog = getConnectedObj(self.rootQuery.cog, 'control[0]')
			cogBind = getConnectedObj(self.rootQuery.cog, 'bindJoint[0]')

			if cog:
				cmds.parent(self.fkControl[0][1], cog)
				cmds.parent(self.bindJoint[0], cogBind)


class HEAD(BASE):
	def __init__(self, selected=None, name='head', scale=1, *args):
		super(HEAD, self).__init__(selected=selected, name=name, scale=scale, typ=ults.component.head)

		if self.selected:
			self.createControls()
			self.createFKIKNetwork()
			self.createFKIK()
			self.updateNetwork()

	def createControls(self):
		self.createBindJoints()
		self.createFK(self.bindJoint)
		cmds.parentConstraint(self.fkControl[0][0], self.bindJoint[0])
		self.createIK(self.bindJoint)

	def createIK(self, objects):
		cmds.select(d=True)

		distance = cmds.xform(objects[-1], q=True, ws=True, rp=True)[1] / 2

		ikJnt = cmds.joint(n='{}_ik_jnt'.format(removeJointStr(objects[-1])))
		cmds.setAttr('{}.v'.format(ikJnt), 0)
		ikCtl = control(n='{}_ik_ctl'.format(removeJointStr(objects[-1])), axis=[1, 0, 0], t=False, r=False)

		snap(objects[-1], ikJnt, t=True, r=True)
		snap(objects[-1], ikCtl[-1], t=True, r=False)
		cmds.xform(ikCtl[-1], ws=True, t=[0, 0, distance], r=True)

		cmds.parent(ikJnt, self.fkControl[0][0])
		makeAimVector(ikCtl[0], ikJnt)

		presetWireColor(ikCtl[0], typ=ults.component.ik)

		self.ikJoint = [ikJnt]
		self.ikControl = [ikCtl]

	def createFKIK(self):
		fkik = createFKIK(self.bindJoint[-1], self.fkJoint[-1], self.ikJoint[-1], ctl=self.fkikNetwork)
		cmds.connectAttr('{}.outputX'.format(fkik[1][0]), '{}.v'.format(self.fkControl[-1][1]))
		cmds.connectAttr('{}.{}'.format(self.fkikNetwork, fkik[2]), '{}.v'.format(self.ikControl[0][1]))

	def updateNetwork(self):
		self.createSet()

		if self.rootQuery.network:
			connectToNetwork(self.network, self.rootQuery.network, ults.component.head)

			rootCtl = getConnectedObj(self.rootQuery.network, 'control[0]')

			if rootCtl:
				cmds.parent(self.ikControl[0][1], rootCtl)

			if self.rootQuery.cog:
				cog = getConnectedObj(self.rootQuery.cog, 'control[0]')
				if cog:
					createLocalWorld(self.fkControl[-1][0], local=self.bindJoint[0], world=cog)

			if self.rootQuery.spine:
				spineFKIK = getConnectedObj(self.rootQuery.spine, 'fkikNetwork')
				spineJnt = cmds.listConnections('{}.bindJoint'.format(spineFKIK))

				if spineJnt:
					cmds.parent(self.fkControl[0][-1], self.bindJoint[0], spineJnt[-1])


class COLLAR(BASE):
	def __init__(self, selected=None, name='collar', scale=1, index=0, *args):
		super(COLLAR, self).__init__(selected=selected, name=name, scale=scale, index=index,
		                             typ=ults.component.collar)

		if self.selected:
			self.bindJoint = [self.selected[0]]
			self.createControls()
			self.createFKIKNetwork(self.bindJoint[0], self.fkJoint[0], self.ikJoint[0])
			self.updateNetwork()

	def createControls(self):
		self.createFK(self.bindJoint[0])
		self.createIK(self.selected)
		self.createFKPoleVector()

	def createIK(self, selected):
		ikJnt = createJointChain(selected, typ='ik_aux', world=False)
		ikCtl = control(selected[1], n='{}_ik_ctl'.format(removeJointStr(selected[0])), axis=[1, 0, 0],
		                parent=False)
		ikHandle = cmds.ikHandle(n='collar_{}_ikHandle'.format(self.side[0].upper()), sj=ikJnt[0], ee=ikJnt[1],
		                         sol='ikSCsolver')[0]
		cmds.setAttr('{}.v'.format(ikHandle), 0)
		cmds.parent(ikHandle, ikCtl[0])

		presetWireColor(ikCtl[0], ults.component.ik)

		self.control.append(ikCtl[0])

		self.ikJoint = ikJnt
		self.ikControl = [ikCtl]
		self.ikHandle = ikHandle

	def createFKPoleVector(self):
		fkPoleVector = cmds.group(n='{}_fkPoleVector_null'.format(self.fkJoint[0]), em=True)
		snap(self.ikJoint[1], fkPoleVector, t=True, r=True)
		cmds.parent(fkPoleVector, self.fkJoint[0])

		self.fkPoleVector = fkPoleVector

	def updateNetwork(self):
		if self.rootQuery.network:
			if self.rootQuery.cog:
				cog = cmds.listConnections('{}.control[0]'.format(self.rootQuery.cog))
				if cog:
					cmds.parent(self.ikControl[0][1], cog)

			if self.rootQuery.spine:
				spineFKIK = getConnectedObj(self.rootQuery.spine, 'fkikNetwork')
				spineJnt = cmds.listConnections('{}.bindJoint'.format(spineFKIK))
				if spineFKIK:
					cmds.parent(self.fkControl[0][1], self.ikJoint[0], spineJnt[-1])


class ARM(BASE):
	def __init__(self, selected=None, name='arm', scale=1, index=0, *args):
		super(ARM, self).__init__(selected=selected, name=name, scale=scale, index=index, typ=ults.component.arm)

		if self.selected:
			self.createControls()
			self.updateNetwork()

	def createControls(self):
		self.createBindJoints()

		if len(self.bindJoint) == 4:
			self.createFKIK([self.bindJoint[1], self.bindJoint[2], self.bindJoint[3]])
			self.createCollar(self.bindJoint[0], self.bindJoint[1])

		elif len(self.bindJoint) == 3:
			self.createFKIK(self.bindJoint)

		self.createHand()

	def createCollar(self, start, end):
		collar = COLLAR([start, end])
		presetWireColor(collar.fkControl[0], ults.component.fk)
		presetWireColor(collar.ikControl[0], ults.component.ik)

		connectToNetwork(collar.network, self.network, 'collar')
		cmds.parent(self.fkControl[0][1], self.ikControl[0][1], collar.bindJoint[0])

		self.control = self.control + collar.control

		if self.rootQuery.cog:
			cog = cmds.listConnections('{}.control'.format(self.rootQuery.cog))[0]
			if cog:
				createLocalWorld(self.fkControl[0][0], local=collar.bindJoint[0], world=cog)

		cmds.addAttr(self.attrControl[0], ln='collarFKIK', dv=0, min=0, max=1, k=True)
		cmds.connectAttr('{}.collarFKIK'.format(self.attrControl[0]), '{}.FKIK'.format(collar.fkikNetwork))

	def createHand(self):
		hand = HAND(self.selected[-1])
		connectToNetwork(hand.network, self.network, 'hand')

		self.control = self.control + hand.control

		cmds.parent(hand.group, [x[0] for x in hand.bindJoint], self.bindJoint[-1])

	def updateNetwork(self):
		self.createSet()

		if self.rootQuery.network:
			connectToNetwork(self.network, self.rootQuery.network, ults.component.arm)
			rootCtl = cmds.listConnections('{}.control'.format(self.rootQuery.network))

			if rootCtl:
				cmds.parent(self.ikControl[1][1], self.ikControl[2][1], rootCtl[0])

			if self.rootQuery.spine:
				spineFKIK = getConnectedObj(self.rootQuery.spine, 'fkikNetwork')
				spineJnt = cmds.listConnections('{}.bindJoint'.format(spineFKIK))

				if spineJnt:
					cmds.parent(self.bindJoint[0], spineJnt[-1])


class LEG(BASE):
	def __init__(self, selected=None, name='leg', scale=1, *args):
		super(LEG, self).__init__(selected=selected, name=name, scale=scale, typ=ults.component.leg)

		if self.selected:
			self.createControls()
			self.updateNetwork()

	def createControls(self):
		self.createBindJoints()

		if len(self.bindJoint) == 4:
			self.createFK(self.bindJoint)
			self.createIKLeg([self.bindJoint[0], self.bindJoint[1], self.bindJoint[2]])
			self.createFKIKNetwork(self.bindJoint, self.fkJoint, self.ikJoint)
			self.createAttrControl(self.bindJoint[2])

		elif len(self.bindJoint) == 3:
			self.createFKIK(self.bindJoint)

	def createIKLeg(self, objects):
		self.createIK(objects)

		ballJnt = createJointChain(self.bindJoint[-1], typ=ults.component.ik, world=True)[0]
		cmds.parent(ballJnt, self.ikJoint[-1])
		self.ikJoint.append(ballJnt)

		self.createFoot()

	def createFoot(self):
		foot = createIKFootPivot(n=self.createName('ik_footPivot'), ik=self.ikHandle,
		                         start=self.selected[2], end=self.ikJoint[-1], ctl=self.ikControl[-1][0])

	def updateNetwork(self):
		cmds.setAttr('{}.FKIK'.format(self.attrControl[0]), 1)

		if self.rootQuery.network:
			connectToNetwork(self.network, self.rootQuery.network, ults.component.leg)
			rootCtl = cmds.listConnections('{}.control'.format(self.rootQuery.network))

			if rootCtl:
				cmds.parent(self.ikControl[1][1], self.ikControl[2][1], rootCtl[0])

			cogCtl = None
			if self.rootQuery.cog:
				cogCtl = cmds.listConnections('{}.control'.format(self.rootQuery.cog))

			if self.rootQuery.hip:
				hipCtl = cmds.listConnections('{}.control'.format(self.rootQuery.hip))
				hipBind = getConnectedObj(self.rootQuery.hip, 'bindJoint[0]')

				if hipBind:
					cmds.parent(self.bindJoint[0], hipBind)

				if hipCtl:
					cmds.parent(self.ikControl[0][1], self.fkControl[0][1], hipCtl[0])

					if cogCtl:
						createLocalWorld(self.fkControl[0][0], local=hipCtl[0], world=cogCtl[0])


class HAND(BASE):
	def __init__(self, selected=None, name='hand', scale=1, index=0, *args):
		super(HAND, self).__init__(selected=selected, name=name, scale=scale, index=0, typ=ults.component.hand)

		self.handDict = {
			ults.component.thumb: [],
			ults.component.index: [],
			ults.component.middle: [],
			ults.component.ring: [],
			ults.component.pinky: [],
		}

		if self.selected:
			self.createControls()

	def createControls(self):
		self.bindJoint = []

		cmds.addAttr(self.network, ln='finger', dt='string', m=True)

		jointChain = self.getJointOrder()
		if jointChain:
			masterGrp = cmds.group(n=self.createName('rig_fk_ctl_grp'), em=True)
			snap(self.selected[0], masterGrp, t=True, r=True)

			i = 0
			for chain in jointChain:
				fingerRig = FINGER(jointChain[chain], index=i)
				connectToNetwork(fingerRig.network, self.network, 'finger')

				self.control = self.control + fingerRig.control
				self.bindJoint.append(fingerRig.bindJoint)
				cmds.parent(fingerRig.fkControl[0][1], masterGrp)
				i += 1

			self.group = masterGrp

	def getJointOrder(self):
		return self.getJointOrderByName() if not self.getJointOrderByLabel() else self.getJointOrderByLabel()

	def getJointOrderByName(self):
		chain = handJointHierarchy(self.selected)

		handDict = self.handDict

		for x in self.handDict:
			for jnt in chain:
				for j in jnt:
					if x in j:
						handDict[x] = jnt
						break

		return handDict

	def getJointOrderByLabel(self):
		chain = handJointHierarchy(self.selected)
		handDict = self.handDict

		newChain = []
		for c in chain:
			for x in c:
				newChain.append(x)

		newChain = jointLabel(newChain).get(self.typ, self.side)

		i = 0
		for x in self.handDict:
			handDict[x] = newChain[i]
			i += 1

		return handDict


class FINGER(BASE):
	def __init__(self, selected=None, name='finger', scale=1, index=0, *args):
		super(FINGER, self).__init__(selected=selected, name=name, scale=scale, index=index,
		                             typ=ults.component.finger)

		if self.selected:
			self.createControls()
			self.updateNetwork()

	def createControls(self):
		self.determineControlScale(self.selected[-1])
		self.createBindJoints()
		self.createFK(self.bindJoint)

		i = 0
		for jnt in self.fkJoint:
			cmds.parentConstraint(jnt, self.bindJoint[i], mo=True)
			i += 1

	def determineControlScale(self, selected):
		bound = estimateBoundsByJoint(selected)
		if bound:
			self.scale = getDistance(bound.maxZ, bound.minZ) / 2

	def updateNetwork(self):
		self.createFKIKNetwork()


class NOODLE(BASE):
	def __init__(self, selected=None, name='limb', typ=ults.component.noodle, scale=1, *args):
		super(NOODLE, self).__init__(selected=selected, name=name, scale=scale, typ=typ)

		if self.selected:

			if len(self.selected) % 2 == 0:
				cmds.warning('Need Odd Number of Joints.')

			else:
				self.midNum = (len(self.selected) / 2) + 1
				self.mainControl = None

				self.createControls()
				self.createConnections()
				self.updateNetwork()

	def createControls(self):
		self.bindJoint = self.createBindJoints(self.selected)
		self.createBindControls()
		self.createMainControls()

		upperList = [self.mainControl[0][0], self.mainControl[1][0], self.mainControl[2][0]]
		lowerList = [self.mainControl[2][0], self.mainControl[3][0], self.mainControl[4][0]]

		self.upperBound = self.createCurveBound(upperList, name='upperBound_curve1', amount=self.midNum)
		self.lowerBound = self.createCurveBound(lowerList, name='lowerBound_curve1', amount=self.midNum)

	# self.smoothBound = self.createCurveBound([x[0] for x in self.mainControl], name='smoothBound_curve1',
	#                                         amount=len(self.bindJoint))

	def createBindControls(self):
		for jnt in self.bindJoint:
			ctl = control(jnt, n='{}_ctl'.format(removeJointStr(jnt)), typ='circle', axis=[1, 0, 0], nest=True,
			              parent=False)
			self.control.append(ctl)

	def createMainControls(self):
		start = self.bindJoint[0]
		mid = self.bindJoint[len(self.bindJoint) / 2]
		end = self.bindJoint[-1]

		# Main Controls

		mainCtlList = []
		i = 0
		for jnt in [start, mid, end]:
			ctl = control(jnt, n=self.createName('main_{}_ctl'.format(i)),
			              typ='square',
			              axis=[1, 0, 0], parent=False)
			mainCtlList.append(ctl)
			i += 1

		# Main Curve
		self.mainBound = self.makeCurve(selected=[x[0] for x in mainCtlList],
		                                name=self.createName('main_curve1'), amount=len(self.bindJoint))

		# Int Controls

		intCtlList = []
		i = 0
		for obj in ['upper', 'lower']:
			ctl = control(n=self.createName('{}Bound_{}_ctl'.format(obj, i)),
			              typ='square',
			              axis=[1, 0, 0])
			cmds.delete(cmds.pointConstraint(mainCtlList[i][1], mainCtlList[i + 1][1], ctl[1]))
			snap(mainCtlList[i][1], ctl[1], r=True, t=False)
			intCtlList.append(ctl)
			i += 1

		mainCtlList.insert(1, intCtlList[0])
		mainCtlList.insert(3, intCtlList[1])

		self.mainControl = mainCtlList

	def createCurveBound(self, selected, name, amount, parent=True, start=True, end=True, d=2):
		return self.makeCurve(selected,
		                      name=self.createName(name),
		                      amount=amount,
		                      parent=parent,
		                      start=start,
		                      end=end,
		                      d=d)

	def createBindJoints(self, selected):
		bindJoints = createJointChain(selected, typ=self.typ, world=True)

		i = 0
		for jnt in bindJoints:
			cmds.parentConstraint(jnt, selected[i], mo=True)
			cmds.scaleConstraint(jnt, selected[i], mo=True)
			i += 1

		return bindJoints

	class makeCurve(object):
		def __init__(self, selected, name, amount, upObject=None, parent=True, start=True, end=True, d=1):
			curve = makeNurbsCurve(selected, n=name, d=d)
			clusters = clusterCurve(curve, n='{}_cluster'.format(curve))
			null = locOnCurve(curve=curve, intLoc=amount, n='{}_null'.format(curve), upObject=upObject, start=start,
			                  end=end)
			grp = cmds.group(null, n='{}_null_grp'.format(name))

			if parent:
				i = 0
				for c in clusters:
					cmds.parent(c, selected[i])
					i += 1

			self.curve = curve
			self.cluster = clusters
			self.null = null
			self.group = grp

	def createConnections(self):

		cmds.addAttr(self.network, ln='smooth', at='double', dv=0, min=0, max=1)

		for i in [self.midNum / 2, self.midNum]:
			cmds.parent(self.mainControl[i][1], self.mainBound.null[i])

		del (self.upperBound.null)[-1]

		i = 0
		for null in self.upperBound.null + self.lowerBound.null:
			cmds.parent(self.control[i][1], null)
			i += 1

	def updateNetwork(self):
		pass


class createIKFootPivot():
	def __init__(self, n='ik_footPivot', ik=None, start=None, end=None, ctl=None, *args):

		side = getPositionSide(start)

		# Query IK

		if not ik:
			ik = queryIK(start).ikHandle

		# Create Nulls

		grpList = []

		for grp in ['inner', 'outter', 'heel', 'toe', 'ball']:
			g = cmds.group(n='{}_{}_null'.format(n, grp), em=True)
			grpList.append(g)

		i = 0
		for g in grpList:
			if i != 0:
				cmds.parent(g, grpList[i - 1])
			i += 1

		masterGrp = cmds.group(grpList[0], n='{}_grp'.format(n))

		# Toe Raise

		toeRaise = cmds.group(n='{}_toeRaise_null'.format(n), em=True)
		cmds.parent(toeRaise, grpList[3])
		grpList.append(toeRaise)

		# Pivot Locations

		snap(start, masterGrp, t=True, r=False)
		loc = cmds.spaceLocator()
		snap(end, loc, t=True, r=False)
		cmds.delete(
			cmds.aimConstraint(loc, masterGrp, aimVector=[0, 0, 1], upVector=[0, 1, 0], worldUpType='vector',
			                   worldUpVector=[0, 1, 0], skip=['x', 'z']))
		cmds.delete(loc)

		bounds = estimateBoundsByJoint(start)

		if bounds.verts:
			if side == ults.component.right:
				grpList[0], grpList[1] = grpList[1], grpList[0]

			i = 0
			for b in [bounds.minX, bounds.maxX, bounds.minZ, bounds.maxZ]:
				cmds.xform(grpList[i], ws=True, rp=[b[0], 0, b[2]])
				i += 1

		for grp in [grpList[4], grpList[5]]:
			snap(end, grp, t=True, r=False)
			freezeTransform(grp)

		# Ball Control

		ballCtl = control(end, n='{}_ball_ctl'.format(n), axis=[1, 0, 0], parent=False)
		cmds.parent(ballCtl[1], grpList[4])

		# Toe Control

		toeCtl = control(grpList[3], n='{}_toe_ctl'.format(n), axis=[1, 0, 0], parent=False)
		cmds.parent(toeCtl[1], grpList[5])
		snap(end, toeCtl[1], t=False, r=True)

		toePos = cmds.xform(grpList[5], q=True, ws=True, rp=True)
		cmds.xform(toeCtl[0], ws=True, rp=toePos)
		cmds.xform(toeCtl[1], ws=True, rp=toePos)
		cmds.orientConstraint(toeCtl[0], end, mo=True)

		# Main Control

		if not ctl:
			ctl = network(n='{}_Network_0'.format(n), typ='foot')
			cmds.setAttr('{}.side'.format(ctl), side, type='string', l=True)

			i = 0
			for null in ['inner', 'outter', 'heel', 'toe', 'ball', 'toeRaise']:
				connectToNetwork(grpList[i], ctl, '{}_pivot'.format(null))
				i += 1

		else:
			cmds.parent(masterGrp, ctl)

		addEmptyAttr(ctl, n='footPivot')

		attrDict = {
			'roll': 0,
			'heelAngle': 45,
			'ballAngle': 45,
			'toeAngle': 70,
			'toeRaise': 0,
			'bank': 0,
		}

		for attr in attrDict:
			cmds.addAttr(ctl, ln=attr, at='double', dv=attrDict[attr], k=True)

		# Control Visibility

		cmds.addAttr(ctl, ln='footControls', at='bool', k=True)
		cmds.setAttr('{}.footControls'.format(ctl), e=True, channelBox=True)

		for x in [ballCtl[1], toeCtl[1]]:
			cmds.connectAttr('{}.footControls'.format(ctl), '{}.v'.format(x))

		# Heel

		mul = cmds.createNode('multDoubleLinear')
		cmds.setAttr('{}.input2'.format(mul), -1)

		cmds.connectAttr('{}.heelAngle'.format(ctl), '{}.input1'.format(mul))

		range = cmds.createNode('setRange')
		cmds.setAttr('{}.oldMinX'.format(range), -10)

		cmds.connectAttr('{}.output'.format(mul), '{}.minX'.format(range))
		cmds.connectAttr('{}.roll'.format(ctl), '{}.valueX'.format(range))

		cmds.connectAttr('{}.outValueX'.format(range), '{}.rx'.format(grpList[2]))

		# Toe Pivot Connections

		range = cmds.createNode('setRange')
		cmds.setAttr('{}.oldMinX'.format(range), 10)
		cmds.setAttr('{}.oldMaxX'.format(range), 20)

		cmds.connectAttr('{}.toeAngle'.format(ctl), '{}.maxX'.format(range))
		cmds.connectAttr('{}.roll'.format(ctl), '{}.valueX'.format(range))

		cmds.connectAttr('{}.outValueX'.format(range), '{}.rx'.format(grpList[3]))
		cmds.connectAttr('{}.toeRaise'.format(ctl), '{}.rx'.format(toeRaise))

		# Ball Pivot Connections

		range = cmds.createNode('setRange')
		cmds.setAttr('{}.oldMaxX'.format(range), 10)
		cmds.setAttr('{}.oldMinY'.format(range), 10)
		cmds.setAttr('{}.oldMaxY'.format(range), 20)

		cmds.connectAttr('{}.ballAngle'.format(ctl), '{}.maxX'.format(range))
		cmds.connectAttr('{}.ballAngle'.format(ctl), '{}.minY'.format(range))
		cmds.connectAttr('{}.roll'.format(ctl), '{}.valueX'.format(range))
		cmds.connectAttr('{}.roll'.format(ctl), '{}.valueY'.format(range))

		con = cmds.createNode('condition')
		cmds.setAttr('{}.secondTerm'.format(con), 10)
		cmds.setAttr('{}.operation'.format(con), 2)

		cmds.connectAttr('{}.roll'.format(ctl), '{}.firstTerm'.format(con))
		cmds.connectAttr('{}.outValueX'.format(range), '{}.colorIfFalseR'.format(con))
		cmds.connectAttr('{}.outValueY'.format(range), '{}.colorIfTrueR'.format(con))
		cmds.connectAttr('{}.outColorR'.format(con), '{}.rx'.format(grpList[4]))

		# Inner / Outter

		con = cmds.createNode('condition')
		cmds.setAttr('{}.operation'.format(con), 2)

		cmds.connectAttr('{}.bank'.format(ctl), '{}.firstTerm'.format(con))
		cmds.connectAttr('{}.bank'.format(ctl), '{}.colorIfTrueR'.format(con))
		cmds.connectAttr('{}.bank'.format(ctl), '{}.colorIfFalseG'.format(con))

		cmds.connectAttr('{}.outColorR'.format(con), '{}.rz'.format(grpList[0]))
		cmds.connectAttr('{}.outColorG'.format(con), '{}.rz'.format(grpList[1]))

		# IK

		if ik:
			cmds.parent(ik, ballCtl[0])

		# Return

		# self.network = net
		self.pivot = grpList
		self.group = masterGrp
		self.control = [ballCtl, toeCtl]
		self.attr = attrDict


#########################################################################################################################
#																														#
#																														#
#	Auto Rig    																								        #
#																														#
#																														#
#########################################################################################################################

class autoRig():
	def __init__(self, characterName='character', *args):

		selected = cmds.ls(sl=True)

		if not selected:
			selected = self.queryScene()

		if selected:
			joints = cmds.listRelatives(selected[0], ad=True, type='joint')
			joints.append(selected[0])

			jointQuery = jointLabel(joints, isDebug=False)

			# BiPed
			root = jointQuery.get(ults.component.root)
			cog = jointQuery.get(ults.component.cog)
			hip = jointQuery.get(ults.component.hip)
			spine = jointQuery.get(ults.component.spine)
			head = jointQuery.get(ults.component.head)
			armLeft = jointQuery.get(ults.component.arm, ults.component.left)
			armRight = jointQuery.get(ults.component.arm, ults.component.right)
			legLeft = jointQuery.get(ults.component.leg, ults.component.left)
			legRight = jointQuery.get(ults.component.leg, ults.component.right)

			pUI = progressWindow(st='Creating Control Modules...', max=9)

			ROOT(root)
			pUI.update()

			COG(cog)
			pUI.update()

			HIP(hip)
			pUI.update()

			SPINE(spine)
			pUI.update()

			HEAD(head)
			pUI.update()

			ARM(armLeft)
			pUI.update()

			ARM(armRight)
			pUI.update()

			LEG(legLeft)
			pUI.update()

			LEG(legRight)
			pUI.update()

	def queryScene(self):
		joints = cmds.ls(type='joint')
		return jointLabel(joints).get(ults.component.root)


########################################################################################################################
#
#
#	Menu
#
#
########################################################################################################################


def menu():
	cmds.menuItem(l='Root', c=ROOT)
	cmds.menuItem(l='COG', c=COG)
	cmds.menuItem(d=True)
	cmds.menuItem(l='Spine', c=SPINE)
	cmds.menuItem(l='Neck', )
	cmds.menuItem(l='Head', c=HEAD)
	cmds.menuItem(d=True)
	cmds.menuItem(l='Collar')
	cmds.menuItem(l='Arm', c=ARM)
	cmds.menuItem(l='Hand')
	cmds.menuItem(d=True)
	cmds.menuItem(l='Hip')
	cmds.menuItem(l='Leg', c=LEG)
	cmds.menuItem(l='Foot')
	cmds.menuItem(d=True)
	cmds.menuItem(l='Tail')
	return
