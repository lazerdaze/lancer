# Lancer Modules
from attribute import *
from general import *
from naming import *
from customError import *

# Python Modules
import re

# Maya Modules
from maya import cmds


def nodeExists(node):
	return cmds.objExists(node)


def replacementNodeName(name):
	query = re.search(r'\d+$', name)

	if query is not None:
		replace = query.group()
		index = int(replace)

		while nodeExists(name.replace(replace, str(index))):
			index += 1

		return name.replace(replace, str(index))
	else:
		return '{}1'.format(name)


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
#	Abstract Node Class
#
#
########################################################################################################################

class AbstractNode(object):
	def __init__(self,
	             name=None,
	             prefix=None,
	             parent=None,
	             color=None,
	             side=None,
	             index=None,
	             sector=None,
	             kind=None,
	             fullpath=None,
	             ):
		'''
		Abstract Node to be sub-classed by all dag node related classes.

		:param str name:            Name of Node.
		:param str prefix:          Prefix name of the control
		:param object str parent:   Parent of Node.
		:param list children:       Direct descendants of Node.
		:param list color:          RGB Color.
		:param str side:            Side of the controls origin.
		:param int index:           Used to determined rig priority.
		:param str sector:          Sector of control. Possible Sectors: "A", "B", "C"
		:param str kind:            Label of the control to determine rig type.
		'''

		# Name
		self._fullpath = fullpath
		self._name = name
		self._prefix = prefix
		self._parent = parent
		self._children = []
		self._descendants = []

		# Custom Maya Attributes
		self._side = side
		self._sector = sector
		self._index = index
		self._kind = kind

		# Attributes
		self.exists = False
		self.color = color

		# Nodes
		self.transform = None
		self.shape = None

	####################################################################################################################
	# Name Properties
	####################################################################################################################
	def __str__(self):
		return self.longName

	def __repr__(self):
		return self.longName

	@property
	def fullpath(self):
		return self._fullpath

	@fullpath.setter
	def fullpath(self, fullpath):
		self._fullpath = fullpath
		return

	@property
	def prefix(self):
		return self._prefix

	@prefix.setter
	def prefix(self, prefix):
		self._prefix = prefix
		return

	@property
	def side(self):
		return self._side

	@side.setter
	def side(self, side):
		self._side = side
		return

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name
		return

	@property
	def sector(self):
		return self._prefix

	@sector.setter
	def sector(self, sector):
		self._sector = sector
		return

	@property
	def index(self):
		return self._index

	@index.setter
	def index(self, index):
		self._index = index
		return

	@property
	def kind(self):
		return self._kind

	@kind.setter
	def kind(self, kind):
		self._kind = kind
		return

	@property
	def longName(self):
		if self.exists:
			return self._name
		else:
			return longName(self._prefix,
			                self._side[0].upper() if self._side else None,
			                self._name,
			                self._sector,
			                self._index,
			                self._kind,
			                )

	####################################################################################################################
	# Hierarchy
	####################################################################################################################
	@property
	def parent(self):
		return self._parent

	@parent.setter
	def parent(self, parent):
		self._parent = parent
		return

	@property
	def children(self):
		return self._children

	@children.setter
	def children(self, children):
		self._children = children
		return

	@property
	def descendants(self):
		return self._descendants

	@descendants.setter
	def descendants(self, descendants):
		self._descendants = descendants
		return

	####################################################################################################################
	# Attributes
	####################################################################################################################
	def getAttribute(self, attribute):
		if hasattr(self, attribute):
			return getattr(self, attribute)
		return None

	def setAttribute(self, attribute, value):
		if hasattr(self, attribute):
			setattr(self, attribute, value)
			return True
		return False

	def hasAttribute(self, attribute):
		return hasattr(self, attribute)

	def addAttribute(self,
	                 attribute,
	                 value,
	                 ):

		if hasattr(self, attribute):
			raise AttributeError('Attribute "{}" already exists.'.format(attribute))

		setattr(self, attribute, value)
		return


########################################################################################################################
#
#
#	Node Class
#
#
########################################################################################################################

