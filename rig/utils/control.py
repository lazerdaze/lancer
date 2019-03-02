# Lancer Modules
from wire import *
from network import *
from constraint import *
from joint import *
from naming import *
from node import *

# Maya Modules
from maya import cmds


def createControl(name='control', shape=WireType.circle, axis=None, scale=1.0, color=None, kind=None):
	axis = axis if axis else [1, 0, 0]

	# Joint Node
	node = cmds.createNode('joint', name=name)
	cmds.setAttr('{}.segmentScaleCompensate'.format(node), 0)
	cmds.setAttr('{}.drawStyle'.format(node), 2)
	cmds.setAttr('{}.radius'.format(node), keyable=False, channelBox=False)
	cmds.setAttr('{}.v'.format(node), keyable=False, channelBox=True)
	cmds.setAttr('{}.rotateOrder'.format(node), k=True)

	# Curve Shape
	curve = createWire(kind=shape, axis=axis)
	curveShape = cmds.listRelatives(curve, shapes=True)[0]

	# Set Scale
	for axis in ['x', 'y', 'z']:
		cmds.setAttr('{}.s{}'.format(curve, axis), scale)

	freezeTransform(curve)

	# Parent
	cmds.parent(curveShape, node, r=True, s=True)
	cmds.delete(curve)

	# Add Kind Attribute
	if kind:
		addAttribute(node=node,
					 attribute=UserAttr.kind,
					 kind=MayaAttrType.string,
					 value=kind,
					 lock=True,
					 )

	# Color
	if color and isinstance(color, list):
		cmds.setAttr(attributeName(curveShape, MayaAttr.useObjectColor), 0)
		cmds.setAttr(attributeName(curveShape, MayaAttr.overrideEnabled), 1)
		cmds.setAttr(attributeName(curveShape, MayaAttr.overrideRGBColors), 1)

		i = 0
		for x in ['R', 'G', 'B']:
			cmds.setAttr('{}.overrideColor{}'.format(curveShape, x), color[i])
			i += 1

	curveShape = cmds.rename(curveShape, '{}Shape'.format(name))

	return [node, curveShape]


########################################################################################################################
#
#
#	Control Class
#
#
########################################################################################################################


class Control(Joint):
	def __init__(self,
				 prefix=None,
				 side=None,
				 name='rigControl',
				 sector=None,
				 index=None,
				 kind=Component.control,
				 parent=None,
				 type=None,
				 otherType=None,
				 item=None,
				 wire=WireType.circleRotate,
				 axis=None,
				 scale=1.0,
				 color=WireColor.blue,
				 offset=False,
				 *args,
				 **kwargs
				 ):

		Joint.__init__(self,
					   prefix=prefix,
					   side=side,
					   name=name,
					   sector=sector,
					   index=index,
					   kind=kind,
					   parent=parent,
					   radius=1.0,
					   drawStyle=JointDrawStyle.none,
					   type=type,
					   otherType=otherType,
					   color=color,
					   *args,
					   **kwargs
					   )

		'''
		Base Control class to be used in all parts classes.
		Created as a joint with nurbs shape node and default attributes.

		:param str None item:            Object that is parented to the control.
		:param str None wire:            Preset wire type.
		:param list None axis:           Forward axis of the control.
		:param int float None scale:     Scale of control. Default is 1.
		:param bool str None offset:     Create Offset Control
		'''

		# Control attributes
		self.item = item
		self.axis = axis
		self.offset = offset
		self.wire = wire
		self.wireScale = scale

	def create(self, *args, **kwargs):
		# Main Control
		result = createControl(name=self.longName,
							   shape=self.wire,
							   axis=self.axis,
							   scale=self.wireScale,
							   color=self.color,
							   )

		self.transform, self.shape = result
		self.disableSegmentScale()
		return

	def constrainItem(self, item=None, point=False, orient=False, scale=False, offset=True):
		if not item:
			if not self.item:
				raise RuntimeError('No valid item provided.'.format(self.item))
			else:
				item = self.item

		if point:
			cmds.pointConstraint(self.longName, item, mo=offset)
		if orient:
			cmds.orientConstraint(self.longName, item, mo=offset)
		if scale:
			cmds.scaleConstraint(self.longName, item, mo=offset)
		return

	def connectItem(self, item=None, translate=False, rotate=False, scale=False, offset=True):
		if not item:
			if not self.item:
				raise RuntimeError('No valid item provided.'.format(self.item))
			else:
				item = self.item

		if translate:
			pass
		if rotate:
			pass
		if scale:
			pass
		return


