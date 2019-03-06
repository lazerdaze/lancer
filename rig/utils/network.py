# Lancer Modules
from general import *
from attribute import *
from naming import *

# Maya Modules
from maya import cmds


def createRelationship(source,
					   sourceAttr,
					   destination,
					   destinationAttr,
					   kind=MayaAttrType.message,
					   array=False,
					   *args,
					   **kwargs
					   ):
	sourceName = attributeName(source, sourceAttr)
	destinationName = attributeName(destination, destinationAttr)

	# Source
	if not attributeExist(source, sourceAttr):
		addAttribute(node=source, attribute=sourceAttr, kind=kind, array=array)
	else:
		array = attributeArray(source, sourceAttr)

	# Next Available
	if array:
		index = int(cmds.listAttr(sourceName, m=True)[-1].split('[')[-1].split(']')[0])
		sourceName = '{}.{}[{}]'.format(source, sourceAttr, index)

	# Destination
	if not attributeExist(destination, destinationAttr):
		addAttribute(node=destination, attribute=destinationAttr, kind=MayaAttrType.message)

	# Connection
	cmds.connectAttr(sourceName, destinationName, force=True)

	if kind == MayaAttrType.message:
		cmds.connectAttr(destinationName, sourceName, force=True)

	return


def createMonoRelationship(source, destination, sourceAttr=None, destinationAttr=None):
	if sourceAttr and destinationAttr:
		pass
	else:
		if '.' in source:
			sourceResult = source.split('.')
			source = sourceResult[0]
			sourceAttr = sourceResult[1]
		else:
			sourceAttr = 'child'

		if '.' in destination:
			destinationResult = destination.split('.')
			destination = destinationResult[0]
			destinationAttr = destinationResult[1]
		else:
			destinationAttr = 'parent'

	# Create Source Attribute
	if not attributeExist(source, sourceAttr):
		addAttribute(node=source, attribute=sourceAttr, kind=MayaAttrType.message)

	# Create Destination Attribute
	if not attributeExist(destination, destinationAttr):
		addAttribute(node=destination, attribute=destinationAttr, kind=MayaAttrType.message)

	# Make Connection
	cmds.connectAttr(attributeName(source, sourceAttr),
					 attributeName(destination, destinationAttr),
					 force=True
					 )
	cmds.connectAttr(attributeName(destination, destinationAttr),
					 attributeName(source, sourceAttr),
					 force=True
					 )
	return


def createPolyRelationship(*args, **kwargs):
	source = kwargs.get('source', None)
	sourceAttr = kwargs.get('sourceAttr', None)
	destinationAttr = kwargs.get('destinationAttr', False)

	for arg in args:
		if isinstance(arg, (list, tuple, dict)):
			pass

	return


