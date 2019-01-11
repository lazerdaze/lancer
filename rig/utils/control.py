# Lancer Modules
from wire import *
from network import *
from constraint import *
from joint import *
from naming import *
from node import *

# Maya Modules
from maya import cmds


def createControl(name='control', shape=WireType.circle, axis=None, scale=1, color=None, kind=None):
	axis = axis if axis else [1, 0, 0]

	# Joint Node
	node = cmds.createNode('joint', name=name)
	cmds.setAttr('{}.segmentScaleCompensate'.format(node), 0)
	cmds.setAttr('{}.drawStyle'.format(node), 2)
	cmds.setAttr('{}.radius'.format(node), keyable=False, channelBox=False)
	cmds.setAttr('{}.v'.format(node), keyable=False, channelBox=True)
	cmds.setAttr('{}.rotateOrder'.format(node), k=False, channelBox=True)

	# Curve Shape
	curve = createWire(kind=shape, axis=axis)
	curveShape = cmds.rename(cmds.listRelatives(curve, shapes=True)[0],
	                         '{}Shape'.format(name))

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

	return [node, curveShape]


########################################################################################################################
#
#
#	Control Class
#
#
########################################################################################################################


class Control(Node):
	def __init__(self,
	             prefix='rig',
	             name=None,
	             item=None,
	             wire=WireType.circleRotate,
	             axis=None,
	             scale=1.0,
	             index=None,
	             side=None,
	             sector=None,
	             color=WireColor.blue,
	             offset=False,
	             kind=Component.control,
	             ):
		'''
		Base Control class to be used in all parts classes.
		Created as a joint with nurbs shape node and default attributes.

		:param str prefix:          Prefix name of the control
		:param str name:            Name of the control.
		:param str item:            Object that is parented to the control.
		:param str kind:            Label of the control to determine rig type.
		:param str wire:            Preset wire type.
		:param list axis:           Forward axis of the control.
		:param int, float scale:    Scale of control. Default is 1.
		:param int index:           Used to determined rig priority.
		:param str side:            Side of the controls origin.
		:param str sector:          Sector of control. Possible Sectors: "A", "B", "C"
		:param list color:          RGB Color of control.
		:param bool offset:         Create Offset Control
		'''

		Node.__init__(self,
		              name=name,
		              prefix=prefix,
		              kind=kind,
		              index=index,
		              side=side,
		              sector=sector,
		              color=color,
		              )

		self.item = item

		# Null Groups
		self.nullPosition = None
		self.nullConnection = None
		self.nullZero = None

		# Offset Control
		self.offset = None
		self.offsetTransform = None
		self.offsetShape = None

		# Init
		self._create(wire, axis, scale, side, index, sector, kind, color, offset)

	def _create(self, wire, axis, scale, side, index, sector, kind, color, offset):
		if not self.isValid():
			# Main Control
			result = createControl(name=self.longName,
			                       shape=wire,
			                       axis=axis,
			                       scale=scale,
			                       color=color,
			                       )
			self.transform, self.shape = result

			# Offset Control
			if offset:
				offsetName = self.longName.replace('_{}'.format(Component.control),
				                                   '_{}'.format(Component.offsetControl)
				                                   )
				resultOffset = createControl(
						name=offsetName,
						shape=wire,
						axis=axis,
						scale=scale * .90,
						color=color,
						kind=Component.offsetControl
				)

				self.offsetTransform, self.offsetShape = resultOffset

				# Add Offset Index Attribute
				if index is not None:
					addAttribute(self.offsetTransform,
					             attribute=UserAttr.index,
					             kind=MayaAttrType.int,
					             value=index,
					             lock=True,
					             )

				# Add Offset Sector Attribute
				if sector is not None:
					addAttribute(self.offsetTransform,
					             attribute=UserAttr.sector,
					             kind=MayaAttrType.string,
					             value=sector,
					             lock=True,
					             )

				# Set Offset Side Attributes
				sideValue = JointLabelSide.none
				if hasattr(JointLabelSide, side):
					sideValue = getattr(JointLabelSide, side)

				setAttribute(self.offsetTransform,
				             attribute=MayaAttr.side,
				             value=sideValue
				             )

				# Connect Offset Controls
				cmds.parent(self.offsetTransform, self.transform)

				attribute = UserAttr.offsetVisibility

				addAttribute(node=self.transform,
				             attribute=attribute,
				             kind=MayaAttrType.bool,
				             keyable=False,
				             channelBox=True,
				             destinationNode=self.offsetTransform,
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
			self.side = side
			self.index = index
			self.sector = sector
			self.kind = kind
			self.exists = True
		return

	def updateName(self):
		Node.updateName(self)

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
			constraint(self.offsetTransform, self.item, offset=True)
		return

	def connectItem(self):
		if self.item:
			pass
		return

	def snapTo(self, node, translation=True, rotation=True):
		snap(node, self.nullPosition, t=translation, r=rotation)
		return


########################################################################################################################
#
#
#	Master Control Class
#
#
########################################################################################################################

class MasterControl(Control):
	def __init__(self,
	             prefix='rig',
	             name=None,
	             scale=1,
	             index=None,
	             side=None,
	             sector=None,
	             ):
		Control.__init__(self,
		                 prefix=prefix,
		                 name=name,
		                 kind=Component.master,
		                 wire=WireType.lollipop,
		                 axis=[0, 1, 1],
		                 scale=scale,
		                 index=index,
		                 side=side,
		                 sector=sector,
		                 color=WireColor.purple,
		                 offset=False,
		                 )

	def masterAttributes(self):
		return
