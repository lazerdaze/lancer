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

# Axel Modules
from ... import *

# Python Modules
import os
import platform
import json

# Maya Modules
from maya import cmds, mel
from maya import OpenMayaUI as omu

########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################

DEBUGMODE = True
LOCALPATH = os.path.dirname(os.path.abspath(__file__))
PREFSFILE = os.path.join(LOCALPATH, 'user_prefs.json')

ANIMCURVES = ['animCurveTL',
			  'animCurveTA',
			  'animCurveTT',
			  'animCurveTU',
			  ]

ANIMLAYERS = ['animBlendNodeAdditive']

ROOTATTRIBUTES = ['fileName',
				  'filePath',
				  'fileType',
				  'dateModified',
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

METAATTRIBUTES = ['filename',
				  'filepath',
				  'filetype',
				  'dateCreated',
				  'thumbnail']


class component(object):
	animation = 'animation'
	anim = 'anim'
	pose = 'pose'


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################

def joinAttrStr(*args):
	var = ''

	i=0
	for arg in args:
		if i < len(args) - 1:
			var += '{}.'.format(arg)
		else:
			var += '{}'.format(arg)
		i+=1
	return var


def splitAttrStr():
	return


def keyableAttributes(item):
	return cmds.listAttr(item, keyable=True)


def getStaticAttributes(item):
	return


def getAllKeys(animCurve):
	return cmds.keyframe(animCurve, q=True)


def getObjectValues(node):
	values = {'name': node.split(':')[-1],
			  'namespace': node.split(':')[0] if ':' in node else None,
			  'type': str(cmds.objectType(node))}
	return values


def getAttributeValues(attr):
	values = {'name': attr,
			  'type': cmds.getAttr(attr, type=True),
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
	values = {'name': animCurve,
			  'type': cmds.nodeType(animCurve),
			  'preInfinity': cmds.setInfinity(attr, at=animCurve, q=True, pri=True)[0],
			  'postInfinity': cmds.setInfinity(attr, at=animCurve, q=True, poi=True)[0],
			  'weighted': int(cmds.keyTangent(animCurve, q=True, wt=True)[0]),
			  }
	return values


def getKeyValues(animCurve, key):
	values = {'time': key,
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
	values = {'name': layerName,
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
#	BUILD TREES
#
#
########################################################################################################################


def buildMasterTree():
	return


def buildPoseTree():
	return


def buildAnimTree():
	return


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
#	THUMBNAILS
#
#
########################################################################################################################


def exportThumbnail(filepath, ext='jpg', w=200, h=200):
	imagefilepath = '{0}_thumbnail.{1}'.format(filepath, ext)

	focus = cmds.getPanel(wf=True)

	if cmds.modelPanel(focus, q=True, exists=True):
		# Get Camera Info

		focusCam = cmds.modelPanel(focus, q=True, cam=True)
		focusCamShape = cmds.listRelatives(focusCam, shapes=True)[0]

		# Set Pan Zoom

		cmds.setAttr(focusCamShape + '.panZoomEnabled', 1)
		cmds.panZoom(focusCamShape, abs=True, l=0, u=0, z=0.50)

		# Create Window w/ Model Editor

		cmds.window('pbWin')
		cmds.paneLayout()
		pbPanel = cmds.modelPanel(cam=focusCam)

		cmds.modelEditor(pbPanel,
						 e=True,
						 allObjects=False,
						 manipulators=True,
						 grid=False,
						 sel=False,
						 polymeshes=True,
						 imagePlane=True,
						 displayAppearance='smoothShaded',
						 ignorePanZoom=False,
						 )

		# Playblast
		cmds.playblast(epn=pbPanel, p=100, wh=(w, h), fr=cmds.currentTime(q=True), fmt='image', cf=imagefilepath,
					   c=ext, fo=True, v=False, orn=False, os=True, sqt=False, qlt=100)

		# Remove UI
		cmds.deleteUI('pbWin', window=True)

		# Reset Pan Zoom
		cmds.setAttr(focusCamShape + '.panZoomEnabled', 0)
		return imagefilepath


########################################################################################################################
#
#
#	ITEM CLASS
#
#
########################################################################################################################


class AbstractItem(object):
	def __init__(self,
				 filepath=None,
				 kind=None,
				 metaData=None,
				 data=None,
				 thumbnail=None,
				 comment=None,
				 date=None,
				 tags=None,
				 ):

		self.filepath = filepath
		self.kind = kind
		self.metaData = metaData
		self.data = data
		self.thumbnail = thumbnail
		self.comment = comment
		self.date = date
		self.tags = tags if tags is list else [tags]

	def __str__(self):
		value = ''
		for x in vars(self).iterkeys():
			if x == 'data':
				value += 'Data: {}\n'.format(True if self.data else None)

			elif x == 'metaData':
				if type(self.metaData) is dict:
					for key in x:
						value += '{}: {}\n'.format(key.capitalize(), x[key])
				else:
					value += 'MetaData: {}\n'.format(self.metaData)

			elif '__' not in x:
				value += '{}: {}\n'.format(x.capitalize(), vars(self)[x])
		return value

	def setFilepath(self, filepath):
		self.filepath = filepath
		return

	def getFilepath(self, filepath):
		return

	def setData(self, data):
		self.data = data
		return

	def getData(self):
		return self.data

	def setKind(self, kind):
		self.kind = kind
		return

	def getKind(self):
		return self.kind

	def setMetaData(self, data):
		self.metaData = data
		return

	def getMetaData(self):
		return self.metaData

	def setComment(self, comment):
		self.comment = comment
		return

	def getComment(self):
		return self.comment

	def setDate(self, date):
		self.date = date
		return

	def getDate(self):
		return self.date

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
