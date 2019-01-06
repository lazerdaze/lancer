# LANCER.RIG.CONTROL
#
#
#
#
#

# Lancer Modules
from wire import *
from general import *

# Maya Modules
from maya import cmds


def createControl(name='control0', shape=WireType.circle, axis=None, scale=1):
	axis = axis if axis else [1, 0, 0]

	# Joint Node
	node = cmds.createNode('joint', name=name)
	cmds.setAttr('{}.segmentScaleCompensate'.format(node), 0)
	cmds.setAttr('{}.drawStyle'.format(node), 2)
	cmds.setAttr('{}.radius'.format(node), keyable=False, channelBox=False)
	cmds.setAttr('{}.v'.format(node), keyable=False, channelBox=False)
	cmds.setAttr('{}.rotateOrder'.format(node), k=True)

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

	return [node, curveShape]


########################################################################################################################
#
#
#	Control Class
#
#
########################################################################################################################


class Control(Node):
	def __init__(self, name='oontrol0', wire=WireType.circle, axis=None, scale=1):
		Node.__init__(self, name=name, kind=Component.control)

		self.create(wire, axis, scale)

	def create(self, wire, axis, scale):
		if not self.isValid():
			result = createControl(name=self.name, shape=wire, axis=axis, scale=scale)
			self.transform = result[0]
			self.shape = result[1]
			self.exists = True
		else:
			raise NodeExistsError('Control already exists.')
		return
