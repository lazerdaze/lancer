# Lancer Modules
from rig.utils import *
from rig.piece import *

# Maya Moudles
from maya import cmds


class BASE(object):
	def __init__(self,
	             objects=None,
	             name=Component.base,
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

		self.objects = rigging.listCheck(objects)
		self.name = name
		self.fkName = fkName if fkName else longName(name, Component.fk)
		self.ikName = ikName if ikName else longName(name, Component.ik)

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
			rigging.snap(child, self.parent, t=True, r=True)
		return

	def parentToObjectParent(self, child, obj):
		parent = cmds.listRelatives(child, parent=True)
		if parent:
			cmds.parent(obj, parent[0])
		return

	def createDetailChain(self, objects):
		objects = rigging.listCheck(objects)
		indexNum = 0
		for obj in objects:
			i = objects.index(obj)
			children = getBindJoint(obj)

			if children:
				for child in children:
					ctl = DETAILCONTROL(name=longName(self.name,
					                                  self.side.upper()[0],
					                                  self.index,
					                                  Component.detail,
					                                  indexNum,
					                                  Component.control
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

					grandchildren = getAllBindJoints(child)
					if grandchildren:

						for grandchild in grandchildren:
							gctl = GRANDCHILDCONTROL(name=longName(grandchild,
							                                       Component.control
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
		objects = rigging.listCheck(objects)
		i = 0
		indexNum = 0
		for obj in objects:
			children = getBindJoint(obj)

			if children:
				for child in children:

					grandchildren = getBindJoint(child)
					if grandchildren:

						for grandchild in grandchildren:
							ctl = GRANDCHILDCONTROL(name=longName(grandchild,
							                                      Component.control
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
		upperObjects = getBindJoint(start)
		lowerObjects = getBindJoint(mid)

		if upperObjects and lowerObjects:
			midObjects = lowerObjects[0]
			lowerObjects.remove(lowerObjects[0])

			ribbon = RIBBONLIMB(name=longName(self.name,
			                                  self.side[0].upper(),
			                                  self.index,
			                                  Component.ribbon,
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

			self.detailObjects = self.detailObjects + upperObjects + lowerObjects + rigging.listCheck(midObjects)
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
		chain = TWISTCHAIN(start=start,
		                   mid=mid,
		                   end=end,
		                   scale=self.scale,
		                   axis=self.axis,
		                   name=longName(self.name,
		                                 self.side.upper()[0],
		                                 self.index,
		                                 Component.aux,
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
		name = longName(self.name,
		                self.side.upper()[0],
		                self.index,
		                Component.fk,
		                )
		fk = FKCHAIN(objects,
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
		name = longName(self.name,
		                self.side.upper()[0],
		                self.index,
		                Component.ik,
		                )
		ik = IKCHAIN(objects,
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
		fkPoleVector = cmds.group(n=longName(self.name,
		                                     self.side.upper()[0],
		                                     self.index,
		                                     Component.fk,
		                                     Component.poleVector,
		                                     Component.null,
		                                     ),
		                          em=True)
		rigging.snap(self.ikControl[1], fkPoleVector, t=True, r=True)
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
		ctl = ATTRCONTROL(name=longName(self.name,
		                                self.side.upper()[0],
		                                self.index,
		                                Component.attr,
		                                Component.control,
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
		rigging.lockKeyableAttributes(self.attrControl, hide=True)
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

	def createFKIKConnections(self, ctl, name=Component.fkik):
		# Constraints
		fkik = rigging.createFKIK(obj=self.objects,
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
		attrName = Component.stretch
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
		name = longName(self.name,
		                self.side.upper()[0],
		                self.index,
		                Component.network,
		                )

		self.network = cmds.createNode('network', n=name)
		self.addDefaultNetworkAttributes(typ)

		if self.networkParent:
			self.connectToNetworkRoot()

		if self.networkRoot:
			self.multiConnectToNetwork(self.network, self.networkRoot, longName(self.name, self.side[0]))
			# self.connectToNetwork(self.network, self.networkRoot, typ)
			for attr in ['jointDisplay', 'controlDisplay']:
				cmds.connectAttr('{}.{}'.format(self.networkRoot, attr), '{}.{}'.format(self.network, attr))
		return

	def addDefaultNetworkAttributes(self, typ):
		node = self.network
		cmds.addAttr(node, ln='type', dt='string')
		rigging.addSideAttr(node)
		cmds.addAttr(node, ln='index', at='long')
		cmds.setAttr('{}.type'.format(node), typ, type='string', lock=True)
		cmds.setAttr('{}.index'.format(node), self.index)
		rigging.setEnumByString(node, 'side', self.side)
		cmds.addAttr(node, ln='children', dt='string')
		rigging.addBoolAttr(node, 'jointDisplay')
		rigging.addBoolAttr(node, 'controlDisplay')
		return

	def createSet(self, objects):
		name = longName(self.name,
		                self.side.upper()[0],
		                self.index,
		                Component.set,
		                )

		cmds.select(d=True)
		objects = rigging.listCheck(objects)
		self.set = cmds.sets(objects, name=name)

		if self.networkRoot:
			rootSet = self.getConnected(self.networkRoot, Component.set)

			if cmds.objExists(str(rootSet)):
				cmds.sets(self.set, add=rootSet)
		return

	def hideObjectsAttributes(self, objects):
		objects = rigging.listCheck(objects)
		for obj in objects:
			rigging.hideAttributes(obj)
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

				rigging.addIndexValue(obj, i)
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
		objects = rigging.listCheck(objects)
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
			rigging.addIndexValue(obj, i)
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
				rigging.createLocalWorld(obj=obj,
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
			rigging.addBoolAttr(self.network, attrName)

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
			attrName = Component.detailControlDisplay

			if not cmds.attributeQuery(attrName, node=self.attrControl, ex=True):
				rigging.addBoolAttr(self.attrControl, attrName)
			cmds.connectAttr('{}.{}'.format(self.attrControl, attrName), '{}.{}'.format(self.network, attrName))

		# Attr To Network FKIK
		# cmds.addAttr(self.network, ln=Component.fkik, min=0, max=1, dv=0)
		# cmds.connectAttr('{}.{}'.format(self.attrControl, Component.fkik),
		#                  '{}.{}'.format(self.network, Component.fkik))
		return

	def createAttrControlConnections(self):
		if self.attrControl:
			cmds.addAttr(self.network, ln=Component.fkik, min=0, max=1, dv=0)
			cmds.connectAttr('{}.{}'.format(self.attrControl, Component.fkik),
			                 '{}.{}'.format(self.network, Component.fkik))
		return
