# Lancer Modules
from rig.utils import *
from bodyBase import BASE

# Maya Modules
from maya import cmds


class DIGIT(BASE):
	def __init__(self,
	             objects,
	             side=None,
	             networkRoot=None,
	             name=Part.digit,
	             index=0,
	             ):
		BASE.__init__(self,
		              objects=objects,
		              networkRoot=networkRoot,
		              name=name,
		              side=side,
		              index=index,
		              )

		self.getScale()
		self.createFKChain(self.objects)
		self.createDetailChain(self.objects)
		self.setupHierarchy()

		self.createNetwork(typ=longName(self.name,
		                                self.side.upper()[0],
		                                self.index,
		                                )
		                   )
		self.createSet(self.fkControl)
		self.createNetworkConnections()

	def getScale(self):
		self.scale = rigging.getDistance(self.objects[0], self.objects[1]) / 2
		return

	def setupHierarchy(self):
		for obj in self.objects:
			i = self.objects.index(obj)
			cmds.parentConstraint(self.fkControl[i], obj, mo=True)
		return