class DagNode(AbstractNode):
	def __init__(self, *args, **kwargs):
		AbstractNode.__init__(self, *args, **kwargs)

		# Attributes
		self.canUpdateName = False

		# Node In Scene
		if nodeExists(self.name):
			self.exists = True
			self.transform = self.name
			self.shape = nodeShapes(self.name)

	def isValid(self):
		return nodeExists(self.longName)

	def create(self, *args, **kwargs):
		if not self.isValid():
			self.transform = cmds.group(name=self.longName, empty=True)
			self.canUpdateName = True
		else:
			raise NodeExistsError('Node "{}" already exists.'.format(self.longName))

	####################################################################################################################
	# Attributes
	####################################################################################################################

	def getAttribute(self, attribute):
		value = AbstractNode.getAttribute(self, attribute)
		if value is not None:
			return value
		else:
			if attributeExist(self.longName, attribute):
				return getAttribute(self.longName, attribute)
			else:
				return None

	def setAttribute(self, attribute, value):
		result = AbstractNode.setAttribute(self, attribute, value)

		if result:
			if self.isValid():
				if attributeLocked(self.longName, attribute):
					raise AttributeError('Attribute "{}" is locked.'.format(attribute))
				elif attributeConnected(self.longName, attribute):
					raise AttributeError('Attribute "{}" is connected.'.format(attribute))
				else:
					setAttribute(self.longName, attribute, value)
		else:
			raise AttributeError('Attribute "{}" does not exist.'.format(attribute))
		return

	def hasAttribute(self, attribute):
		if hasattr(self, attribute):
			return True
		else:
			return attributeExist(self, attribute)

	def addAttribute(self,
	                 attribute,
	                 value,
	                 *args,
	                 **kwargs
	                 ):
		AbstractNode.addAttribute(self, attribute, value)

		kind = kwargs.get('kind', MayaAttrType.float)
		minValue = kwargs.get('minValue', None)
		maxValue = kwargs.get('maxValue', None)
		lock = kwargs.get('lock', False)
		channelBox = kwargs.get('channelBox', False)
		keyable = kwargs.get('keyable', True)
		array = kwargs.get('array', False)

		addAttribute(self.longName,
		             attribute=attribute,
		             kind=kind,
		             value=value,
		             minValue=minValue,
		             maxValue=maxValue,
		             keyable=keyable,
		             channelBox=channelBox,
		             lock=lock,
		             array=array,
		             )
		return

	####################################################################################################################
	# Translate Properties
	####################################################################################################################
	@property
	def translate(self):
		if self.isValid():
			return [self.translateX, self.translateY, self.translateZ]
		return None

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
		return None

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
		return None

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
		return None

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
		return None

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
		return None

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
		return None

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
		return None

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
		return None

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
		return None

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
		return None

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
		return None

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
			return bool(cmds.getAttr(attributeName(self.longName, MayaAttr.visibility)))
		return None

	@visibility.setter
	def visibility(self, value):
		if self.isValid():
			setAttribute(self.longName, attribute=MayaAttr.visibility, value=bool(value), force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	####################################################################################################################
	# Custom Properties
	####################################################################################################################
	def updateName(self):
		if self.isValid() and self.transform:
			self.transform = cmds.rename(self.transform, self.longName)
			return True
		return False

	@property
	def side(self):
		if attributeExist(self.longName, MayaAttr.side):
			return cmds.getAttr(attributeName(self.longName, MayaAttr.side), asString=True).lower()
		else:
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
			setAttribute(self.longName, attribute=MayaAttr.side, value=value)
		else:
			self._side = side
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
		else:
			self._sector = sector
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
		else:
			self._index = index
		return

	@property
	def kind(self):
		if attributeExist(self.longName, UserAttr.kind):
			return getAttribute(self.longName, UserAttr.kind)
		else:
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
		else:
			self._kind = kind
		return

	####################################################################################################################
	# Hierarchy
	####################################################################################################################
	@property
	def parent(self):
		if self.isValid():
			return nodeParent(self.longName)
		return self._parent

	@parent.setter
	def parent(self, parent):
		self._parent = parent

		if self.isValid() and nodeExists(parent):
			cmds.parent(self.longName, parent)
		return

	@property
	def children(self):
		if self.isValid():
			return nodeChildren(self.longName)
		return self._children

	@children.setter
	def children(self, children):
		if self.isValid():
			pass
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
		if self.isValid():
			snap(node, self.longName, t=translation, r=rotation)
		return

	def freezeTransforms(self):
		if self.isValid():
			freezeTransform(self.transform, True, True, True)
		return
