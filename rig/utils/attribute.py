# Lancer Modules
from naming import *

# Maya Modules
from maya import cmds

DataTypes = ['string',
             'stringArray',
             'matrix',
             'reflectanceRGB',
             'spectrumRGB',
             'float2',
             'float3',
             'double2',
             'double3',
             'long2',
             'long3',
             'short2',
             'short3',
             'doubleArray',
             'floatArray',
             'Int32Array',
             'vectorArray',
             'nurbsCurve',
             'nurbsSurface',
             'mesh',
             'lattice',
             'pointArray',
             ]

AttributeTypes = ['bool',
                  'long',
                  'short',
                  'byte',
                  'char',
                  'enum',
                  'float',
                  'double',
                  'doubleAngle',
                  'doubleLinear',
                  'compound',
                  'message',
                  'time',
                  'fltMatrix',
                  'reflectance',
                  'spectrum',
                  'float2',
                  'float3',
                  'double2',
                  'double3',
                  'long2',
                  'long3',
                  'short2',
                  'short3'
                  ]


def addAttribute(node,
                 attribute,
                 kind=MayaAttrType.float,
                 value=None,
                 minValue=None,
                 maxValue=None,
                 keyable=True,
                 channelBox=True,
                 lock=False,
                 destinationNode=None,
                 destinationAttribute=None,
                 array=False,
                 ):
	name = attributeName(node, attribute)

	if not attributeExist(node, attribute):

		# Create
		if kind == MayaAttrType.enum:
			if isinstance(value, (str, list, dict, tuple)):
				cmds.addAttr(node, longName=attribute, attributeType=kind, enumName=enumName(value), m=array)
			else:
				raise ValueError('No default enum values specified.')
		else:
			if kind in DataTypes:
				cmds.addAttr(node, longName=attribute, dataType=kind, m=array)

			elif kind in AttributeTypes:
				cmds.addAttr(node, longName=attribute, attributeType=kind, keyable=keyable, m=array)
			else:
				cmds.addAttr(node, longName=attribute, m=array)

		# Set Keyable
		try:
			cmds.setAttr(name, channelBox=channelBox, keyable=keyable)
		except RuntimeError:
			pass

		# Set Default Values
		if value is not None and kind != MayaAttrType.enum:
			if isinstance(value, (int, float)):
				cmds.addAttr(name, edit=True, defaultValue=float(value))
				cmds.setAttr(name, float(value))
			elif isinstance(value, str):
				cmds.setAttr(name, value, type=MayaAttrType.string)

		if minValue is not None:
			cmds.addAttr(name, edit=True, minValue=float(minValue))

		if maxValue is not None:
			cmds.addAttr(name, edit=True, maxValue=float(maxValue))

		# Set Lock
		if lock:
			cmds.setAttr(name, lock=lock)

		# Connect To Destination
		if destinationNode and destinationAttribute:
			destinationName = attributeName(destinationNode, destinationAttribute)

			if attributeExist(destinationNode, destinationAttribute):
				cmds.connectAttr(name, destinationName, force=True)
			else:
				raise AttributeError('Attribute "{}" does not exist.'.format(destinationName))
	else:
		raise AttributeError('Attribute "{}" already exists.'.format(name))
	return


def setAttribute(node, attribute, value, lock=None, force=False):
	name = attributeName(node, attribute)
	kind = attributeType(node, attribute)
	isLocked = attributeLocked(node, attribute)
	isConnected = attributeConnected(node, attribute)

	if isLocked and not force:
		raise AttributeError('Attribute "{}" is currently locked. Use "force=True" parameter to bypass.'.format(name))
	elif isConnected:
		raise AttributeError('Attribute "{}" has incoming connections.'.format(name))
	else:
		if isLocked and force:
			cmds.setAttr(name, lock=False)

		if kind == MayaAttrType.string:
			cmds.setAttr(name, value, type=kind)
		else:
			cmds.setAttr(name, value)

		if isLocked or lock:
			cmds.setAttr(name, lock=True)
	return


def getAttribute(node, attribute):
	name = attributeName(node, attribute)
	return cmds.getAttr(name)


def attributeType(node, attribute):
	return str(cmds.getAttr(attributeName(node, attribute), type=True))


