# LANCER.RIG.PARTS
#
#
#
#
#

# Lancer Modules
import naming
import ults
import control
import network
import skeleton

reload(naming)
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


class component(object):
	left = 'Left'
	right = 'Right'
	center = 'Center'

	fk = 'fk'
	ik = 'ik'
	bind = 'rig'
	fkik = 'fkik'
	character = 'character'
	set = 'set'
	noodle = 'noodle'
	detail = 'detail'
	attr = 'attr'

	root = 'root'
	cog = 'cog'
	hip = 'hip'
	spine = 'spine'
	neck = 'neck'
	head = 'head'
	arm = 'arm'
	collar = 'collar'
	leg = 'leg'
	hand = 'hand'
	foot = 'foot'
	finger = 'finger'
	toe = 'toe'
	limb = 'limb'
	digit = 'digit'

	thumb = 'thumb'
	index = 'index'
	middle = 'middle'
	ring = 'ring'
	pinky = 'pinky'


########################################################################################################################
#
#
#	CONTROL CLASSES
#
#
########################################################################################################################


class CONTROL(object):
	def __init__(self,
	             name=naming.rig.control,
	             typ='circle',
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
		"""
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
		"""

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
		for attr in [naming.rig.character,
		             naming.rig.skeletonNetwork,
		             naming.rig.rigNetwork,
		             naming.rig.rigNetworkRoot,
		             ]:
			cmds.addAttr(selected, ln=attr, at='message')

		cmds.addAttr(selected, ln=naming.rig.index, at='long', dv=self.index)
		return

	def setColor(self):
		if type(self.color) is str:
			ults.presetWireColor(self.transform, self.color)
		if type(self.color) is list:
			ults.overrideColor(ults.listCheck(self.transform), color=self.color)
		return

	def createGroup(self):
		self.group = cmds.group(name=naming.convention(self.transform, naming.rig.grp), em=True)
		cmds.parent(self.transform, self.group)
		if self.child:
			ults.snap(self.child, self.group, t=True, r=True)
		self.setAttributes(self.group)
		return

	def setLabel(self):
		if self.side and self.label:
			skeleton.setJointLabel(self.transform, side=self.side.capitalize(), typ=self.label)
		elif self.side and not self.label:
			skeleton.setJointLabel(self.transform, side=self.side.capitalize(), typ='None')
		elif self.label and not self.side:
			skeleton.setJointLabel(self.transform, side='Center', typ=self.label)
		return


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
		                 typ=control.component.circleRotate,
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
		                 typ=control.component.cube,
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
		                 typ=control.component.doubleLollipop,
		                 scale=scale * 1.5,
		                 child=child,
		                 parent=parent,
		                 index=index,
		                 side=side,
		                 label=label,
		                 color=[.5, 1, 1],
		                 axis=axis,
		                 )


########################################################################################################################
#
#
#	RIG COMPONENTS
#
#
########################################################################################################################


def createJointChain(objects, name=naming.rig.jnt):
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
	             side=None,
	             ):
		self.name = name
		self.objects = objects
		self.controlClass = controlClass
		self.scale = scale
		self.index = index
		self.axis = axis
		self.side = side if side else 'Center'
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
		i = 0
		for obj in self.objects:
			objectLabel = skeleton.getJointLabel(obj)
			objectSide = objectLabel[0]
			objectType = objectLabel[1]
			objectIndex = skeleton.getJointIndex(obj)

			ctl = self.controlClass(name=naming.convention(self.name,
			                                               objectType.replace(' ',''),
			                                               objectIndex if objectIndex else i,
			                                               naming.rig.ctl,
			                                               ),
			                        child=obj,
			                        scale=self.scale,
			                        side=objectSide,
			                        label=objectType,
			                        index=self.index if self.index else objectIndex,
			                        axis=self.axis,
			                        )
			controlList.append(ctl.transform)
			groupList.append(ctl.group)
			i += 1
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
		self.parent = ults.createGroup(self.group[0], n=naming.convention(self.name, naming.rig.grp))
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
		self.createStretch()
		self.lockGroups()

	def createStretch(self):
		attrName = naming.rig.stretch
		stretchGroup = []
		cmds.addAttr(self.parent, ln=attrName, m=True, at='double', k=True)
		for ctl in self.control:
			i = self.control.index(ctl)
			grp = ults.createGroup(ctl, n=naming.convention(ctl, attrName, naming.rig.grp))
			cmds.connectAttr('{}.{}[{}]'.format(self.parent, attrName, i), '{}.tx'.format(grp))
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
		self.createStretch()
		self.lockGroups()

	def createJointChain(self):
		name = naming.convention(naming.rig.ik, naming.rig.chain, naming.rig.jnt)
		self.joint = createJointChain(self.objects, name=name)
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
		self.ikHandle = cmds.ikHandle(name=naming.convention(self.name, naming.rig.ikHandle),
		                              sj=start,
		                              ee=end,
		                              sol='ikRPsolver')[0]

		cmds.parent(self.ikHandle, self.control[-1])
		cmds.orientConstraint(self.ikHandle, end, mo=True)
		cmds.setAttr('{}.v'.format(self.ikHandle), 0)

		# Pole Vector
		pvPos = ults.getPoleVectorPosition(start, mid, end)
		cmds.xform(self.control[1], ws=True, t=pvPos)
		poleVector = ults.createPoleVector(joint=mid,
		                                   ctl=self.control[1],
		                                   ik=self.ikHandle,
		                                   name='{}_poleVector'.format(self.name),
		                                   )

		ults.swapShape(par=self.control[1],
		               child=control.wire(control.component.sphere,
		                                  scale=self.scale / 3,
		                                  ),
		               )

		ults.presetWireColor(self.control[1], ults.component.ik)
		return

	def createStretch(self):
		attrName = naming.rig.stretch
		stretchGroup = []
		cmds.addAttr(self.parent, ln=attrName, m=True, at='double', k=True)
		for joint in self.joint:
			i = self.joint.index(joint)
			grp = cmds.group(joint, em=True, n=naming.convention(joint,
			                                                     attrName,
			                                                     naming.rig.grp
			                                                     ))
			ults.snap(joint, grp, t=True, r=True)
			if i == 0:
				cmds.parent(grp, self.parent)
			else:
				cmds.parent(grp, stretchGroup[i - 1])
			origPos = cmds.getAttr('{}.tx'.format(grp))
			cmds.connectAttr('{}.tx'.format(grp), '{}.tx'.format(joint))

			add = cmds.createNode('addDoubleLinear', name='{}_add0'.format(grp))
			cmds.connectAttr('{}.{}[{}]'.format(self.parent, attrName, i), '{}.input1'.format(add), f=True)
			cmds.setAttr('{}.input2'.format(add), origPos)
			cmds.connectAttr('{}.output'.format(add), '{}.tx'.format(grp))
			ults.lockAttributes(grp, hide=True)
			stretchGroup.append(grp)

		self.stretchGroup = stretchGroup


