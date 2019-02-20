# Lancer Modules
from rig.utils import *
from rigBase import RIGBASE

# Maya Modules
from maya import cmds


class DIGIT(RIGBASE):
	def __init__(self,
	             items,
	             side=None,
	             networkRoot=None,
	             name=Part.digit,
	             index=0,
	             ):
		RIGBASE.__init__(self,
		                 items=items,
		                 networkRoot=networkRoot,
		                 name=name,
		                 side=side,
		                 index=index,
		                 )

		self.getScale()
		self.createFKChain(self.items)
		self.createDetailChain(self.items)
		self.setupHierarchy()

		self.createNetwork(typ=longName(self.name,
		                                self.side.upper()[0],
		                                self.index,
		                                )
		                   )
		self.createSet(self.fkControl)
		self.createNetworkConnections()

	def getScale(self):
		self.scale = rigging.getDistance(self.items[0], self.items[1]) / 2
		return

	def setupHierarchy(self):
		for obj in self.items:
			i = self.items.index(obj)
			cmds.parentConstraint(self.fkControl[i], obj, mo=True)
		return
