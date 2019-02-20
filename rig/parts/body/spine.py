# Lancer Modules
from rig.utils import *
from rig.piece import *
from rigBase import RIGBASE

# Maya Moudles
from maya import cmds


class SPINE(RIGBASE):
	def __init__(self,
	             items,
	             networkRoot=None,
	             name='spine',
	             scale=1,
	             master=None,
	             ):
		RIGBASE.__init__(self,
		                 items=items,
		                 networkRoot=networkRoot,
		                 name=name,
		                 side='Center',
		                 scale=scale,
		                 master=master,
		                 axis=[1, 1, 0],
		                 )

		self.getScale()
		self.createFKChain(self.items)
		self.constrainSpine()
		self.createParent(name='rig_grp'.format(self.name), child=self.items[0])
		self.setupHierarchy()
		self.createDetailChain(self.items)
		self.overrideColor()

		self.createSet(self.fkControl)
		self.createNetwork(typ=self.name)
		self.createNetworkConnections()

	def getScale(self):
		if len(self.items) > 1:
			start = self.items[0]
			end = self.items[1]
			distance = rigging.getDistance(start, end)
			self.scale = distance * 1.5
		return

	def constrainSpine(self):
		for obj in self.items:
			i = self.items.index(obj)
			cmds.parentConstraint(self.fkControl[i], obj, mo=True)

	def setupHierarchy(self):
		cmds.parent(self.fkParent, self.parent)

		parent = cmds.listRelatives(self.items[0], parent=True)
		parent = parent[0] if parent else None
		if parent:
			cmds.parent(self.parent, parent)
		return

	def overrideColor(self):
		rigging.presetWireColor(self.fkControl, 'center')
		return


########################################################################################################################
#
#
#	NECK CLASS
#
#
########################################################################################################################


class NECK(SPINE):
	def __init__(self,
	             items,
	             networkRoot=None,
	             name=Part.neck,
	             scale=1,
	             master=None,
	             ):
		SPINE.__init__(self,
		               items=items,
		               networkRoot=networkRoot,
		               name=name,
		               scale=scale,
		               master=master,
		               )

		self.createLocalWorld(obj=self.fkControl[0],
		                      local=self.fkGroup[0],
		                      )

	def getScale(self):
		distanceList = []
		children = cmds.listRelatives(self.items[0], children=True)
		if children:
			for child in children:
				start = self.items[0]
				end = child
				distanceList.append(rigging.getDistance(start, end))

		self.scale = max(distanceList) + 0.25
		return