class CONTROL(Control):
	def __init__(self,
				 prefix=None,
				 side=None,
				 name='rigControl',
				 sector=None,
				 index=None,
				 kind=Component.control,
				 parent=None,
				 type=None,
				 otherType=None,
				 item=None,
				 wire=WireType.circleRotate,
				 axis=None,
				 scale=1.0,
				 color=WireColor.blue,
				 offset=False,
				 *args,
				 **kwargs
				 ):

		Control.__init__(self,
						 prefix=prefix,
						 side=side,
						 name=name,
						 sector=sector,
						 index=index,
						 kind=camelCase(kind, Component.control, capitalize=False),
						 parent=parent,
						 item=item,
						 wire=wire,
						 axis=axis,
						 scale=scale,
						 color=color,
						 type=type,
						 otherType=otherType,
						 *args,
						 **kwargs
						 )

		# Null Groups
		self.nullPosition = None
		self.nullConnection = None
		self.nullZero = None

		# Offset Control
		self.offset = offset
		self.offsetTransform = None
		self.offsetShape = None


	def create(self, *args, **kwargs):
		Control.create(self)

		# Offset Control
		if self.offset:
			offsetWire = self.wire

			if not isinstance(self.offset, bool) and hasattr(WireType, self.offset):
				offsetWire = self.offset

			offsetName = self.longName.replace('_{}'.format(self.kind),
											   '_{}_{}'.format(Component.offset, self.kind)
											   )
			resultOffset = createControl(name=offsetName,
										 shape=offsetWire,
										 axis=self.axis,
										 scale=self.wireScale * .8,
										 color=self.color,
										 kind=Component.offsetControl
										 )

			self.offsetTransform, self.offsetShape = resultOffset

			# Connect Offset Controls
			cmds.parent(self.offsetTransform, self.transform)

			attribute = UserAttr.offsetVisibility

			addAttribute(node=self.transform,
						 attribute=attribute,
						 kind=MayaAttrType.bool,
						 keyable=False,
						 channelBox=True,
						 destinationNode=self.offsetShape,
						 destinationAttribute=MayaAttr.visibility,
						 )

			createMonoRelationship(source=self.transform,
								   destination=self.offsetTransform,
								   sourceAttr=Component.offset,
								   destinationAttr=Component.parent,
								   )

		# Create Nulls
		nulls = createNull(longName(self.longName, Component.position),
						   longName(self.longName, Component.connection),
						   longName(self.longName, Component.zero),
						   child=self.transform,
						   )

		self.nullPosition, self.nullConnection, self.nullZero = nulls
		return

	def updateName(self):
		DagNode.updateName(self)

		self.nullPosition = cmds.rename(self.nullPosition,
										longName(self.longName, Component.position)
										)
		self.nullConnection = cmds.rename(self.nullConnection,
										  longName(self.longName, Component.connection)
										  )
		self.nullZero = cmds.rename(self.nullZero,
									longName(self.longName, Component.zero)
									)

		if self.offsetTransform:
			self.offsetTransform = cmds.rename(self.offsetTransform,
											   self.longName.replace('_{}'.format(self.longName.split('_')[-1]),
																	 '_{}'.format(
																		 Component.offsetControl)
																	 ))
		return

	def constrainItem(self):
		if self.item:
			if self.offsetTransform:
				constraint(self.offsetTransform, self.item, offset=True)
			elif self.transform:
				constraint(self.transform, self.item, offset=True)
			else:
				raise RuntimeError('Unable to constrain item "{}"'.format(self.item))
		else:
			raise RuntimeError('No valid item provided.'.format(self.item))

	def connectItem(self):
		if self.item:
			pass
		return

	def snapTo(self, node, translation=True, rotation=True):
		snap(node, self.nullPosition, t=translation, r=rotation)
		return

	def parentTo(self, node):
		cmds.parent(self.nullPosition, node)
		return


