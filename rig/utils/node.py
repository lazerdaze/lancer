# Lancer Modules
from attribute import *
from general import *
from naming import *

# Maya Modules
from maya import cmds


def nodeExists(node):
	return cmds.objExists(node)


def nodeParent(node):
	parent = cmds.listRelatives(node, parent=True)
	return parent[0] if parent else None


def nodeShapes(node):
	return cmds.listRelatives(node, shapes=True)


def nodeType(node):
	shapes = nodeShapes(node)
	return cmds.nodeType(shapes[0]) if shapes else cmds.nodeType(node)


def nodeChildren(node):
	children = cmds.listRelatives(node, type='transform')
	return [str(child) for child in children] if children else None


def nodeLocalPosition(node):
	return


def nodeLocalRotation(node):
	return


def nodeWorldPosition(node):
	return


def nodeWorldRotation(node):
	return


def createNode(name, kind=MayaNodeType.null):
	return cmds.createNode(kind, name=name, skipSelect=True)


def createNull(*args, **kwargs):
	nulls = []

	kwargs['node'] = kwargs.get('node', None)
	node = kwargs['node']

	for arg in args:
		index = args.index(arg)
		null = cmds.group(name=arg, empty=True)

		if index > 0:
			cmds.parent(null, args[index - 1])

		nulls.append(null)

	if len(nulls) > 0 and node:
		snap(node, nulls[0], t=True, r=True)
		parent = nodeParent(node)

		if parent:
			cmds.parent(nulls[0], parent)

		cmds.parent(node, nulls[-1])
	return nulls


########################################################################################################################
#
#
#	Node Class
#
#
########################################################################################################################

class Node(object):
	def __init__(self,
	             name,
	             prefix=None,
	             parent=None,
	             kind=None,
	             children=None,
	             exists=False,
	             sector=None,
	             index=0,
	             side=None,
	             color=None,
	             ):

		self.name = longName(prefix,
		                     side[0].upper() if side else None,
		                     name,
		                     sector[0].upper() if sector else None,
		                     index,
		                     kind
		                     )
		self.prefix = prefix
		self.kind = kind
		self.parent = parent
		self.children = children if isinstance(children, list) else []
		self.exists = exists
		self.color = color
		self.index = index
		self.sector = sector
		self.side = side

		# Nodes
		self.transform = None
		self.shape = None

		# Maya Attributes

		self.translateX = 0
		self.translateY = 0
		self.translateZ = 0
		self.rotateX = 0
		self.rotateY = 0
		self.rotateZ = 0
		self.scaleX = 0
		self.scaleY = 0
		self.scaleZ = 0
		self.visibility = 1

		# Init
		self.populateAttributes()

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = cmds.rename(self.name, name)
		return

	def addKind(self, kind):
		if self.isValid():
			addAttribute(node=self.name,
			             attribute=UserAttr.kind,
			             kind=MayaAttrType.string,
			             value=kind,
			             keyable=False,
			             channelBox=False,
			             lock=True,
			             )
		else:
			raise RuntimeError('Add Kind: Node "{}" is not a valid object.'.format(self.name))
		return

	def getKind(self):
		return self.kind

	def setKind(self, kind):
		self.kind = kind
		return

	def getParent(self):
		return self.parent

	def setParent(self, parent):
		self.parent = parent
		return

	def getChildren(self):
		return self.children

	def setChildren(self, children):
		self.children = children
		return

	def appendChild(self, child):
		self.children.append(child)
		return

	def removeChild(self, child):
		if child in self.children:
			self.children.remove(child)
		return

	def setExists(self, exists):
		self.exists = exists
		return

	def getExists(self):
		return self.exists

	def addIndex(self, index):
		if self.isValid():
			addAttribute(node=self.name,
			             attribute=UserAttr.index,
			             kind=MayaAttrType.int,
			             value=index,
			             keyable=False,
			             channelBox=False,
			             lock=True,
			             )
		else:
			raise RuntimeError('Add Index: Node "{}" is not a valid object.'.format(self.name))
		return

	def getIndex(self):
		return self.index

	def setIndex(self, index):
		self.index = index
		return

	def move(self, *args, **kwargs):
		if self.isValid():
			worldSpace = kwargs.get('worldSpace', False)
			x = kwargs.get('x', None)
			y = kwargs.get('y', None)
			z = kwargs.get('z', None)

			if isinstance(args, list) or len(args) == 3:
				cmds.xform(self.name, translation=args, worldSpace=worldSpace)
			else:
				if x is not None:
					cmds.move(x, self.name, x=True, worldSpace=worldSpace)

				if y is not None:
					cmds.move(y, self.name, y=True, worldSpace=worldSpace)

				if z is not None:
					cmds.move(z, self.name, z=True, worldSpace=worldSpace)
			self.populateAttributes()
		return

	def rotate(self, *args, **kwargs):
		if self.isValid():
			worldSpace = kwargs.get('worldSpace', False)
			x = kwargs.get('x', None)
			y = kwargs.get('y', None)
			z = kwargs.get('z', None)

			if isinstance(args, list) or len(args) == 3:
				cmds.xform(self.name, rotatePivot=args, worldSpace=worldSpace)
			else:
				if x:
					cmds.rotate(x, self.name, x=True, worldSpace=worldSpace)
				if y:
					cmds.rotate(y, self.name, y=True, worldSpace=worldSpace)
				if z:
					cmds.rotate(z, self.name, z=True, worldSpace=worldSpace)
			self.populateAttributes()
		return

	def snapTo(self, node, translation=True, rotation=True):
		snap(node, self.name, t=translation, r=rotation)
		self.populateAttributes()
		return

	def isValid(self):
		if self.name:
			self.exists = nodeExists(self.name)
			return self.exists
		self.exists = False
		return self.exists

	def isAttributeLocked(self, attribute):
		return attributeLocked(self.name, attribute)

	def getAttribute(self, attribute):
		return getattr(self, attribute)

	def setAttribute(self, attribute, value):
		if self.isValid():
			if isinstance(attribute, str):
				if hasattr(self, attribute):
					if self.isAttributeLocked(attribute):
						raise AttributeError('Attribute "{}" is locked.'.format(attribute))
					else:
						if getattr(self, attribute) != value:
							setattr(self, attribute, value)
						setAttribute(self.name, attribute, value)
				else:
					raise AttributeError('Attribute "{}" does not exist.'.format(attribute))
				return
			else:
				raise TypeError('Attribute must be str.')

	def populateAttributes(self):
		exceptions = ['message', 'TdataCompound']

		if self.isValid():
			for attribute in listAllAttributes(self.name):
				if hasattr(self, attribute):
					name = attributeName(self.name, attribute)

					try:
						kind = str(cmds.getAttr(name, type=True))
						value = cmds.getAttr(name) if kind not in exceptions else None
						setattr(self, attribute, value)

					except ValueError:
						pass
		return

	def populateFromScene(self):
		if self.isValid():
			# self.parent = utils.nodeParent(self.name)
			self.kind = nodeType(self.name)

			children = nodeChildren(self.name)

			if children:
				for child in children:
					childNode = Node(parent=self, name=child)
					childNode.populateFromScene()
					self.appendChild(childNode)
		return

