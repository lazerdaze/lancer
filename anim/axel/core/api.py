# AXEL.API
#
#
#
#
#
'''
Structure:

Root
	|- 	Object
		|- 	Attribute
			|- 	Static Value
			|- 	Animation Layer
				|- 	Animation Curve
					|-  Key


'''

# Lancer Modules
from library import xfer

# Python Modules
import os
import platform
import json
import time
import datetime
import xml.dom
from xml.dom import minidom
from xml.dom import minidom
from xml.dom.minidom import parse
from xml.etree import ElementTree as etree

# Maya Modules
MAYALOADED = True
MAYAVERSION = None
try:
	from maya import cmds, mel, OpenMayaUI
except:
	MAYALOADED = False
########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################
# Operating System
OSPLATFORM = platform.system()

# Script Paths
APPNAME = 'AXEL'
EXTENSION = 'axel'
DIRPATH = os.path.dirname(os.path.abspath(__file__))
SUBDIR = os.walk(DIRPATH)
DEFAULTLIBRARY = os.path.join(os.path.dirname(DIRPATH), 'default_library')
PREFSFILEPATH = os.path.join(DIRPATH, 'user_prefserences.json')

DEBUGMODE = True

KIND = ['pose', 'anim', 'axel']

ANIMCURVES = ['animCurveTL',
			  'animCurveTA',
			  'animCurveTT',
			  'animCurveTU',
			  ]

ANIMLAYERS = ['animBlendNodeAdditive']

ROOTATTRIBUTES = ['fileName',
				  'filePath',
				  'fileType',
				  'dateCreated',
				  'objects',
				  'namespaces',
				  'animLayers',
				  'frameStartTime',
				  'frameEndTime',
				  'frameTotalTime',
				  'thumbnail'
				  ]

OBJECTATTRIBUTES = ['name',
					'namespace',
					'type',
					]

POSEATTRIBUTES = ['name',
				  'type',
				  'value',
				  ]

LAYERATTRIBUTES = ['name',
				   'parent',
				   'mute',
				   'solo',
				   'lock',
				   'override',
				   'passThrough',
				   'weight',
				   ]

CURVEATTRIBUTES = ['name',
				   'type',
				   'preInfinity',
				   'postInfinity',
				   'weighted',
				   ]

KEYATTRIBUTES = ['time',
				 'value',
				 'inTangent',
				 'outTangent',
				 'inAngle',
				 'outAngle',
				 'inWeight',
				 'outWeight',
				 'ix',
				 'iy',
				 'ox',
				 'oy',
				 'tangentUnity',
				 'tangentWeight',
				 ]

METAATTRIBUTES = ['name',
				  'kind',
				  'owner',
				  'created',
				  'rating',
				  'size',
				  'start',
				  'end',
				  'items',
				  'shapes',
				  'layers',
				  'comment',
				  'tags',
				  ]

METADATA = {
	'name': 'test',
	'comment': 'This is a comment.',
	'tags': ['tag1', 'tag2'],
	'kind': 'animation',
	'objects': 10,
	'size': '10000',
	'start': 0,
	'end': 100,
	'created': '10/1/2018',
	'owner': None,
}


class component(object):
	directory = 'directory'
	animation = 'animation'
	anim = 'anim'
	pose = 'pose'
	axel = 'axel'
	root = 'root'
	object = 'object'
	attribute = 'attribute'
	animCurve = 'animCurve'
	layer = 'layer'
	key = 'key'
	static = 'static'


########################################################################################################################
#
#
#	File / Directory
#
#
########################################################################################################################

def directoryExist(filepath):
	return os.path.isdir(filepath)


def fileExist(filepath):
	return os.path.isfile(filepath)


def createDirectory(filepath):
	if not directoryExist(filepath):
		return os.mkdir(filepath)


def getDirectoriesInPath(path):
	files = xfer.getAllDirectoriesInPath(path)
	return [f for f in files if not xfer.hasExtension(f)]


def getFilesInPath(path):
	files = xfer.getAllDirectoriesInPath(path)
	return [f for f in files if xfer.hasExtension(f) == EXTENSION]


def isAnimFilepath(filepath):
	base = xfer.pathBaseName(filepath)
	return True if base.endswith(component.anim) else False


def isPoseFilepath(filepath):
	base = xfer.pathBaseName(filepath)
	return True if base.endswith(component.pose) else False


