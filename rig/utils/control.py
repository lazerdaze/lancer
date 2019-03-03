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
		self.rigPart = self.prefix
		self.disableSegmentScale()
		return

	####################################################################################################################
	# Methods
	####################################################################################################################

	def constrainItem(self, *args, **kwargs):
		item = kwargs.get('item', None)
		point = kwargs.get('point', False)
		orient = kwargs.get('orient', False)
		scale = kwargs.get('scale', False)
		offset = kwargs.get('offset', False)

		# Edge Case
		if not item:
			if not self.item:
				raise RuntimeError('No valid item provided.'.format(self.item))
			else:
				item = self.item

		if not self.isValid():
			raise RuntimeError('Node "{}" does not have a valid transform.'.format(self.longName))

		else:
			if point:
				cmds.pointConstraint(self.longName, item, mo=offset)
			if orient:
				cmds.orientConstraint(self.longName, item, mo=offset)
			if scale:
				cmds.scaleConstraint(self.longName, item, mo=offset)
		return

	def connectItem(self, *args, **kwargs):
		item = kwargs.get('item', None)
		translate = kwargs.get('translate', False)
		rotate = kwargs.get('rotate', False)
		scale = kwargs.get('scale', False)
		offset = kwargs.get('offset', False)

		# Edge Case
		if not item:
			if not self.item:
				raise RuntimeError('No valid item provided.'.format(self.item))
			else:
				item = self.item

		if not self.isValid():
			raise RuntimeError('Node "{}" does not have a valid transform.'.format(self.longName))

		else:
			if translate:
				connectTranslate(source=self.longName,
								 destination=item,
								 offset=offset,
								 )
			if rotate:
				connectRotate(source=self.longName,
							  destination=item,
							  offset=offset,
							  )
			if scale:
				connectScale(source=self.longName,
							 destination=item,
							 offset=offset,
							 )
		return


########################################################################################################################
#
#
#	Rig Control Class
#
#
########################################################################################################################

