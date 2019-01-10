# Lancer Modules
from wire import *
from error import *
from network import *
from constraint import *
from joint import *
from naming import *

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
				 kind=Component.control,
				 wire=WireType.circleRotate,
				 axis=None,
				 scale=1,
				 index=None,
				 side=None,
				 sector=None,
				 color=WireColor.blue,
				 offset=False,
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
		self.create(wire, axis, scale, index, sector, color, offset)

	def create(self, wire, axis, scale, index, sector, color, offset):
		if not self.isValid():

			# Main Control
			result = createControl(name=self.name,
								   shape=wire,
								   axis=axis,
								   scale=scale,
								   color=color,
								   )
			self.transform = result[0]
			self.shape = result[1]

			# Add Index Attribute
			if index is not None:
				addIndexAttribute(self.transform, index)

			# Add Sector
			if sector is not None:
				addAttribute(self.transform,
							 attribute=UserAttr.sector,
							 kind=MayaAttrType.string,
							 value=sector,
							 )

			# Add Side
			if self.side is not None:
				setAttribute(self.transform, attribute=MayaAttr.side, value=getattr(JointLabelSide, self.side))
			else:
				setAttribute(self.transform, attribute=MayaAttr.side, value=JointLabelSide.none)

			# Offset Control
			if offset:
				resultOffset = createControl(
					name=self.name.replace(Component.control, longName(Component.offset, Component.control)),
					shape=wire,
					axis=axis,
					scale=scale * .75,
					color=color,
				)

				self.offsetTransform = resultOffset[0]
				self.offsetShape = resultOffset[1]

				# Add Offset Index Attribute
				if index is not None:
					addAttribute(self.offsetTransform,
								 attribute=UserAttr.index,
								 kind=MayaAttrType.int,
								 value=index,
								 )

				# Add Offset Sector
				if sector is not None:
					addAttribute(self.offsetTransform,
								 attribute=UserAttr.sector,
								 kind=MayaAttrType.string,
								 value=sector,
								 )

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
			nulls = createNull(longName(self.name, Component.position),
							   longName(self.name, Component.connection),
							   longName(self.name, Component.zero),
							   node=self.transform,
							   )

			self.nullPosition = nulls[0]
			self.nullConnection = nulls[1]
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
