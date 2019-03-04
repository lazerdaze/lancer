# Lancer Modules
from rig.utils import *
from rig.parts.baseRig import BASERIG

# Maya Moudles
from maya import cmds


class SPINE(BASERIG):
	def __init__(self,
				 items,
				 root=None,
				 ):
		BASERIG.__init__(self,
						 prefix=Part.spine,
						 side=Position.center,
						 kind=Part.spine,
						 items=items,
						 axis=[1, 1, 0],
						 root=root,
						 )
		self.create()

	def create(self):
		# Scale
		self.scale = self.scaleByDistance(self.items) * 2.0

		# Top Node
		self.topNode = self.createTopNode(self.items)

		# Rig Joints
		self.joint = self.createJointChain(self.items, hierarchy=True)

		# Bind Controls
		self.createBindChain(self.items)

		# Parent
		if self.root:
			if isinstance(self.root, object):
				self.interface = getattr(self.root, 'cogControl')
			else:
				self.interface = self.root
		else:
			self.interface = self.topNode

		# Controls
		self.createFKChain(self.items, autoName=False)
		# self.createSplineFKIK(self.items)  # TODO: SPLINE IK
		self.constrainChain(self.fkControl, self.joint)
		self.constrainChain(self.joint, self.items)

		# Hierarchy
		cmds.parent(self.fkTopNode, self.joint[0], self.topNode)

		local = None
		world = None

		if self.root:
			if isinstance(self.root, object):
				if hasattr(self.root, Component.world):
					world = getattr(self.root, Component.world)
				if hasattr(self.root, Component.local):
					local = getattr(self.root, Component.local)
		if local:
			cmds.parent(self.topNode, local)

		# Cleanup
		self.set = self.createSet(self.allControls)
		self.finalize()
		return
