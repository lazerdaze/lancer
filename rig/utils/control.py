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


class Control(Node):
	def __init__(self,
	             name='rig',
	             parent=None,
	             prefix=None,
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

		:param str None prefix:          Prefix name of the control
		:param str None name:            Name of the control.
		:param str None item:            Object that is parented to the control.
		:param str None kind:            Label of the control to determine rig type.
		:param str None wire:            Preset wire type.
		:param list None axis:           Forward axis of the control.
		:param int float None scale:     Scale of control. Default is 1.
		:param int None index:           Used to determined rig priority.
		:param str None side:            Side of the controls origin.
		:param str None sector:          Sector of control. Possible Sectors: "A", "B", "C"
		:param list None color:          RGB Color of control.
		:param bool offset:              Create Offset Control
		'''

		Node.__init__(self,
		              name=name,
		              parent=parent,
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
		self.offsetTransform = None
		self.offsetShape = None

		# Init
		if not nodeExists(name):
			self.create(wire, axis, scale, color, offset)

	def create(self, wire, axis, scale, color, offset):
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
			offsetName = self.longName.replace('_{}'.format(self.kind),
			                                   '_{}_{}'.format(Component.offset, self.kind)
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

		self.side = self._side
		self.index = self._index
		self.sector = self._sector
		self.kind = self._kind
		self.canUpdateName = True
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
