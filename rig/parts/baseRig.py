# Lancer Modules
from rig.utils import *

# Python
import logging

# Maya Modules
from maya import cmds


# TODO: Rigging Logger

class AbstractRig(AbstractNode):
	def __init__(self,
				 prefix=None,
				 side=None,
				 name=Component.rig,
				 sector=None,
				 index=None,
				 kind=None,
				 items=None,
				 parent=None,
				 root=None,
				 axis=None,
				 scale=1.0,
				 opposite=None,
				 *args,
				 **kwargs
				 ):
		'''
		Naming convention:
		[prefix][side][name/itemLabel][sector][index][kind]
		"arm_L_shoulder_A_0_fkControl"
		"arm_L_shoulder_A_0_bindControl"

		:param str None name:
		:param str object None parent:
		:param str object None root:
		:param str None prefix:
		:param list tuple dict None items:
		:param list None axis:
		:param int float None scale:
		:param int None index:
		:param str None side:
		:param str None sector:
		:param str None kind:
		'''

		AbstractNode.__init__(self,
							  name=name,
							  prefix=prefix,
							  parent=parent,
							  side=side,
							  index=index,
							  sector=sector,
							  kind=kind,
							  *args,
							  **kwargs
							  )

		# Interface
		self.interface = None
		self.rigKind = kind if kind else prefix if prefix else None

		# Hierarchy
		self.root = root
		self.topNode = None
		self.joint = []
		self.set = None
		self.opposite = opposite
		self.local = None
		self.world = None

		# Items
		self.items = items
		self.childItems = []
		self.grandchildItems = []

		# Attributes
		self.axis = axis
		self.scale = scale

		# FK
		self.fkControl = []
		self.fkPoleVector = None
		self.fkStretch = None
		self.fkTopNode = None

		# IK
		self.ikControl = []
		self.ikJoint = []
		self.ikHandle = None
		self.ikPoleVector = None
		self.ikStretch = []
		self.ikTopNode = None

		# Child Controls
		self.childControl = []
		self.grandchildControl = []