class CONTROL(Control):
	def __init__(self,
				 name=Component.rig,
				 parent=None,
				 prefix=None,
				 item=None,
				 wireType=WireType.circleRotate,
				 axis=None,
				 scale=1.0,
				 index=None,
				 side=None,
				 sector=None,
				 color=WireColor.blue,
				 offset=False,
				 kind=None,
				 ):
		Control.__init__(self,
						 name=name,
						 parent=parent,
						 prefix=prefix,
						 item=item,
						 wire=wireType,
						 axis=axis,
						 scale=scale,
						 index=index,
						 side=side,
						 sector=sector,
						 color=color,
						 offset=offset,
						 kind=camelCase(kind, Component.control, capitalize=False),
						 )

		self.setDefaults()

	def setDefaults(self):
		for item in [self.transform, self.offsetTransform]:
			if item:
				addAttribute(node=item, attribute=Component.rigPart, value=self.prefix, kind=MayaAttrType.string,
							 lock=True)

				for attr in [Component.parent,
							 Component.rig,
							 ]:
					if not attributeExist(item, attr):
						addAttribute(node=item, attribute=attr, kind=MayaAttrType.message)

				for attr in [Component.children]:
					if not attributeExist(item, attr):
						addAttribute(node=item, attribute=attr, kind=MayaAttrType.string, lock=True)
		return


class FKCONTROL(CONTROL):
	def __init__(self,
				 name=Component.rig,
				 parent=None,
				 prefix=None,
				 item=None,
				 wireType=WireType.circleRotate,
				 axis=None,
				 scale=1.0,
				 index=None,
				 side=None,
				 sector=None,
				 color=None,
				 ):

		if color is None:
			if side == Position.left:
				color = WireColor.blue
			elif side == Position.right:
				color = WireColor.red
			elif side == Position.center:
				color = WireColor.yellow
			else:
				color = WireColor.blue

		CONTROL.__init__(self,
						 name=name,
						 parent=parent,
						 prefix=prefix,
						 item=item,
						 wireType=wireType,
						 axis=axis,
						 scale=scale,
						 index=index,
						 side=side,
						 sector=sector,
						 offset=True,
						 kind=Component.fk,
						 color=color,
						 )


class IKCONTROL(CONTROL):
	def __init__(self,
				 name=Component.rig,
				 parent=None,
				 prefix=None,
				 item=None,
				 wireType=WireType.sphere,
				 axis=None,
				 scale=1.0,
				 index=None,
				 side=None,
				 sector=None,
				 color=None,
				 ):

		if color is None:
			if side == Position.left:
				color = WireColor.cyan
			elif side == Position.right:
				color = WireColor.magenta
			elif side == Position.center:
				color = WireColor.green
			else:
				color = WireColor.red

		CONTROL.__init__(self,
						 name=name,
						 parent=parent,
						 prefix=prefix,
						 item=item,
						 wireType=wireType,
						 axis=axis,
						 scale=scale,
						 index=index,
						 side=side,
						 sector=sector,
						 color=color,
						 offset=True,
						 kind=Component.ik,
						 )


