# Lancer Modules
from rig.utils import *
from bodyBase import BASE

# Maya Moudles
from maya import cmds

class LEG(BASE):
	def __init__(self,
	             side,
	             hip,
	             knee,
	             foot,
	             toe=None,
	             networkRoot=None,
	             name=naming.component.leg,
	             index=0,
	             ):
		BASE.__init__(self,
		              networkRoot=networkRoot,
		              name=name,
		              side=side,
		              index=index,
		              )

		self.toe = toe
		self.toeFKControl = None
		self.toeFKGroup = None
		self.toeIKControl = None
		self.toeIKGroup = None
		self.roll = None

		self.hip = hip
		self.knee = knee
		self.foot = foot

		self.objects = [hip, knee, foot]

		self.getScale()
		self.createFKIKChain(self.objects)
		self.resetRotations()
		self.createTwistChain(self.hip, self.knee, self.foot)
		self.setDefaultAttrValues()

		if self.toe:
			self.createDetailChain(self.toe)
			self.createFootRoll()
			self.createToe()
			self.createToeFKIK()

		self.createGrandchildren([self.hip, self.knee, self.foot])
		self.createLocalWorld(obj=self.fkControl[0],
		                      local=self.fkGroup[0],
		                      )
		self.createSet(self.fkControl + self.ikControl)
		self.createNetwork(typ=naming.convention(self.name,
		                                         self.side.upper()[0],
		                                         self.index,
		                                         )
		                   )
		self.createNetworkConnections()

	def getScale(self):
		self.scale = rigging.getDistance(self.hip, self.knee) / 5
		return

	def setDefaultAttrValues(self):
		cmds.setAttr('{}.{}'.format(self.attrControl, naming.rig.fkik), 1)
		return

	def resetRotations(self):
		cmds.parent(self.ikHandle, world=True)

		for axis in ['x', 'y', 'z']:
			cmds.setAttr('{}.r{}'.format(self.ikGroup[-1], axis), lock=False)
			cmds.setAttr('{}.r{}'.format(self.ikGroup[-1], axis), 0)

		cmds.parent(self.ikHandle, self.ikControl[-1])
		rigging.lockRotate(self.ikGroup[-1])

		return

	def createToe(self):
		ctl = rig.api.component.CONTROL(name=naming.convention(self.name,
		                                                       self.side[0],
		                                                       self.index,
		                                                       naming.rig.fk,
		                                                       naming.component.toe.capitalize(),
		                                                       naming.rig.ctl,
		                                                       ),
		                                typ=control.component.circleRotate,
		                                scale=self.scale,
		                                axis=[1, 0, 0],
		                                child=self.toe,
		                                side=self.side,
		                                label=naming.component.collar,
		                                color=rigging.component.fk,
		                                )
		rigging.lockScale(ctl.transform)

		parent = cmds.listRelatives(self.toe, parent=True)
		if parent:
			cmds.parent(ctl.group, parent[0])

		self.toeFKControl = ctl.transform
		self.toeFKGroup = ctl.group
		self.objects.insert(0, self.toe)
		return

	def createFootRoll(self):
		self.roll = rigging.createIKFootRollNulls(foot=self.foot,
		                                          toe=self.toe,
		                                          control=self.ikControl[-1],
		                                          name=naming.convention(self.name,
		                                                              self.side[0],
		                                                              self.index,
		                                                              naming.rig.ik,
		                                                              'footRoll'),
		                                          )

		# self.roll.accuratePositions()
		self.roll.createWire()

		cmds.parent(self.ikHandle, self.roll.ball[0])

		for axis in ['x', 'y', 'z']:
			cmds.setAttr('{}.t{}'.format(self.ikGroup[-1], axis), lock=False)

		rigging.snap(self.roll.wire, self.ikGroup[-1], t=True)
		rigging.lockAttributes(self.ikGroup[-1])

		cmds.parent(self.roll.wire, self.ikGroup[-1])
		rigging.freezeTransform(self.roll.wire)
		rigging.swapShape(self.ikControl[-1], self.roll.wire)
		cmds.parent(self.roll.parent, self.ikControl[-1])

		self.toeIKControl = self.roll.toe[0]
		return

	def createToeFKIK(self):
		pc = cmds.parentConstraint(self.toeFKControl,
		                           self.toeIKControl,
		                           self.toe,
		                           n='{}_fkik_pc0'.format(self.toe),
		                           mo=True)[0]

		for axis in ['X', 'Y', 'Z']:
			cmds.disconnectAttr('{}.constraintTranslate{}'.format(pc, axis), '{}.translate{}'.format(self.toe, axis))

		pcAttr = cmds.parentConstraint(pc, q=True, wal=True)
		cmds.connectAttr('{}.{}'.format(self.attrControl, naming.rig.fkik), '{}.{}'.format(pc, pcAttr[-1]), f=True)

		reverse = cmds.createNode('reverse', n='{}_fkik_re0'.format(self.toe))
		cmds.connectAttr('{}.{}'.format(self.attrControl, naming.rig.fkik), '{}.inputX'.format(reverse), f=True)
		cmds.connectAttr('{}.outputX'.format(reverse), '{}.{}'.format(pc, pcAttr[0]), f=True)
		cmds.connectAttr('{}.outputX'.format(reverse), '{}.v'.format(self.toeFKGroup), f=True)
		return