# Lancer Modules
from rig.utils import *
from rig.parts.baseRig import BASERIG

# Maya Moudles
from maya import cmds


class SPINE(BASERIG):
	def __init__(self,
	             items,
	             parent=None,
	             root=None,
	             ):
		BASERIG.__init__(self,
		                 prefix=Part.spine,
		                 side=Position.center,
		                 kind=Part.spine,
		                 items=items,
		                 parent=parent,
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
		if self.parent:
			if isinstance(self.parent, object):
				self.rigControl = getattr(self.parent, 'cogControl')
			else:
				self.rigControl = self.parent
		else:
			self.rigControl = self.topNode

		# Controls
		self.createFKChain(self.items)
		# self.createSplineFKIK(self.items)  # TODO: SPLINE IK
		self.constrainChain(self.fkControl, self.joint)
		self.constrainChain(self.joint, self.items)

		# Hierarchy
		cmds.parent(self.fkTopNode, self.joint[0], self.topNode)
		if self.parent:
			if isinstance(self.parent, object):
				cmds.parent(self.topNode, self.parent.cogControl.offsetTransform)

		# Cleanup
		self.set = self.createSet(self.allAnimationControls)
		self.finalize()
		return