class RIGCONTROL(CONTROL):
	def __init__(self,
				 name=Component.rig,
				 parent=None,
				 prefix=None,
				 item=None,
				 wireType=WireType.master,
				 axis=None,
				 scale=1.0,
				 index=None,
				 side=None,
				 sector=None,
				 offset=False,
				 ):
		CONTROL.__init__(self,
						 name=name,
						 parent=parent,
						 prefix=prefix,
						 item=item,
						 wireType=wireType,
						 axis=axis,
						 scale=scale,
						 index=index,
						 side=side,
						 sector=sector,
						 color=WireColor.purple,
						 kind=Component.rig,
						 offset=offset
						 )

	def setDefaults(self):
		CONTROL.setDefaults(self)

		item = self.transform

		for attr in [Component.joint,
					 ]:

			if not attributeExist(item, attr):
				addAttribute(node=item, attribute=attr, kind=MayaAttrType.string, lock=True)

		for attr in [Component.fkControl,
					 Component.ikControl,
					 Component.ikJoint,
					 Component.bindControl,
					 Component.leafControl,
					 ]:

			if not attributeExist(item, attr):
				addAttribute(node=item, attribute=attr, kind=MayaAttrType.string, array=True)

		for attr in [Component.bindTwist,
					 Component.fkStretch,
					 Component.ikStretch,
					 Component.bindStretch,
					 Component.bindSns,
					 ]:

			if not attributeExist(item, attr):
				addAttribute(node=item, attribute=attr, kind=MayaAttrType.float, array=True,
							 keyable=False)

		for attr in [Component.fkik,
					 Component.fkLocalWorld,
					 Component.ikLocalWorld,
					 Component.twistAuto,
					 Component.twist,
					 Component.stretchAuto,
					 Component.stretch,
					 Component.snsAuto,
					 Component.sns,
					 ]:

			if not attributeExist(item, attr):
				minValue = None
				maxValue = None
				defaultValue = None

				if 'local' in attr.lower():
					minValue = 0
					maxValue = 1
					defaultValue = 0

				elif 'auto' in attr.lower():
					minValue = 0
					maxValue = 1
					defaultValue = 1

				elif Component.fkik == attr:
					minValue = 0
					maxValue = 1
					defaultValue = 0

				addAttribute(node=item, attribute=attr, kind=MayaAttrType.float, minValue=minValue, maxValue=maxValue,
							 value=defaultValue, channelBox=False, keyable=True)

		for attr in [Component.mirror,
					 Component.fkPoleVector,
					 Component.ikPoleVector,
					 Component.ikHandle,
					 Component.set,
					 ]:

			if not attributeExist(item, attr):
				addAttribute(node=item, attribute=attr, kind=MayaAttrType.message)

		for attr in [Component.jointDisplay, Component.controlDisplay, Component.detailControlDisplay]:
			if not attributeExist(item, attr):
				addAttribute(node=item, attribute=attr, kind=MayaAttrType.bool, channelBox=True, keyable=False)
		return


class BINDCONTROL(CONTROL):
	def __init__(self,
				 name=Component.rig,
				 parent=None,
				 prefix=None,
				 item=None,
				 wireType=WireType.doubleLollipop,
				 axis=None,
				 scale=1.0,
				 index=None,
				 side=None,
				 sector=None,
				 ):
		CONTROL.__init__(self,
						 name=name,
						 parent=parent,
						 prefix=prefix,
						 item=item,
						 wireType=wireType,
						 axis=axis,
						 scale=scale * 1.5,
						 index=index,
						 side=side,
						 sector=sector,
						 color=[.5, 1, 1],
						 kind=Component.bind,
						 )


class LEAFCONTROL(CONTROL):
	def __init__(self,
				 name=Component.rig,
				 parent=None,
				 prefix=None,
				 item=None,
				 wireType=WireType.diamond,
				 axis=None,
				 scale=1.0,
				 index=None,
				 side=None,
				 sector=None,
				 ):
		CONTROL.__init__(self,
						 name=name,
						 parent=parent,
						 prefix=prefix,
						 item=item,
						 wireType=wireType,
						 axis=axis,
						 scale=scale,
						 index=index,
						 side=side,
						 sector=sector,
						 color=[.5, 1, 1],
						 kind=Component.leaf,
						 )