def isAxelFilepath(filepath):
	base = xfer.pathBaseName(filepath)
	extension = base.split('.')[-1].strip()
	return True if extension == EXTENSION else False


def collectSequenceFromFilepath(filepath):
	sequence = []
	directory = os.path.dirname(filepath)
	filename, extension = os.path.splitext(filepath)

	basename = os.path.basename(filepath).replace(extension, '')

	if '.' in basename:
		basename = basename.split('.')[0]

		for f in os.listdir(directory):
			if basename in f:
				sequence.append(os.path.join(directory, f))

	return sorted(sequence) if sequence else None


def getStyleSheet(filepath):
	return xfer.styleSheetImport(filepath)


def readDataFromJson(filepath):
	data = None
	fileType = os.path.basename(filepath.split('.')[-1].strip())

	if fileType == 'json':
		with open(filepath, 'r') as readFile:
			data = json.load(readFile)
		readFile.close()
	return data


def writeDataToJson(filepath, data, indent=0):
	with open(filepath, 'w') as writeFile:
		json.dump(data, writeFile, indent=indent)
	writeFile.close()
	return


########################################################################################################################
#
#
#	STRING UTILITIES
#
#
########################################################################################################################

def joinAttrStr(*args):
	var = ''

	i = 0
	for arg in args:
		if i < len(args) - 1:
			var += '{}.'.format(arg)
		else:
			var += '{}'.format(arg)
		i += 1
	return var


def splitAttrStr():
	return


def convertStrToNiceStr(string):
	if type(string) is int or type(string) is float or type(string) is bool or type(string) is unicode:
		string = str(string)

	if type(string) is str:
		var = ''

		# Filepaths
		if '/' in string or '\\' in string:
			return string

		# Namespaces
		elif ':' in string:
			string = string.split(':')[-1]

		i = 0
		for x in string:

			# Special Characters
			if x in '-_':
				var += ' '

			# Capital Letters
			elif x == x.capitalize():
				var += ' ' + x.lower()

			# Everything Else
			else:
				var += x.lower()
			i += 1
		return var.title().strip()
	elif type(string) is list:
		var = ''
		for x in string:
			var += convertStrToNiceStr(x) + ', '
		return var


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################


def getSelectedObjects(shapes=False):
	objects = []
	selected = cmds.ls(sl=True)

	if selected:
		for sel in selected:
			objects.append(str(sel))
			if shapes:
				shapeNodes = [str(x) for x in cmds.listRelatives(sel, shapes=True)]
				if shapeNodes:
					objects = objects + shapeNodes

	return objects if objects else None


def getFileValues(filepath, kind, comment=''):
	values = {
		'filePath': filepath,
		'fileType': kind,
		'dateCreated': datetime.datetime.now().strftime('%Y/%m/%d %I:%M%p'),
		'comment': comment,
	}
	return values


def keyableAttributes(item):
	return cmds.listAttr(item, keyable=True)


def getStaticAttributes(item):
	return


def getAllKeys(animCurve):
	return cmds.keyframe(animCurve, q=True)


def getObjectValues(node):
	values = {
		'name': node.split(':')[-1],
		'namespace': node.split(':')[0] if ':' in node else '',
		'type': str(cmds.objectType(node))
	}
	return values


def getAttributeValues(item, attr):
	values = {
		'name': attr,
		'type': cmds.getAttr('{}.{}'.format(item, attr), type=True),
	}
	return values


def getStaticValues(attr):
	attrType = cmds.getAttr(attr, type=True)
	attrValue = None

	if attrType == 'bool' or attrType == 'enum':
		attrValue = cmds.getAttr(attr)
	else:
		attrValue = float(cmds.getAttr(attr))

	values = {'value': attrValue}

	return values


def getCurveValues(attr, animCurve):
	values = {
		'name': animCurve,
		'type': cmds.nodeType(animCurve),
		'preInfinity': cmds.setInfinity(attr, at=animCurve, q=True, pri=True)[0],
		'postInfinity': cmds.setInfinity(attr, at=animCurve, q=True, poi=True)[0],
		'weighted': int(cmds.keyTangent(animCurve, q=True, wt=True)[0]),
	}
	return values


