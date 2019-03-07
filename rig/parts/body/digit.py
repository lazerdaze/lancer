# Lancer Modules
from rig.utils import *
from rig.parts.baseRig import BASERIG

# Maya Modules
from maya import cmds


class DIGIT(BASERIG):
	def __init__(self,
				 prefix=Part.digit,
				 side=Position.left,
				 name=None,
				 sector=None,
				 index=None,
				 items=None,
				 parent=None,
				 root=None,
				 ):

		metacarpal = None

		if len(items) == 4:
			metacarpal = items[0]
			items.remove(metacarpal)

		self.metacarpalItem = metacarpal
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

		# MetaCarpel
		if self.metacarpalItem:
			self.createMetacarpal()

		# Phalanges
		self.createPhalanges()

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


def THUMBFINGER(DIGIT):
	def __init__(self, *args, **kwargs):
		DIGIT.__init__(self, *args, **kwargs)


def INDEXFINGER(DIGIT):
	def __init__(self, *args, **kwargs):
		DIGIT.__init__(self, *args, **kwargs)


def MIDDLEFINGER(DIGIT):
	def __init__(self, *args, **kwargs):
		DIGIT.__init__(self, *args, **kwargs)


def RINGFINGER(DIGIT):
	def __init__(self, *args, **kwargs):
		DIGIT.__init__(self, *args, **kwargs)


def PINKYFINGER(DIGIT):
	def __init__(self, *args, **kwargs):
		DIGIT.__init__(self, *args, **kwargs)


def BIGTOE(DIGIT):
	def __init__(self, *args, **kwargs):
		DIGIT.__init__(self, *args, **kwargs)


def INDEXTOE(DIGIT):
	def __init__(self, *args, **kwargs):
		DIGIT.__init__(self, *args, **kwargs)


def MIDDLETOE(DIGIT):
	def __init__(self, *args, **kwargs):
		DIGIT.__init__(self, *args, **kwargs)


def RINGTOE(DIGIT):
	def __init__(self, *args, **kwargs):
		DIGIT.__init__(self, *args, **kwargs)


def PINKYTOE(DIGIT):
	def __init__(self, *args, **kwargs):
		DIGIT.__init__(self, *args, **kwargs)
