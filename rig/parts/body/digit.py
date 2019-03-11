# Lancer Modules
from rig.utils import *
from rig.parts.baseRig import BASERIG

# Maya Modules
from maya import cmds


# TODO: Create "Uber" Plugin Node that handles Curl, Spread, etc - Pose SDK

class DIGIT(BASERIG):
	def __init__(self,
				 items,
				 prefix=Part.digit,
				 side=Position.left,
				 name=None,
				 sector=None,
				 index=None,
				 parent=None,
				 root=None,
				 ):

		metacarpal = None

		if len(items) == 4:
			metacarpal = items[0]
			items.remove(metacarpal)

		self.metacarpalItem = metacarpal
		self.metacarpalChild = []
		self.metacarpalGrandchild = []
		self._metacarpalJoint = None

		BASERIG.__init__(self,
						 prefix=prefix,
						 side=side,
						 name=name,
						 sector=sector,
						 index=index,
						 items=items,
						 parent=parent,
						 root=root,
						 axis=[1, 1, 0],
						 )

	####################################################################################################################
	# Properties
	####################################################################################################################
	@property
	def metacarpalJoint(self):
		if self._metacarpalJoint:
			return self._metacarpalJoint

		if self.interface:
			if attributeExist(self.interface, 'metacarpalJoint'):
				return getConnectedNode(self.interface, 'metacarpalJoint')

		return self._metacarpalJoint

	@metacarpalJoint.setter
	def metacarpalJoint(self, joint):
		if self.interface:
			self.connectToInterface(child=joint,
									interface=self.interface,
									attribute='metacarpalJoint'
									)

		self._metacarpalJoint = joint
		return

	####################################################################################################################
	# Methods
	####################################################################################################################

	def create(self):
		# Scale
		self.scale = self.scaleByDistance(self.items) * 1.5

		# TopNode
		self.topNode = self.createTopNode(self.items)

		# Interface
		self.interface = self.createInterfaceControl(child=self.items[0])

		# Phalanges
		self.createPhalanges()

		# MetaCarpel
		if self.metacarpalItem:
			self.createMetacarpal()
			cmds.aimConstraint(self.joint[0],
							   self.metacarpalJoint,
							   name='{}_constraint0'.format(self.metacarpalJoint),
							   mo=True,
							   aimVector=[1, 0, 0],
							   upVector=[0, 1, 0],
							   worldUpType='none',
							   worldUpVector=[0, 1, 0],
							   )

		# Child Controls
		self.createChildChain(self.items)

		# Hierarchy
		# Local
		if self.parent:
			local = self.getLocal(self.parent)

			if local:
				cmds.parent(self.topNode, local)

		# World
		if not self.root:
			if self.parent:
				self.root = self.getRoot(self.parent)

		if self.root:
			world = self.getWorld(self.root)

			if world:
				cmds.parent(self.ikTopNode, world)
		return

	def createPhalanges(self):
		self.create3PointFKIK()
		return

	def createMetacarpal(self):
		self.metacarpalJoint = Joint(prefix=self.prefix,
									 name='metacarpal',
									 side=self.side,
									 kind=camelCase(Component.rig, Component.joint, capitalize=False),
									 drawStyle=JointDrawStyle.none,
									 item=self.metacarpalItem
									 )

		self.metacarpalJoint.snapTo(self.metacarpalItem)
		self.metacarpalJoint.freezeTransforms()

		# Hierarchy
		self.metacarpalJoint.parent = self.topNode

		# Constrain
		cmds.parentConstraint(self.metacarpalJoint, self.metacarpalItem, mo=True)
		cmds.scaleConstraint(self.metacarpalJoint, self.metacarpalItem, mo=True)
		return


class FINGER(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.finger
		DIGIT.__init__(self, *args, **kwargs)


class TOE(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.toe
		DIGIT.__init__(self, *args, **kwargs)


class LEFTTHUMB(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.thumb
		kwargs['side'] = Position.left
		DIGIT.__init__(self, *args, **kwargs)


class LEFTINDEXFINGER(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.indexFinger
		kwargs['side'] = Position.left
		DIGIT.__init__(self, *args, **kwargs)


class LEFTMIDDLEFINGER(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.middleFinger
		kwargs['side'] = Position.left
		DIGIT.__init__(self, *args, **kwargs)


class LEFTRINGFINGER(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.ringFinger
		kwargs['side'] = Position.left
		DIGIT.__init__(self, *args, **kwargs)


class LEFTPINKYFINGER(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.pinkyFinger
		kwargs['side'] = Position.left
		DIGIT.__init__(self, *args, **kwargs)


class LEFTBIGTOE(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.bigToe
		kwargs['side'] = Position.left
		DIGIT.__init__(self, *args, **kwargs)


class LEFTINDEXTOE(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.indexToe
		kwargs['side'] = Position.left
		DIGIT.__init__(self, *args, **kwargs)


class LEFTMIDDLETOE(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.middleToe
		kwargs['side'] = Position.left
		DIGIT.__init__(self, *args, **kwargs)


class LEFTRINGTOE(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.ringToe
		kwargs['side'] = Position.left
		DIGIT.__init__(self, *args, **kwargs)


class LEFTPINKYTOE(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.pinkyToe
		kwargs['side'] = Position.left
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTTHUMB(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.thumb
		kwargs['side'] = Position.right
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTINDEXFINGER(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.indexFinger
		kwargs['side'] = Position.right
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTMIDDLEFINGER(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.middleFinger
		kwargs['side'] = Position.right
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTRINGFINGER(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.ringFinger
		kwargs['side'] = Position.right
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTPINKYFINGER(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.pinkyFinger
		kwargs['side'] = Position.right
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTBIGTOE(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.bigToe
		kwargs['side'] = Position.right
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTINDEXTOE(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.indexToe
		kwargs['side'] = Position.right
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTMIDDLETOE(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.middleToe
		kwargs['side'] = Position.right
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTRINGTOE(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.ringToe
		kwargs['side'] = Position.right
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTPINKYTOE(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.pinkyToe
		kwargs['side'] = Position.right
		DIGIT.__init__(self, *args, **kwargs)
