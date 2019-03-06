# Lancer Modules
from rig.utils import *
from rigBase import RIGBASE
from rig.parts.baseRig import BASERIG

# Maya Modules
from maya import cmds


class DIGIT(BASERIG):
	def __init__(self, *args, **kwargs):

		items = kwargs.get('items', [])

		metacarpal = None

		if len(items) == 4:
			metacarpal = items[0]
			items.remove(metacarpal)

		self.metacarpalItem = metacarpal
		self._metacarpalJoint = None

		BASERIG.__init__(self, *args, **kwargs)

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
			createRelationship(source=self.interface,
			                   sourceAttr='cogControl',
			                   destination=joint,
			                   destinationAttr='rigParent'
			                   )

			createRelationship(source=self.interface,
			                   sourceAttr='rigChildren',
			                   destination=joint,
			                   destinationAttr='rigInterface',
			                   kind=MayaAttrType.string,
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
		# TODO: Simplify: Parent, Root, Hierarchy

		local = None

		if self.parent:
			if isinstance(self.parent, object):
				if hasattr(self.parent, Component.local):
					local = getattr(self.parent, Component.local)

		if local:
			cmds.parent(self.topNode, local)

		world = None

		if self.root:
			if isinstance(self.root, object):
				if hasattr(self.root, Component.local):
					world = getattr(self.root, Component.local)

			else:
				if attributeExist(self.root, 'cogControl'):
					cog = getConnectedNode(self.root, 'cogControl')

					if attributeExist(cog, 'offset'):
						world = getConnectedNode(cog, 'offset')

		if world and self.ikTopNode:
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