class RIBBONCHAIN(CHAIN):
	def __init__(self,
	             objects,
	             name=naming.rig.ribbon,
	             scale=1,
	             axis=None,
	             side=None,
	             ):
		CHAIN.__init__(self,
		               objects=objects,
		               controlClass=DETAILCONTROL,
		               name=name,
		               scale=scale,
		               axis=axis,
		               side=side,
		               )
		self.create()
		self.createFlexiPlane()

	def createFlexiPlane(self):
		startObject = self.objects[0]
		endObject = self.objects[-1]
		amount = len(self.objects)
		distance = ults.getDistance(startObject, endObject)
		flex = ults.createFlexiPlane(name=self.name, amount=amount, width=distance, side=self.side)

		cmds.delete(cmds.parentConstraint(startObject, endObject, flex.parent))

		for grp in self.group:
			i = self.group.index(grp)
			cmds.parent(grp, flex.follicle[i])

		self.ribbonLocators = flex.control
		self.ribbonLocatorsGroup = flex.group
		self.parent = flex.parent
		return


class RIBBONLIMB:
	def __init__(self,
	             start,
	             mid,
	             end,
	             upperObjects,
	             midObject,
	             lowerObjects,
	             name=naming.rig.ribbon,
	             scale=1,
	             axis=None,
	             side=naming.side.left,
	             ):
		self.start = start
		self.startParent = self.getStartParent()
		self.mid = mid
		self.end = end
		self.objects = [start, mid, end]

		self.upperObjects = upperObjects
		self.lowerObjects = lowerObjects
		self.midObject = midObject
		self.name = name
		self.scale = scale
		self.axis = axis
		self.side = side
		self.color = [0, .7, .7]

		self.mainControl = []
		self.mainGroup = []

		self.upperControl = []
		self.upperGroup = []
		self.midControl = []
		self.midGroup = []
		self.lowerControl = []
		self.lowerGroup = []

		self.detailControl = []
		self.detailGroup = []

		self.upperFlexiPlane = None
		self.lowerFlexiPlane = None

		self.getScale()
		self.createMainControls()
		self.createIntermediateControls()
		self.createDetailControls()
		self.createRibbon()
		self.createHierarchy()
		self.createTwist()
		self.cleanUp()

	def getScale(self):
		self.scale = ults.getDistance(self.start, self.mid) / 3
		return

	def getStartParent(self):
		parent = cmds.listRelatives(self.start, parent=True)
		return parent[0] if parent else None

	def createMainControls(self):
		for obj in self.objects:
			i = self.objects.index(obj)
			ctl = CONTROL(name=naming.convention(self.name,
			                                     'main',
			                                     i,
			                                     naming.rig.ctl,
			                                     ),
			              typ=control.component.octagon,
			              scale=self.scale,
			              axis=self.axis,
			              child=obj,
			              color=self.color,
			              )

			cmds.parent(ctl.group, obj)
			self.mainControl.append(ctl.transform)
			self.mainGroup.append(ctl.group)

		cmds.delete(cmds.orientConstraint(self.mainGroup[0], self.mainGroup[2], self.mainGroup[1]))
		return

	def createIntermediateControls(self):
		for i in range(2):
			ctl = CONTROL(name=naming.convention(self.name,
			                                     'intermediate',
			                                     i,
			                                     naming.rig.ctl,
			                                     ),
			              typ=control.component.hexigon,
			              scale=self.scale,
			              axis=self.axis,
			              color=self.color,
			              )

			cmds.parent(ctl.group, self.objects[i])

			if i == 0:
				j = 1
				startIndex = 0
				endIndex = 1
			else:
				j = 2
				startIndex = 2
				endIndex = 3

			cmds.delete(cmds.parentConstraint(self.mainControl[startIndex], self.mainControl[endIndex], ctl.group))
			cmds.pointConstraint(self.mainControl[startIndex], self.mainControl[endIndex], ctl.group, mo=True)
			self.mainControl.insert(i + j, ctl.transform)
			self.mainGroup.insert(i + j, ctl.group)
		return

	def createDetailControls(self):
		upperIndex = len(self.upperObjects) - 1
		midIndex = upperIndex + 1
		objects = self.upperObjects + ults.listCheck(self.midObject) + self.lowerObjects
		i = 0
		for obj in objects:
			i = objects.index(obj)
			ctl = DETAILCONTROL(name=naming.convention(self.name,
			                                           'detail',
			                                           i,
			                                           naming.rig.ctl,
			                                           ),
			                    scale=self.scale,
			                    axis=self.axis,
			                    child=obj,
			                    )

			cmds.parentConstraint(ctl.transform, obj, mo=True)
			cmds.scaleConstraint(ctl.transform, obj, mo=True)

			if i < midIndex:
				self.upperControl.append(ctl.transform)
				self.upperGroup.append(ctl.group)

			elif i == midIndex:
				self.midControl.append(ctl.transform)
				self.midGroup.append(ctl.group)

			else:
				self.lowerControl.append(ctl.transform)
				self.lowerGroup.append(ctl.group)

			self.detailControl.append(ctl.transform)
			self.detailGroup.append(ctl.group)
			i += 1

		return

	def createRibbon(self):
		upper = self.createFlexiPlane(start=self.start,
		                              end=self.mid,
		                              amount=len(self.upperObjects + ults.listCheck(self.midObject)),
		                              name=naming.convention(self.name,
		                                                     'upper',
		                                                     ),
		                              )
		lower = self.createFlexiPlane(start=self.mid,
		                              end=self.end,
		                              amount=len(self.upperObjects + ults.listCheck(self.midObject)),
		                              name=naming.convention(self.name,
		                                                     'lower',
		                                                     ),
		                              )

		cmds.delete(upper.constraint, lower.constraint)

		self.upperFlexiPlane = upper
		self.lowerFlexiPlane = lower
		return

	def createHierarchy(self):
		i = 0
		for ctl in self.upperFlexiPlane.control:
			cmds.pointConstraint(self.mainControl[i], ctl)
			i += 1

		i = 2
		for ctl in self.lowerFlexiPlane.control:
			cmds.pointConstraint(self.mainControl[i], ctl)
			i += 1

		i = 0
		for grp in self.upperGroup:
			cmds.parent(grp, self.upperFlexiPlane.follicle[i])
			i += 1

		i = 1
		for grp in self.lowerGroup:
			cmds.parent(grp, self.lowerFlexiPlane.follicle[i])
			i += 1

		cmds.parent(self.midGroup[0], self.upperFlexiPlane.follicle[-1])
		cmds.orientConstraint(self.mainControl[2], self.midGroup[0], mo=True)
		cmds.orientConstraint(self.mainControl[-1], self.detailGroup[-1], mo=True)

		if self.startParent:
			cmds.parent(self.upperFlexiPlane.parent, self.startParent)
			cmds.parent(self.lowerFlexiPlane.parent, self.startParent)
		return

	def createTwist(self):
		cmds.connectAttr('{}.rx'.format(self.mainControl[0]), '{}.startTwistAmount'.format(self.upperFlexiPlane.parent))
		cmds.connectAttr('{}.rx'.format(self.mainControl[2]), '{}.endTwistAmount'.format(self.upperFlexiPlane.parent))

		cmds.connectAttr('{}.rx'.format(self.mainControl[2]), '{}.startTwistAmount'.format(self.lowerFlexiPlane.parent))
		cmds.connectAttr('{}.rx'.format(self.mainControl[-1]), '{}.endTwistAmount'.format(self.lowerFlexiPlane.parent))

		cmds.connectAttr('{}.rx'.format(self.start), '{}.endTwistAdd'.format(self.upperFlexiPlane.parent))
		cmds.connectAttr('{}.rx'.format(self.start), '{}.startTwistAdd'.format(self.lowerFlexiPlane.parent))

		add = cmds.createNode('addDoubleLinear', name='{}_lower_ribbon_add0'.format(self.name))
		cmds.connectAttr('{}.rx'.format(self.start), '{}.input1'.format(add))
		cmds.connectAttr('{}.rx'.format(self.end), '{}.input2'.format(add))
		cmds.connectAttr('{}.output'.format(add), '{}.endTwistAdd'.format(self.lowerFlexiPlane.parent))

		return

	def createFlexiPlane(self, start, end, amount, name):
		distance = ults.getDistance(start, end)
		flex = ults.createFlexiPlane(name=name,
		                             amount=amount,
		                             width=distance,
		                             side=self.side,
		                             )

		cmds.delete(cmds.parentConstraint(start, end, flex.parent))
		return flex

	def cleanUp(self):
		for obj in self.upperFlexiPlane.group + self.lowerFlexiPlane.group:
			ults.setVisibility(obj)

		for obj in self.mainControl:
			ults.lockScale(obj)

		return


