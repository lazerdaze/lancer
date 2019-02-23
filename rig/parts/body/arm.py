# Lancer Modules
from rig.utils import *
from rigBase import RIGBASE
from digit import DIGIT

# Maya Moudles
from maya import cmds


class ARM(RIGBASE):
	def __init__(self,
	             side,
	             shoulder,
	             elbow,
	             hand,
	             collar=None,
	             networkRoot=None,
	             name=Part.arm,
	             index=0,
	             ):
		RIGBASE.__init__(self,
		                 networkRoot=networkRoot,
		                 name=name,
		                 side=side,
		                 index=index,
		                 )

		self.collar = collar
		self.collarFKControl = None
		self.collarFKGroup = None
		self.collarIKControl = None
		self.collarIKGroup = None

		self.shoulder = shoulder
		self.elbow = elbow
		self.hand = hand
		self.objects = [shoulder, elbow, hand]

		self.getScale()
		self.createFKIKChain(self.objects)


		#self.createTwistChain(self.shoulder, self.elbow, self.hand)

		if self.collar:
			self.createDetailChain(self.collar)
			self.createCollar()

		self.createGrandchildren([self.shoulder, self.elbow, self.hand])

		# FIXME: HAND Class
		#self.createHand()
		self.createLocalWorld(obj=self.fkControl[0],
		                      local=self.fkGroup[0],
		                      )
		self.createSet([self.collarFKControl] + self.fkControl + self.ikControl)
		self.createNetwork(typ=self.name)

		self.createNetworkConnections()
		self.updateNetwork()

	def getScale(self):
		self.scale = rigging.getDistance(self.shoulder, self.elbow) / 2.5
		return

	def createCollar(self):
		ctl = CONTROL(name=longName(self.name,
		                            self.side[0],
		                            self.index,
		                            Component.fk,
		                            Part.collar.capitalize(),
		                            Component.control,
		                            ),
		              typ=WireType.dumbbell,
		              scale=self.scale,
		              axis=[1, 0, 0],
		              child=self.collar,
		              side=self.side,
		              label=Part.collar,
		              color=Component.fk,
		              )
		rigging.lockScale(ctl.transform)
		cmds.parentConstraint(ctl.transform, self.collar)

		parent = cmds.listRelatives(self.collar, parent=True)
		if parent:
			cmds.parent(ctl.group, parent[0])

		self.collarFKControl = ctl.transform
		self.collarFKGroup = ctl.group

		self.objects.insert(0, self.collar)
		return

	def createHand(self):
		HAND(hand=self.hand,
		     side=self.side,
		     networkRoot=self.networkRoot,
		     index=self.index
		     )
		return

	def updateNetwork(self):
		# Collar
		if self.collar:
			self.connectToNetwork(self.collar, self.network, 'skeletonCollar')

		if self.collarFKControl:
			self.connectToNetwork(self.collarFKControl, self.network, 'collarFkControl')
		return


class HAND(RIGBASE):
	def __init__(self,
	             hand,
	             side,
	             networkRoot=None,
	             name=Part.hand,
	             index=0,
	             ):
		RIGBASE.__init__(self,
		                 items=rigging.listCheck(hand),
		                 networkRoot=networkRoot,
		                 name=name,
		                 side=side,
		                 index=index,
		                 )

		self.hand = hand
		self.finger = []
		self.createFingers()

		self.createNetwork(typ=longName(self.name,
		                                self.side.upper()[0],
		                                self.index,
		                                )
		                   )
		self.updateNetwork()

	def createFingers(self):
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

	def updateNetwork(self):
		return


class LEFTARM(ARM):
	def __init__(self, *args, **kwargs):
		ARM.__init__(self, side=Position.left, *args, **kwargs)


class RIGHTARM(ARM):
	def __init__(self, *args, **kwargs):
		ARM.__init__(self, side=Position.right, *args, **kwargs)