class BASERIG(AbstractRig):
	def __init__(self, *args, **kwargs):
		AbstractRig.__init__(self, *args, **kwargs)

	def printAttributes(self):
		var = ''
		for x in sorted(vars(self).iterkeys()):
			var += '{}: {}\n'.format(x, vars(self)[x])
		print var
		return var

	####################################################################################################################
	# Custom Properties
	####################################################################################################################

	@property
	def allControls(self):
		result = []

		for ctrl in flatList(self.interface,
							 self.fkControl,
							 self.ikControl,
							 self.childControl,
							 self.grandchildControl
							 ):
			if isinstance(ctrl, object):
				for attr in ['transform', 'offsetTransform']:
					if hasattr(ctrl, attr):
						value = getattr(ctrl, attr)
						if value:
							result.append(value)
			elif ctrl is not None:
				result.append(self.interface)

		return result

	####################################################################################################################
	# Scale
	####################################################################################################################

	@staticmethod
	def scaleByDistance(items):
		return averageDistance(items)

	@staticmethod
	def scaleByHeight(items):
		return hierarchyHeight(items[0])

	####################################################################################################################
	# Joint Chain
	####################################################################################################################

	def createJointChain(self, items=None, kind=Component.rig, hierarchy=False, autoName=True):
		if items is None:
			items = self.items

		if not isinstance(items, (list, tuple, dict)):
			raise TypeError('Items must be iter type.')

		chainNames = []
		chain = []

		i = 0
		for item in items:
			name = self.name
			index = i

			label = None
			otherLabel = None

			if autoName:
				if attributeExist(item, MayaAttr.type) and attributeExist(item, MayaAttr.otherType):
					label = getJointLabelType(item)
					otherLabel = getJointLabelOtherType(item)

					if label.lower() != 'none':
						name = label
						index = None
					else:
						if otherLabel:
							name = otherLabel
							index = None

			if i != 0 and name == chainNames[i - 1]:
				index = i

			joint = Joint(prefix=self.prefix,
						  name=name.lower(),
						  side=self.side,
						  sector=self.sector,
						  index=index,
						  kind=camelCase(kind, Component.joint, capitalize=False),
						  drawStyle=JointDrawStyle.none,
						  type=label,
						  otherType=otherLabel,
						  )

			joint.snapTo(item)
			joint.freezeTransforms()
			chainNames.append(name)
			chain.append(joint)
			i += 1

		if hierarchy:
			i = 0
			for link in chain:
				if i != 0:
					link.parent = chain[i - 1]
				i += 1
		return chain

	####################################################################################################################
	# FK Chain
	####################################################################################################################

	def createFKChain(self, items=None, interface=None, autoName=True):
		# Edge Case
		if items is None:
			items = self.items

		if not isinstance(items, (list, tuple, dict)):
			raise TypeError('Items must be iter type.')

		if interface is None:
			interface = self.interface

		if not interface:
			raise ValueError('No parent provided.')

		chainNames = []

		# Controls
		i = 0
		for item in items:
			name = self.name
			index = i

			label = None
			otherLabel = None

			if autoName:
				if attributeExist(item, MayaAttr.type) and attributeExist(item, MayaAttr.otherType):
					label = getJointLabelType(item)
					otherLabel = getJointLabelOtherType(item)

					if label.lower() != 'none':
						name = label
						index = None
					else:
						if otherLabel:
							name = otherLabel
							index = None

			if i != 0 and name == chainNames[i - 1]:
				index = i

			ctrl = FKCONTROL(name=name,
							 prefix=self.prefix,
							 item=item,
							 axis=self.axis,
							 scale=self.scale,
							 index=index,
							 side=self.side,
							 sector=self.sector,
							 type=label,
							 otherType=otherLabel,
							 )

			ctrl.snapTo(item)
			self.fkControl.append(ctrl)
			chainNames.append(name)
			i += 1

		# Hierarchy
		self.fkTopNode = self.createTopNode(kind=Component.fk)

		i = 0
		for ctrl in self.fkControl:
			if i == 0:
				ctrl.parent = self.fkTopNode
			else:
				parentCtrl = self.fkControl[i - 1].offset.transform
				ctrl.parent = parentCtrl
			i += 1

		# FK PoleVector
		if len(items) == 3:
			self.fkPoleVector = cmds.group(n=longName(self.longName, Component.fkPoleVector), em=True)
			pvPos = getPoleVectorPosition(items[0], items[1], items[2])
			cmds.xform(self.fkPoleVector, ws=True, t=pvPos)
			cmds.parent(self.fkPoleVector, self.fkControl[1].offset.transform)
			freezeTransform(self.fkPoleVector)
			lockKeyableAttributes(self.fkPoleVector, hide=True)

		# Stretch
		attrName = Component.fkStretch

		if not attributeExist(interface, Component.stretch):
			cmds.addAttr(interface, ln=Component.stretch, at='double', k=True)

		if not attributeExist(interface, attrName):
			cmds.addAttr(interface, ln=attrName, m=True, at='double')

		i = 0
		for null in [x.nullPosition for x in self.fkControl]:
			if i != 0:
				offsetNode = cmds.createNode(MayaNodeType.addDoubleLinear,
											 name=longName(interface, Component.fkStretch, Component.offset, 0),
											 )

				offsetValue = cmds.getAttr('{}.tx'.format(null))
				cmds.setAttr(attributeName(offsetNode, 'input2'), offsetValue)

				# Connect Offset
				cmds.connectAttr('{}.{}[{}]'.format(interface, attrName, i),
								 attributeName(offsetNode, 'input1'),
								 force=True
								 )

				cmds.connectAttr(attributeName(offsetNode, 'output'),
								 '{}.tx'.format(null),
								 force=True
								 )
				cmds.connectAttr('{}.{}'.format(interface, Component.stretch),
								 '{}.{}[{}]'.format(interface, attrName, i),
								 force=True,
								 )
			i += 1
		return

	####################################################################################################################
	# IK Chain
	####################################################################################################################

	def createIKChain(self, items=None, interface=None, autoName=True):
		# Edge Case
		if items is None:
			items = self.items

		if not isinstance(items, (list, tuple, dict)):
			raise TypeError('Items must be iter type.')

		if len(items) != 3:
			raise TypeError('Must provide only 3 items.')

		if interface is None:
			interface = self.interface

		if not interface:
			raise ValueError('No parent provided.')

		# Joints
		self.ikJoint = self.createJointChain(items=items, kind=Component.ik, hierarchy=True)

		# Controls
		chainNames = []

		i = 0
		for item in items:
			index = i
			name = self.name

			label = None
			otherLabel = None

			if autoName:
				if attributeExist(item, MayaAttr.type) and attributeExist(item, MayaAttr.otherType):
					label = getJointLabelType(item)
					otherLabel = getJointLabelOtherType(item)

					if label.lower() != 'none':
						name = label
						index = None
					else:
						if otherLabel:
							name = otherLabel
							index = None

			if i != 0 and name == chainNames[i - 1]:
				index = i

			ctrl = IKCONTROL(name=name,
							 prefix=self.prefix,
							 item=item,
							 axis=self.axis,
							 scale=self.scale,
							 index=index,
							 side=self.side,
							 sector=self.sector,
							 type=label,
							 otherType=otherLabel,
							 )

			ctrl.snapTo(item)
			chainNames.append(name)
			self.ikControl.append(ctrl)
			i += 1

		# Hierarchy
		self.ikTopNode = self.createTopNode(kind=Component.ik)

		for ctrl in self.ikControl:
			ctrl.parent = self.ikTopNode

		# IK Handle
		self.ikHandle = cmds.ikHandle(name=longName(self.longName, Component.ikHandle),
									  sj=self.ikJoint[0].transform,
									  ee=self.ikJoint[-1].transform,
									  sol='ikRPsolver')[0]

		cmds.parent(self.ikHandle, self.ikControl[-1].offset.transform)
		cmds.orientConstraint(self.ikHandle, self.ikJoint[-1].transform, mo=True)
		cmds.setAttr('{}.v'.format(self.ikHandle), 0)
		cmds.pointConstraint(self.ikControl[0].offset.transform, self.ikJoint[0].transform, mo=True)

		# Pole Vector
		pvPos = getPoleVectorPosition(self.ikJoint[0].transform,
									  self.ikJoint[1].transform,
									  self.ikJoint[2].transform
									  )
		cmds.xform(self.ikControl[1].nullPosition, ws=True, t=pvPos)
		poleVector = createPoleVector(name=longName(self.longName, Component.ikPoleVector),
									  joint=self.ikJoint[1].transform,
									  ctl=self.ikControl[1].offset.transform,
									  ik=self.ikHandle,
									  )
		self.ikPoleVector = poleVector

		# IK Stretch
		attrName = Component.ikStretch
		stretchGroup = []

		if not attributeExist(interface, attrName):
			cmds.addAttr(interface, ln=Component.stretch, at='double')
			cmds.addAttr(interface, ln=attrName, m=True, at='double')

		i = 0
		for joint in self.ikJoint:
			null = cmds.group(joint, em=True, n=longName(joint,
														 Component.stretch,
														 ))
			snap(joint, null, t=True, r=True)
			if i != 0:
				cmds.parent(null, stretchGroup[i - 1])
				cmds.connectAttr('{}.tx'.format(null), '{}.tx'.format(joint))

				offsetNode = cmds.createNode(MayaNodeType.addDoubleLinear,
											 name=longName(interface, Component.fkStretch, Component.offset, 0),
											 )
				offsetValue = cmds.getAttr('{}.tx'.format(null))
				cmds.setAttr(attributeName(offsetNode, 'input2'), offsetValue)

				cmds.connectAttr('{}.{}[{}]'.format(interface, attrName, i),
								 attributeName(offsetNode, 'input1'),
								 force=True
								 )

				cmds.connectAttr(attributeName(offsetNode, 'output'), '{}.tx'.format(null), force=True)
				cmds.connectAttr('{}.{}'.format(interface, Component.stretch),
								 '{}.{}[{}]'.format(interface, attrName, i))
			stretchGroup.append(null)
			i += 1

		self.ikStretch = stretchGroup
		return

	# TODO: IK Spline
	def createIKSplineChain(self):
		return

	####################################################################################################################
	# Bind Chain
	####################################################################################################################

	def createBindChain(self, items):
		bindDict = {}
		sectors = CHARACTERSTR

		itemIndex = 0
		for item in items:
			bindControls = []
			leafControls = []

			# Name
			name = self.name

			if attributeExist(item, MayaAttr.type) and attributeExist(item, MayaAttr.otherType):
				label = getJointLabelType(item)
				otherLabel = getJointLabelOtherType(item)

				if label.lower() != 'none':
					name = label
				else:
					if otherLabel:
						name = otherLabel

			# Bind Joints
			children = getImmediateBindJoints(item)

			if children:
				childIndex = 0
				for child in children:
					bind = CHILDCONTROL(name=name,
										prefix=self.prefix,
										item=child,
										scale=self.scale,
										index=childIndex,
										side=self.side,
										sector=sectors[itemIndex].upper(),
										axis=self.axis,
										)

					bind.snapTo(child)

					if self.joint:
						bind.parentTo(self.joint[itemIndex])

					cmds.parentConstraint(bind, child, mo=True)
					cmds.scaleConstraint(bind, child, mo=True)
					bindControls.append(bind)
					self.childControl.append(bind)

					# Grand Children / Leaf
					grandChildren = getAllJointChildren(child)

					if grandChildren:
						grandIndex = 0
						for grandChild in grandChildren:
							leaf = GRANDCHILDCONTROL(name=name,
													 prefix=self.prefix,
													 item=grandChild,
													 scale=self.scale * .25,
													 index=grandIndex,
													 side=self.side,
													 sector=sectors[itemIndex].upper(),
													 )

							leaf.snapTo(grandChild)
							leaf.parentTo(bind)
							cmds.parentConstraint(leaf, grandChild, mo=True)
							cmds.scaleConstraint(leaf, grandChild, mo=True)
							leafControls.append(leaf)
							self.leafControls.append(leaf)
							grandIndex += 1

					childIndex += 1
			bindDict[item] = {'bind': bindControls, 'leaf': leafControls}
			itemIndex += 1
		return bindDict

	####################################################################################################################
	# Constrain
	####################################################################################################################

	@staticmethod
	def constrainChain(parentItems, childItems):
		if not isinstance(parentItems, (list, dict, tuple)):
			raise TypeError('Must provide iter type for parentItems.')

		if not isinstance(childItems, (list, dict, tuple)):
			raise TypeError('Must provide iter type for childItems.')

		if len(parentItems) != len(childItems):
			raise ValueError('Must provide same number of parentItems({}) to childItems({}).'.format(len(parentItems),
																									 len(childItems)))

		result = []

		i = 0
		for parent in parentItems:
			con = cmds.parentConstraint(parent, childItems[i], mo=True)
			result.append(con)
			i += 1

		return result

	####################################################################################################################
	# Hierarchy
	####################################################################################################################

	def createTopNode(self, items=None, kind=None):
		if items is None:
			items = self.items

		if not items:
			raise ValueError('No items provided.')

		child = None

		if isinstance(items, (list, dict, tuple)):
			child = items[0]
		elif isinstance(items, str):
			child = items

		topNode = cmds.group(name=longName(self.longName, camelCase(kind, Component.group, capitalize=False)), em=True)

		if child:
			snap(child, topNode, True, True)
		return topNode

	####################################################################################################################
	# Master
	####################################################################################################################

	def createRigControl(self, child=None, wireType=WireType.master):
		axis = [0, 0, 0]

		if wireType == WireType.master:
			if self.side == Position.left:
				axis = [1, -1, 0]
			elif self.side == Position.right:
				axis = [1, 1, 0]

		ctl = INTERFACE_CONTROL(name=self.name,
								prefix=self.prefix,
								item=child,
								axis=axis,
								scale=self.scale,
								index=self.index,
								side=self.side,
								sector=self.sector,
								wireType=wireType,
								)

		if child:
			ctl.snapTo(child)

		return ctl

	####################################################################################################################
	# Sets
	####################################################################################################################

	def createSet(self, items, parentSet=None):
		if not items:
			raise ValueError('No items provided.')

		name = longName(self.longName, Component.set)

		cmds.select(d=True)
		items = listCheck(items)
		set = cmds.sets(items, name=name)

		if not parentSet:
			if self.root:
				if isinstance(self.root, object) and hasattr(self.root, Component.set):
					parentSet = getattr(self.root, Component.set)
				else:
					if attributeExist(self.root, Component.set):
						parentSet = getConnectedNode(self.root, Component.set)

		if parentSet and nodeExists(str(parentSet)):
			cmds.sets(set, add=parentSet)
		return set

	####################################################################################################################
	# FKIK
	####################################################################################################################

	def create3PointFKIK(self, items=None, parent=None):
		# Edge Cases
		if items is None:
			items = self.items

		if not items:
			raise ValueError('No items provided')

		if len(items) != 3:
			raise ValueError('Must provide 3 items.')

		if parent is None:
			if self.interface:
				parent = self.interface
			else:
				self.interface = self.createRigControl(items[-1])
				parent = self.interface

		if not parent:
			raise ValueError('No parent provided.')

		# Rig
		self.topNode = self.createTopNode(items)
		self.joint = self.createJointChain(items=items, kind=Component.rig, hierarchy=True)
		self.createFKChain(items, parent)
		self.createIKChain(items, parent)

		# Hierarchy
		for x in [self.joint[0], self.fkTopNode, self.ikJoint[0], self.ikStretch[0], self.ikControl[0].nullPosition]:
			cmds.parent(x, self.topNode)

		if hasattr(parent, 'nullPosition'):
			parent.parentTo(self.joint[-1])
		else:
			cmds.parent(parent, self.joint[-1])

		self.createFKIKConnections(self.joint, parent)
		# self.parentToRootControl(self.ikGroup[1])
		# self.parentToRootControl(self.ikGroup[2])
		return

	def createSplineFKIK(self, items):
		return

	####################################################################################################################
	# Twist
	####################################################################################################################

	# FIXME: Twist Chain
	def create3PointTwistChain(self, items):
		start = items[0]
		mid = items[1]
		end = items[2]

		self.upperObject = getBindJoint(start)
		self.lowerObject = getBindJoint(mid)

		if self.upperObject and self.lowerObject:
			self.midObject = self.lowerObject[0]

			self.upperChain = DETAILCHAIN(joint=self.start,
										  scale=self.scale,
										  axis=self.axis,
										  name=longName(self.name,
														'upper',
														Component.detail,
														)
										  )
			self.lowerChain = DETAILCHAIN(joint=self.mid,
										  scale=self.scale,
										  axis=self.axis,
										  name=longName(self.name,
														'lower',
														Component.detail
														)
										  )

		self.objects = self.upperObject + self.lowerObject
		self.control = self.upperChain.control + self.lowerChain.control
		self.group = self.upperChain.group + self.lowerChain.group
		self.stretch = []
		self.distance = []

		self.upperTwist = None
		self.lowerTwist = None

		self.createIKTwist()
		self.createTwistStretch(objects=self.upperChain.control, start=self.start, end=self.mid, typ='upper',
								ctl=self.upperTwist.parent)
		self.createTwistStretch(objects=self.lowerChain.control, start=self.mid, end=self.end, typ='lower',
								ctl=self.lowerTwist.parent)

		self.createSnS()

	def createIKTwist(self):
		self.upperTwist = createIKTwist(start=self.start,
										end=self.mid,
										name=longName(self.name, 'upper_twist'),
										)

		self.lowerTwist = createIKTwist(start=self.end,
										end=self.mid,
										name=longName(self.name, 'lower_twist'),
										)

		self.createTwistConnections(self.upperChain.group, self.upperTwist.joint[0], self.upperTwist.parent,
									typ='upper')
		self.createTwistConnections(self.lowerChain.group, self.lowerTwist.joint[0], self.lowerTwist.parent,
									typ='lower')
		cmds.parent(self.lowerTwist.ikHandle, self.end)
		cmds.parent(self.lowerTwist.parent, self.mid)
		return

	def createTwistConnections(self, objects, twist, ctl, typ):
		attrName = 'twist'
		cmds.addAttr(ctl, ln=attrName, m=True, at='double', k=True)

		max = 1.0
		step = max / float(len(objects))
		var = max if typ == 'upper' else 0.0
		for obj in objects:
			i = objects.index(obj)
			mult = cmds.createNode('multDoubleLinear', name='{}_twist_mult0'.format(obj))
			cmds.connectAttr('{}.{}[{}]'.format(ctl, attrName, i), '{}.input1'.format(mult))
			cmds.connectAttr('{}.rx'.format(twist), '{}.input2'.format(mult))
			cmds.connectAttr('{}.output'.format(mult), '{}.rx'.format(obj))
			cmds.setAttr('{}.{}[{}]'.format(ctl, attrName, i), var)
			var += -step if typ == 'upper' else step
		return

	def createTwistStretch(self, objects, start, end, ctl, typ):
		attrName = Component.stretch
		cmds.addAttr(ctl, ln=attrName, m=True, at='double', k=True)
		distance = createDistanceNode(start=start, end=end,
									  n=longName(self.name, '{}_distance0'.format(typ)))

		max = 1.0
		if typ == 'upper':
			step = max / float(len(objects))
		else:
			step = max / float(len(objects) - 1)
		var = 0

		for obj in objects:
			i = objects.index(obj)
			cmds.setAttr('{}.{}[{}]'.format(ctl, attrName, i), var)
			grp = createGroup(obj, name=longName(obj, attrName, Component.group))
			self.stretch.append(grp)
			if i != 0:
				sub = cmds.createNode('plusMinusAverage', name='{}_subtract0'.format(grp))
				mult = cmds.createNode('multDoubleLinear', name='{}_mult0'.format(grp))
				cmds.connectAttr('{}.distance'.format(distance[0]), '{}.input3D[0].input3Dx'.format(sub))
				cmds.setAttr('{}.input3D[1].input3Dx'.format(sub), distance[1])
				cmds.setAttr('{}.operation'.format(sub), 2)
				cmds.connectAttr('{}.output3Dx'.format(sub), '{}.input1'.format(mult))
				cmds.connectAttr('{}.output'.format(mult), '{}.tx'.format(grp))
				cmds.connectAttr('{}.{}[{}]'.format(ctl, attrName, i), '{}.input2'.format(mult))
			var += step
		self.distance.append(distance[0])
		return

	def createSnS(self):
		globalGrp = self.upperTwist.parent
		cmds.addAttr(globalGrp, ln='sns', min=0, max=1, dv=0, k=True)
		cmds.addAttr(globalGrp, ln='snsAdd', k=True)

		maxDistance = getDistance(self.start, self.mid) + getDistance(self.mid, self.end)
		# distance = ults.createDistanceNode(self.start, self.end)
		distanceAdd = cmds.createNode('addDoubleLinear', name='{}_add0'.format(self.name))
		cmds.connectAttr('{}.distance'.format(self.distance[0]), '{}.input1'.format(distanceAdd))
		cmds.connectAttr('{}.distance'.format(self.distance[1]), '{}.input2'.format(distanceAdd))

		divideA = cmds.createNode('multiplyDivide', name='{}_divide0'.format(self.name))
		cmds.setAttr('{}.operation'.format(divideA), 2)
		cmds.setAttr('{}.input2X'.format(divideA), maxDistance)
		divideB = cmds.createNode('multiplyDivide', name='{}_divide0'.format(self.name))
		cmds.setAttr('{}.operation'.format(divideB), 2)
		cmds.setAttr('{}.input1X'.format(divideB), 1)

		cmds.connectAttr('{}.output'.format(distanceAdd), '{}.input1X'.format(divideA))
		cmds.connectAttr('{}.outputX'.format(divideA), '{}.input2X'.format(divideB))

		setRange = cmds.createNode('setRange', name='{}_sns_setRange0'.format(self.name))
		cmds.setAttr('{}.minX'.format(setRange), 1)
		cmds.setAttr('{}.oldMaxX'.format(setRange), 1)
		cmds.connectAttr('{}.sns'.format(globalGrp), '{}.valueX'.format(setRange))
		cmds.connectAttr('{}.outputX'.format(divideB), '{}.maxX'.format(setRange))

		add = cmds.createNode('addDoubleLinear', name='{}_add0'.format(self.name))
		cmds.connectAttr('{}.outValueX'.format(setRange), '{}.input1'.format(add))
		cmds.connectAttr('{}.snsAdd'.format(globalGrp), '{}.input2'.format(add))

		amount = len(self.objects)
		var = 0
		step = 1.0 / float(len(self.objects) - 1)
		stepRangePos = []

		for x in range(amount):
			if x == 0:
				stepRangePos.append(.1)
			else:
				stepRangePos.append(var)
			var += step

		for grp in self.stretch:
			for axis in ['y', 'z']:
				cmds.connectAttr('{}.output'.format(add), '{}.s{}'.format(grp, axis))
		return

	####################################################################################################################
	# Ribbon
	####################################################################################################################

	def createFlexiPlane(self):
		startObject = self.items[0]
		endObject = self.items[-1]
		amount = len(self.items)
		distance = getDistance(startObject, endObject)
		flex = createFlexiPlane(name=self.name, amount=amount, width=distance, side=self.side)

		cmds.delete(cmds.parentConstraint(startObject, endObject, flex.parent))

		for grp in self.group:
			i = self.group.index(grp)
			cmds.parent(grp, flex.follicle[i])

		self.ribbonLocators = flex.control
		self.ribbonLocatorsGroup = flex.group
		self.parent = flex.parent
		return

	####################################################################################################################
	# Relationships
	####################################################################################################################

	@staticmethod
	def limitRotations(item):
		cmds.transformLimits(item, erx=[1, 1], rx=[-180, 180])
		return

	@staticmethod
	def resetRotations(item):
		for axis in ['x', 'y', 'z']:
			cmds.setAttr('{}.r{}'.format(item, axis), 0)
		return

	@staticmethod
	def getConnected(obj, attr, indexValue=0):
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

		if self.interface:
			cogNetwork = self.getConnected(self.interface, 'cog_C')
			cog = self.getConnected(cogNetwork, 'fkControl', 0) if cogNetwork else None

			if cog:
				localWorldConstraint(obj=obj,
									 local=local,
									 world=cog,
									 n=attrName,
									 )
		return

	def createFKIKConnections(self, items=None, parent=None):
		# Edge Case
		if items is None:
			items = self.items

		if not items:
			raise ValueError('No items provided.')

		if parent is None:
			parent = self.interface

		if not parent:
			raise ValueError('No parent provided.')

		if not self.fkControl:
			raise ValueError('No FK Controls provided.')

		if not self.ikControl:
			raise ValueError('No IK Controls provided.')

		if len(self.items) != len(self.fkControl) != len(self.ikControl):
			raise ValueError(
				'Items({}), FK({}), and IK({}) do not have same length.'.format(len(self.items),
																				len(self.fkControl),
																				len(self.ikControl)))

		# Constraints
		fkik = createFKIK(items=items,
						  fkControls=self.fkControl,
						  ikControls=self.ikJoint,
						  parent=parent,
						  attrName=Component.fkik,
						  )

		# Visibility
		i = 0
		for ctrl in self.fkControl:
			cmds.connectAttr('{}.outputX'.format(fkik[1][i]), '{}.v'.format(ctrl.nullConnection), f=True)
			i += 1

		for ctrl in self.ikControl:
			cmds.connectAttr('{}.{}'.format(parent, Component.fkik), '{}.v'.format(ctrl.nullConnection), f=True)
		return

	def connectToRig(self, child, parent, name):
		attrName = Component.rig
		childAttr = '{}.{}'.format(child, attrName)
		parentAttr = '{}.{}'.format(parent, name)

		if not attributeExist(parent, name):
			cmds.addAttr(parent, ln=name, at='message')

		if not attributeExist(child, attrName):
			cmds.addAttr(child, ln=attrName, at='message')

		if cmds.attributeQuery(name, node=parent, ex=True):
			if cmds.attributeQuery(name, node=parent, m=True):
				mList = cmds.listAttr('{}.{}'.format(parent, name), m=True)
				if mList:
					i = mList.index(mList[-1]) + 1
				else:
					i = 0

				addIndexAttribute(child, i)
				parentAttr = '{}.{}[{}]'.format(parent, name, i)

		cmds.connectAttr(parentAttr, childAttr, force=True)
		self.connectToParent(child, parent)
		return

	@staticmethod
	def connectToParent(child, parent):
		if not attributeExist(parent, 'children'):
			addAttribute(parent, 'children', kind=MayaAttrType.string, lock=True)

		if not attributeExist(child, 'parent'):
			addAttribute(child, 'parent', kind=MayaAttrType.message)

		cmds.connectAttr('{}.children'.format(parent), '{}.parent'.format(child), force=True)
		return

	def multiConnectToRig(self, items, parent, name):
		items = listCheck(items)
		attrName = Component.rig

		if not cmds.attributeQuery(name, node=parent, ex=True):
			cmds.addAttr(parent, ln=name, dt='string', m=True)
			i = 0
		else:
			if cmds.listAttr('{}.{}'.format(parent, name), m=True):
				i = int(cmds.listAttr('{}.{}'.format(parent, name), m=True)[-1].split('[')[-1].split(']')[0])
			else:
				i = 0

		for item in items:
			self.connectToParent(item, parent)

			if not cmds.attributeQuery(attrName, node=item, ex=True):
				cmds.addAttr(item, ln=attrName, at='message')

			cmds.connectAttr('{}.{}[{}]'.format(parent, name, i), '{}.{}'.format(item, attrName), f=True)

			if not attributeExist(item, 'index'):
				addIndexAttribute(item, i)
			else:
				setAttribute(item, 'index', i, lock=True, force=True)
			i += 1
		return

	def finalize(self, items=None, parent=None):
		# Edge case
		if parent is None:
			parent = self.interface

		if not parent:
			raise ValueError('No parent provided.')

		# Rig Joints
		if self.joint:
			self.multiConnectToRig(self.joint, parent, Component.joint)

		# Set
		if self.set:
			self.connectToRig(child=self.set, parent=parent, name=Component.set)

		# FK
		if self.fkControl:
			self.multiConnectToRig(self.fkControl, parent, Component.fkControl)

		if self.fkPoleVector:
			self.connectToRig(self.fkPoleVector, parent, Component.fkPoleVector)

		# IK
		if self.ikControl:
			self.multiConnectToRig(self.ikControl, parent, Component.ikControl)

		if self.ikJoint:
			self.multiConnectToRig(self.ikJoint, parent, Component.ikJoint)

		if self.ikPoleVector:
			self.connectToRig(self.ikPoleVector, parent, Component.ikPoleVector)

		if self.ikHandle:
			self.connectToRig(self.ikHandle, parent, Component.ikHandle)

		# Bind Controls
		if self.childControl:
			self.multiConnectToRig(self.childControl, parent, Component.bindControl)

			attrName = Component.detailControlDisplay
			if not attributeExist(parent, attrName):
				addAttribute(node=parent, attribute=attrName, kind=MayaAttrType.bool, channelBox=True, keyable=False)

			for child in self.childControl:
				cmds.connectAttr('{}.{}'.format(parent, attrName), '{}.v'.format(child.nullConnection))

		if self.grandchildControl:
			self.multiConnectToRig(self.grandchildControl, parent, Component.leafControl)

			attrName = Component.detailControlDisplay
			if not attributeExist(parent, attrName):
				addAttribute(node=parent, attribute=attrName, kind=MayaAttrType.bool, channelBox=True, keyable=False)

			for grandchild in self.grandchildControl:
				cmds.connectAttr('{}.{}'.format(parent, attrName), '{}.v'.format(grandchild.nullConnection))
		return