def getKeyValues(animCurve, key):
	values = {
		'time': key,
		'value': cmds.keyframe(animCurve, q=True, t=(key, key), vc=True)[0],
		'inTangent': cmds.keyTangent(animCurve, q=True, t=(key, key), itt=True)[0],
		'outTangent': cmds.keyTangent(animCurve, q=True, t=(key, key), ott=True)[0],
		'inAngle': cmds.keyTangent(animCurve, q=True, t=(key, key), ia=True)[0],
		'outAngle': cmds.keyTangent(animCurve, q=True, t=(key, key), oa=True)[0],
		'inWeight': cmds.keyTangent(animCurve, q=True, t=(key, key), iw=True)[0],
		'outWeight': cmds.keyTangent(animCurve, q=True, t=(key, key), ow=True)[0],
		'ix': cmds.keyTangent(animCurve, q=True, t=(key, key), ix=True)[0],
		'iy': cmds.keyTangent(animCurve, q=True, t=(key, key), iy=True)[0],
		'ox': cmds.keyTangent(animCurve, q=True, t=(key, key), ox=True)[0],
		'oy': cmds.keyTangent(animCurve, q=True, t=(key, key), oy=True)[0],
		'tangentUnity': int(cmds.keyTangent(animCurve, q=True, t=(key, key), l=True)[0]),
		'tangentWeight': int(cmds.keyTangent(animCurve, q=True, t=(key, key), wl=True)[0]),
	}
	return values


def getLayerValues(layerName):
	values = {
		'name': layerName,
		'parent': cmds.animLayer(layerName, q=True, p=True),
		'mute': int(cmds.animLayer(layerName, q=True, m=True)),
		'solo': int(cmds.animLayer(layerName, q=True, m=True)),
		'lock': int(cmds.animLayer(layerName, q=True, m=True)),
		'override': int(cmds.animLayer(layerName, q=True, o=True)),
		'passthrough': int(cmds.animLayer(layerName, q=True, pth=True)),
		'weight': float(cmds.animLayer(layerName, q=True, w=True)),
	}
	return values


def isObjectInLayer(obj, animLayer):
	objAnimLayers = cmds.animLayer([obj], q=True, affectedLayers=True) or []
	if animLayer in objAnimLayers:
		return True
	else:
		return False


def isObjectInScene(obj, namespace=None):
	if not namespace:
		if ':' in obj:
			namespace = obj.split(':')[0]
			obj = obj.split(':')[-1]

	objNamespace = '{}:{}'.format(namespace, obj)
	namespaceWild = '*:{}*'.format(obj)

	if cmds.objExists(objNamespace):
		return True

	elif cmds.objExists(namespaceWild):
		return True

	elif cmds.objExists(obj):
		return True
	else:
		return False


def doesAttributeExist(attribute, node=None):
	if '.' in attribute:
		node = attribute.split('.')[0]
		attribute = attribute.split('.')[1]
		return True if cmds.attributeQuery(attribute, node=node, ex=True) else False
	elif node:
		return True if cmds.attributeQuery(attribute, node=node, ex=True) else False
	else:
		return False


def isAnimCurve(node):
	return True if cmds.nodeType(node) in ANIMCURVES else False


def isAnimLayer(node):
	return True if cmds.nodeType(node) in ANIMLAYERS else False


def isAttributeConnected(attribute, node=None):
	if '.' in attribute:
		attrLN = attribute
	else:
		attrLN = '{}.{}'.format(node, attribute)

	if cmds.connectionInfo(attrLN, id=True):
		return cmds.connectionInfo(attrLN, sfd=True)
	else:
		return False


def hasAnimation(attribute, node=None):
	connection = isAttributeConnected(attribute, node)

	if connection:
		connection = connection.split('.')[0]
		if isAnimCurve(connection) or isAnimLayer(connection):
			return connection
	return False


########################################################################################################################
#
#
#	TAGS
#
#
########################################################################################################################

def createTagsFromString(string):
	if type(string) is not str:
		raise TypeError('Argument must be a string.')
	else:
		if string:
			return [x.strip() for x in string.split(',')]
		else:
			return []


########################################################################################################################
#
#
#	BUILD TREES
#
#
########################################################################################################################