########################################################################################################################
#
#
#	BASE CLASS
#
#
########################################################################################################################


class BASE(object):
	def __init__(self,
	             objects=None,
	             name=naming.rig.base,
	             fkName=None,
	             ikName=None,
	             scale=1,
	             axis=None,
	             side=None,
	             index=0,
	             networkRoot=None,
	             networkParent=None,
	             ):
		""""
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
		"""

		self.objects = ults.listCheck(objects)
		self.name = name
		self.fkName = fkName if fkName else naming.convention(name, naming.rig.fk)
		self.ikName = ikName if ikName else naming.convention(name, naming.rig.ik)

		self.scale = scale
		self.axis = axis
		self.side = side
		self.index = index

		self.fkControl = []
		self.fkGroup = []
		self.fkPoleVector = None
		self.fkParent = None

		self.ikJoint = []
		self.ikControl = []
		self.ikGroup = []
		self.ikHandle = None
		self.ikPoleVector = None
		self.ikParent = None

		self.ribbonControl = []
		self.ribbonGroup = []

		self.detailObjects = []
		self.detailControl = []
		self.detailGroup = []

		self.attrControl = None
		self.attrGroup = None

		self.parent = None
		self.network = None
		self.networkRoot = networkRoot
		self.networkParent = networkParent
		self.set = None

	def __str__(self):
		print ''
		for x in sorted(vars(self).iterkeys()):
			print '{}: {}'.format(x, vars(self)[x])
		return str()

	def createParent(self, name, child=None):
		self.parent = cmds.group(n='{}_{}'.format(self.name, name), em=True)
		if child:
			ults.snap(child, self.parent, t=True, r=True)
		return

	def parentToObjectParent(self, child, obj):
		parent = cmds.listRelatives(child, parent=True)
		if parent:
			cmds.parent(obj, parent[0])
		return

	def createDetailChain(self, objects):
		objects = ults.listCheck(objects)
		indexNum = 0
		for obj in objects:
			i = objects.index(obj)
			children = skeleton.getBindJoint(obj)

			if children:
				for child in children:
					ctl = DETAILCONTROL(name=naming.convention(self.name,
					                                           self.side.upper()[0],
					                                           self.index,
					                                           naming.rig.detail,
					                                           indexNum,
					                                           naming.rig.ctl
					                                           ),
					                    scale=self.scale,
					                    parent=None,
					                    child=child,
					                    index=i,
					                    axis=self.axis,
					                    )
					indexNum += 1
					cmds.parent(ctl.group, obj)
					cmds.parentConstraint(ctl.transform, child, mo=True)
					cmds.scaleConstraint(ctl.transform, child, mo=True)

					self.detailObjects.append(child)
					self.detailControl.append(ctl.transform)
					self.detailGroup.append(ctl.group)
		return

	def createRibbonChain(self, start, mid, end):
		upperObjects = skeleton.getBindJoint(start)
		lowerObjects = skeleton.getBindJoint(mid)

		if upperObjects and lowerObjects:
			midObjects = lowerObjects[0]
			lowerObjects.remove(lowerObjects[0])

			ribbon = RIBBONLIMB(name=naming.convention(self.name,
			                                           self.side[0].upper(),
			                                           self.index,
			                                           naming.rig.ribbon,
			                                           ),
			                    start=start,
			                    mid=mid,
			                    end=end,
			                    upperObjects=upperObjects,
			                    lowerObjects=lowerObjects,
			                    midObject=midObjects,
			                    side=self.side,
			                    )

			self.detailObjects = self.detailObjects + upperObjects + lowerObjects + ults.listCheck(midObjects)
			self.detailControl = self.detailControl + ribbon.detailControl
			self.detailGroup = self.detailGroup + ribbon.detailGroup

			self.ribbonControl = ribbon.mainControl
			self.ribbonGroup = ribbon.mainGroup

			if self.attrControl:
				attrName = ['sns', 'snsAdd']
				cmds.addAttr(self.attrControl, ln=attrName[0], min=0, max=1, dv=0, k=True)
				cmds.addAttr(self.attrControl, ln=attrName[1], k=True)

				for attr in attrName:
					cmds.connectAttr('{}.{}'.format(self.attrControl, attr),
					                 '{}.{}'.format(ribbon.upperFlexiPlane.parent, attr))
					cmds.connectAttr('{}.{}'.format(self.attrControl, attr),
					                 '{}.{}'.format(ribbon.lowerFlexiPlane.parent, attr))

		return

	def createFKChain(self, objects):
		name = naming.convention(self.name,
		                         self.side.upper()[0],
		                         self.index,
		                         naming.rig.fk,
		                         )
		fk = FKCHAIN(objects,
		             name=name,
		             scale=self.scale,
		             axis=self.axis,
		             side=self.side,
		             )
		self.parentToObjectParent(objects[0], fk.parent)
		self.fkControl = fk.control
		self.fkGroup = fk.group
		self.fkParent = fk.parent
		return

	def createIKChain(self, objects):
		name = naming.convention(self.name,
		                         self.side.upper()[0],
		                         self.index,
		                         naming.rig.ik,
		                         )
		ik = IKCHAIN(objects,
		             name=name,
		             scale=self.scale,
		             axis=self.axis,
		             side=self.side,
		             )

		self.parentToObjectParent(objects[0], ik.parent)
		self.ikJoint = ik.joint
		self.ikControl = ik.control
		self.ikGroup = ik.group
		self.ikHandle = ik.ikHandle
		self.ikPoleVector = ik.ikPoleVector
		self.ikParent = ik.parent

		return

	def createFKPoleVector(self):
		fkPoleVector = cmds.group(n=naming.convention(self.name,
		                                              self.side.upper()[0],
		                                              self.index,
		                                              naming.rig.fk,
		                                              naming.rig.poleVector,
		                                              naming.rig.null,
		                                              ),
		                          em=True)
		ults.snap(self.ikControl[1], fkPoleVector, t=True, r=True)
		cmds.parent(fkPoleVector, self.fkControl[1])
		self.fkPoleVector = fkPoleVector
		return

	def createAttrControl(self, obj):
		if self.side == 'Left':
			axis = [1, -1, 0]
		elif self.side == 'Right':
			axis = [1, 1, 0]

		if self.name == 'leg':
			if self.side == 'Left':
				axis = [1, 0, 1]
			elif self.side == 'Right':
				axis = [1, 0, -1]

		ctl = ATTRCONTROL(name=naming.convention(self.name,
		                                         self.side.upper()[0],
		                                         self.index,
		                                         naming.rig.attr,
		                                         naming.rig.ctl,
		                                         ),
		                  child=obj,
		                  scale=self.scale + .25,
		                  side=self.side,
		                  label='None',
		                  axis=axis,
		                  )

		self.attrControl = ctl.transform
		self.attrGroup = ctl.group
		cmds.parent(self.attrGroup, obj)
		ults.lockAttributes(self.attrControl, hide=True)
		return

	def createFKIKChain(self, objects):
		self.createFKChain(objects)
		self.createIKChain(objects)
		self.createFKPoleVector()
		self.createAttrControl(objects[-1])
		self.createFKIKConnections(ctl=self.attrControl)
		self.parentToRootControl(self.ikGroup[1])
		self.parentToRootControl(self.ikGroup[2])
		return

	def createFKIKConnections(self, ctl, name=naming.rig.fkik):
		# Constraints
		fkik = ults.createFKIK(obj=self.objects,
		                       fk=self.fkControl,
		                       ik=self.ikJoint,
		                       ctl=ctl,
		                       n=name,
		                       )

		# Visibility
		for grp in self.fkGroup:
			i = self.fkGroup.index(grp)
			cmds.setAttr('{}.v'.format(grp), lock=False)
			cmds.connectAttr('{}.outputX'.format(fkik[1][i]), '{}.v'.format(grp), f=True)

		for grp in self.ikGroup:
			cmds.setAttr('{}.v'.format(grp), lock=False)
			cmds.connectAttr('{}.{}'.format(self.attrControl, name), '{}.v'.format(grp), f=True)

		# Stretch
		attrName = naming.rig.stretch
		cmds.addAttr(ctl, ln=attrName, k=True)
		if self.side == 'Right':
			mult = cmds.createNode('multiplyDivide', name='{}_mult0'.format(ctl))
			axis = ['X', 'Y', 'Z']
			for ax in axis:
				cmds.setAttr('{}.input2{}'.format(mult, ax), -1)

		for i in range(1, 3, 1):
			if self.side == 'Right':
				cmds.connectAttr('{}.{}'.format(ctl, attrName),
				                 '{}.input1{}'.format(mult, axis[i]))

				cmds.connectAttr('{}.output{}'.format(mult, axis[i]),
				                 '{}.{}[{}]'.format(self.ikParent, attrName, i))
				cmds.connectAttr('{}.output{}'.format(mult, axis[i]),
				                 '{}.{}[{}]'.format(self.fkParent, attrName, i))
			else:
				cmds.connectAttr('{}.{}'.format(ctl, attrName),
				                 '{}.{}[{}]'.format(self.fkParent, attrName, i))
				cmds.connectAttr('{}.{}'.format(ctl, attrName),
				                 '{}.{}[{}]'.format(self.ikParent, attrName, i))

		return

	def createNetwork(self, typ):
		name = naming.convention(self.name,
		                         self.side.upper()[0],
		                         self.index,
		                         naming.rig.network,
		                         )

		self.network = cmds.createNode('network', n=name)
		self.addDefaultNetworkAttributes(typ)

		if self.networkParent:
			self.connectToNetworkRoot()

		if self.networkRoot:
			self.connectToNetwork(self.network, self.networkRoot, typ)
			for attr in ['jointDisplay', 'controlDisplay']:
				cmds.connectAttr('{}.{}'.format(self.networkRoot, attr), '{}.{}'.format(self.network, attr))
		return

	def addDefaultNetworkAttributes(self, typ):
		node = self.network
		cmds.addAttr(node, ln='type', dt='string')
		ults.addSideAttr(node)
		cmds.addAttr(node, ln='index', at='long')
		cmds.setAttr('{}.type'.format(node), typ, type='string', lock=True)
		cmds.setAttr('{}.index'.format(node), self.index)
		ults.setEnumByString(node, 'side', self.side)
		cmds.addAttr(node, ln='children', dt='string')
		ults.addBoolAttr(node, 'jointDisplay')
		ults.addBoolAttr(node, 'controlDisplay')
		return

	def createSet(self, objects):
		name = naming.convention(self.name,
		                         self.side.upper()[0],
		                         self.index,
		                         naming.rig.set,
		                         )

		cmds.select(d=True)
		objects = ults.listCheck(objects)
		self.set = cmds.sets(objects, name=name)

		if self.networkRoot:
			rootSet = self.getConnected(self.networkRoot, naming.rig.set)

			if cmds.objExists(str(rootSet)):
				cmds.sets(self.set, add=rootSet)
		return

	def hideObjectsAttributes(self, objects):
		objects = ults.listCheck(objects)
		for obj in objects:
			ults.hideAttributes(obj)
		return

	def connectToNetwork(self, obj, network, name):
		attrName = 'rigNetworkRoot'
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
		return

	def connectToNetworkRoot(self, obj, network):
		attrName = 'rigNetworkRoot'
		if not cmds.attributeQuery(attrName, node=obj, ex=True):
			cmds.addAttr(obj, ln=attrName, at='message')
		if not self.getConnected(obj, attrName):
			cmds.connectAttr('{}.children'.format(network), '{}.{}'.format(obj, attrName), f=True)
		return

	def multiConnectToNetwork(self, objects, network, name):
		objects = ults.listCheck(objects)
		attrName = 'rigNetwork'

		if not cmds.attributeQuery(name, node=network, ex=True):
			cmds.addAttr(network, ln=name, dt='string', m=True)
			i = 0
		else:
			if cmds.listAttr('{}.{}'.format(network, name), m=True):
				i = int(cmds.listAttr('{}.{}'.format(network, name), m=True)[-1].split('[')[-1].split(']')[0])
			else:
				i = 0

		for obj in objects:
			if self.networkRoot:
				self.connectToNetworkRoot(obj, self.networkRoot)

			if not cmds.attributeQuery(attrName, node=obj, ex=True):
				cmds.addAttr(obj, ln=attrName, at='message')

			cmds.connectAttr('{}.{}[{}]'.format(network, name, i), '{}.{}'.format(obj, attrName), f=True)
			ults.addIndexValue(obj, i)
			i += 1
		return

	def getConnected(self, obj, attr, indexValue=0):
		attrName = '{}.{}'.format(obj, attr)
		attrNameIndex = '{}.{}[{}]'.format(obj, attr, indexValue)
		if cmds.attributeQuery(attr, node=obj, ex=True):
			if cmds.attributeQuery(attr, node=obj, m=True):
				query = cmds.listConnections(attrNameIndex)
				return query[0] if query else None
			elif cmds.connectionInfo(attrName, id=True):
				query = cmds.listConnections(cmds.connectionInfo(attrName, ged=True))
				return query[0] if query else None
			else:
				query = cmds.listConnections(attrName)
				return query[0] if query else None
		else:
			return None

	def createLocalWorld(self, obj, local):
		attrName = 'localWorld'
		cogNetwork = self.getConnected(self.networkRoot, 'cog')
		cog = self.getConnected(cogNetwork, 'fkControl', 0) if cogNetwork else None

		if cog:
			ults.createLocalWorld(obj=obj,
			                      local=local,
			                      world=cog,
			                      n=attrName,
			                      )
		return

	def parentToRootControl(self, obj):
		if self.networkRoot:
			offset = self.getConnected(self.networkRoot, 'fkControl', indexValue=1)

			if offset:
				cmds.parent(obj, offset)
		return

	def createNetworkConnections(self):
		# Parent
		if self.parent:
			self.connectToNetwork(self.parent, self.network, 'parentGroup')

		# Attr Control
		if self.attrControl:
			self.connectToNetwork(self.attrControl, self.network, 'attrControl')

		# Set
		if self.set:
			self.connectToNetwork(self.set, self.network, 'set')

		# FK
		if self.fkParent:
			self.connectToNetwork(self.fkParent, self.network, 'fkParent')

		if self.fkPoleVector:
			self.connectToNetwork(self.fkPoleVector, self.network, 'fkPoleVector')

		# IK
		if self.ikParent:
			self.connectToNetwork(self.ikParent, self.network, 'ikParent')

		if self.ikPoleVector:
			self.connectToNetwork(self.ikPoleVector, self.network, 'ikPoleVector')

		if self.ikHandle:
			self.connectToNetwork(self.ikHandle, self.network, 'ikHandle')

		# Skeleton
		if self.objects:
			self.multiConnectToNetwork(self.objects, self.network, 'skeleton')
			con = cmds.createNode('condition', name='{}_jointDisplay_condition'.format(self.network))
			cmds.setAttr('{}.colorIfTrueR'.format(con), 2)
			cmds.setAttr('{}.colorIfFalseR'.format(con), 0)
			cmds.connectAttr('{}.jointDisplay'.format(self.network), '{}.firstTerm'.format(con))
			for obj in self.objects:
				cmds.connectAttr('{}.outColorR'.format(con), '{}.drawStyle'.format(obj))

			if self.detailObjects:
				self.multiConnectToNetwork(self.detailObjects, self.network, 'skeletonDetail')
				for detail in self.detailObjects:
					cmds.connectAttr('{}.outColorR'.format(con), '{}.drawStyle'.format(detail))

		# Detail Controls
		if self.detailControl:
			attrName = 'detailControlDisplay'
			self.multiConnectToNetwork(self.detailControl, self.network, 'detailControl')
			ults.addBoolAttr(self.network, attrName)

			for detail in self.detailGroup:
				cmds.connectAttr('{}.{}'.format(self.network, attrName), '{}.v'.format(detail))

			if self.ribbonControl:
				self.multiConnectToNetwork(self.ribbonControl, self.network, 'ribbonControl')

				for ribbon in self.ribbonGroup:
					cmds.connectAttr('{}.{}'.format(self.network, attrName), '{}.v'.format(ribbon))

		# FK Control
		if self.fkControl:
			self.multiConnectToNetwork(self.fkControl, self.network, 'fkControl')

		# IK Control
		if self.ikControl:
			self.multiConnectToNetwork(self.ikControl, self.network, 'ikControl')

		if self.ikJoint:
			self.multiConnectToNetwork(self.ikJoint, self.network, 'ikJoint')

		if self.attrControl:
			# Attr Display
			attrName = naming.rig.detailControlDisplay
			ults.addBoolAttr(self.attrControl, attrName)
			cmds.connectAttr('{}.{}'.format(self.attrControl, attrName), '{}.{}'.format(self.network, attrName))

			# Attr To Network FKIK
			cmds.addAttr(self.network, ln=naming.rig.fkik, min=0, max=1, dv=0)
			cmds.connectAttr('{}.{}'.format(self.attrControl, naming.rig.fkik),
			                 '{}.{}'.format(self.network, naming.rig.fkik))
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
		              objects=[start, mid, end],
		              name=name,
		              )

		self.createFKIKChain(self.objects)
		self.createNetwork(typ='fkik')
		self.createNetworkConnections()


