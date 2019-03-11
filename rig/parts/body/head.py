# Lancer Modules
from rig.utils import *
from rig.parts.baseRig import BASERIG

# Maya Modules
from maya import cmds


class HEAD(BASERIG):
	def __init__(self,
	             head,
	             parent=None,
	             rootRig=None,
	             ):
		# Items
		self.headItem = head

		BASERIG.__init__(self,
		                 prefix=Part.head,
		                 side=None,
		                 items=[head],
		                 parent=parent,
		                 axis=[1, 1, 0],
		                 root=rootRig,
		                 )

	def create(self):
		# Top Node
		self.topNode = self.createTopNode(self.items)

		# Joints
		self.joint = self.createJointChain(self.items, autoName=False)
		cmds.parent(self.joint[0], self.topNode)
		self.constrainChain(self.joint, self.items)

		# Head
		self.createHead()

	def createHead(self):
		# Scale
		distance = distanceFromOrigin(self.headItem)
		self.scale = distance

		# Rig Control / FK Control
		self.interface = INTERFACE_CONTROL(prefix=self.prefix,
		                                   side=self.side,
		                                   item=self.headItem,
		                                   wire=WireType.master,
		                                   axis=[0, 0, 1],
		                                   scale=self.scale * .2,
		                                   )

		self.interface.snapTo(self.headItem, True, False)
		self.interface.parent = self.topNode

		# FK Pole Vector
		self.fkPoleVector = cmds.group(n=longName(self.longName, Component.fkPoleVector), em=True)
		snap(self.headItem, self.fkPoleVector, True, False)
		cmds.xform(self.fkPoleVector, ws=True, t=[0, 0, distance], r=True)
		cmds.parent(self.fkPoleVector, self.interface.transform)
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
		               wire=WireType.sphere,
		               axis=[0, 0, 0],
		               scale=self.scale * 0.05,
		               )

		ik.snapTo(self.headItem, True, False)
		cmds.xform(ik.nullPosition, ws=True, t=[0, 0, distance], r=True)

		ik.parent = self.ikTopNode
		self.ikControl.append(ik)

		print ik.offset

		# IK Aim
		createAimVector(ik, self.ikJoint[0], name=longName(self.longName, 'aimVector0'))

		# FKIK
		fkik = createFKIK(items=self.joint[-1],
		                  fkControls=self.interface,
		                  ikControls=self.ikJoint,
		                  parent=self.interface,
		                  attrName=Component.fkik,
		                  )

		# Visibility
		cmds.connectAttr('{}.{}'.format(self.interface, Component.fkik),
		                 '{}.v'.format(ik.nullConnection),
		                 force=True,
		                 )
		return
