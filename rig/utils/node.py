# Lancer Modules
from attribute import *
from general import *
from naming import *
from customError import *

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
	child = kwargs.get('child', None)
	nulls = []

	for arg in args:
		index = args.index(arg)
		null = cmds.group(name=arg, empty=True)

		if index > 0:
			cmds.parent(null, args[index - 1])

		nulls.append(null)

	if len(nulls) > 0 and child:
		snap(child, nulls[0], t=True, r=True)
		parent = nodeParent(child)

		if parent:
			cmds.parent(nulls[0], parent)

		cmds.parent(child, nulls[-1])
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
	             name='rigNode',
	             prefix=None,
	             parent=None,
	             children=None,
	             color=None,
	             side=None,
	             index=None,
	             sector=None,
	             kind=Component.transform,
	             ):

		'''
		Base Node class to be sub-classed in all Component classes.

		:param str name:            Name of Node.
		:param str prefix:          Prefix name of the control
		:param object parent:       Parent of Node.
		:param list children:       Direct descendants of Node.
		:param list color:          RGB Color.
		:param str side:            Side of the controls origin.
		:param int index:           Used to determined rig priority.
		:param str sector:          Sector of control. Possible Sectors: "A", "B", "C"
		:param str kind:            Label of the control to determine rig type.
		'''

		self._name = name
		self._prefix = prefix
		self._parent = parent
		self._children = children if isinstance(children, list) else []
		self._descendants = []
		self.exists = False
		self.canUpdateName = False
		self.color = color

		# Nodes
		self.transform = None
		self.shape = None

		# Custom Maya Attributes
		self._side = side
		self._sector = sector
		self._index = index
		self._kind = kind

		if nodeExists(name):
			self._kind = None
			self.longName = name

	def __str__(self):
		return self.longName

	def __repr__(self):
		return self.longName

	def create(self, *args, **kwargs):
		if not self.isValid():
			self.transform = cmds.group(name=self.longName, empty=True)
			if self._side:
				self.side = self._side
			if self._index:
				self.index = self._index
			if self._sector:
				self.sector = self._sector
			if self._kind:
				self.kind = self._kind
		else:
			raise NodeExistsError('Node "{}" already exists.'.format(self.longName))

	####################################################################################################################
	# Name Properties
	####################################################################################################################
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name
		self.updateName()
		return

	@property
	def prefix(self):
		return self._prefix

	@prefix.setter
	def prefix(self, prefix):
		self._prefix = prefix
		self.updateName()
		return

	@property
	def longName(self):
		return longName(self._prefix,
		                self._side[0].upper() if self.side else None,
		                self._name,
		                self._sector,
		                self._index,
		                self._kind,
		                )

	@longName.setter
	def longName(self, name):
		if self.isValid():
			nc = NameConvention(name)
			self._prefix = nc.prefix
			self._name = nc.name
			self._side = nc.side
			self._sector = nc.sector
			self._index = nc.index
			self._kind = nc.kind
		return

	####################################################################################################################
	# Translate Properties
	####################################################################################################################
	@property
	def translate(self):
		if self.isValid():
			return [self.translateX, self.translateY, self.translateZ]
		else:
			return [0.0, 0.0, 0.0]

	@translate.setter
	def translate(self, *args):
		if self.isValid():
			if len(args) == 1:
				if isinstance(args[0], (list, dict, tuple)) and len(args[0]) == 3:
					self.translateX = args[0][0]
					self.translateY = args[0][1]
					self.translateZ = args[0][2]

				else:
					raise ValueError('Must provide "XYZ" values in a list, dict, or tuple.')
			elif len(args) == 3:
				self.translateX = args[0]
				self.translateY = args[1]
				self.translateZ = args[2]
			else:
				raise ValueError('Must provide 3 values for "XYZ".')
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def translateX(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.translateX))
		else:
			return 0.0

	@translateX.setter
	def translateX(self, value):
		if self.isValid():
			setAttribute(self.longName, attribute=MayaAttr.translateX, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def translateY(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.translateY))
		else:
			return 0

	@translateY.setter
	def translateY(self, value):
		if self.isValid():
			setAttribute(self.longName, attribute=MayaAttr.translateY, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def translateZ(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.translateZ))
		else:
			return 0.0

	@translateZ.setter
	def translateZ(self, value):
		if self.isValid():
			setAttribute(self.longName, attribute=MayaAttr.translateZ, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	####################################################################################################################
	# Rotate Properties
	####################################################################################################################
	@property
	def rotate(self):
		if self.isValid():
			return [self.rotateX, self.rotateY, self.rotateZ]
		else:
			return [0.0, 0.0, 0.0]

	@rotate.setter
	def rotate(self, *args):
		if self.isValid():
			if len(args) == 1:
				if isinstance(args[0], (list, dict, tuple)) and len(args[0]) == 3:
					self.rotateX = args[0][0]
					self.rotateY = args[0][1]
					self.rotateZ = args[0][2]
				else:
					raise ValueError('Must provide "XYZ" values in a list, dict, or tuple.')
			elif len(args) == 3:
				self.rotateX = args[0]
				self.rotateY = args[1]
				self.rotateZ = args[2]
			else:
				raise ValueError('Must provide 3 values for "XYZ".')
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def rotateX(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.rotateX))
		else:
			return 0.0

	@rotateX.setter
	def rotateX(self, value):
		if self.isValid():
			setAttribute(self.longName, attribute=MayaAttr.rotateX, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def rotateY(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.rotateY))
		else:
			return 0.0

	@rotateY.setter
	def rotateY(self, value):
		if self.isValid():
			setAttribute(self.longName, attribute=MayaAttr.rotateY, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def rotateZ(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.rotateZ))
		else:
			return 0.0

	@rotateZ.setter
	def rotateZ(self, value):
		if self.isValid():
			setAttribute(self.longName, attribute=MayaAttr.rotateZ, value=value)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	####################################################################################################################
	# Scale Properties
	####################################################################################################################
	@property
	def scale(self):
		if self.isValid():
			return [self.scaleX, self.scaleY, self.scaleZ]
		else:
			return [1.0, 1.0, 1.0]

	@scale.setter
	def scale(self, *args):
		if self.isValid():
			if len(args) == 1:
				if isinstance(args[0], (list, dict, tuple)) and len(args[0]) == 3:
					self.scaleX = args[0][0]
					self.scaleY = args[0][1]
					self.scaleZ = args[0][2]
				elif isinstance(args[0], (int, float)):
					self.scaleX = args[0]
					self.scaleY = args[0]
					self.scaleZ = args[0]
				else:
					raise ValueError('Must provide "XYZ" values in a list, dict, or tuple.')
			elif len(args) == 3:
				self.scaleX = args[0]
				self.scaleY = args[1]
				self.scaleZ = args[2]
			else:
				raise ValueError('Must provide 3 values for "XYZ".')
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def scaleX(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.scaleX))
		else:
			return 1.0

	@scaleX.setter
	def scaleX(self, value):
		if self.isValid():
			setAttribute(self.longName, attribute=MayaAttr.scaleX, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def scaleY(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.scaleY))
		else:
			return 1.0

	@scaleY.setter
	def scaleY(self, value):
		if self.isValid():
			setAttribute(self.longName, attribute=MayaAttr.scaleY, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def scaleZ(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.scaleZ))
		else:
			return 1.0

	@scaleZ.setter
	def scaleZ(self, value):
		if self.isValid():
			setAttribute(self.longName, attribute=MayaAttr.scaleZ, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	####################################################################################################################
	# Visibility Properties
	####################################################################################################################
	@property
	def visibility(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.visibility))
		else:
			return 1.0

	@visibility.setter
	def visibility(self, value):
		if self.isValid():
			setAttribute(self.longName, attribute=MayaAttr.visibility, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	####################################################################################################################
	# Custom Properties
	####################################################################################################################
	def updateName(self):
		if self.transform:
			self.transform = cmds.rename(self.transform, self.longName)
		return

	@property
	def side(self):
		return self._side

	@side.setter
	def side(self, side):
		sideList = ['Center', 'Left', 'Right', 'None']

		if self.isValid():
			if not attributeExist(self.longName, MayaAttr.side):
				addAttribute(node=self.longName,
				             attribute=MayaAttr.side,
				             kind=MayaAttrType.enum,
				             value=sideList,
				             keyable=False,
				             channelBox=False,
				             )

			if side is None:
				value = JointLabelSide.none
				self._side = None

			elif isinstance(side, str):
				if hasattr(JointLabelSide, side):
					value = getattr(JointLabelSide, side)
					self._side = side
				else:
					raise ValueError('Side "{}" is not valid.'.format(side))

			elif isinstance(side, (int, float)):
				value = side
				self._side = sideList[int(side)]
			else:
				raise ValueError('Invalid side type provided: {}'.format(type(side)))

			if self.canUpdateName:
				self.updateName()
			setAttribute(self.longName, attribute=MayaAttr.side, value=value)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def sector(self):
		return self._sector

	@sector.setter
	def sector(self, sector):
		if self.isValid():
			if sector is None:
				return
			elif isinstance(sector, str):
				value = sector
			else:
				value = str(sector)

			if not attributeExist(self.longName, UserAttr.sector):
				addAttribute(node=self.longName,
				             attribute=UserAttr.sector,
				             kind=MayaAttrType.string,
				             value=value,
				             keyable=False,
				             channelBox=False,
				             lock=True,
				             )
			else:
				setAttribute(self.longName, attribute=UserAttr.sector, value=value, force=True)

			self._sector = sector
			if self.canUpdateName:
				self.updateName()
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def index(self):
		return self._index

	@index.setter
	def index(self, index):
		if self.isValid():
			if index is None:
				return
			elif not isinstance(index, (int, float)):
				raise ValueError('Index must be a numeric value.'.format(index))
			else:
				value = int(index)
				if not attributeExist(self.longName, UserAttr.index):
					addAttribute(node=self.longName,
					             attribute=UserAttr.index,
					             kind=MayaAttrType.int,
					             value=value,
					             minValue=0,
					             keyable=False,
					             channelBox=False,
					             lock=True,
					             )

				else:
					setAttribute(self.longName, attribute=UserAttr.index, value=value, force=True)

				self._index = int(index)
				if self.canUpdateName:
					self.updateName()
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def kind(self):
		return self._kind

	@kind.setter
	def kind(self, kind):
		if self.isValid():
			if kind is None:
				value = ''
			elif isinstance(kind, str):
				value = kind
			else:
				value = str(kind)

			if not attributeExist(self.longName, UserAttr.kind):
				addAttribute(node=self.longName,
				             attribute=UserAttr.kind,
				             kind=MayaAttrType.string,
				             value=value,
				             keyable=False,
				             channelBox=False,
				             lock=True,
				             )
			else:
				setAttribute(self.longName, attribute=UserAttr.kind, value=value, force=True)

			self._kind = kind
			if self.canUpdateName:
				self.updateName()
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return


	####################################################################################################################
	# Children Methods
	####################################################################################################################
	def append(self, child):
		self._children.append(child)
		return

	def remove(self, child):
		if child in self._children:
			self._children.remove(child)
		return

	####################################################################################################################
	# Methods
	####################################################################################################################
	def move(self, *args, **kwargs):
		if self.isValid():
			worldSpace = kwargs.get('worldSpace', False)
			x = kwargs.get('x', None)
			y = kwargs.get('y', None)
			z = kwargs.get('z', None)

			if isinstance(args[0], list) or len(args[0]) == 3:
				cmds.xform(self.longName, translation=args[0], worldSpace=worldSpace)
			else:
				if x is not None:
					cmds.move(x, self.longName, x=True, worldSpace=worldSpace)

				if y is not None:
					cmds.move(y, self.longName, y=True, worldSpace=worldSpace)

				if z is not None:
					cmds.move(z, self.longName, z=True, worldSpace=worldSpace)
		return

	def rotation(self, *args, **kwargs):
		if self.isValid():
			worldSpace = kwargs.get('worldSpace', False)
			x = kwargs.get('x', None)
			y = kwargs.get('y', None)
			z = kwargs.get('z', None)

			if isinstance(args[0], list) or len(args[0]) == 3:
				cmds.xform(self.longName, rotatePivot=args[0], worldSpace=worldSpace)
			else:
				if x:
					cmds.rotate(x, self.longName, x=True, worldSpace=worldSpace)
				if y:
					cmds.rotate(y, self.longName, y=True, worldSpace=worldSpace)
				if z:
					cmds.rotate(z, self.longName, z=True, worldSpace=worldSpace)
		return

	def snapTo(self, node, translation=True, rotation=True):
		snap(node, self.longName, t=translation, r=rotation)
		return

	def isValid(self):
		if self.longName:
			self.exists = nodeExists(self.longName)
			return self.exists
		self.exists = False
		return self.exists

	def isAttributeLocked(self, attribute):
		return attributeLocked(self.longName, attribute)

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
						setAttribute(self.longName, attribute, value)
				else:
					raise AttributeError('Attribute "{}" does not exist.'.format(attribute))
				return
			else:
				raise TypeError('Attribute must be str.')

	def populateAttributes(self):
		exceptions = ['message', 'TdataCompound']

		if self.isValid():
			for attribute in listAllAttributes(self.longName):
				if hasattr(self, attribute):
					name = attributeName(self.longName, attribute)

					try:
						kind = str(cmds.getAttr(name, type=True))
						value = cmds.getAttr(name) if kind not in exceptions else None
						setattr(self, attribute, value)

					except ValueError:
						pass
		return

	def populateFromScene(self):
		if self.isValid():
			# self.parent = utils.nodeParent(self._name)
			self._kind = nodeType(self.longName)

			children = nodeChildren(self.longName)

			if children:
				for child in children:
					childNode = Node(parent=self, name=child)
					childNode.populateFromScene()
					self.append(childNode)
		return