def buildAnimLayerTree(obj, attr, animLayers):
	# for parent, child in animLayers.iteritems():
	#
	# 	layerName = parent
	#
	# 	if isObjectInLayer(attr, layerName):
	#
	# 		animLayer_node = xmlAnimLayer(xmlParent, layerName)
	#
	# 		# Get Layer Weight Anim Curve
	#
	# 		if cmds.connectionInfo('{0}.weight'.format(layerName), id=True):
	# 			xml.addAttr(animLayer_node, 'layerWeight', 'animCurve')
	#
	# 			animCurve = cmds.connectionInfo('{0}.weight'.format(layerName), sfd=True).split('.')[0]
	#
	# 			weight_node = xml.createElement(animLayer_node, 'weightAnimCurve')
	#
	# 			xml.addAttr(weight_node, 'name', animCurve)
	# 			xml.addAttr(weight_node, 'type', cmds.nodeType(animCurve))
	# 			xml.addAttr(weight_node, 'preInfinity',
	# 						cmds.setInfinity('{0}.weight'.format(layerName), at=animCurve, q=True, pri=True)[0])
	# 			xml.addAttr(weight_node, 'postInfinity',
	# 						cmds.setInfinity('{0}.weight'.format(layerName), at=animCurve, q=True, poi=True)[0])
	# 			xml.addAttr(weight_node, 'weighted', int(cmds.keyTangent(animCurve, q=True, wt=True)[0]))
	#
	# 			# Get Weight Keys
	#
	# 			for key in cmds.keyframe(animCurve, q=True):
	# 				key_node = xmlKey(weight_node, key, animCurve)
	#
	# 		# Get Base Animation Curves
	#
	# 		if layerName == cmds.animLayer(q=True, root=True):
	#
	# 			connections = cmds.listConnections(attr, type='animBlendNodeBase', s=True, d=False)
	# 			blendNode = None
	#
	# 			while connections:
	# 				blendNode = connections[0]
	# 				connections = cmds.listConnections(blendNode, type='animBlendNodeBase', s=True, d=False)
	#
	# 			input = '{0}.inputA'.format(blendNode)
	#
	# 		# Get Other Layer Animation Curves
	#
	# 		else:
	#
	# 			input = mel.eval('animLayer -q -layeredPlug {0} {1}'.format(attr, layerName))
	#
	# 		# Get AnimCurve Values
	#
	# 		if input:
	#
	# 			animCurve = cmds.connectionInfo(input, sfd=True).split('.')[0]
	# 			anim_node = xmlAnimCurve(animLayer_node, animCurve, input)
	#
	# 			# Get Keys
	#
	# 			for key in cmds.keyframe(animCurve, q=True):
	# 				key_node = xmlKey(anim_node, key, animCurve)
	#
	# 	# Continue Recursion
	#
	# 	if isinstance(child, dict):
	# 		recurseAnimLayers(obj, attr, child, xmlParent)
	pass
	return


########################################################################################################################
#
#
#	BASE CLASS
#
#
########################################################################################################################

class BaseDirectories(object):
	def __init__(self, filepath):
		self.datapath = os.path.join(filepath, 'data.xml')
		self.thumbnaildir = os.path.join(filepath, 'thumbnail')
		self.thumbnailpath = os.path.join(self.thumbnaildir, 'thumbnail.0000.jpg')
		self.metadatapath = os.path.join(filepath, 'metadata.json')

	def getDataFilepath(self):
		return self.datapath

	def getThumbnailDirFilepath(self):
		return self.thumbnaildir

	def getThumbnailFilepath(self):
		return self.thumbnailpath

	def getMetdataFilepath(self):
		return self.metadatapath


