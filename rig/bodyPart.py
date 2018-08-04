# LANCER.RIG.BODYPART
#
#
#
#
#

# Lancer Modules
import naming
import ults
import control
import network
import skeleton
import component

reload(naming)
reload(ults)
reload(control)
reload(network)
reload(skeleton)
reload(component)

# Maya Modules
from maya import cmds


########################################################################################################################
#
#
#	BASE CLASS
#
#
########################################################################################################################


class BASE(object):
	def __init__(self,
	             objects=None,
	             name=naming.rig.base,
	             fkName=None,
	             ikName=None,
	             scale=1,
	             axis=None,
	             side=None,
	             index=0,
	             networkRoot=None,
	             networkParent=None,
	             attrControl=None,
	             ):
		""""
		:param start:
		:param mid:
		:param end:
		:param name:
		:param fkName:
		:param ikName:
		:param scale:
		:param axis:
		:param side:
		:param index:
		:param networkRoot:
		"""

		self.objects = ults.listCheck(objects)
		self.name = name
		self.fkName = fkName if fkName else naming.convention(name, naming.rig.fk)
		self.ikName = ikName if ikName else naming.convention(name, naming.rig.ik)

		self.scale = scale
		self.axis = axis
		self.side = side
		self.index = index

		self.fkControl = []
		self.fkGroup = []
		self.fkPoleVector = None
		self.fkParent = None

		self.ikJoint = []
		self.ikControl = []
		self.ikGroup = []
		self.ikHandle = None
		self.ikPoleVector = None
		self.ikParent = None

		self.ribbonControl = []
		self.ribbonGroup = []

		self.detailObjects = []
		self.detailControl = []
		self.detailGroup = []

		self.attrControl = attrControl
		self.attrGroup = None

		self.parent = None
		self.network = None
		self.networkRoot = networkRoot
		self.networkParent = networkParent
		self.set = None

	def __str__(self):
		print ''
		for x in sorted(vars(self).iterkeys()):
			print '{}: {}'.format(x, vars(self)[x])
		return str()

	def createParent(self, name, child=None):
		self.parent = cmds.group(n='{}_{}'.format(self.name, name), em=True)
		if child:
			ults.snap(child, self.parent, t=True, r=True)
		return

	def parentToObjectParent(self, child, obj):
		parent = cmds.listRelatives(child, parent=True)
		if parent:
			cmds.parent(obj, parent[0])
		return

	def createDetailChain(self, objects):
		objects = ults.listCheck(objects)
		indexNum = 0
		for obj in objects:
			i = objects.index(obj)
			children = skeleton.getBindJoint(obj)

			if children:
				for child in children:
					ctl = component.DETAILCONTROL(name=naming.convention(self.name,
					                                                     self.side.upper()[0],
					                                                     self.index,
					                                                     naming.rig.detail,
					                                                     indexNum,
					                                                     naming.rig.ctl
					                                                     ),
					                              scale=self.scale,
					                              parent=None,
					                              child=child,
					                              index=i,
					                              axis=self.axis,
					                              )
					indexNum += 1
					cmds.parent(ctl.group, obj)
					cmds.parentConstraint(ctl.transform, child, mo=True)
					cmds.scaleConstraint(ctl.transform, child, mo=True)

					self.detailObjects.append(child)
					self.detailControl.append(ctl.transform)
					self.detailGroup.append(ctl.group)

					grandchildren = skeleton.getAllBindJoints(child)
					if grandchildren:

						for grandchild in grandchildren:
							gctl = component.GRANDCHILDCONTROL(name=naming.convention(grandchild,
							                                                          naming.rig.ctl
							                                                          ),
							                                   scale=cmds.getAttr('{}.radius'.format(grandchild)),
							                                   parent=None,
							                                   child=grandchild,
							                                   index=i,
							                                   axis=self.axis,
							                                   )
							indexNum += 1
							cmds.parent(gctl.group, child)
							cmds.parentConstraint(gctl.transform, grandchild, mo=True)
							cmds.scaleConstraint(gctl.transform, grandchild, mo=True)
							self.detailObjects.append(grandchild)
							self.detailControl.append(gctl.transform)
							self.detailGroup.append(gctl.group)
		return

	def createGrandchildren(self, objects):
		objects = ults.listCheck(objects)
		i = 0
		indexNum = 0
		for obj in objects:
			children = skeleton.getBindJoint(obj)

			if children:
				for child in children:

					grandchildren = skeleton.getBindJoint(child)
					if grandchildren:

						for grandchild in grandchildren:
							ctl = component.GRANDCHILDCONTROL(name=naming.convention(grandchild,
							                                                         naming.rig.ctl
							                                                         ),
							                                  scale=cmds.getAttr('{}.radius'.format(grandchild)),
							                                  parent=None,
							                                  child=grandchild,
							                                  index=i,
							                                  axis=self.axis,
							                                  )

							cmds.parent(ctl.group, child)
							cmds.parentConstraint(ctl.transform, grandchild, mo=True)
							cmds.scaleConstraint(ctl.transform, grandchild, mo=True)
							self.detailObjects.append(grandchild)
							self.detailControl.append(ctl.transform)
							self.detailGroup.append(ctl.group)
							indexNum += 1
							i += 1

		return

	def createRibbonChain(self, start, mid, end):
		upperObjects = skeleton.getBindJoint(start)
		lowerObjects = skeleton.getBindJoint(mid)

		if upperObjects and lowerObjects:
			midObjects = lowerObjects[0]
			lowerObjects.remove(lowerObjects[0])

			ribbon = component.RIBBONLIMB(name=naming.convention(self.name,
			                                                     self.side[0].upper(),
			                                                     self.index,
			                                                     naming.rig.ribbon,
			                                                     ),
			                              start=start,
			                              mid=mid,
			                              end=end,
			                              upperObjects=upperObjects,
			                              lowerObjects=lowerObjects,
			                              midObject=midObjects,
			                              side=self.side,
			                              scale=self.scale / 1.2,
			                              )

			self.detailObjects = self.detailObjects + upperObjects + lowerObjects + ults.listCheck(midObjects)
			self.detailControl = self.detailControl + ribbon.detailControl
			self.detailGroup = self.detailGroup + ribbon.detailGroup

			self.ribbonControl = ribbon.mainControl
			self.ribbonGroup = ribbon.mainGroup

			if self.attrControl:
				attrName = ['sns', 'snsAdd']
				cmds.addAttr(self.attrControl, ln=attrName[0], min=0, max=1, dv=0, k=True)
				cmds.addAttr(self.attrControl, ln=attrName[1], k=True)

				for attr in attrName:
					cmds.connectAttr('{}.{}'.format(self.attrControl, attr),
					                 '{}.{}'.format(ribbon.upperFlexiPlane.parent, attr))
					cmds.connectAttr('{}.{}'.format(self.attrControl, attr),
					                 '{}.{}'.format(ribbon.lowerFlexiPlane.parent, attr))

		return

	def createTwistChain(self, start, mid, end):
		chain = component.TWISTCHAIN(start=start,
		                             mid=mid,
		                             end=end,
		                             scale=self.scale,
		                             axis=self.axis,
		                             name=naming.convention(self.name,
		                                                    self.side.upper()[0],
		                                                    self.index,
		                                                    naming.rig.aux,
		                                                    ))
		self.detailObjects = chain.objects
		self.detailControl = chain.control
		self.detailGroup = chain.group

		if self.attrControl:
			attrName = ['sns', 'snsAdd']
			cmds.addAttr(self.attrControl, ln=attrName[0], min=0, max=1, dv=0, k=True)
			cmds.addAttr(self.attrControl, ln=attrName[1], k=True)

			for attr in attrName:
				cmds.connectAttr('{}.{}'.format(self.attrControl, attr),
				                 '{}.{}'.format(chain.upperTwist.parent, attr))

		return

	def createFKChain(self, objects):
		name = naming.convention(self.name,
		                         self.side.upper()[0],
		                         self.index,
		                         naming.rig.fk,
		                         )
		fk = component.FKCHAIN(objects,
		                       name=name,
		                       scale=self.scale,
		                       axis=self.axis,
		                       side=self.side,
		                       )
		self.parentToObjectParent(objects[0], fk.parent)
		self.fkControl = fk.control
		self.fkGroup = fk.group
		self.fkParent = fk.parent
		return

	def createIKChain(self, objects):
		name = naming.convention(self.name,
		                         self.side.upper()[0],
		                         self.index,
		                         naming.rig.ik,
		                         )
		ik = component.IKCHAIN(objects,
		                       name=name,
		                       scale=self.scale,
		                       axis=self.axis,
		                       side=self.side,
		                       )

		self.parentToObjectParent(objects[0], ik.parent)
		self.ikJoint = ik.joint
		self.ikControl = ik.control
		self.ikGroup = ik.group
		self.ikHandle = ik.ikHandle
		self.ikPoleVector = ik.ikPoleVector
		self.ikParent = ik.parent

		return

	def createFKPoleVector(self):
		fkPoleVector = cmds.group(n=naming.convention(self.name,
		                                              self.side.upper()[0],
		                                              self.index,
		                                              naming.rig.fk,
		                                              naming.rig.poleVector,
		                                              naming.rig.null,
		                                              ),
		                          em=True)
		ults.snap(self.ikControl[1], fkPoleVector, t=True, r=True)
		cmds.parent(fkPoleVector, self.fkControl[1])
		self.fkPoleVector = fkPoleVector
		return

	def createAttrControl(self, obj):
		if self.side == 'Left':
			axis = [1, -1, 0]
		elif self.side == 'Right':
			axis = [1, 1, 0]
		'''
		if self.name == 'leg':
			if self.side == 'Left':
				axis = [1, 0, 1]
			elif self.side == 'Right':
				axis = [1, 0, -1]
		'''
		ctl = component.ATTRCONTROL(name=naming.convention(self.name,
		                                                   self.side.upper()[0],
		                                                   self.index,
		                                                   naming.rig.attr,
		                                                   naming.rig.ctl,
		                                                   ),
		                            child=obj,
		                            scale=self.scale + .25,
		                            side=self.side,
		                            label='None',
		                            axis=axis,
		                            )

		self.attrControl = ctl.transform
		self.attrGroup = ctl.group
		cmds.parent(self.attrGroup, obj)
		ults.lockAttributes(self.attrControl, hide=True)
		return

	def createFKIKChain(self, objects):
		self.createFKChain(objects)
		self.createIKChain(objects)
		self.createFKPoleVector()
		self.createAttrControl(objects[-1])
		self.createFKIKConnections(ctl=self.attrControl)
		self.parentToRootControl(self.ikGroup[1])
		self.parentToRootControl(self.ikGroup[2])
		return

	def createFKIKConnections(self, ctl, name=naming.rig.fkik):
		# Constraints
		fkik = ults.createFKIK(obj=self.objects,
		                       fk=self.fkControl,
		                       ik=self.ikJoint,
		                       ctl=ctl,
		                       n=name,
		                       )

		# Visibility
		for grp in self.fkGroup:
			i = self.fkGroup.index(grp)
			cmds.setAttr('{}.v'.format(grp), lock=False)
			cmds.connectAttr('{}.outputX'.format(fkik[1][i]), '{}.v'.format(grp), f=True)

		for grp in self.ikGroup:
			cmds.setAttr('{}.v'.format(grp), lock=False)
			cmds.connectAttr('{}.{}'.format(self.attrControl, name), '{}.v'.format(grp), f=True)

		# Stretch
		attrName = naming.rig.stretch
		cmds.addAttr(ctl, ln=attrName, k=True)
		if self.side == 'Right':
			mult = cmds.createNode('multiplyDivide', name='{}_mult0'.format(ctl))
			axis = ['X', 'Y', 'Z']
			for ax in axis:
				cmds.setAttr('{}.input2{}'.format(mult, ax), -1)

		for i in range(1, 3, 1):
			if self.side == 'Right':
				cmds.connectAttr('{}.{}'.format(ctl, attrName),
				                 '{}.input1{}'.format(mult, axis[i]))

				cmds.connectAttr('{}.output{}'.format(mult, axis[i]),
				                 '{}.{}[{}]'.format(self.ikParent, attrName, i))
				cmds.connectAttr('{}.output{}'.format(mult, axis[i]),
				                 '{}.{}[{}]'.format(self.fkParent, attrName, i))
			else:
				cmds.connectAttr('{}.{}'.format(ctl, attrName),
				                 '{}.{}[{}]'.format(self.fkParent, attrName, i))
				cmds.connectAttr('{}.{}'.format(ctl, attrName),
				                 '{}.{}[{}]'.format(self.ikParent, attrName, i))

		return

	def createNetwork(self, typ):
		name = naming.convention(self.name,
		                         self.side.upper()[0],
		                         self.index,
		                         naming.rig.network,
		                         )

		self.network = cmds.createNode('network', n=name)
		self.addDefaultNetworkAttributes(typ)

		if self.networkParent:
			self.connectToNetworkRoot()

		if self.networkRoot:
			self.multiConnectToNetwork(self.network, self.networkRoot, naming.convention(self.name, self.side[0]))
			# self.connectToNetwork(self.network, self.networkRoot, typ)
			for attr in ['jointDisplay', 'controlDisplay']:
				cmds.connectAttr('{}.{}'.format(self.networkRoot, attr), '{}.{}'.format(self.network, attr))
		return

	def addDefaultNetworkAttributes(self, typ):
		node = self.network
		cmds.addAttr(node, ln='type', dt='string')
		ults.addSideAttr(node)
		cmds.addAttr(node, ln='index', at='long')
		cmds.setAttr('{}.type'.format(node), typ, type='string', lock=True)
		cmds.setAttr('{}.index'.format(node), self.index)
		ults.setEnumByString(node, 'side', self.side)
		cmds.addAttr(node, ln='children', dt='string')
		ults.addBoolAttr(node, 'jointDisplay')
		ults.addBoolAttr(node, 'controlDisplay')
		return

	def createSet(self, objects):
		name = naming.convention(self.name,
		                         self.side.upper()[0],
		                         self.index,
		                         naming.rig.set,
		                         )

		cmds.select(d=True)
		objects = ults.listCheck(objects)
		self.set = cmds.sets(objects, name=name)

		if self.networkRoot:
			rootSet = self.getConnected(self.networkRoot, naming.rig.set)

			if cmds.objExists(str(rootSet)):
				cmds.sets(self.set, add=rootSet)
		return

	def hideObjectsAttributes(self, objects):
		objects = ults.listCheck(objects)
		for obj in objects:
			ults.hideAttributes(obj)
		return

	def connectToNetwork(self, obj, network, name):
		attrName = 'rigNetworkRoot'
		objAttr = '{}.{}'.format(obj, attrName)
		networkAttr = '{}.{}'.format(network, name)

		if not cmds.attributeQuery(attrName, node=obj, ex=True):
			cmds.addAttr(obj, ln=attrName, at='message')

		if cmds.attributeQuery(name, node=network, ex=True):
			if cmds.attributeQuery(name, node=network, m=True):
				mList = cmds.listAttr('{}.{}'.format(network, name), m=True)
				if mList:
					i = mList.index(mList[-1]) + 1
				else:
					i = 0

				ults.addIndexValue(obj, i)
				networkAttr = '{}.{}[{}]'.format(network, name, i)
		else:
			cmds.addAttr(network, ln=name, at='message')

		cmds.connectAttr(networkAttr, objAttr, force=True)
		return

	def connectToNetworkRoot(self, obj, network):
		attrName = 'rigNetworkRoot'
		if not cmds.attributeQuery(attrName, node=obj, ex=True):
			cmds.addAttr(obj, ln=attrName, at='message')
		if not self.getConnected(obj, attrName):
			cmds.connectAttr('{}.children'.format(network), '{}.{}'.format(obj, attrName), f=True)
		return

	def multiConnectToNetwork(self, objects, network, name):
		objects = ults.listCheck(objects)
		attrName = 'rigNetwork'

		if not cmds.attributeQuery(name, node=network, ex=True):
			cmds.addAttr(network, ln=name, dt='string', m=True)
			i = 0
		else:
			if cmds.listAttr('{}.{}'.format(network, name), m=True):
				i = int(cmds.listAttr('{}.{}'.format(network, name), m=True)[-1].split('[')[-1].split(']')[0])
			else:
				i = 0

		for obj in objects:
			if self.networkRoot:
				self.connectToNetworkRoot(obj, self.networkRoot)

			if not cmds.attributeQuery(attrName, node=obj, ex=True):
				cmds.addAttr(obj, ln=attrName, at='message')

			cmds.connectAttr('{}.{}[{}]'.format(network, name, i), '{}.{}'.format(obj, attrName), f=True)
			ults.addIndexValue(obj, i)
			i += 1
		return

	def getConnected(self, obj, attr, indexValue=0):
		attrName = '{}.{}'.format(obj, attr)
		attrNameIndex = '{}.{}[{}]'.format(obj, attr, indexValue)
		if cmds.attributeQuery(attr, node=obj, ex=True):
			if cmds.attributeQuery(attr, node=obj, m=True):
				query = cmds.listConnections(attrNameIndex)
				return query[0] if query else None
			elif cmds.connectionInfo(attrName, id=True):
				query = cmds.listConnections(cmds.connectionInfo(attrName, ged=True))
				return query[0] if query else None
			else:
				query = cmds.listConnections(attrName)
				return query[0] if query else None
		else:
			return None

	def createLocalWorld(self, obj, local):
		attrName = 'localWorld'

		if self.networkRoot:
			cogNetwork = self.getConnected(self.networkRoot, 'cog_C')
			cog = self.getConnected(cogNetwork, 'fkControl', 0) if cogNetwork else None

			if cog:
				ults.createLocalWorld(obj=obj,
				                      local=local,
				                      world=cog,
				                      n=attrName,
				                      )
		return

	def parentToRootControl(self, obj):
		if self.networkRoot:
			offset = self.getConnected(self.networkRoot, 'fkControl', indexValue=1)

			if offset:
				cmds.parent(obj, offset)
		return

	def createNetworkConnections(self):
		# Parent
		if self.parent:
			self.connectToNetwork(self.parent, self.network, 'parentGroup')

		# Attr Control
		if self.attrControl:
			self.connectToNetwork(self.attrControl, self.network, 'attrControl')

		# Set
		if self.set:
			self.connectToNetwork(self.set, self.network, 'set')

		# FK
		if self.fkParent:
			self.connectToNetwork(self.fkParent, self.network, 'fkParent')

		if self.fkPoleVector:
			self.connectToNetwork(self.fkPoleVector, self.network, 'fkPoleVector')

		# IK
		if self.ikParent:
			self.connectToNetwork(self.ikParent, self.network, 'ikParent')

		if self.ikPoleVector:
			self.connectToNetwork(self.ikPoleVector, self.network, 'ikPoleVector')

		if self.ikHandle:
			self.connectToNetwork(self.ikHandle, self.network, 'ikHandle')

		# Skeleton
		if self.objects:
			self.multiConnectToNetwork(self.objects, self.network, 'skeleton')
			con = cmds.createNode('condition', name='{}_jointDisplay_condition'.format(self.network))
			cmds.setAttr('{}.colorIfTrueR'.format(con), 2)
			cmds.setAttr('{}.colorIfFalseR'.format(con), 0)
			cmds.connectAttr('{}.jointDisplay'.format(self.network), '{}.firstTerm'.format(con))
			for obj in self.objects:
				cmds.connectAttr('{}.outColorR'.format(con), '{}.drawStyle'.format(obj))

			if self.detailObjects:
				self.multiConnectToNetwork(self.detailObjects, self.network, 'skeletonDetail')
				for detail in self.detailObjects:
					cmds.connectAttr('{}.outColorR'.format(con), '{}.drawStyle'.format(detail))

		# Detail Controls
		if self.detailControl:
			attrName = 'detailControlDisplay'
			self.multiConnectToNetwork(self.detailControl, self.network, 'detailControl')
			ults.addBoolAttr(self.network, attrName)

			for detail in self.detailGroup:
				cmds.connectAttr('{}.{}'.format(self.network, attrName), '{}.v'.format(detail))

			if self.ribbonControl:
				self.multiConnectToNetwork(self.ribbonControl, self.network, 'ribbonControl')

				for ribbon in self.ribbonGroup:
					cmds.connectAttr('{}.{}'.format(self.network, attrName), '{}.v'.format(ribbon))

		# FK Control
		if self.fkControl:
			self.multiConnectToNetwork(self.fkControl, self.network, 'fkControl')

		# IK Control
		if self.ikControl:
			self.multiConnectToNetwork(self.ikControl, self.network, 'ikControl')

		if self.ikJoint:
			self.multiConnectToNetwork(self.ikJoint, self.network, 'ikJoint')

		if self.attrControl:
			# Attr Display
			attrName = naming.rig.detailControlDisplay

			if not cmds.attributeQuery(attrName, node=self.attrControl, ex=True):
				ults.addBoolAttr(self.attrControl, attrName)
			cmds.connectAttr('{}.{}'.format(self.attrControl, attrName), '{}.{}'.format(self.network, attrName))

		# Attr To Network FKIK
		# cmds.addAttr(self.network, ln=naming.rig.fkik, min=0, max=1, dv=0)
		# cmds.connectAttr('{}.{}'.format(self.attrControl, naming.rig.fkik),
		#                  '{}.{}'.format(self.network, naming.rig.fkik))
		return

	def createAttrControlConnections(self):
		if self.attrControl:
			cmds.addAttr(self.network, ln=naming.rig.fkik, min=0, max=1, dv=0)
			cmds.connectAttr('{}.{}'.format(self.attrControl, naming.rig.fkik),
			                 '{}.{}'.format(self.network, naming.rig.fkik))
		return