def attributeLocked(node, attribute):
	return cmds.getAttr(attributeName(node, attribute), lock=True)


def disconnectAttribute(attribute):
	if cmds.connectionInfo(attribute, isDestination=True):
		source = cmds.connectionInfo(attribute, sourceFromDestination=True)
		cmds.disconnectAttr(source, attribute)
	return


def connectAttribute(*args, **kwargs):
	# Get Keywords
	offset = kwargs.get('offset', False)
	source = kwargs.get('source', None)
	sourceAttr = kwargs.get('sourceAttr', None)
	destination = kwargs.get('destination', None)
	destinationAttr = kwargs.get('destinationAttr', None)

	# Get Args
	if len(args) == 2:
		if not source:
			source = args[0]

		if not destination:
			destination = args[1]

	if source and destination:
		if not sourceAttr and not destinationAttr:
			if '.' in source:
				sourceResult = source.split('.')
				source = sourceResult[0]
				sourceAttr = sourceResult[1]

			if '.' in destination:
				destinationResult = destination.split('.')
				destination = destinationResult[0]
				destinationAttr = destinationResult[1]

		# Connect
		if sourceAttr and destinationAttr:
			sourceName = attributeName(source, sourceAttr)
			destinationName = attributeName(destination, destinationAttr)

			# Disconnect
			disconnectAttribute(destinationName)

			if attributeExist(source, sourceAttr) and attributeExist(destination, destinationAttr):

				# Offset
				if offset:
					offsetNode = cmds.createNode(MayaNodeType.addDoubleLinear,
					                             name=longName(source, Component.offset, 0),
					                             )

					sourceValue = cmds.getAttr(sourceName)
					destinationValue = cmds.getAttr(destinationName)

					cmds.setAttr(attributeName(offsetNode, 'input2'), destinationValue - sourceValue)

					# Connect Offset
					cmds.connectAttr(sourceName, attributeName(offsetNode, 'input1'), force=True)
					sourceName = attributeName(offsetNode, 'output')

				cmds.connectAttr(sourceName, destinationName, force=True)

			else:
				raise ValueError('Source or destination attribute does not exist.')
		else:
			raise ValueError('A valid source or destination attribute was not provided.')
	else:
		raise ValueError('Must provide two nodes.')
	return


def connectDefaultAttributes(*args, **kwargs):
	offset = kwargs.get('offset', False)
	source = kwargs.get('source', None)
	sourceAttr = kwargs.get('sourceAttr', None)
	destination = kwargs.get('destination', None)
	destinationAttr = kwargs.get('destinationAttr', None)

	translate = kwargs.get('translate', False)
	rotate = kwargs.get('rotate', False)
	scale = kwargs.get('scale', False)

	attributes = {
		MayaAttr.translate: translate,
		MayaAttr.rotate   : rotate,
		MayaAttr.scale    : scale,
	}

	if len(args) > 1:
		parent = args[0]

		for arg in args:
			if arg != parent:
				for attr in attributes:
					if attributes[attr]:
						for axis in ['x', 'y', 'z']:
							connectAttr = '{}{}'.format(attr, axis.upper())

							if not attributeLocked(parent, connectAttr) and not attributeLocked(arg, connectAttr):
								cmds.connectAttr(attributeName(parent, connectAttr),
								                 attributeName(arg, connectAttr)
								                 )
	else:
		raise ValueError('Must provide two nodes.')
	return


def getKeyableAttributes(node):
	result = cmds.listAttr(node, k=True)
	try:
		result = [x for x in result if attributeType(node, x) not in ['string']]
	except TypeError:
		return []
	return result if result else []


def getNonKeyableAttributes(node):
	result = cmds.listAttr(node, cb=True)
	return result if result else []


def getChannelBoxAttributes(node):
	return getKeyableAttributes(node) + getNonKeyableAttributes(node)


def attributeExist(node, attribute):
	return cmds.attributeQuery(attribute, node=node, ex=True)


def hideAttributes(node):
	attributes = cmds.listAttr(node, k=True)
	if attributes:
		for attr in attributes:
			cmds.setAttr('{}.{}'.format(node, attr), keyable=False, channelBox=False)
	return


def listAllAttributes(node):
	return cmds.listAttr(node)


