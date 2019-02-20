# Lancer Modules
from rig.utils import *
from rig.piece import *
from rigBase import RIGBASE

# Maya Modules
from maya import cmds


class HEAD(RIGBASE):
	def __init__(self,
	             head,
	             networkRoot=None,
	             name=Part.head,
	             scale=1,
	             master=None,
	             ):
		RIGBASE.__init__(self,
		                 items=rigging.listCheck(head),
		                 networkRoot=networkRoot,
		                 name=name,
		                 side=Position.center,
		                 scale=scale,
		                 master=master,
		                 )

		self.head = head

		self.getScale()
		self.createControls()
		self.createIK()
		self.setupHierarchy()
		self.createFKIK()
		self.createDetailChain(self.items)

		self.createLocalWorld(obj=self.fkControl[0],
		                      local=self.fkGroup[0],
		                      )
		self.createSet([self.fkControl[0], self.ikControl[1]])
		self.createNetwork(typ=self.name)
		self.createNetworkConnections()
		self.parentToRootControl(self.ikGroup[1])

	def getScale(self):
		height = cmds.xform(self.head, q=True, ws=True, rp=True)[1]
		self.scale = height / 6
		return

	def createControls(self):
		ctl = CONTROL(name='{}_ctl'.format(self.name),
		              typ=WireType.lollipop,
		              scale=self.scale,
		              axis=[1, 0, -1],
		              )
		rigging.snap(self.head, ctl.group, t=True, r=True)
		rigging.presetWireColor(ctl.transform, typ=Position.center)
		rigging.lockScale(ctl.transform)

		self.fkControl = [ctl.transform]
		self.fkGroup = [ctl.group]
		return

	def createIK(self):
		ctl = CONTROL(name='{}_ik_ctl'.format(self.name),
		              typ=WireType.sphere,
		              scale=self.scale / 8,
		              axis=[0, 0, 0],
		              )

		rigging.snap(self.head, ctl.group, t=True)
		distance = cmds.xform(self.head, q=True, ws=True, rp=True)[1]
		cmds.xform(ctl.group, ws=True, t=[0, 0, distance], r=True)

		ikNull = cmds.group(name='{}_ik_aim'.format(self.name), em=True)
		ikGrp = cmds.group(ikNull, name='{}_grp'.format(ikNull))
		rigging.snap(self.head, ikGrp, t=True, r=True)
		rigging.createAimVector(ctl.transform, ikNull, name='{}_aimVector'.format(self.name))
		rigging.presetWireColor(ctl.transform, typ=Component.ik)

		self.ikControl = [ikNull, ctl.transform]
		self.ikGroup = [ikGrp, ctl.group]
		return

	def setupHierarchy(self):
		parent = cmds.listRelatives(self.head, parent=True)
		if parent:
			parent = parent[0]
			cmds.parent(self.fkGroup[0], self.ikGroup[0], parent)
		return

	def createFKIK(self):
		attrName = Component.fkik
		rigging.createFKIK(items=self.head,
		                   fkControls=self.fkControl[0],
		                   master=self.fkControl[0],
		                   ikControls=self.ikControl[0],
		                   attrName=attrName,
		                   )

		cmds.connectAttr('{}.{}'.format(self.fkControl[0], attrName), '{}.v'.format(self.ikGroup[1]))
		return