class RIBBONLIMB:
	def __init__(self,
				 start,
				 mid,
				 end,
				 upperObjects,
				 midObject,
				 lowerObjects,
				 name=Component.ribbon,
				 scale=1,
				 axis=None,
				 side=Position.left,
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

		self.createMainControls()
		self.createIntermediateControls()
		self.createDetailControls()
		self.createRibbon()
		self.createHierarchy()
		self.createTwist()
		self.cleanUp()

	def getStartParent(self):
		parent = cmds.listRelatives(self.start, parent=True)
		return parent[0] if parent else None

	def createMainControls(self):
		for obj in self.objects:
			i = self.objects.index(obj)
			ctl = CONTROL(name=longName(self.name,
										'main',
										i,
										Component.control,
										),
						  typ=WireType.octagon,
						  scale=self.scale,
						  axis=self.axis,
						  child=obj,
						  color=self.color,
						  )

			cmds.parent(ctl.group, obj)
			self.mainControl.append(ctl.transform)
			self.mainGroup.append(ctl.group)

		snap(self.mid, self.mainGroup[-1], r=True)

		cmds.delete(cmds.orientConstraint(self.mainGroup[0], self.mainGroup[2], self.mainGroup[1]))
		return

	def createIntermediateControls(self):
		for i in range(2):
			ctl = CONTROL(name=longName(self.name,
										'intermediate',
										i,
										Component.control,
										),
						  typ=WireType.hexigon,
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
		objects = self.upperObjects + listCheck(self.midObject) + self.lowerObjects
		i = 0
		for obj in objects:
			i = objects.index(obj)
			ctl = CHILDCONTROL(name=longName(self.name,
											 'detail',
											 i,
											 Component.control,
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

	def createFlexiPlane(self, start, end, amount, name):
		distance = getDistance(start, end)
		flex = createFlexiPlane(name=name,
								amount=amount,
								width=distance,
								side=self.side,
								)

		cmds.delete(cmds.parentConstraint(start, end, flex.parent))
		return flex

	def createRibbon(self):
		self.upperFlexiPlane = self.createFlexiPlane(start=self.start,
													 end=self.mid,
													 amount=len(self.upperObjects + listCheck(self.midObject)),
													 name=longName(self.name,
																   'upper',
																   ),
													 )
		self.lowerFlexiPlane = self.createFlexiPlane(start=self.mid,
													 end=self.end,
													 amount=len(self.upperObjects + listCheck(self.midObject)),
													 name=longName(self.name,
																   'lower',
																   ),
													 )
		return

	def createHierarchy(self):

		cmds.pointConstraint(self.mainControl[0], self.upperFlexiPlane.control[0])
		cmds.pointConstraint(self.mainControl[2], self.upperFlexiPlane.control[2])

		cmds.pointConstraint(self.mainControl[2], self.lowerFlexiPlane.control[0])
		cmds.pointConstraint(self.mainControl[4], self.lowerFlexiPlane.control[2])

		cmds.connectAttr('{}.t'.format(self.mainControl[1]), '{}.t'.format(self.upperFlexiPlane.control[1]))
		cmds.connectAttr('{}.t'.format(self.mainControl[3]), '{}.t'.format(self.lowerFlexiPlane.control[1]))

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

		# if self.startParent:
		#	cmds.parent(self.upperFlexiPlane.masterGroup, self.startParent)
		#	cmds.parent(self.lowerFlexiPlane.masterGroup, self.startParent)

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

	def cleanUp(self):
		for obj in self.mainControl:
			lockScale(obj)
		return
