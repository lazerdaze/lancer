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
	             color=WireColor.blue,
	             offset=False,
	             *args,
	             **kwargs
	             ):
		# Null Groups
		self._nullPosition = None
		self._nullConnection = None
		self._nullZero = None

		# Offset Control
		self.createOffset = offset
		self._offset = None

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

		if not self.wrapper:
			self.createNulls()

	def create(self, *args, **kwargs):
		Control.create(self)

		# Offset Control
		if self.createOffset:
			offsetWire = self.wire

			if isinstance(self.createOffset, str) and hasattr(WireType, self.createOffset):
				offsetWire = self.createOffset

			self.offset = Control(prefix=self.prefix,
			                      side=self._side,
			                      name=self.name,
			                      sector=self.sector,
			                      index=self.index,
			                      kind=Component.offsetControl,
			                      axis=self.axis,
			                      scale=self.wireScale * .8,
			                      color=self.color,
			                      parent=self.transform,
			                      wire=offsetWire,
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

	def createNulls(self):
		# Create Nulls
		nullList = []
		i = 0
		for null in [Component.position, Component.connection, Component.zero]:
			nullNode = DagNode(prefix=self.prefix,
			                   side=self.side,
			                   name=self.name,
			                   sector=self.sector,
			                   index=self.index,
			                   kind=null,
			                   )

			if i != 0:
				nullNode.parent = nullList[i - 1]

			nullList.append(nullNode)
			i += 1

		self.nullPosition, self.nullConnection, self.nullZero = nullList
		cmds.parent(self.longName, self._nullZero)
		return nullList

	####################################################################################################################
	# Null Properties
	####################################################################################################################

	@property
	def nullPosition(self):
		attr = Component.position

		if self._nullPosition:
			return self._nullPosition

		if self.isValid():
			if attributeExist(self.longName, attr):
				return getConnectedNode(self.longName, attr)

	@nullPosition.setter
	def nullPosition(self, null):
		if self.isValid():
			createRelationship(source=self.longName,
			                   sourceAttr=Component.position,
			                   destination=null,
			                   destinationAttr='rigParent',
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
			createRelationship(source=self.longName,
			                   sourceAttr=Component.connection,
			                   destination=null,
			                   destinationAttr='rigParent',
			                   )

		self._nullConnection = null
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
			createRelationship(source=self.longName,
			                   sourceAttr=Component.zero,
			                   destination=null,
			                   destinationAttr='rigParent',
			                   )

		self._nullZero = null
		return

	####################################################################################################################
	# Offset Property
	####################################################################################################################

	@property
	def offset(self):
		attr = Component.offset

		if self._offset:
			return self._offset
		else:
			if self.isValid():
				if attributeExist(self.longName, attr):
					return getConnectedNode(self.longName, attr)

	@offset.setter
	def offset(self, offset):
		if self.isValid():
			createMonoRelationship(source=self.longName,
			                       sourceAttr=Component.offset,
			                       destination=offset,
			                       destinationAttr='rigParent',
			                       )
		self._offset = offset
		return

	####################################################################################################################
	# Methods
	####################################################################################################################

	def constrainItem(self, *args, **kwargs):
		if self._offset:
			self._offset.contrainItem(*args, **kwargs)
		else:
			Control.constrainItem(self, *args, **kwargs)
		return

	def connectItem(self, *args, **kwargs):
		if self._offset:
			self._offset.connectItem(*args, **kwargs)
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
		if self.isValid():
			if parent and nodeExists(parent):
				cmds.parent(self._nullPosition, parent)
		self._parent = parent
		return

	@property
	def children(self):
		if self.isValid():
			if self.offset:
				return nodeChildren(self.offset.transform)
			else:
				return nodeChildren(self.transform)
		return self._children

	@children.setter
	def children(self, children):
		children = flatList(children)

		if self.isValid():
			if self.offset:
				cmds.parent(children, self.offset.transform)
			else:
				cmds.parent(children, self.transform)

		for child in children:
			if child not in self._children:
				self._children.append(child)
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
	             wire=WireType.master,
	             axis=None,
	             scale=1.0,
	             index=None,
	             side=None,
	             kind='interface',
	             sector=None,
	             offset=False,
	             ):

		RIGCONTROL.__init__(self,
		                    name=name,
		                    parent=parent,
		                    prefix=prefix,
		                    item=item,
		                    wire=wire,
		                    axis=axis,
		                    scale=scale,
		                    index=index,
		                    side=side,
		                    sector=sector,
		                    color=WireColor.purple,
		                    kind=kind,
		                    offset=offset,
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

		# Child Controls
		self._childControl = []
		self._grandchildControl = []

	####################################################################################################################
	# Properties
	####################################################################################################################

	@property
	def joint(self):
		if self._joint:
			return self._joint

		if self.isValid():
			if attributeExist(self, Component.joint):
				getConnectedNode(self, Component.joint)
		return self._joint

	@joint.setter
	def joint(self, joints):
		joints = flatList(joints)

		if self.isValid():
			for joint in joints:
				createRelationship(source=self.longName,
				                   sourceAttr=Component.joint,
				                   destination=joint,
				                   destinationAttr='rigInterface',
				                   )

		for joint in joints:
			if joint not in self._joint:
				self._joint.append(joint)
		return

	@property
	def set(self):
		if self._set:
			return self._joint

		if self.isValid():
			if attributeExist(self, Component.set):
				getConnectedNode(self, Component.set)
		return self._set

	@set.setter
	def set(self, set):
		if self.isValid():
			createRelationship(source=self.longName,
			                   sourceAttr=Component.set,
			                   destination=set,
			                   destinationAttr='rigInterface',
			                   )
		self._set = set
		return

	@property
	def opposite(self):
		if self._opposite:
			return self._opposite

		if self.isValid():
			if attributeExist(self, Component.opposite):
				getConnectedNode(self, Component.opposite)

		return self._opposite

	@opposite.setter
	def opposite(self, opposite):
		if self.isValid():
			createMonoRelationship(source=self.longName,
			                       sourceAttr=Component.opposite,
			                       destination=opposite,
			                       destinationAttr=Component.opposite,
			                       )

		self._opposite = opposite
		return

	####################################################################################################################
	# Child Control Properties
	####################################################################################################################

	@property
	def childControl(self):
		if self._childControl:
			return self._childControl

		if self.isValid():
			if attributeExist(self, Component.childControl):
				getConnectedNode(self, Component.childControl)

		return self._childControl

	@childControl.setter
	def childControl(self, children):
		children = flatList(children)

		if self.isValid():
			for child in children:
				createRelationship(source=self.longName,
				                   sourceAttr=Component.child,
				                   destination=child,
				                   destinationAttr='rigInterface',
				                   )

		for child in children:
			if child not in self._childControl:
				self._childControl.append(child)
		return

	@property
	def grandchildControl(self):
		if self._grandchildControl:
			return self._grandchildControl

		if self.isValid():
			if attributeExist(self, Component.grandchildControl):
				getConnectedNode(self, Component.grandchildControl)

		return self._grandchildControl

	@grandchildControl.setter
	def grandchildControl(self, grandchildren):
		grandchildren = flatList(grandchildren)

		if self.isValid():
			for grandchild in grandchildren:
				createRelationship(source=self.longName,
				                   sourceAttr=Component.grandchildControl,
				                   destination=grandchild,
				                   destinationAttr='rigInterface',
				                   )

		for grandchild in grandchildren:
			if grandchild not in self._grandchildControl:
				self._grandchildControl.append(grandchild)
		return

	####################################################################################################################
	# FK Properties
	####################################################################################################################

	@property
	def fkControl(self):
		if self._fkControl:
			return self._fkControl

		if self.isValid():
			if attributeExist(self, Component.fkControl):
				getConnectedNode(self, Component.fkControl)

		return self._fkControl

	@fkControl.setter
	def fkControl(self, fkControls):
		fkControls = flatList(fkControls)

		if self.isValid():
			for fkControl in fkControls:
				createRelationship(source=self.longName,
				                   sourceAttr=Component.fkControl,
				                   destination=fkControl,
				                   destinationAttr='rigInterface',
				                   )

		for fkControl in fkControls:
			if fkControl not in self._fkControl:
				self._fkControl.append(fkControl)
		return

	@property
	def fkPoleVector(self):
		if self._fkPoleVector:
			return self._fkPoleVector

		if self.isValid():
			if attributeExist(self, Component.fkPoleVector):
				getConnectedNode(self, Component.fkPoleVector)

		return self._fkPoleVector

	@fkPoleVector.setter
	def fkPoleVector(self, fkPoleVector):
		if self.isValid():
			createRelationship(source=self.longName,
			                   sourceAttr=Component.fkPoleVector,
			                   destination=fkPoleVector,
			                   destinationAttr='rigInterface',
			                   )

		self._fkPoleVector = fkPoleVector
		return

	@property
	def fkStretch(self):
		return self._fkStretch

	@fkStretch.setter
	def fkStretch(self, fkStretch):
		self._fkStretch = fkStretch
		return

	@property
	def fkTopNode(self):
		if self._fkTopNode:
			return self._fkTopNode

		if self.isValid():
			if attributeExist(self, Component.fkTopNode):
				getConnectedNode(self, Component.fkTopNode)

		return self._fkTopNode

	@fkTopNode.setter
	def fkTopNode(self, fkTopNode):
		if self.isValid():
			createRelationship(source=self.longName,
			                   sourceAttr=Component.fkTopNode,
			                   destination=fkTopNode,
			                   destinationAttr='rigInterface',
			                   )

		self._fkTopNode = fkTopNode
		return

	####################################################################################################################
	# IK Properties
	####################################################################################################################

	@property
	def ikJoint(self):
		if self._ikJoint:
			return self._ikJoint

		if self.isValid():
			if attributeExist(self, Component.ikJoint):
				getConnectedNode(self, Component.ikJoint)

		return self._ikJoint

	@ikJoint.setter
	def ikJoint(self, ikJoints):
		ikJoints = flatList(ikJoints)

		if self.isValid():
			for ikJoint in ikJoints:
				createRelationship(source=self.longName,
				                   sourceAttr=Component.ikJoint,
				                   destination=ikJoint,
				                   destinationAttr='rigInterface',
				                   )

		for ikJoint in ikJoints:
			if ikJoint not in self._ikJoint:
				self._ikJoint.append(ikJoint)
		return

	@property
	def ikControl(self):
		if self._ikControl:
			return self._ikControl

		if self.isValid():
			if attributeExist(self, Component.ikControl):
				getConnectedNode(self, Component.ikControl)

		return self._ikControl

	@ikControl.setter
	def ikControl(self, ikControls):
		ikControls = flatList(ikControls)

		if self.isValid():
			for ikControl in ikControls:
				createRelationship(source=self.longName,
				                   sourceAttr=Component.ikControl,
				                   destination=ikControl,
				                   destinationAttr='rigInterface',
				                   )

		for ikControl in ikControls:
			if ikControl not in self._ikControl:
				self._ikControl.append(ikControl)
		return

	@property
	def ikPoleVector(self):
		if self._ikPoleVector:
			return self._ikPoleVector

		if self.isValid():
			if attributeExist(self, Component.ikPoleVector):
				getConnectedNode(self, Component.ikPoleVector)

		return self._ikPoleVector

	@ikPoleVector.setter
	def ikPoleVector(self, ikPoleVector):
		if self.isValid():
			createRelationship(source=self.longName,
			                   sourceAttr=Component.ikPoleVector,
			                   destination=ikPoleVector,
			                   destinationAttr='rigInterface',
			                   )

		self._ikPoleVector = ikPoleVector
		return

	@property
	def ikStretch(self):
		return self._ikStretch

	@ikStretch.setter
	def ikStretch(self, ikStretch):
		self._ikStretch = ikStretch
		return

	@property
	def ikTopNode(self):
		if self._ikTopNode:
			return self._ikTopNode

		if self.isValid():
			if attributeExist(self, Component.ikTopNode):
				getConnectedNode(self, Component.ikTopNode)

		return self._ikTopNode

	@ikTopNode.setter
	def ikTopNode(self, ikTopNode):
		if self.isValid():
			createRelationship(source=self.longName,
			                   sourceAttr=Component.ikTopNode,
			                   destination=ikTopNode,
			                   destinationAttr='rigInterface',
			                   )

		self._ikTopNode = ikTopNode
		return

	####################################################################################################################
	# Defaults
	####################################################################################################################

	def setDefaults(self):
		RIGCONTROL.setDefaults(self)

		# Array Attribute
		for attr in [Component.joint,
		             Component.fkControl,
		             Component.ikControl,
		             Component.ikJoint,
		             Component.childControl,
		             Component.grandchildControl,
		             ]:

			if not attributeExist(self.longName, attr):
				addAttribute(node=self.longName, attribute=attr, kind=MayaAttrType.string, array=True)

		for attr in [Component.childTwist,
		             Component.fkStretch,
		             Component.ikStretch,
		             Component.childStretch,
		             Component.childSns,
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
		for attr in [Component.opposite,
		             Component.topNode,
		             Component.fkTopNode,
		             Component.ikTopNode,
		             Component.fkPoleVector,
		             Component.ikPoleVector,
		             Component.ikHandle,
		             Component.set,
		             ]:

			if not attributeExist(self.longName, attr):
				addAttribute(node=self.longName, attribute=attr, kind=MayaAttrType.message)

		# Bool Attributes
		for attr in [Component.jointDisplay,
		             Component.controlDisplay,
		             Component.childControlDisplay,
		             ]:
			if not attributeExist(self.longName, attr):
				addAttribute(node=self.longName,
				             attribute=attr,
				             kind=MayaAttrType.bool,
				             channelBox=True,
				             keyable=False,
				             )
		return

	####################################################################################################################
	# Methods
	####################################################################################################################

	def mirror(self, *args, **kwargs):
		return

	def swap(self, *args, **kwargs):
		return

	def fkikSwitch(self, *args, **kwargs):
		return

	def resetToDefaults(self, *args, **kwargs):
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
	             wire=WireType.circleRotate,
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
		                    wire=wire,
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
	             wire=WireType.sphere,
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
		                    wire=wire,
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
	             wire=WireType.doubleLollipop,
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
		                    wire=wire,
		                    axis=axis,
		                    scale=scale * 1.5,
		                    index=index,
		                    side=side,
		                    sector=sector,
		                    color=[.5, 1, 1],
		                    kind=Component.child,
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
	             wire=WireType.diamond,
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
		                    wire=wire,
		                    axis=axis,
		                    scale=scale,
		                    index=index,
		                    side=side,
		                    sector=sector,
		                    color=[.5, 1, 1],
		                    kind=Component.grandChild,
		                    )