class Base(BaseDirectories):
	def __init__(self,
				 name=None,
				 filepath=None,
				 items=None,
				 data=None,
				 kind=None,
				 comment=None,
				 layers=False,
				 shapes=False,
				 tags=None,
				 rating=0,
				 thumbnail=None,
				 created=None,
				 owner=None,
				 start=None,
				 end=None,
				 size=None,
				 ):

		BaseDirectories.__init__(self,
								 filepath=filepath,
								 )

		'''
		:param name:
		:param filepath:
		:param items:
		:param data:
		:param metaData:
		:param kind:
		:param comment:
		:param layers:
		:param shapes:
		:param tags:
		:param rating:
		:param thumbnail:
		'''
		self.name = name
		self.filepath = filepath
		self.items = items if items and type(items) is list else []
		self.data = data
		self.kind = kind
		self.comment = str(comment) if comment else ''
		self.layers = layers
		self.shapes = shapes
		self.thumbnail = thumbnail
		self.tags = tags if tags and type(tags) is list else []
		self.rating = rating
		self.created = created
		self.owner = owner
		self.start = start
		self.end = end
		self.size = size

	def __str__(self):
		value = ''
		for x in vars(self).iterkeys():
			value += '{}: {}\n'.format(x, vars(self)[x])
		return value

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name
		return

	def getFilepath(self):
		return self.filepath

	def setFilepath(self, filepath):
		self.filepath = filepath
		return

	def getItems(self):
		return self.items

	def setItems(self, items):
		self.items = items if items is list else [items]
		return

	def getData(self):
		return self.data

	def setData(self, data):
		self.data = data
		return

	def getKind(self):
		return self.kind

	def setKind(self, kind):
		self.kind = kind
		return

	def getErrors(self):
		return self.errors

	def getComment(self):
		return self.comment

	def setComment(self, comment):
		self.comment = str(comment)
		return

	def getShapes(self):
		return self.shapes

	def setShapes(self, shapes):
		self.shapes = bool(shapes)
		return

	def getLayers(self):
		return self.layers

	def setLayers(self, layers):
		self.layers = bool(layers)
		return

	def setThumbnail(self, thumbnail):
		self.thumbnail = thumbnail
		return

	def getThumbnail(self):
		return self.thumbnail

	def getTags(self):
		return self.tags

	def addTag(self, tag):
		self.tags.append(tag)
		return

	def removeTag(self, tag):
		if tag in self.tags:
			self.tags.remove(tag)
		return

	def getRating(self):
		return self.rating

	def setRating(self, rating):
		self.rating = rating
		return

	def getMetadata(self):
		return vars(self)

	def getCreated(self):
		return self.created

	def setCreated(self):
		self.created = datetime.datetime.now().strftime('%Y/%m/%d %I:%M%p')
		return

	def getOwner(self):
		return self.owner

	def setOwner(self, owner):
		self.owner = owner
		return

	def getStart(self):
		return self.start

	def setStart(self, time):
		self.start = time
		return

	def getEnd(self):
		return self.end

	def setEnd(self, time):
		self.end = time
		return

	def getSize(self):
		return self.size

	def setSize(self):
		if fileExist(self.datapath):
			self.size = os.path.getsize(self.datapath)
		return

	def getMetadata(self):
		return vars(self)


########################################################################################################################
#
#
#	XML CLASS
#
#
########################################################################################################################

'''
Export Import XML - EIXML

Build Based on Dictonaries

#Write
doc = xml.setup()
root = xml.element('test')
test2 = xml.element('test2', parent=root)
test3 = xml.element('test3', parent=root, attrs={'one':1, 'two':2})
xml.build(doc=doc, filepath='', isDebug=True)

# Read
doc = xml.readFile('/home/jtirado/maya/scripts/lacie_userData/sphereTest_6_pose.xml')
for obj in xml.getElement('object'):
        print xml.getAttr(obj, 'name')
'''


class Xml(object):
	def __init__(self):
		self.root = None

	def __str__(self):
		return self.prettyXML(self.root) if self.root else None

	def getRoot(self):
		return self.root

	def setRoot(self, root):
		self.root = root
		return

	def write(self, filepath, root):
		with open(filepath, 'w') as writeFile:
			writeFile.write(self.prettyXML(root))
		writeFile.close()
		return

	def read(self, filepath):
		with open(filepath, 'r') as readFile:
			self.setRoot(etree.parse(filepath).getroot())
		readFile.close()
		return self.root

	def convertStrToList(self, string):
		return str(string).replace('[', '').replace(']', '').replace("u'", '').replace("'", '').replace(" ",
																										'').split(',')

	def createRoot(self, name):
		root = etree.Element(name)
		self.setRoot(root)
		return root

	def createElement(self, parent, name):
		elem = etree.SubElement(parent, name)
		return elem

	def addAttr(self, node, name, value):
		node.set(str(name), str(value))

	def getElement(self, name, *args):
		pass

	def getAttr(self, obj, name, at='str'):

		var = obj.getAttribute(name)

		if at == 'str':
			var = str(var)
		elif at == 'int':
			var = int(var)
		elif at == 'float':
			var = float(var)
		elif at == 'list':
			var = self.convertStrToList(var)

		return var

	def prettyXML(self, root):
		return xfer.prettyXML(root)