class ROOT(BASE):
	def __init__(self,
	             root=None,
	             name='character',
	             scale=1,
	             ):
		BASE.__init__(self,
		              name=name,
		              side='Center',
		              scale=scale,
		              )
		self.root = root

		if self.root:
			self.objects = [root]
			self.getScale()

		self.createControls()
		self.createRootOffset()
		self.createSet(self.fkControl)
		self.createNetwork(typ='root')
		self.networkRoot = self.network
		self.networkParent = self.network
		self.createNetworkConnections()
		self.setupDisplayAttr()
		self.setupGlobalScale()
		self.hideGroupNodes([self.network] + self.fkGroup)

	def getScale(self):
		self.scale = int(skeleton.determineHeight(self.root) / 2)
		return

	def createControls(self):

		ctl = CONTROL(name='{}_ctl'.format(self.name),
		              typ='root',
		              scale=self.scale + 2,
		              axis=[0, 0, 0],
		              )

		offset = CONTROL(name='{}_offset_ctl'.format(self.name),
		                 typ='center',
		                 scale=self.scale,
		                 axis=[0, 0, 0],
		                 )

		ults.presetWireColor([ctl.transform, offset.transform, ], typ=ults.component.center)
		cmds.parent(offset.group, ctl.transform)
		self.fkControl = [ctl.transform, offset.transform]
		self.fkGroup = [ctl.group, offset.group]

		if self.root:
			cmds.parent(self.root, offset.transform)
		return

	def createRootOffset(self):
		attrName = 'rootOffset'
		parent = self.fkControl[0]

		rootOffset = CONTROL(name='{}_root_offset_ctl'.format(self.name),
		                     typ='center',
		                     scale=self.scale - 0.8,
		                     axis=[0, 0, 0],
		                     )

		ults.presetWireColor([rootOffset.transform], typ=ults.component.center)
		cmds.parent(rootOffset.group, self.fkControl[-1])
		ults.addBoolAttr(obj=parent, name=attrName)
		cmds.connectAttr('{}.{}'.format(parent, attrName), '{}.v'.format(rootOffset.group))

		if self.root:
			cmds.parentConstraint(rootOffset.transform, self.root, mo=True)

		self.fkControl.append(rootOffset.transform)
		self.fkGroup.append(rootOffset.group)
		return

	def setupDisplayAttr(self):
		for attr in ['jointDisplay', 'controlDisplay']:
			ults.addBoolAttr(self.fkControl[0], attr)
			cmds.connectAttr('{}.{}'.format(self.fkControl[0], attr), '{}.{}'.format(self.network, attr))
		return

	def setupGlobalScale(self):
		globalNode = self.fkControl[0]
		attrName = 'globalScale'

		cmds.addAttr(globalNode, ln=attrName, dv=1)
		cmds.setAttr('{}.globalScale'.format(globalNode), k=False, channelBox=True)

		for axis in ['x', 'y', 'z']:
			cmds.connectAttr('{}.{}'.format(globalNode, attrName), '{}.s{}'.format(globalNode, axis))
			cmds.setAttr('{}.s{}'.format(globalNode, axis), k=False, channelBox=False, lock=True)

	def hideGroupNodes(self, objects):
		self.hideObjectsAttributes(objects)
		return