def network(n='network', typ='', *args):
	node = cmds.createNode('network', n=n)
	cmds.addAttr(node, ln='networkType', dt='string')
	cmds.setAttr('{}.networkType'.format(node), typ, type='string', lock=True)
	cmds.addAttr(node, ln='children', dt='string')
	cmds.addAttr(node, ln='set', at='message')

	if typ != Component.fkik:
		cmds.addAttr(node, ln='fkikNetwork', at='message')

	if typ != Component.root:
		cmds.addAttr(node, ln='index', dv=0, at='long')
		cmds.addAttr(node, ln='side', dt='string')
		cmds.addAttr(node, ln='characterNetwork', at='message')
		cmds.addAttr(node, ln='parentNetwork', at='message')

	if typ in [Component.arm, Component.leg]:
		# cmds.addAttr(node, ln='index', dv=0, at='long')
		# cmds.addAttr(node, ln='side', dt='string')
		# cmds.addAttr(node, ln='side', at='enum', en='none:center:left:right')
		cmds.addAttr(node, ln='opposite', at='message')

	if typ == Component.character:
		cmds.addAttr(node, ln='characterName', dt='string')
		cmds.addAttr(node, ln='globalScale', dv=1)
		cmds.addAttr(node, ln='cog', at='message')
		cmds.addAttr(node, ln='hip', at='message')
		cmds.addAttr(node, ln='spine', at='message')
		cmds.addAttr(node, ln='head', at='message')
	# cmds.addAttr(node, ln='arm', dt='string', m=True)
	# cmds.addAttr(node, ln='leg', dt='string', m=True)
	# cmds.addAttr(node, ln='control', dt='string', m=True)
	# cmds.addAttr(node, ln='bindJoint', dt='string', m=True)

	elif typ == Component.cog:
		# cmds.addAttr(node, ln='control', dt='string', m=True)
		# cmds.addAttr(node, ln='bindJoint', dt='string', m=True)
		pass
	elif typ == Component.spine:
		cmds.addAttr(node, ln='neckHead', at='message')
		cmds.addAttr(node, ln='tail', at='message')
	elif typ == Component.collar:
		pass
	# cmds.addAttr(node, ln='side', dt='string')

	elif typ == Component.arm:
		cmds.addAttr(node, ln='collar', at='message')
		cmds.addAttr(node, ln='hand', at='message')
	elif typ == Component.hand:
		pass
	# cmds.addAttr(node, ln='side', dt='string')
	# cmds.addAttr(node, ln='finger', dt='string', m=True)
	elif typ == Component.foot:
		pass
	# cmds.addAttr(node, ln='side', dt='string')
	# cmds.addAttr(node, ln='FKIK', min=0, max=1, dv=0)
	elif typ == Component.leg:
		cmds.addAttr(node, ln='hip', at='message')
		cmds.addAttr(node, ln='foot', at='message')

	elif typ == Component.fkik:
		cmds.addAttr(node, ln='FKIK', dv=0, min=0, max=1)
		cmds.addAttr(node, ln='ikHandle', at='message')
		cmds.addAttr(node, ln='ikPoleVector', at='message')
		cmds.addAttr(node, ln='fkPoleVector', at='message')
	# cmds.addAttr(node, ln='bindJoint', dt='string', m=True)
	# cmds.addAttr(node, ln='fkControl', dt='string', m=True)
	# cmds.addAttr(node, ln='fkJoint', dt='string', m=True)
	# cmds.addAttr(node, ln='ikControl', dt='string', m=True)
	# cmds.addAttr(node, ln='ikJoint', dt='string', m=True)

	return node


def connectToNetwork(obj, network, ln, *args):
	objAttr = '{}.parentNetwork'.format(obj)
	networkAttr = '{}.{}'.format(network, ln)

	if not cmds.attributeQuery('parentNetwork', node=obj, ex=True):
		cmds.addAttr(obj, ln='parentNetwork', at='message')

	if cmds.attributeQuery(ln, node=network, ex=True):
		if cmds.attributeQuery(ln, node=network, m=True):
			mList = cmds.listAttr('{}.{}'.format(network, ln), m=True)
			if mList:
				i = mList.index(mList[-1]) + 1
			else:
				i = 0

			addIndexValue(obj, i)

			networkAttr = '{}.{}[{}]'.format(network, ln, i)
	else:
		cmds.addAttr(network, ln=ln, at='message')

	cmds.connectAttr(networkAttr, objAttr, force=True)

	connectToRoot(obj)

	return [objAttr, networkAttr]


def multiConnectToNetwork(objects, network, ln, *args):
	if not cmds.attributeQuery(ln, node=network, ex=True):
		cmds.addAttr(network, ln=ln, dt='string', m=True)
		i = 0
	else:
		if cmds.listAttr('{}.{}'.format(network, ln), m=True):
			i = int(cmds.listAttr('{}.{}'.format(network, ln), m=True)[-1].split('[')[-1].split(']')[0])
		else:
			i = 0

	objects = listCheck(objects)

	for x in objects:
		connectToRoot(x)

		if not cmds.attributeQuery('parentNetwork', node=x, ex=True):
			cmds.addAttr(x, ln='parentNetwork', at='message')

		cmds.connectAttr('{}.{}[{}]'.format(network, ln, i), '{}.parentNetwork'.format(x), f=True)
		addIndexValue(x, i)
		i += 1

	return