def attributeConnected(node, attribute):
	longName = attributeName(node, attribute)
	return True if cmds.connectionInfo(longName, id=True) else False


def lockAttribute(node, attribute):
	return cmds.setAttr(attributeName(node, attribute), lock=True)


def unlockAttribute(node, attribute):
	return cmds.setAttr(attributeName(node, attribute), lock=False)


def lockKeyableAttributes(node, hide=False):
	hide = False if hide else True
	attributes = getChannelBoxAttributes(node)
	if attributes:
		for attr in attributes:
			cmds.setAttr('{}.{}'.format(node, attr), lock=True, keyable=hide, channelBox=hide)
	return


def lockTranslate(node, hide=False):
	for axis in ['x', 'y', 'z']:
		cmds.setAttr('{}.t{}'.format(node, axis), lock=True, keyable=hide, channelBox=hide)
	return


def lockRotate(node, hide=False):
	for axis in ['x', 'y', 'z']:
		cmds.setAttr('{}.r{}'.format(node, axis), lock=True, keyable=hide, channelBox=hide)
	return


def lockScale(node, hide=False):
	for axis in ['x', 'y', 'z']:
		cmds.setAttr('{}.s{}'.format(node, axis), lock=True, keyable=hide, channelBox=hide)
	return


def setVisibility(node, hide=True):
	hide = False if hide else True
	attrName = '{}.v'.format(node)
	cmds.setAttr(attrName, hide, lock=False)
	return


def zeroAttrs(node, *args):
	for attr in ['t', 'r', 's']:
		value = 0

		if attr == 's':
			value = 1

		for axis in ['x', 'y', 'z']:
			try:
				cmds.setAttr('{}.{}{}'.format(node, attr, axis), value)
			except:
				pass


def addEmptyAttr(node, n='customAttr', *args):
	cmds.addAttr(node, ln=n, at='enum', en='-:', k=True)
	cmds.setAttr('{}.{}'.format(node, n), e=True, channelBox=True)
	return


def addBoolAttr(node, name):
	attrName = '{}.{}'.format(node, name)
	cmds.addAttr(node, ln=name, at='enum', en='off:on')
	cmds.setAttr(attrName, e=True, cb=True)
	return attrName


def setEnumByString(node, attr, value):
	enumString = cmds.attributeQuery(attr, node=node, listEnum=1)[0]
	enumList = enumString.split(':')
	try:
		index = enumList.index(str(value))
	except ValueError:
		try:
			index = enumList.index(str(value).capitalize())
		except ValueError:
			return False
	else:
		return False
	attribute = '{}.{}'.format(node, attr)
	cmds.setAttr(attribute, index)
	return True


def addSideAttr(node):
	cmds.addAttr(node, ln='side', at='enum', en='Center:Left:Right:None:', keyable=True)
	cmds.setAttr('{}.side'.format(node), 3, keyable=False, cb=False)
	return


def getConnectedNode(node, attribute):
	name = '{}.{}'.format(node, attribute)

	if cmds.connectionInfo(name, id=True):
		query = cmds.listConnections(cmds.connectionInfo(name, ged=True), skipConversionNodes=True)
		if query is None:
			return query
		else:
			return query[0] if len(query) == 1 else query
	else:
		query = cmds.listConnections(name, skipConversionNodes=True)
		if query is None:
			return query
		else:
			return query[0] if len(query) == 1 else query


def addIndexAttribute(node, value):
	name = UserAttr.index
	if not attributeExist(node, name):

		addAttribute(node=node,
		             attribute=name,
		             kind=MayaAttrType.int,
		             value=value,
		             keyable=False,
		             channelBox=False,
		             )
	else:
		cmds.setAttr(attributeName(node, name), value)

	return



########################################################################################################################
#
#
#	Attribute Class
#
#
########################################################################################################################


class Attribute(object):
	def __init__(self, node, name, kind=None, value=None, lock=False):
		self.name = attributeName(node, name)
		self.kind = kind
		self.value = value
		self.lock = lock

		# Connections
		self.parentConnection = None
		self.childConnection = None

	def __str__(self):
		value = ''
		for x in sorted(vars(self).iterkeys()):
			value += '{}:\t{}\n'.format(x, vars(self)[x])
		return value

	def __repr__(self):
		return self.name