########################################################################################################################
#
#
#	FKIK CLASS
#
#
########################################################################################################################


class FKIK(BASE):
	def __init__(self,
	             start,
	             mid,
	             end,
	             name='fkik',
	             ):
		BASE.__init__(self,
		              objects=[start, mid, end],
		              name=name,
		              )

		self.createFKIKChain(self.objects)
		self.createNetwork(typ='fkik')
		self.createNetworkConnections()


########################################################################################################################
#
#
#	ROOT CLASS
#
#
########################################################################################################################


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
		self.scale = int(skeleton.determineHeight(self.root) / 2)
		return

	def createControls(self):

		ctl = component.CONTROL(name='{}_ctl'.format(self.name),
		                        typ='root',
		                        scale=self.scale + 2,
		                        axis=[0, 0, 0],
		                        )

		offset = component.CONTROL(name='{}_offset_ctl'.format(self.name),
		                           typ='center',
		                           scale=self.scale,
		                           axis=[0, 0, 0],
		                           )

		ults.presetWireColor([ctl.transform, offset.transform, ], typ=ults.component.center)
		cmds.parent(offset.group, ctl.transform)
		self.fkControl = [ctl.transform, offset.transform]
		self.fkGroup = [ctl.group, offset.group]

		if self.root:
			cmds.parent(self.root, offset.transform)
		return

	def createRootOffset(self):
		attrName = 'rootOffset'
		parent = self.fkControl[0]

		rootOffset = component.CONTROL(name='{}_root_offset_ctl'.format(self.name),
		                               typ='center',
		                               scale=self.scale - 0.8,
		                               axis=[0, 0, 0],
		                               )

		ults.presetWireColor([rootOffset.transform], typ=ults.component.center)
		cmds.parent(rootOffset.group, self.fkControl[-1])
		ults.addBoolAttr(obj=parent, name=attrName)
		cmds.connectAttr('{}.{}'.format(parent, attrName), '{}.v'.format(rootOffset.group))

		if self.root:
			cmds.parentConstraint(rootOffset.transform, self.root, mo=True)

		self.fkControl.append(rootOffset.transform)
		self.fkGroup.append(rootOffset.group)
		return

	def setupDisplayAttr(self):
		for attr in ['jointDisplay', 'controlDisplay']:
			ults.addBoolAttr(self.fkControl[0], attr)
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