class RIGCONTROL(Control):
	def __init__(self,
				 prefix=None,
				 side=None,
				 name=Component.rig,
				 sector=None,
				 index=None,
				 kind=None,
				 parent=None,
				 type=None,
				 otherType=None,
				 item=None,
				 wire=WireType.circleRotate,
				 axis=None,
				 scale=1.0,
				 color=None,
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
		self._nullPosition = None
		self._nullConnection = None
		self._nullZero = None

		# Offset Control
		self.createOffset = offset
		self.offset = None

	def create(self, *args, **kwargs):
		Control.create(self)

		# Offset Control
		if self.createOffset:
			offsetWire = self.wire

			if not isinstance(self.createOffset, bool) and hasattr(WireType, self.createOffset):
				offsetWire = self.createOffset

			self.offset = Control(prefix=self.prefix,
								  side=self.side,
								  name=self.name,
								  sector=self.sector,
								  index=self.index,
								  kind=camelCase(Component.offset, self.kind, capitalize=False),
								  shape=offsetWire,
								  axis=self.axis,
								  scale=self.wireScale * .8,
								  color=self.color,
								  parent=self.transform,
								  type=self.type,
								  otherType=self.type,
								  wire=WireType.circleRotate,
								  )

			# Connect Offset Controls
			addAttribute(node=self.transform,
						 attribute=UserAttr.offsetVisibility,
						 kind=MayaAttrType.bool,
						 keyable=False,
						 channelBox=True,
						 destinationNode=self.offset.shape,
						 destinationAttribute=MayaAttr.visibility,
						 )

			createMonoRelationship(source=self.transform,
								   destination=self.offset.transform,
								   sourceAttr=Component.offset,
								   destinationAttr=Component.parent,
								   )

		# Create Nulls
		nullList = []

		i = 0
		for null in [Component.position, Component.connection, Component.zero]:
			nullNode = DagNode(prefix=self.prefix,
							   side=self.side,
							   name=self.name,
							   sector=self.sector,
							   index=self.index,
							   kind=camelCase(self.kind, null, capitalize=False),
							   )

			if i != 0:
				nullNode.parent = nullList[i - 1]

			nullList.append(nullNode)
			i += 1

		self.nullPosition, self.nullConnection, self.nullZero = nullList
		cmds.parent(self.longName, self._nullZero)
		return

	####################################################################################################################
	# Null Properties
	####################################################################################################################

	@property
	def nullPosition(self):
		attr = Component.position

		if self.isValid():
			if attributeExist(self.longName, attr):
				return getConnectedNode(self.longName, attr)
		return self._nullPosition

	@nullPosition.setter
	def nullPosition(self, null):
		if self.isValid():
			createMonoRelationship(source=self.longName,
								   destination=null,
								   sourceAttr=Component.position,
								   destinationAttr=Component.parent
								   )

		self._nullPosition = null
		return

	@property
	def nullConnection(self):
		attr = Component.connection

		if self.isValid():
			if attributeExist(self.longName, attr):
				return getConnectedNode(self.longName, attr)
		return self._nullConnection

	@nullConnection.setter
	def nullConnection(self, null):
		if self.isValid():
			createMonoRelationship(source=self.longName,
								   destination=null,
								   sourceAttr=Component.connection,
								   destinationAttr=Component.parent
								   )

		self._nullPosition = null
		return

	@property
	def nullZero(self):
		attr = Component.zero

		if self.isValid():
			if attributeExist(self.longName, attr):
				return getConnectedNode(self.longName, attr)
		return self._nullZero

	@nullZero.setter
	def nullZero(self, null):
		if self.isValid():
			createMonoRelationship(source=self.longName,
								   destination=null,
								   sourceAttr=Component.zero,
								   destinationAttr=Component.parent
								   )

		self._nullPosition = null
		return

	####################################################################################################################
	# Methods
	####################################################################################################################

	def constrainItem(self, *args, **kwargs):
		if self.offset:
			self.offset.contrainItem(*args, **kwargs)
		else:
			Control.constrainItem(self, *args, **kwargs)
		return

	def connectItem(self, *args, **kwargs):
		if self.offset:
			self.offset.connectItem(*args, **kwargs)
		else:
			Control.connectItem(self, *args, **kwargs)
		return

	def snapTo(self, item, translation=True, rotation=True):
		snap(item, self._nullPosition, t=translation, r=rotation)
		return

	@property
	def parent(self):
		if self.isValid():
			return nodeParent(self._nullPosition)
		return self._parent

	@parent.setter
	def parent(self, parent):
		self._parent = str(parent)

		if self.isValid() and nodeExists(parent):
			cmds.parent(self._nullPosition, parent)
		return


########################################################################################################################
#
#
#	Interface Control Class
#
#
########################################################################################################################

class INTERFACE_CONTROL(RIGCONTROL):
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

		RIGCONTROL.__init__(self,
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
							kind='interface',
							offset=offset
							)

		# Hierarchy
		self._joint = []
		self._set = None
		self._opposite = None

		# FK
		self._fkControl = []
		self._fkPoleVector = None
		self._fkStretch = None
		self._fkTopNode = None

		# IK
		self._ikControl = []
		self._ikJoint = []
		self._ikHandle = None
		self._ikPoleVector = None
		self._ikStretch = []
		self._ikTopNode = None

		# Detail
		self._childControl = []
		self._grandchildControl = []

	def setDefaults(self):
		RIGCONTROL.setDefaults(self)

		# Array Attribute
		for attr in [Component.joint,
					 Component.fkControl,
					 Component.ikControl,
					 Component.ikJoint,
					 Component.bindControl,
					 Component.leafControl,
					 ]:

			if not attributeExist(self.longName, attr):
				addAttribute(node=self.longName, attribute=attr, kind=MayaAttrType.string, array=True)

		for attr in [Component.bindTwist,
					 Component.fkStretch,
					 Component.ikStretch,
					 Component.bindStretch,
					 Component.bindSns,
					 ]:

			if not attributeExist(self.longName, attr):
				addAttribute(node=self.longName, attribute=attr, kind=MayaAttrType.float, array=True,
							 keyable=False)

		# Float Attributes
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

			if not attributeExist(self.longName, attr):
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

				addAttribute(node=self.longName,
							 attribute=attr,
							 kind=MayaAttrType.float,
							 minValue=minValue,
							 maxValue=maxValue,
							 value=defaultValue,
							 channelBox=False,
							 keyable=True
							 )

		# Message Attriibutes
		for attr in [Component.mirror,
					 Component.fkPoleVector,
					 Component.ikPoleVector,
					 Component.ikHandle,
					 Component.set,
					 ]:

			if not attributeExist(self.longName, attr):
				addAttribute(node=self.longName, attribute=attr, kind=MayaAttrType.message)

		# Bool Attributes
		for attr in [Component.jointDisplay, Component.controlDisplay, Component.detailControlDisplay]:
			if not attributeExist(self.longName, attr):
				addAttribute(node=self.longName,
							 attribute=attr,
							 kind=MayaAttrType.bool,
							 channelBox=True,
							 keyable=False,
							 )
		return


########################################################################################################################
#
#
#	FK Control Class
#
#
########################################################################################################################

class FKCONTROL(RIGCONTROL):
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

		RIGCONTROL.__init__(self,
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


########################################################################################################################
#
#
#	IK Control Class
#
#
########################################################################################################################

class IKCONTROL(RIGCONTROL):
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

		RIGCONTROL.__init__(self,
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


########################################################################################################################
#
#
#	Child Control Class
#
#
########################################################################################################################
class CHILDCONTROL(RIGCONTROL):
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
		RIGCONTROL.__init__(self,
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


########################################################################################################################
#
#
#	Grandchild Control Class
#
#
########################################################################################################################

class GRANDCHILDCONTROL(RIGCONTROL):
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
		RIGCONTROL.__init__(self,
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