class COG(BASE):
	def __init__(self,
	             cog,
	             hip=None,
	             networkRoot=None,
	             name='cog',
	             scale=1,
	             ):
		BASE.__init__(self,
		              networkRoot=networkRoot,
		              name=name,
		              side='Center',
		              scale=scale,
		              )

		self.cog = cog
		self.hip = hip
		self.objects = [cog]

		self.getScale()
		self.createControls()
		self.createHipControl()
		self.hideObjectsAttributes(self.fkGroup)

		if self.networkRoot:
			self.createSet(self.fkControl)
			self.createNetwork(typ='cog')
			self.createNetworkConnections()
			self.setupHierarchy()

	def getScale(self):
		self.scale = skeleton.determineHeight(self.cog) / 4 + .25
		return

	def createControls(self):
		ctl = CONTROL(name='{}_ctl'.format(self.name),
		              typ='center',
		              scale=self.scale,
		              axis=[0, 0, 0],
		              child=self.cog,
		              )

		ults.presetWireColor(ctl.transform, typ=ults.component.center)
		cmds.parentConstraint(ctl.transform, self.cog)
		self.fkControl = [ctl.transform]
		self.fkGroup = [ctl.group]
		return

	def createHipControl(self):
		if self.hip:
			ctl = CONTROL(name='hip_ctl',
			              typ=control.component.circleRotate,
			              scale=self.scale - .25,
			              axis=[0, 0, 0],
			              child=self.hip,
			              )
			ults.presetWireColor(ctl.transform, typ=ults.component.center)
			cmds.parentConstraint(ctl.transform, self.hip)
			cmds.parent(ctl.group, self.fkControl[-1])
			self.objects.append(self.hip)
			self.fkControl.append(ctl.transform)
			self.fkGroup.append(ctl.group)
		return

	def setupHierarchy(self):
		parent = self.getConnected(self.networkRoot, 'fkControl', 1)
		if parent:
			cmds.parent(self.fkGroup[0], parent)

		rootOffset = self.getConnected(self.networkRoot, 'fkControl', 2)
		if rootOffset:
			grp = ults.createGroup(rootOffset, '{}_pos_grp'.format(rootOffset))
			cmds.pointConstraint(self.fkControl[0], grp, skip='y', mo=True)