########################################################################################################################
#
#
#	COG CLASS
#
#
########################################################################################################################


class COG(BASE):
	def __init__(self,
	             cog,
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
		self.objects = [cog]

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
		self.scale = skeleton.determineHeight(self.cog) / 4 + .25
		return

	def createControls(self):
		ctl = component.CONTROL(name='{}_ctl'.format(self.name),
		                        typ='center',
		                        scale=self.scale,
		                        axis=[0, 0, 0],
		                        )
		ults.snap(self.cog, ctl.group, t=True, r=False)
		ults.presetWireColor(ctl.transform, typ=ults.component.center)
		cmds.parentConstraint(ctl.transform, self.cog, mo=True)
		self.fkControl = [ctl.transform]
		self.fkGroup = [ctl.group]
		return

	def createHipControl(self):
		ctl = component.CONTROL(name='hip_ctl',
		                        typ=control.component.hip,
		                        scale=self.scale - .15,
		                        axis=[0, 0, 0],
		                        )
		ults.snap(self.hip, ctl.group, t=True, r=False)
		ults.presetWireColor(ctl.transform, typ=ults.component.center)
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
			grp = ults.createGroup(rootOffset, '{}_pos_grp'.format(rootOffset))
			cmds.pointConstraint(self.fkControl[0], grp, skip='y', mo=True)


########################################################################################################################
#
#
#	SPINE CLASS
#
#
########################################################################################################################


class SPINE(BASE):
	def __init__(self,
	             objects,
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
			distance = ults.getDistance(start, end)
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
		ults.presetWireColor(self.fkControl, 'center')
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
	             objects,
	             networkRoot=None,
	             name=naming.component.neck,
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
				distanceList.append(ults.getDistance(start, end))

		self.scale = max(distanceList) + 0.25
		return


########################################################################################################################
#
#
#	HEAD CLASS
#
#
########################################################################################################################


class HEAD(BASE):
	def __init__(self,
	             head,
	             networkRoot=None,
	             name=naming.component.head,
	             scale=1,
	             attrControl=None,
	             ):
		BASE.__init__(self,
		              objects=ults.listCheck(head),
		              networkRoot=networkRoot,
		              name=name,
		              side=naming.side.center,
		              scale=scale,
		              attrControl=attrControl,
		              )

		self.head = head
		self.getScale()
		self.createControls()
		self.createIK()
		self.setupHierarchy()
		self.createFKIK()
		self.createDetailChain(self.objects)

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
		ctl = component.CONTROL(name='{}_ctl'.format(self.name),
		                        typ=control.component.lollipop,
		                        scale=self.scale,
		                        axis=[1, 0, -1],
		                        )
		ults.snap(self.head, ctl.group, t=True, r=True)
		ults.presetWireColor(ctl.transform, typ=ults.component.center)
		ults.lockScale(ctl.transform)

		self.fkControl = [ctl.transform]
		self.fkGroup = [ctl.group]
		return

	def createIK(self):
		ctl = component.CONTROL(name='{}_ik_ctl'.format(self.name),
		                        typ=control.component.sphere,
		                        scale=self.scale / 8,
		                        axis=[0, 0, 0],
		                        )

		ults.snap(self.head, ctl.group, t=True)
		distance = cmds.xform(self.head, q=True, ws=True, rp=True)[1]
		cmds.xform(ctl.group, ws=True, t=[0, 0, distance], r=True)

		ikNull = cmds.group(name='{}_ik_aim'.format(self.name), em=True)
		ikGrp = cmds.group(ikNull, name='{}_grp'.format(ikNull))
		ults.snap(self.head, ikGrp, t=True, r=True)
		ults.createAimVector(ctl.transform, ikNull, name='{}_aimVector'.format(self.name))
		ults.presetWireColor(ctl.transform, typ=ults.component.ik)

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
		attrName = naming.rig.fkik
		ults.createFKIK(obj=self.head,
		                fk=self.fkControl[0],
		                ctl=self.fkControl[0],
		                ik=self.ikControl[0],
		                n=attrName,
		                )

		cmds.connectAttr('{}.{}'.format(self.fkControl[0], attrName), '{}.v'.format(self.ikGroup[1]))
		return


########################################################################################################################
#
#
#	ARM CLASS
#
#
########################################################################################################################


class ARM(BASE):
	def __init__(self,
	             side,
	             shoulder,
	             elbow,
	             hand,
	             collar=None,
	             networkRoot=None,
	             name=naming.component.arm,
	             index=0,
	             ):
		BASE.__init__(self,
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
		self.createTwistChain(self.shoulder, self.elbow, self.hand)

		if self.collar:
			self.createDetailChain(self.collar)
			self.createCollar()

		self.createGrandchildren([self.shoulder, self.elbow, self.hand])
		self.createHand()
		self.createLocalWorld(obj=self.fkControl[0],
		                      local=self.fkGroup[0],
		                      )
		self.createSet([self.collarFKControl] + self.fkControl + self.ikControl)
		self.createNetwork(typ=self.name)

		self.createNetworkConnections()
		self.updateNetwork()

	def getScale(self):
		self.scale = ults.getDistance(self.shoulder, self.elbow) / 2.5
		return

	def createCollar(self):
		ctl = component.CONTROL(name=naming.convention(self.name,
		                                               self.side[0],
		                                               self.index,
		                                               naming.rig.fk,
		                                               naming.component.collar.capitalize(),
		                                               naming.rig.ctl,
		                                               ),
		                        typ=control.component.dumbbell,
		                        scale=self.scale,
		                        axis=[1, 0, 0],
		                        child=self.collar,
		                        side=self.side,
		                        label=naming.component.collar,
		                        color=ults.component.fk,
		                        )
		ults.lockScale(ctl.transform)
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


class HAND(BASE):
	def __init__(self,
	             hand,
	             side,
	             networkRoot=None,
	             name=naming.component.hand,
	             index=0,
	             ):
		BASE.__init__(self,
		              objects=ults.listCheck(hand),
		              networkRoot=networkRoot,
		              name=name,
		              side=side,
		              index=index,
		              )

		self.hand = hand
		self.finger = []
		self.createFingers()

		self.createNetwork(typ=naming.convention(self.name,
		                                         self.side.upper()[0],
		                                         self.index,
		                                         )
		                   )
		self.updateNetwork()

	def createFingers(self):
		children = skeleton.getJointChildren(self.hand)

		i = 0
		for child in children:
			joints = skeleton.getJointOrder(child)
			finger = DIGIT(objects=joints,
			               name=naming.component.finger,
			               side=self.side,
			               networkRoot=self.networkRoot,
			               index=i,
			               )
			self.finger.append(finger)
			i += 1
		return

	def updateNetwork(self):
		return


class DIGIT(BASE):
	def __init__(self,
	             objects,
	             side=None,
	             networkRoot=None,
	             name=naming.component.digit,
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

		self.createNetwork(typ=naming.convention(self.name,
		                                         self.side.upper()[0],
		                                         self.index,
		                                         )
		                   )
		self.createSet(self.fkControl)
		self.createNetworkConnections()

	def getScale(self):
		self.scale = ults.getDistance(self.objects[0], self.objects[1]) / 2
		return

	def setupHierarchy(self):
		for obj in self.objects:
			i = self.objects.index(obj)
			cmds.parentConstraint(self.fkControl[i], obj, mo=True)
		return


########################################################################################################################
#
#
#	LEG CLASS
#
#
########################################################################################################################


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
		self.scale = ults.getDistance(self.hip, self.knee) / 5
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
		ults.lockRotate(self.ikGroup[-1])

		return

	def createToe(self):
		ctl = component.CONTROL(name=naming.convention(self.name,
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
		                        color=ults.component.fk,
		                        )
		ults.lockScale(ctl.transform)

		parent = cmds.listRelatives(self.toe, parent=True)
		if parent:
			cmds.parent(ctl.group, parent[0])

		self.toeFKControl = ctl.transform
		self.toeFKGroup = ctl.group
		self.objects.insert(0, self.toe)
		return

	def createFootRoll(self):
		self.roll = ults.createIKFootRollNulls(foot=self.foot,
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

		ults.snap(self.roll.wire, self.ikGroup[-1], t=True)
		ults.lockAttributes(self.ikGroup[-1])

		cmds.parent(self.roll.wire, self.ikGroup[-1])
		ults.freezeTransform(self.roll.wire)
		ults.swapShape(self.ikControl[-1], self.roll.wire)
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