def connectToRoot(obj, *args):
	root = queryNetwork().network

	if root:
		if not cmds.attributeQuery('characterNetwork', node=obj, ex=True):
			cmds.addAttr(obj, ln='characterNetwork', at='message')
		if not getConnectedNode(obj, 'characterNetwork'):
			cmds.connectAttr('{}.children'.format(root), '{}.characterNetwork'.format(obj), f=True)
	return


def findRootNetwork(*args):
	global rootNetwork

	networks = cmds.ls(type='network')
	root = None

	if networks:
		for x in networks:
			if cmds.attributeQuery('networkType', node=x, ex=True):
				if cmds.getAttr('{}.networkType'.format(x)) == rootNetwork:
					root = x

	return root


class queryNetwork():
	def __init__(self, selected=None, typ='character', *args):

		self.characterName = None
		self.typ = typ
		self.network = None
		self.cog = None
		self.spine = None
		self.leg = None
		self.arm = None
		self.fkik = None
		self.hip = None
		self.set = None

		selected = listCheck(selected)

		if selected:
			self.getNetworkFromSelected(selected)

		else:
			if typ == Component.character:
				self.getRoot()
			else:
				self.network = self.findNetwork(typ)

	def findNetwork(self, typ):
		networks = self.findAllNetworksByType(typ)
		node = None

		if networks:
			if len(networks) > 1:
				node = cmds.layoutDialog(t='{} Network'.format(typ.capitalize()), ui=self.networkPromptUI)
			else:
				node = networks[0]

		return node

	def findAllNetworksByType(self, typ):
		networks = cmds.ls(type='network')
		networksList = []

		if networks:
			for net in networks:
				if cmds.attributeQuery('networkType', node=net, ex=True):
					if cmds.getAttr('{}.networkType'.format(net)) == typ:
						networksList.append(net)

		return networksList

	def getRoot(self):

		# Get Root

		root = self.findNetwork(Component.character)
		self.network = root

		# Get CharacterName
		if root:
			self.characterName = cmds.getAttr('{}.characterName'.format(root))

		# Get COG

		if root:
			self.cog = self.getConnected(root, Component.cog)

		# Get HIP

		if root:
			self.hip = self.getConnected(root, Component.hip)

		# Get Spine
		if root:
			self.spine = self.getConnected(root, Component.spine)

		# Get Arm
		if root:
			self.arm = self.getConnected(root, Component.arm)

		# Get Leg
		if root:
			self.leg = self.getConnected(root, Component.leg)

		# Get FKIK
		if root:
			self.fkik = self.getConnected(root, Component.fkik)

		# Get Set
		if root:
			self.set = self.getConnected(root, Component.set)

	def networkPromptUI(self, *args):
		networks = self.findAllNetworksByType(self.typ)

		cmds.columnLayout(adj=True)
		textVar = cmds.textScrollList(append=networks)
		cmds.button(l='Select',
					c=lambda x: cmds.layoutDialog(dismiss=str(cmds.textScrollList(textVar, q=True, si=True)[0])))
		cmds.setParent('..')

	def getConnected(self, obj, attr, *args):
		name = '{}.{}'.format(obj, attr)
		if cmds.attributeQuery(attr, node=obj, ex=True):

			if cmds.connectionInfo(name, id=True):
				query = cmds.listConnections(cmds.connectionInfo(name, ged=True))[0]
				return query
			else:
				query = cmds.listConnections(name)
				if query:
					query = query[0]
					return query

				else:
					return None
		else:
			return None

	def getNetworkFromSelected(self, selected=[], *args):
		network = []
		parent = []

		if selected:
			if len(selected) != 1:
				for obj in selected:
					networkQ = self.getConnected(obj, 'characterNetwork')
					parentQ = self.getConnected(obj, 'parentNetwork')
					if networkQ:
						if networkQ not in network:
							network.append(networkQ)
					if parentQ:
						if parentQ not in parent:
							parent.append(parentQ)
			else:
				network = self.getConnected(selected[0], 'characterNetwork')
				parent = self.getConnected(selected[0], 'parentNetwork')

		self.network = network
		self.parent = parent