class SPINE(BASE):
	def __init__(self,
	             objects,
	             networkRoot=None,
	             name='spine',
	             scale=1,
	             ):
		BASE.__init__(self,
		              objects=objects,
		              networkRoot=networkRoot,
		              name=name,
		              side='Center',
		              scale=scale,
		              )

		self.getScale()
		self.createFKChain(self.objects)
		self.constrainSpine()
		self.createParent(name='rig_grp'.format(self.name), child=self.objects[0])
		self.setupHierarchy()
		self.createDetailChain(self.objects)

		if self.networkRoot:
			self.createSet(self.fkControl)
			self.createNetwork(typ=self.name)
			self.createNetworkConnections()

	def getScale(self):
		if len(self.objects) > 1:
			start = self.objects[0]
			end = self.objects[1]
			distance = ults.getDistance(start, end)
			self.scale = distance
		return

	def constrainSpine(self):
		for obj in self.objects:
			i = self.objects.index(obj)
			cmds.parentConstraint(self.fkControl[i], obj, mo=True)

	def setupHierarchy(self):
		cmds.parent(self.fkParent, self.parent)

		parent = cmds.listRelatives(self.objects[0], parent=True)
		parent = parent[0] if parent else None
		if parent:
			cmds.parent(self.parent, parent)
		return


