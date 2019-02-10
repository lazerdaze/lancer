# Lancer Modules
from rig.utils import *
from rig.piece import *
from bodyBase import BASE

# Maya Moudles
from maya import cmds


class COG(BASE):
	def __init__(self,
	             cog=None,
	             hip=None,
	             networkRoot=None,
	             name='cog',
	             scale=1,
	             ):
		BASE.__init__(self,
		              networkRoot=networkRoot,
		              name=name,
		              side='Center',
		              scale=scale,
		              )
		self.cog = cog
		self.hip = hip

	def create(self):
		self.objects = [self.cog]

		self.getScale()
		self.createControls()

		if self.hip:
			self.createHipControl()

		self.hideObjectsAttributes(self.fkGroup)

		self.createSet(self.fkControl)
		self.createNetwork(typ='cog')
		self.createNetworkConnections()
		self.setupHierarchy()

	def getScale(self):
		self.scale = determineHeight(self.cog) / 4 + .25
		return

	def createControls(self):
		ctl = CONTROL(name='{}_ctl'.format(self.name),
		              typ=Position.center,
		              scale=self.scale,
		              axis=[0, 0, 0],
		              )
		rigging.snap(self.cog, ctl.group, t=True, r=False)
		rigging.presetWireColor(ctl.transform, typ=Position.center)
		cmds.parentConstraint(ctl.transform, self.cog, mo=True)
		self.fkControl = [ctl.transform]
		self.fkGroup = [ctl.group]
		return

	def createHipControl(self):
		ctl = CONTROL(name='hip_ctl',
		              typ=Part.hip,
		              scale=self.scale - .15,
		              axis=[0, 0, 0],
		              )
		rigging.snap(self.hip, ctl.group, t=True, r=False)
		rigging.presetWireColor(ctl.transform, typ=Position.center)
		cmds.parentConstraint(ctl.transform, self.hip, mo=True)
		cmds.parent(ctl.group, self.fkControl[-1])
		self.objects.append(self.hip)
		self.fkControl.append(ctl.transform)
		self.fkGroup.append(ctl.group)
		return

	def setupHierarchy(self):
		parent = self.getConnected(self.networkRoot, 'fkControl', 1)
		if parent:
			cmds.parent(self.fkGroup[0], parent)

		rootOffset = self.getConnected(self.networkRoot, 'fkControl', 2)
		if rootOffset:
			grp = rigging.createGroup(rootOffset, '{}_pos_grp'.format(rootOffset))
			cmds.pointConstraint(self.fkControl[0], grp, skip='y', mo=True)