########################################################################################################################
#
#
#	IMPORT / EXPORT CLASSES
#
#
########################################################################################################################


class Export(Base, Xml):
	def __init__(self,
				 name,
				 filepath,
				 kind,
				 items=None,
				 tags=None,
				 comment=None,
				 layers=False,
				 ):

		Base.__init__(self,
					  name=name,
					  filepath=filepath,
					  items=items,
					  kind=kind,
					  tags=tags,
					  comment=comment,
					  layers=layers,
					  )

	def createDirectories(self):
		createDirectory(self.filepath)
		createDirectory(self.thumbpath)
		return

	def createMetaData(self):
		writeDataToJson(self.metadatapath, data=vars(self), indent=0)
		return

	def createRootNode(self):
		root = self.createRoot(component.root)
		rootAttrs = getFileValues(self.datapath, self.kind)

		for attr in rootAttrs:
			self.addAttr(root, attr, rootAttrs[attr])

		self.addAttr(root, 'objects', self.items)
		return root

	def createObjectNode(self, parent, item):
		itemNode = self.createElement(parent, component.object)
		itemAttrs = getObjectValues(item)

		for attr in itemAttrs:
			self.addAttr(itemNode, attr, itemAttrs[attr])
		return itemNode

	def createAttrNode(self, parent, item, attribute):
		attributeNode = self.createElement(parent, component.attribute)
		atttributeAttrs = getAttributeValues(item, attribute)

		for attr in atttributeAttrs:
			self.addAttr(attributeNode, attr, atttributeAttrs[attr])
		return attributeNode

	def createCurveNode(self, parent, item, attribute, curve):
		curveNode = self.createElement(parent, component.animCurve)
		curveAttrs = getCurveValues(joinAttrStr(item, attribute), curve)

		for attr in curveAttrs:
			self.addAttr(curveNode, attr, curveAttrs[attr])
		return curveNode

	def createKeyNode(self, parent, curve):
		for key in getAllKeys(curve):
			keyNode = self.createElement(parent, component.key)
			keyAttrs = getKeyValues(curve, key)

			for attr in keyAttrs:
				self.addAttr(keyNode, attr, keyAttrs[attr])
		return

	def createStaticNode(self, parent, item, attribute):
		staticNode = self.createElement(parent, component.static)
		staticAttrs = getStaticValues(joinAttrStr(item, attribute))

		for attr in staticAttrs:
			self.addAttr(staticNode, attr, staticAttrs[attr])
		return staticNode

	def exportToFilepath(self):
		t1 = time.time()
		self.createDirectories()

		# Root Node
		root = self.createRootNode()

		# Object Nodes
		for item in self.items:
			itemNode = self.createObjectNode(root, item)

			# Attribute Nodes
			for attribute in keyableAttributes(item):
				attributeNode = self.createAttrNode(itemNode, item, attribute)

				# Curve Nodes
				connection = hasAnimation(attribute, item)
				if self.kind == component.anim and connection:
					if isAnimCurve(connection):
						curveNode = self.createCurveNode(attributeNode, item, attribute, connection)
						self.createKeyNode(curveNode, connection)

					# Layers
					elif isAnimLayer(connection):
						pass

				# Static Nodes
				else:
					self.createStaticNode(attributeNode, item, attribute)

			self.write(self.datapath, root)
			self.createMetaData()
			print 'Axel File Export: "{}" successfully in {} seconds.'.format(self.filepath, time.time() - t1),
			return


class Import(Base, Xml):
	def __init__(self,
				 filepath,
				 ):
		Base.__init__(self,
					  filepath=filepath,
					  )

	def readMetadata(self):
		if fileExist(self.metadatapath):
			metadata = readDataFromJson(self.metadatapath)
			for data in metadata:
				if data in vars(self):
					setattr(self, data, metadata[data])
		return

	def importFromFilepath(self):
		return


########################################################################################################################
#
#
#	ITEM CLASSES
#
#
########################################################################################################################


class AbstractItem(Export, Import):
	def __init__(self,
				 filepath,
				 name=None,
				 kind=None,
				 items=None,
				 comment=None,
				 tags=None,
				 layers=False,
				 ):
		Export.__init__(self,
						filepath=filepath,
						name=name,
						kind=kind,
						items=items,
						tags=tags,
						comment=comment,
						layers=layers,
						)

		Import.__init__(self,
						filepath=filepath,
						)
