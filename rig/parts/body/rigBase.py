# Lancer Modules
from rig.utils import *

# Maya Moudles
from maya import cmds


class RIGBASE(object):
	def __init__(self,
	             items=None,
	             prefix=None,
	             name=Component.base,
	             parent=None,
	             children=None,
	             sector=None,
	             kind=Component.rig,
	             fkName=None,
	             ikName=None,
	             scale=1.0,
	             axis=None,
	             side=None,
	             index=None,
	             masterParent=None,
	             master=None,
	             ):
		'''
		Base Class for rigging body parts.

		:param list items:          Items to be rigged
		:type items:                list or dict or tuple or None
		:param str prefix:          Prefix name
		:type prefix:               str or None
		:param str name:            Base name
		:type name:                 str or None
		:param object parent:       Parent Class
		:type parent:               object or str or None
		:param list children:       Class children
		:type children:             list or dict or tuple or None
		:param str sector:          Sector name
		:type sector:               str or None
		:param str kind:            Kind name
		:type kind:                 str or None
		:param str fkName:          FK prefix name
		:type fkName:               str or None
		:param str ikName:          IK prefix name
		:type ikName:               str or None
		:param float scale:         Scale of controls
		:type scale:                float or None
		:param list axis:           Controls axis direction
		:type axis:                 list or None
		:param str side:            Side name
		:type side:                 str or None
		:param int index:           Index value
		:type index:                int or None
		:param object master:       Root of class that contains all relationship information and functionality
		:type master:               object or str or None
		:param str networkRoot:
		:param str networkParent:
		'''

		# Name
		self.prefix = prefix
		self.side = side
		self.name = name
		self.sector = sector
		self.index = index
		self.kind = kind

		# Relationships
		self.parent = parent
		self.children = listCheck(children)
		self.items = listCheck(items)
		self.topNode = None
		self.masterParent = masterParent
		self.set = None

		# Attributes
		self.scale = scale
		self.axis = axis

		# FK
		self._fkPrefix = fkName if fkName else None
		self.fkControl = []
		self.fkGroup = []
		self.fkPoleVector = None
		self.fkParent = None

		# IK
		self._ikPrefix = ikName if ikName else None
		self.ikJoint = []
		self.ikControl = []
		self.ikGroup = []
		self.ikHandle = None
		self.ikPoleVector = None
		self.ikParent = None

		# Ribbon
		self.ribbonControl = []
		self.ribbonGroup = []

		# Detail
		self.detailObjects = []
		self.detailControl = []
		self.detailGroup = []

		# Master
		self.master = master
		self.masterGroup = None

	def __str__(self):
		return '{} {}'.format(self.__class__.__name__, self.longName)

	####################################################################################################################
	# Name
	####################################################################################################################

	@property
	def longName(self):
		return longName(self.prefix,
		                self.side[0].upper() if self.side else None,
		                self.name,
		                self.sector,
		                self.index,
		                )

	@longName.setter
	def longName(self, prefix=None, name=None, side=None, sector=None, index=None):
		if prefix:
			self.prefix = prefix
		if name:
			self.name = name
		if side:
			self.side = side
		if sector:
			self.sector = sector
		if index:
			self.index = index
		return

	@property
	def fkPrefix(self):
		if self._fkPrefix:
			return self._fkPrefix
		return longName(self.longName, Component.fk)

	@property
	def ikPrefix(self):
		if self._fkPrefix:
			return self._fkPrefix
		return longName(self.longName, Component.ik)

	def printAttributes(self):
		var = ''
		for x in sorted(vars(self).iterkeys()):
			var += '{}: {}\n'.format(x, vars(self)[x])
		print var
		return var

	####################################################################################################################
	# Hierarchy
	####################################################################################################################

	def createParent(self, name, child=None):
		self.parent = cmds.group(n='{}_{}'.format(self.name, name), em=True)
		if child:
			snap(child, self.parent, t=True, r=True)
		return

	@staticmethod
	def parentToObjectParent(child, obj):
		parent = cmds.listRelatives(child, parent=True)
		if parent:
			cmds.parent(obj, parent[0])
		return

	####################################################################################################################
	# Control
	####################################################################################################################

	def createControl(self,
	                  name='rig',
	                  parent=None,
	                  item=None,
	                  wireType=WireType.circleRotate,
	                  axis=None,
	                  scale=1.0,
	                  index=None,
	                  color=WireColor.blue,
	                  offset=False,
	                  kind=None,
	                  ):

		ctrl = Control(prefix=self.prefix,
		               name=name,
		               side=self.side,
		               sector=self.sector,
		               index=index,
		               parent=parent,
		               item=item,
		               axis=axis,
		               scale=scale,
		               wire=wireType,
		               color=color,
		               offset=offset,
		               kind=camelCase(kind, Component.control, capitalize=False)
		               )
		return ctrl

	####################################################################################################################
	# Chains
	####################################################################################################################

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
		snap(self.ikControl[1], fkPoleVector, t=True, r=True)
		cmds.parent(fkPoleVector, self.fkControl[1])
		self.fkPoleVector = fkPoleVector
		return

	def createFKIKChain(self, objects):
		self.createFKChain(objects)
		self.createIKChain(objects)
		self.createFKPoleVector()
		self.createMaster(objects[-1])
		self.createFKIKConnections(ctl=self.master)
		self.parentToRootControl(self.ikGroup[1])
		self.parentToRootControl(self.ikGroup[2])
		return

	def createDetailChain(self, objects):
		objects = listCheck(objects)
		indexNum = 0
		for obj in objects:
			i = objects.index(obj)
			children = getBindJoint(obj)

			if children:
				for child in children:
					ctl = BINDCONTROL(name=longName(self.name,
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
							gctl = LEAFCONTROL(name=longName(grandchild,
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
		objects = listCheck(objects)
		i = 0
		indexNum = 0
		for obj in objects:
			children = getBindJoint(obj)

			if children:
				for child in children:

					grandchildren = getBindJoint(child)
					if grandchildren:

						for grandchild in grandchildren:
							ctl = LEAFCONTROL(name=longName(grandchild,
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

			self.detailObjects = self.detailObjects + upperObjects + lowerObjects + listCheck(midObjects)
			self.detailControl = self.detailControl + ribbon.detailControl
			self.detailGroup = self.detailGroup + ribbon.detailGroup

			self.ribbonControl = ribbon.mainControl
			self.ribbonGroup = ribbon.mainGroup

			if self.master:
				attrName = ['sns', 'snsAdd']
				cmds.addAttr(self.master, ln=attrName[0], min=0, max=1, dv=0, k=True)
				cmds.addAttr(self.master, ln=attrName[1], k=True)

				for attr in attrName:
					cmds.connectAttr('{}.{}'.format(self.master, attr),
					                 '{}.{}'.format(ribbon.upperFlexiPlane.parent, attr))
					cmds.connectAttr('{}.{}'.format(self.master, attr),
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

		if self.master:
			attrName = ['sns', 'snsAdd']
			cmds.addAttr(self.master, ln=attrName[0], min=0, max=1, dv=0, k=True)
			cmds.addAttr(self.master, ln=attrName[1], k=True)

			for attr in attrName:
				cmds.connectAttr('{}.{}'.format(self.master, attr),
				                 '{}.{}'.format(chain.upperTwist.parent, attr))

		return

	####################################################################################################################
	# Master
	####################################################################################################################

	def createMaster(self, child=None, wireType=None):
		kind = Component.master
		name = longName(self.longName, kind)

		axis = [0, 0, 0]

		if self.side.lower() == Position.left:
			axis = [1, -1, 0]
		elif self.side.lower() == Position.right:
			axis = [1, 1, 0]

		ctl = RIGCONTROL(name=longName(self.name,
		                               self.side.upper()[0],
		                               self.index,
		                               Component.attr,
		                               Component.control,
		                               ),
		                 child=child,
		                 scale=self.scale * 2.0,
		                 side=self.side,
		                 label='None',
		                 axis=axis,
		                 )

		self.master = ctl.transform
		self.masterGroup = ctl.group
		cmds.parent(self.masterGroup, child)
		lockKeyableAttributes(self.master, hide=True)
		return

	def createNetwork(self, typ):
		name = longName(self.name,
		                self.side.upper()[0],
		                self.index,
		                Component.network,
		                )

		self.network = cmds.createNode('network', n=name)
		self.addDefaultNetworkAttributes(typ)

		if self.masterParent:
			self.connectItemToNetworkRoot()

		if self.master:
			self.multiConnectToNetwork(self.network, self.master, longName(self.name, self.side[0]))
			# self.connectToNetwork(self.network, self.master, typ)
			for attr in ['jointDisplay', 'controlDisplay']:
				cmds.connectAttr('{}.{}'.format(self.master, attr), '{}.{}'.format(self.network, attr))
		return

	def createFKIKConnections(self, ctl, name=Component.fkik):
		# Constraints
		fkik = createFKIK(items=self.items,
		                  fkControls=self.fkControl,
		                  ikControls=self.ikJoint,
		                  parent=ctl,
		                  attrName=name,
		                  )

		# Visibility
		for grp in self.fkGroup:
			i = self.fkGroup.index(grp)
			cmds.setAttr('{}.v'.format(grp), lock=False)
			cmds.connectAttr('{}.outputX'.format(fkik[1][i]), '{}.v'.format(grp), f=True)

		for grp in self.ikGroup:
			cmds.setAttr('{}.v'.format(grp), lock=False)
			cmds.connectAttr('{}.{}'.format(self.master, name), '{}.v'.format(grp), f=True)

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

	####################################################################################################################
	# Relationships
	####################################################################################################################

	def addDefaultNetworkAttributes(self, typ):
		node = self.network
		cmds.addAttr(node, ln='type', dt='string')
		addSideAttr(node)
		cmds.addAttr(node, ln='index', at='long')
		cmds.setAttr('{}.type'.format(node), typ, type='string', lock=True)
		cmds.setAttr('{}.index'.format(node), self.index)
		setEnumByString(node, 'side', self.side)
		cmds.addAttr(node, ln='children', dt='string')
		addBoolAttr(node, 'jointDisplay')
		addBoolAttr(node, 'controlDisplay')
		return

	def createSet(self, objects):
		name = longName(self.name,
		                self.side.upper()[0],
		                self.index,
		                Component.set,
		                )

		cmds.select(d=True)
		objects = listCheck(objects)
		self.set = cmds.sets(objects, name=name)

		if self.master:
			rootSet = self.getConnected(self.master, Component.set)

			if cmds.objExists(str(rootSet)):
				cmds.sets(self.set, add=rootSet)
		return

	def hideObjectsAttributes(self, objects):
		objects = listCheck(objects)
		for obj in objects:
			hideAttributes(obj)
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

				addIndexAttribute(obj, i)
				networkAttr = '{}.{}[{}]'.format(network, name, i)
		else:
			cmds.addAttr(network, ln=name, at='message')

		cmds.connectAttr(networkAttr, objAttr, force=True)
		return

	def connectItemToNetworkRoot(self, item, networkRoot):
		attrName = 'rigNetworkRoot'
		if not cmds.attributeQuery(attrName, node=item, ex=True):
			cmds.addAttr(item, ln=attrName, at='message')
		if not self.getConnected(item, attrName):
			cmds.connectAttr('{}.children'.format(networkRoot), '{}.{}'.format(item, attrName), f=True)
		return

	def multiConnectToNetwork(self, objects, network, name):
		objects = listCheck(objects)
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
			if self.master:
				self.connectItemToNetworkRoot(obj, self.master)

			if not cmds.attributeQuery(attrName, node=obj, ex=True):
				cmds.addAttr(obj, ln=attrName, at='message')

			cmds.connectAttr('{}.{}[{}]'.format(network, name, i), '{}.{}'.format(obj, attrName), f=True)
			addIndexAttribute(obj, i)
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

		if self.master:
			cogNetwork = self.getConnected(self.master, 'cog_C')
			cog = self.getConnected(cogNetwork, 'fkControl', 0) if cogNetwork else None

			if cog:
				localWorldConstraint(obj=obj,
				                     local=local,
				                     world=cog,
				                     n=attrName,
				                     )
		return

	def parentToRootControl(self, obj):
		if self.master:
			offset = self.getConnected(self.master, 'fkControl', indexValue=1)

			if offset:
				cmds.parent(obj, offset)
		return

	def createNetworkConnections(self):
		# Parent
		if self.parent:
			self.connectToNetwork(self.parent, self.network, 'parentGroup')

		# Attr Control
		if self.master:
			self.connectToNetwork(self.master, self.network, 'attrControl')

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
		if self.items:
			self.multiConnectToNetwork(self.items, self.network, 'skeleton')
			con = cmds.createNode('condition', name='{}_jointDisplay_condition'.format(self.network))
			cmds.setAttr('{}.colorIfTrueR'.format(con), 2)
			cmds.setAttr('{}.colorIfFalseR'.format(con), 0)
			cmds.connectAttr('{}.jointDisplay'.format(self.network), '{}.firstTerm'.format(con))
			for obj in self.items:
				cmds.connectAttr('{}.outColorR'.format(con), '{}.drawStyle'.format(obj))

			if self.detailObjects:
				self.multiConnectToNetwork(self.detailObjects, self.network, 'skeletonDetail')
				for detail in self.detailObjects:
					cmds.connectAttr('{}.outColorR'.format(con), '{}.drawStyle'.format(detail))

		# Detail Controls
		if self.detailControl:
			attrName = 'detailControlDisplay'
			self.multiConnectToNetwork(self.detailControl, self.network, 'detailControl')
			addBoolAttr(self.network, attrName)

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

		if self.master:
			# Attr Display
			attrName = Component.detailControlDisplay

			if not cmds.attributeQuery(attrName, node=self.master, ex=True):
				addBoolAttr(self.master, attrName)
			cmds.connectAttr('{}.{}'.format(self.master, attrName), '{}.{}'.format(self.network, attrName))

		# Attr To Network FKIK
		# cmds.addAttr(self.network, ln=Component.fkik, min=0, max=1, dv=0)
		# cmds.connectAttr('{}.{}'.format(self.attrControl, Component.fkik),
		#                  '{}.{}'.format(self.network, Component.fkik))
		return

	def createAttrControlConnections(self):
		if self.master:
			cmds.addAttr(self.network, ln=Component.fkik, min=0, max=1, dv=0)
			cmds.connectAttr('{}.{}'.format(self.master, Component.fkik),
			                 '{}.{}'.format(self.network, Component.fkik))
		return