class NECK(SPINE):
	def __init__(self,
	             objects,
	             networkRoot=None,
	             name='neck',
	             scale=1,
	             ):
		SPINE.__init__(self,
		               objects=objects,
		               networkRoot=networkRoot,
		               name=name,
		               scale=scale,
		               )

		if self.networkRoot:
			self.createLocalWorld(obj=self.fkControl[0],
			                      local=self.fkGroup[0],
			                      )

	def getScale(self):
		distanceList = []
		children = cmds.listRelatives(self.objects[0], children=True)
		if children:
			for child in children:
				start = self.objects[0]
				end = child
				distanceList.append(ults.getDistance(start, end))

		self.scale = max(distanceList) + 0.25
		return


class HEAD(BASE):
	def __init__(self,
	             head,
	             networkRoot=None,
	             name=naming.component.head,
	             scale=1,
	             ):
		BASE.__init__(self,
		              objects=ults.listCheck(head),
		              networkRoot=networkRoot,
		              name=name,
		              side=naming.side.center,
		              scale=scale,
		              )

		self.head = head
		self.getScale()
		self.createControls()
		self.createIK()
		self.setupHierarchy()
		self.createFKIK()
		self.createDetailChain(self.objects)

		if self.networkRoot:
			self.createLocalWorld(obj=self.fkControl[0],
			                      local=self.fkGroup[0],
			                      )
			self.createSet([self.fkControl[0], self.ikControl[1]])
			self.createNetwork(typ=self.name)
			self.createNetworkConnections()
			self.updateNetwork()
			self.parentToRootControl(self.ikGroup[1])

	def getScale(self):
		height = cmds.xform(self.head, q=True, ws=True, rp=True)[1]
		self.scale = height / 6
		return

	def createControls(self):
		ctl = CONTROL(name='{}_ctl'.format(self.name),
		              typ=control.component.lollipop,
		              scale=self.scale,
		              axis=[1, 0, -1],
		              )
		ults.snap(self.head, ctl.group, t=True, r=True)
		ults.presetWireColor(ctl.transform, typ=ults.component.center)
		ults.lockScale(ctl.transform)

		self.fkControl = [ctl.transform]
		self.fkGroup = [ctl.group]
		return

	def createIK(self):
		ctl = CONTROL(name='{}_ik_ctl'.format(self.name),
		              typ=control.component.sphere,
		              scale=self.scale / 8,
		              axis=[0, 0, 0],
		              )

		ults.snap(self.head, ctl.group, t=True)
		distance = cmds.xform(self.head, q=True, ws=True, rp=True)[1]
		cmds.xform(ctl.group, ws=True, t=[0, 0, distance], r=True)

		ikNull = cmds.group(name='{}_ik_aim'.format(self.name), em=True)
		ikGrp = cmds.group(ikNull, name='{}_grp'.format(ikNull))
		ults.snap(self.head, ikGrp, t=True, r=True)
		ults.createAimVector(ctl.transform, ikNull, name='{}_aimVector'.format(self.name))
		ults.presetWireColor(ctl.transform, typ=ults.component.ik)

		self.ikControl = [ikNull, ctl.transform]
		self.ikGroup = [ikGrp, ctl.group]
		return

	def setupHierarchy(self):
		parent = cmds.listRelatives(self.head, parent=True)
		if parent:
			parent = parent[0]
			cmds.parent(self.fkGroup[0], self.ikGroup[0], parent)
		return

	def createFKIK(self):
		attrName = naming.rig.fkik
		ults.createFKIK(obj=self.head,
		                fk=self.fkControl[0],
		                ctl=self.fkControl[0],
		                ik=self.ikControl[0],
		                n=attrName,
		                )

		cmds.connectAttr('{}.{}'.format(self.fkControl[0], attrName), '{}.v'.format(self.ikGroup[1]))
		return

	def updateNetwork(self):
		attrName = 'detailControlDisplay'
		ults.addBoolAttr(self.fkControl[0], attrName)
		cmds.connectAttr('{}.{}'.format(self.fkControl[0], attrName), '{}.{}'.format(self.network, attrName))
		return


