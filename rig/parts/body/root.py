# Lancer Modules
import rig.utils.joint
from rig.utils import *
from bodyBase import BASE

# Maya Moudles
from maya import cmds


class ROOT(BASE):
	def __init__(self,
	             root=None,
	             name='character',
	             scale=1,
	             ):
		BASE.__init__(self,
		              name=name,
		              side='Center',
		              scale=scale,
		              )
		self.root = root

		if self.root:
			self.objects = [root]
			self.getScale()

		self.createControls()
		self.createRootOffset()
		self.createSet(self.fkControl)
		self.createNetwork(typ='root')
		self.networkRoot = self.network
		self.networkParent = self.network
		self.createNetworkConnections()
		self.setupDisplayAttr()
		self.setupGlobalScale()
		self.hideGroupNodes([self.network] + self.fkGroup)

	def getScale(self):
		self.scale = int(rig.utils.joint.determineHeight(self.root) / 2)
		return

	def createControls(self):

		ctl = rig.api.component.CONTROL(name='{}_ctl'.format(self.name),
		                                typ='root',
		                                scale=self.scale + 2,
		                                axis=[0, 0, 0],
		                                )

		offset = rig.api.component.CONTROL(name='{}_offset_ctl'.format(self.name),
		                                   typ='center',
		                                   scale=self.scale,
		                                   axis=[0, 0, 0],
		                                   )

		rigging.presetWireColor([ctl.transform, offset.transform, ], typ=rigging.component.center)
		cmds.parent(offset.group, ctl.transform)
		self.fkControl = [ctl.transform, offset.transform]
		self.fkGroup = [ctl.group, offset.group]

		if self.root:
			cmds.parent(self.root, offset.transform)
		return

	def createRootOffset(self):
		attrName = 'rootOffset'
		parent = self.fkControl[0]

		rootOffset = rig.api.component.CONTROL(name='{}_root_offset_ctl'.format(self.name),
		                                       typ='center',
		                                       scale=self.scale - 0.8,
		                                       axis=[0, 0, 0],
		                                       )

		rigging.presetWireColor([rootOffset.transform], typ=rigging.component.center)
		cmds.parent(rootOffset.group, self.fkControl[-1])
		rigging.addBoolAttr(obj=parent, name=attrName)
		cmds.connectAttr('{}.{}'.format(parent, attrName), '{}.v'.format(rootOffset.group))

		if self.root:
			cmds.parentConstraint(rootOffset.transform, self.root, mo=True)

		self.fkControl.append(rootOffset.transform)
		self.fkGroup.append(rootOffset.group)
		return

	def setupDisplayAttr(self):
		for attr in ['jointDisplay', 'controlDisplay']:
			rigging.addBoolAttr(self.fkControl[0], attr)
			cmds.connectAttr('{}.{}'.format(self.fkControl[0], attr), '{}.{}'.format(self.network, attr))
		return

	def setupGlobalScale(self):
		globalNode = self.fkControl[0]
		attrName = 'globalScale'

		cmds.addAttr(globalNode, ln=attrName, dv=1)
		cmds.setAttr('{}.globalScale'.format(globalNode), k=False, channelBox=True)

		for axis in ['x', 'y', 'z']:
			cmds.connectAttr('{}.{}'.format(globalNode, attrName), '{}.s{}'.format(globalNode, axis))
			cmds.setAttr('{}.s{}'.format(globalNode, axis), k=False, channelBox=False, lock=True)

	def hideGroupNodes(self, objects):
		self.hideObjectsAttributes(objects)
		return