# Lancer Modules
from rig.utils import *
from rig.piece import *
from bodyBase import BASE

# Maya Moudles
from maya import cmds


class SPINE(BASE):
	def __init__(self,
	             objects=None,
	             networkRoot=None,
	             name='spine',
	             scale=1,
	             attrControl=None,
	             ):
		BASE.__init__(self,
		              objects=objects,
		              networkRoot=networkRoot,
		              name=name,
		              side='Center',
		              scale=scale,
		              attrControl=attrControl,
		              )

	def create(self):
		self.getScale()
		self.createFKChain(self.objects)
		self.constrainSpine()
		self.createParent(name='rig_grp'.format(self.name), child=self.objects[0])
		self.setupHierarchy()
		self.createDetailChain(self.objects)
		self.overrideColor()

		self.createSet(self.fkControl)
		self.createNetwork(typ=self.name)
		self.createNetworkConnections()

	def getScale(self):
		if len(self.objects) > 1:
			start = self.objects[0]
			end = self.objects[1]
			distance = rigging.getDistance(start, end)
			self.scale = distance * 1.5
		return

	def constrainSpine(self):
		for obj in self.objects:
			i = self.objects.index(obj)
			cmds.parentConstraint(self.fkControl[i], obj, mo=True)

	def setupHierarchy(self):
		cmds.parent(self.fkParent, self.parent)

		parent = cmds.listRelatives(self.objects[0], parent=True)
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
	             objects=None,
	             networkRoot=None,
	             name=Part.neck,
	             scale=1,
	             attrControl=None,
	             ):
		SPINE.__init__(self,
		               objects=objects,
		               networkRoot=networkRoot,
		               name=name,
		               scale=scale,
		               attrControl=attrControl,
		               )

		self.createLocalWorld(obj=self.fkControl[0],
		                      local=self.fkGroup[0],
		                      )

	def getScale(self):
		distanceList = []
		children = cmds.listRelatives(self.objects[0], children=True)
		if children:
			for child in children:
				start = self.objects[0]
				end = child
				distanceList.append(rigging.getDistance(start, end))

		self.scale = max(distanceList) + 0.25
		return