class ARM(BASE):
	def __init__(self,
	             side,
	             shoulder,
	             elbow,
	             hand,
	             collar=None,
	             networkRoot=None,
	             name=naming.component.arm,
	             index=0,
	             ):
		BASE.__init__(self,
		              networkRoot=networkRoot,
		              name=name,
		              side=side,
		              index=index,
		              )

		self.collar = collar
		self.collarFKControl = None
		self.collarFKGroup = None
		self.collarIKControl = None
		self.collarIKGroup = None

		self.shoulder = shoulder
		self.elbow = elbow
		self.hand = hand
		self.objects = [shoulder, elbow, hand]

		self.getScale()
		self.createFKIKChain(self.objects)

		if self.collar:
			self.createDetailChain(self.collar)
			self.createCollar()

		self.createRibbonChain(self.shoulder, self.elbow, self.hand)
		self.createHand()

		if self.networkRoot:
			self.createLocalWorld(obj=self.fkControl[0],
			                      local=self.fkGroup[0],
			                      )
			self.createSet([self.collarFKControl] + self.fkControl + self.ikControl)
			self.createNetwork(typ=naming.convention(self.name,
			                                         self.side.upper()[0],
			                                         self.index,
			                                         )
			                   )

			self.createNetworkConnections()
			self.updateNetwork()

	def getScale(self):
		self.scale = ults.getDistance(self.shoulder, self.elbow) / 2.5
		return

	def createCollar(self):
		ctl = CONTROL(name=naming.convention(self.name,
		                                     self.side[0],
		                                     self.index,
		                                     naming.rig.fk,
		                                     naming.component.collar.capitalize(),
		                                     naming.rig.ctl,
		                                     ),
		              typ=control.component.dumbbell,
		              scale=self.scale,
		              axis=[1, 0, 0],
		              child=self.collar,
		              side=self.side,
		              label=naming.component.collar,
		              color=ults.component.fk,
		              )
		ults.lockScale(ctl.transform)
		cmds.parentConstraint(ctl.transform, self.collar)

		parent = cmds.listRelatives(self.collar, parent=True)
		if parent:
			cmds.parent(ctl.group, parent[0])

		self.collarFKControl = ctl.transform
		self.collarFKGroup = ctl.group

		self.objects.insert(0, self.collar)
		return

	def createHand(self):
		HAND(hand=self.hand,
		     side=self.side,
		     networkRoot=self.networkRoot,
		     index=self.index
		     )
		return

	def updateNetwork(self):
		# Collar
		if self.collar:
			self.connectToNetwork(self.collar, self.network, 'skeletonCollar')

		if self.collarFKControl:
			self.connectToNetwork(self.collarFKControl, self.network, 'collarFkControl')

		return


class HAND(BASE):
	def __init__(self,
	             hand,
	             side,
	             networkRoot=None,
	             name=naming.component.hand,
	             index=0,
	             ):
		BASE.__init__(self,
		              objects=ults.listCheck(hand),
		              networkRoot=networkRoot,
		              name=name,
		              side=side,
		              index=index,
		              )

		self.hand = hand
		self.createFingers()


	def createFingers(self):
		children = skeleton.getJointChildren(self.hand)

		i = 0
		for child in children:
			joints = skeleton.getJointOrder(child)
			finger = DIGIT(objects=joints,
			               name=naming.component.finger,
			               side=self.side,
			               networkRoot=self.networkRoot,
			               index=i,
			               )
			i+= 1
		return


class DIGIT(BASE):
	def __init__(self,
	             objects,
	             side=None,
	             networkRoot=None,
	             name=naming.component.digit,
	             index=0,
	             ):
		BASE.__init__(self,
		              objects=objects,
		              networkRoot=networkRoot,
		              name=name,
		              side=side,
		              index=index,
		              )

		self.getScale()
		self.createFKChain(self.objects)
		self.createDetailChain(self.objects)
		self.setupHierarchy()

		if self.networkRoot:
			self.createSet(self.fkControl)
			self.createNetwork(typ=naming.convention(self.name,
			                                         self.index,
			                                         )
			                   )

			self.createNetworkConnections()

	def getScale(self):
		self.scale = ults.getDistance(self.objects[0], self.objects[1]) / 2
		return

	def setupHierarchy(self):
		for obj in self.objects:
			i = self.objects.index(obj)
			cmds.parentConstraint(self.fkControl[i], obj, mo=True)
		return



class LEG(BASE):
	def __init__(self,
	             side,
	             hip,
	             knee,
	             foot,
	             toe=None,
	             networkRoot=None,
	             name=naming.component.leg,
	             index=0,
	             ):
		BASE.__init__(self,
		              networkRoot=networkRoot,
		              name=name,
		              side=side,
		              index=index,
		              )

		self.hip = hip
		self.knee = knee
		self.foot = foot
		self.toe = toe
		self.objects = [hip, knee, foot]

		self.getScale()
		self.createFKIKChain(self.objects)
		self.createDetailChain(self.objects)
		# self.swapFootControlWire()

		if self.networkRoot:
			self.createLocalWorld(obj=self.fkControl[0],
			                      local=self.fkGroup[0],
			                      )
			self.createSet(self.fkControl + self.ikControl)
			self.createNetwork(typ=naming.convention(self.name,
			                                         self.side.upper()[0],
			                                         self.index,
			                                         )
			                   )
			self.createNetworkConnections()

	def getScale(self):
		self.scale = ults.getDistance(self.hip, self.knee) / 4
		return

	def swapFootControlWire(self):
		newCurve = control.wire(typ=control.component.cubeFoot, scale=self.scale, axis=[0, 0, 0])
		ults.snap(self.ikControl[-1], newCurve, t=True)
		cmds.setAttr('{}.ty'.format(newCurve), 0)
		ults.freezeTransform(newCurve, t=True)
		return


class LEG2(BASE):
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
