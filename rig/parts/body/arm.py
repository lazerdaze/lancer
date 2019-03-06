# Lancer Modules
from rig.utils import *
from rigBase import RIGBASE
from digit import DIGIT
from rig.parts.baseRig import BASERIG

# Maya Modules
from maya import cmds


class ARM(BASERIG):
	def __init__(self,
				 collar,
				 shoulder,
				 elbow,
				 hand,
				 side,
				 parent=None,
				 root=None,
				 ):
		items = [collar, shoulder, elbow, hand]

		# Items
		self.collarItem = collar
		self.shoulderItem = shoulder
		self.elbowItem = elbow
		self.handItem = hand

		self.armItems = [shoulder, elbow, hand]

		# Collar
		self.collarFKControl = None
		self.collarIKControl = None
		self.collarJoint = None

		BASERIG.__init__(self,
						 prefix=Part.arm,
						 side=side,
						 items=items,
						 parent=parent,
						 root=root,
						 axis=[1, 1, 0],
						 )

	####################################################################################################################
	# Properties
	####################################################################################################################

	@property
	def allControls(self):
		result = BASERIG.allControls

		for ctrl in flatList(self.collarFKControl,
							 self.collarIKControl,
							 ):

			if isinstance(ctrl, object):
				for attr in ['transform', 'offsetTransform']:
					if hasattr(ctrl, attr):
						value = getattr(ctrl, attr)
						if value:
							result.append(value)
			elif ctrl is not None:
				result.append(ctrl)
		return

	####################################################################################################################
	# Methods
	####################################################################################################################

	def create(self, *args, **kwargs):
		# Scale
		self.scale = self.scaleByDistance(self.items) * 1.5

		# Interface
		self.interface = self.createInterfaceControl(child=self.items[-1])

		# Collar
		self.createCollarControl()

		# Arm
		self.create3PointFKIK(items=self.armItems)

		# Child Controls
		self.createChildChain(self.items)

		# Hand
		self.createHandControl()

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

	def createCollarControl(self):
		# Joint
		self.collarJoint = Joint(prefix=self.prefix,
								 name=Part.collar,
								 side=self.side,
								 kind=camelCase(Component.rig, Component.joint, capitalize=False),
								 drawStyle=JointDrawStyle.none,
								 item=self.collarItem
								 )

		self.collarJoint.snapTo(self.collarItem)
		self.collarJoint.freezeTransforms()

		# FK Control
		self.collarFKControl = FKCONTROL(prefix=self.prefix,
										 side=self.side,
										 name=Part.collar,
										 wire=WireType.dumbbell,
										 scale=self.scale,
										 item=self.collarJoint,
										 )

		# TODO: Arm Collar IK Control
		self.collarIKControl = None

		# Constrain
		cmds.parentConstraint(self.collarJoint, self.collarItem, mo=True)
		cmds.scaleConstraint(self.collarJoint, self.collarItem, mo=True)

		self.collarFKControl.constrainItem(point=True,
										   orient=True,
										   scale=True,
										   offset=True
										   )
		return

	def createHandControl(self):
		HAND(hand=self.handItem, interface=self.interface)
		return


class LEFTARM(ARM):
	def __init__(self, side=Position.left, *args, **kwargs):
		ARM.__init__(self, side=side, *args, **kwargs)


class RIGHTARM(ARM):
	def __init__(self, side=Position.right, *args, **kwargs):
		ARM.__init__(self, side=side, *args, **kwargs)


class HAND(AbstractNode):
	def __init__(self,
				 hand,
				 interface=None,
				 *args,
				 **kwargs
				 ):

		AbstractNode.__init__(self, *args, **kwargs)

		self.hand = hand
		self.interface = interface
		self.thumb = None
		self.indexFinger = None
		self.middleFinger = None
		self.ringFinger = None
		self.pinkyFinger = None

		self.finger = []

		self.create()
		self.finalize()

	def create(self):
		children = getJointChildren(self.hand)

		i = 0
		for child in children:
			joints = getJointOrder(child)
			finger = DIGIT(items=joints,
						   name=Part.finger,
						   side=self.side,
						   networkRoot=self.networkRoot,
						   index=i,
						   )
			self.finger.append(finger)
			i += 1
		return

	def finalize(self):
		if self.interface:
			pass
		return





