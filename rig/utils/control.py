# Lancer Modules
from wire import *
from general import *
from node import *
from error import *
from network import *
from constraint import *

# Maya Modules
from maya import cmds


def createControl(name='control', shape=WireType.circle, axis=None, scale=1, index=0, color=None):
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

	# Add Index Attribute
	addIndexAttribute(node, index)

	# Add Kind Attribute
	addAttribute(node=node,
	             attribute=UserAttr.kind,
	             kind=MayaAttrType.string,
	             value=Component.control,
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
	             name='rig',
	             item=None,
	             kind=Component.control,
	             wire=WireType.circleRotate,
	             axis=None,
	             scale=1,
	             index=0,
	             side=None,
	             color=WireColor.blue,
	             ):
		Node.__init__(self,
		              name=name,
		              kind=kind,
		              index=index,
		              side=side,
		              color=color
		              )

		self.item = item

		# Null Groups
		self.nullOrigin = None
		self.nullOffset = None
		self.nullZero = None

		# Offset Control
		self.offset = None
		self.offsetTransform = None
		self.offsetShape = None

		# Init
		self.create(wire, axis, scale, index, color)

	def create(self, wire, axis, scale, index, color):
		if not self.isValid():

			# Main Control
			result = createControl(name=self.name,
			                       shape=wire,
			                       axis=axis,
			                       scale=scale,
			                       index=index,
			                       color=color,
			                       )
			self.transform = result[0]
			self.shape = result[1]

			# Offset Control
			resultOffset = createControl(
					name=self.name.replace(Component.control, longName(Component.offset, Component.control)),
					shape=wire,
					axis=axis,
					scale=scale * .75,
					index=index,
					color=color,
			)

			self.offsetTransform = resultOffset[0]
			self.offsetShape = resultOffset[1]

			# Connect Controls
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
			nulls = createNull(longName(self.name, Component.origin),
			                   longName(self.name, Component.offset),
			                   longName(self.name, Component.zero),
			                   node=self.transform,
			                   )

			self.nullOrigin = nulls[0]
			self.nullOffset = nulls[1]
			self.nullZero = nulls[2]

			self.exists = True
		else:
			raise NodeExistsError('Control already exists.')
		return

	def constrainItem(self):
		if self.item:
			constraint(self.offsetTransform, self.item, offset=True)
		return

	def connectItem(self):
		return


########################################################################################################################
#
#
#	FK Control Class
#
#
########################################################################################################################


class FKControl(Control):
	def __init__(self,
	             name='rig',
	             axis=None,
	             scale=1,
	             index=0,
	             side=None,
	             wire=WireType.circleRotate,
	             color=WireColor.blue,
	             ):
		Control.__init__(self,
		                 name=name,
		                 kind=Component.fkControl,
		                 wire=wire,
		                 axis=axis,
		                 scale=scale,
		                 index=index,
		                 side=side,
		                 color=color,
		                 )


########################################################################################################################
#
#
#	IK Control Class
#
#
########################################################################################################################

class IKControl(Control):
	def __init__(self,
	             name='rig',
	             axis=None,
	             scale=1,
	             index=0,
	             side=None,
	             wire=WireType.sphere,
	             color=WireColor.red,
	             ):
		Control.__init__(self,
		                 name=name,
		                 kind=Component.ikControl,
		                 wire=wire,
		                 axis=axis,
		                 scale=scale,
		                 index=index,
		                 side=side,
		                 color=color,
		                 )


########################################################################################################################
#
#
#	Master Control Class
#
#
########################################################################################################################

class MasterControl(Control):
	def __init__(self,
	             name='rig',
	             axis=None,
	             scale=1,
	             index=0,
	             side=None,
	             wire=WireType.lollipop,
	             color=WireColor.purple,
	             ):
		Control.__init__(self,
		                 name=name,
		                 kind=Component.masterControl,
		                 wire=wire,
		                 axis=axis,
		                 scale=scale,
		                 index=index,
		                 side=side,
		                 color=color,
		                 )


########################################################################################################################
#
#
#	Detail Control Class
#
#
########################################################################################################################

class DetailControl(Control):
	def __init__(self,
	             name='rig',
	             axis=None,
	             scale=1,
	             index=0,
	             side=None,
	             wire=WireType.doubleLollipop,
	             color=WireColor.lightBlue,
	             ):
		Control.__init__(self,
		                 name=name,
		                 kind=Component.detailControl,
		                 wire=wire,
		                 axis=axis,
		                 scale=scale,
		                 index=index,
		                 side=side,
		                 color=color,
		                 )
