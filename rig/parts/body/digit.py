# Lancer Modules
from rig.utils import *
from rig.parts.baseRig import BASERIG

# Maya Modules
from maya import cmds


# TODO: Create "Uber" Plugin Node that handles Curl, Spread, etc - Pose SDK
# TODO: Prop space Switching

class DIGIT(BASERIG):
	def __init__(self,
	             items,
	             prefix=Part.digit,
	             side=Position.left,
	             name=Part.digit,
	             sector=None,
	             index=None,
	             parent=None,
	             root=None,
	             ):

		'''
		Naming Convention:
			- arm_L_indexFinger_0_fkControl
			- indexFinger_L_0_fkControl
		
		:param items: 
		:param prefix: 
		:param side: 
		:param name: 
		:param sector: 
		:param index: 
		:param parent: 
		:param root: 
		'''

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
		lockTranslate(self.interface, hide=True)
		lockRotate(self.interface, hide=True)


		# Phalanges
		self.scale = self.scaleByDistance(self.items) * .5
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

		# Constraint
		self.constrainChain(self.joint, self.items)

		# Hierarchy
		self.interface.parent = self.joint[0]

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
		self.create3PointFKIK(autoName=False)
		return

	def createMetacarpal(self):
		self.metacarpalJoint = Joint(prefix=self.prefix,
		                             name='metacarpal',
		                             side=self.side,
		                             kind=camelCase(Component.rig, Component.joint, capitalize=False),
		                             drawStyle=JointDrawStyle.none,
		                             )

		self.metacarpalJoint.snapTo(self.metacarpalItem)
		self.metacarpalJoint.freezeTransforms()

		# Hierarchy
		self.metacarpalJoint.parent = self.topNode

		# Constrain
		cmds.parentConstraint(self.metacarpalJoint, self.metacarpalItem, mo=True)
		cmds.scaleConstraint(self.metacarpalJoint, self.metacarpalItem, mo=True)
		return


class LEFTDIGIT(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['side'] = Position.left
		DIGIT.__init__(self, *args, **kwargs)


class LEFTTHUMB(LEFTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.thumb
		DIGIT.__init__(self, *args, **kwargs)


class LEFTINDEXFINGER(LEFTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.indexFinger
		DIGIT.__init__(self, *args, **kwargs)


class LEFTMIDDLEFINGER(LEFTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.middleFinger
		DIGIT.__init__(self, *args, **kwargs)


class LEFTRINGFINGER(LEFTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.ringFinger
		DIGIT.__init__(self, *args, **kwargs)


class LEFTPINKYFINGER(LEFTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.pinkyFinger
		DIGIT.__init__(self, *args, **kwargs)
		
class LEFTBIGTOE(LEFTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.bigToe
		DIGIT.__init__(self, *args, **kwargs)


class LEFTINDEXTOE(LEFTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.indexToe
		DIGIT.__init__(self, *args, **kwargs)


class LEFTMIDDLETOE(LEFTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.middleToe
		DIGIT.__init__(self, *args, **kwargs)


class LEFTRINGTOE(LEFTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.ringToe
		DIGIT.__init__(self, *args, **kwargs)


class LEFTPINKYTOE(LEFTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.pinkyToe
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTDIGIT(DIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['side'] = Position.right
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTTHUMB(RIGHTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.thumb
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTINDEXFINGER(RIGHTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.indexFinger
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTMIDDLEFINGER(RIGHTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.middleFinger
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTRINGFINGER(RIGHTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.ringFinger
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTPINKYFINGER(RIGHTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.pinkyFinger
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTBIGTOE(RIGHTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.bigToe
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTINDEXTOE(RIGHTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.indexToe
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTMIDDLETOE(RIGHTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.middleToe
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTRINGTOE(RIGHTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.ringToe
		DIGIT.__init__(self, *args, **kwargs)


class RIGHTPINKYTOE(RIGHTDIGIT):
	def __init__(self, *args, **kwargs):
		kwargs['prefix'] = Part.pinkyToe
		DIGIT.__init__(self, *args, **kwargs)
















if __name__ == '__main__':
	LEFTINDEXFINGER(items=['indexFinger_L_joint',
	                       'indexFinger_L_knuckle_0_joint',
	                       'indexFinger_L_knuckle_1_joint',
	                       'indexFinger_L_knuckle_2_joint'
	                       ]
	                )


