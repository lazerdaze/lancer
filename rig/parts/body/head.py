# Lancer Modules
from rig.utils import *
from rig.parts.baseRig import BASERIG

# Maya Modules
from maya import cmds


class HEAD(BASERIG):
	def __init__(self,
	             head,
	             neck=None,
	             parent=None,
	             rootRig=None,
	             ):
		items = []

		if neck:
			if isinstance(neck, (list, tuple, dict)):
				for x in neck:
					items.append(x)

		items.append(head)

		BASERIG.__init__(self,
		                 prefix=Part.head,
		                 side=Position.center,
		                 kind=Part.head,
		                 items=items,
		                 parent=parent,
		                 axis=[1, 1, 0],
		                 root=rootRig,
		                 )

		# Items
		self.headItem = head
		self.neckItems = neck

		# Controls
		self.fkHeadControl = None
		self.ikHeadControl = None

		# Init
		self.create()

	def create(self):
		# Top Node
		self.topNode = self.createTopNode(self.items)

		# Joints
		self.joint = self.createJointChain(self.items)
		cmds.parent(self.joint[0], self.topNode)
		self.constrainChain(self.joint, self.items)

		# Neck
		if self.neckItems:
			self.createNeck()

		# Head
		self.createHead()

		# Cleanup
		self.set = self.createSet(self.allAnimationControls)
		self.finalize()

	def createHead(self):
		# Scale
		distance = distanceFromOrigin(self.headItem)
		self.scale = distance

		# Rig Control / FK Control
		self.rigControl = CONTROL(prefix=self.prefix,
		                          side=self.side,
		                          item=self.headItem,
		                          wireType=WireType.master,
		                          axis=[0, 0, 1],
		                          scale=self.scale * .2,
		                          color=WireColor.purple,
		                          kind=Component.rig,
		                          )

		self.rigControl.snapTo(self.headItem, True, False)
		self.rigControl.parentTo(self.topNode)

		# FK Pole Vector
		self.fkPoleVector = cmds.group(n=longName(self.longName, Component.fkPoleVector), em=True)
		snap(self.headItem, self.fkPoleVector, True, False)
		cmds.xform(self.fkPoleVector, ws=True, t=[0, 0, distance], r=True)
		cmds.parent(self.fkPoleVector, self.rigControl.transform)
		freezeTransform(self.fkPoleVector)
		lockKeyableAttributes(self.fkPoleVector, hide=True)

		# IK
		self.ikTopNode = self.createTopNode(self.items[-1], kind=Component.ik)

		# IK Joint
		self.ikJoint = self.createJointChain([self.headItem], kind=Component.ik)
		cmds.parent(self.ikJoint, self.topNode)

		# IK Control
		ik = IKCONTROL(prefix=self.prefix,
		               side=self.side,
		               item=self.headItem,
		               wireType=WireType.sphere,
		               axis=[0, 0, 0],
		               scale=self.scale * 0.05,
		               )

		ik.snapTo(self.headItem, True, False)
		cmds.xform(ik._nullPosition, ws=True, t=[0, 0, distance], r=True)
		ik.parentTo(self.ikTopNode)
		self.ikHeadControl = ik

		# IK Aim
		createAimVector(ik, self.ikJoint[0], name=longName(self.longName, 'aimVector0'))

		# FKIK
		fkik = createFKIK(items=self.joint[-1],
		                  fkControls=self.rigControl,
		                  ikControls=self.ikJoint,
		                  parent=self.rigControl,
		                  attrName=Component.fkik,
		                  )

		# Visibility
		cmds.connectAttr('{}.{}'.format(self.rigControl, Component.fkik),
		                 '{}.v'.format(ik._nullConnection),
						 f=True)
		return

	def createNeck(self):
		neck = BASERIG(prefix=Part.neck,
		               side=Position.center,
		               kind=Part.neck,
		               items=self.neckItems,
		               axis=self.axis,
		               )

		neck.createFKChain(parent=self.rigControl, autoName=False)
		neck.createBindChain(self.neckItems)
		neck.constrainChain(neck.fkControl, self.neckItems)
		self.fkControl += neck.fkControl
		self.bindControls += neck.bindControls
		self.leafControls += neck.leafControls
		return
