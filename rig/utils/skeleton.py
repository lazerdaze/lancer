# Lancer Modules
from general import *
from naming import *
from attribute import *
from joint import *
from library import xfer
from library.axml import Axml

# Maya Modules
import maya.cmds as cmds

# Python Modules
import os
import json
import time

"""
Skinning Notes:
	- Skinning Method: Classic Linear (Dual Quaterion isn't supported in realtime game engines)
	- Max Mesh-Influencing Joints: 75
	- Max Total Bones: 256
	- Max bones influences per vertex: 4 - 8 (will be normalized)

HIK Notes:
	- Max Arm / Leg Roll Joints: 5
	- Max Spine Joints: 10
	- Max Neck Joints: 10
	
- Selection:
	- Relationship (fastest)
	- Kind 
	- Name (slowest)
	
"""

########################################################################################################################
#
#
#	Global Variables
#
#
########################################################################################################################

SKELETON_JOINT_ATTRIBUTES = [
	'translateX',
	'translateY',
	'translateZ',
	'jointOrientY',
	'jointOrientX',
	'jointOrientZ',
	'rotateX',
	'rotateY',
	'rotateZ',
	'side',
	'type',
	'otherType',
	'kind',
]


class SkeletonType(object):
	# Two Legs
	biped = 'biped'

	# Four Legs: Mammals
	quadruped = 'quadruped'

	# More than Six Legs: Insects / Spiders / Octopus
	arthropod = 'arthropod'
	hexapod = 'hexapod'
	octopod = 'octopod'

	# More than 8 Legs:
	centipede = 'centipede'
	milipede = 'milipede'


class Biped_Definition(object):
	# Root / Spine
	root = 'root'
	cog = 'cog'
	hip = 'hip'
	spine = 'spine'
	neck = 'neck'
	head = 'head'

	# Arm
	leftCollar = 'leftCollar'
	leftShoulder = 'leftShoulder'
	leftElbow = 'leftElbow'
	leftHand = 'leftHand'

	rightCollar = 'rightCollar'
	rightShoulder = 'rightShoulder'
	rightElbow = 'rightElbow'
	rightHand = 'rightHand'

	# Fingers
	leftThumb = 'leftThumb'
	leftIndexFinger = 'leftIndexFinger'
	leftMiddleFinger = 'leftMiddleFinger'
	leftRingFinger = 'leftRingFinger'
	leftPinkyFinger = 'leftPinkyFinger'

	rightThumb = 'rightThumb'
	rightIndexFinger = 'rightIndexFinger'
	rightMiddleFinger = 'rightMiddleFinger'
	rightRingFinger = 'rightRingFinger'
	rightPinkyFinger = 'rightPinkyFinger'

	# Leg
	leftHip = 'leftHip'
	leftKnee = 'leftKnee'
	leftFoot = 'leftFoot'
	leftToe = 'leftToe'
	leftHeel = 'leftHeel'

	rightHip = 'rightHip'
	rightKnee = 'rightKnee'
	rightFoot = 'rightFoot'
	rightToe = 'rightToe'
	rightHeel = 'rightHeel'

	# Toes
	leftBigToe = 'leftBigToe'
	leftIndexToe = 'leftIndexToe'
	leftMiddleToe = 'leftMiddleToe'
	leftRingToe = 'leftRingToe'
	leftPinkyToe = 'leftPinkyToe'

	rightBigToe = 'rightBigToe'
	rightIndexToe = 'rightIndexToe'
	rightMiddleToe = 'rightMiddleToe'
	rightRingToe = 'rightRingToe'
	rightPinkyToe = 'rightPinkyToe'


class HIK_Definition(object):
	Reference = 'Reference'
	Hips = 'Hips'
	Spine = 'Spine'
	Neck = 'Neck'
	Head = 'Head'

	LeftShoulder = 'LeftShoulder'
	LeftArm = 'LeftArm'
	LeftFoot = 'LeftFoot'
	LeftToeBase = 'LeftToeBase'
	LeftForeArm = 'LeftForeArm'
	LeftHand = 'LeftHand'
	LeftHandThumb = 'LeftHandThumb'

	LeftInHandIndex = 'LeftInHandIndex'
	LeftHandIndex = 'LeftHandIndex'
	LeftInHandMiddle = 'LeftInHandMiddle'
	LeftHandMiddle = 'LeftHandMiddle'
	LeftInHandRing = 'LeftInHandRing'
	LeftHandRing = 'LeftHandRing'
	LeftInHandPinky = 'LeftInHandPinky'
	LeftHandPinky = 'LeftHandPinky'

	LeftLeg = 'LeftLeg'
	LeftUpLeg = 'LeftUpLeg'

	RightShoulder = 'RightShoulder'
	RightArm = 'RightArm'
	RightFoot = 'RightFoot'
	RightToeBase = 'RightToeBase'
	RightForeArm = 'RightForeArm'
	RightHand = 'RightHand'
	RightHandThumb = 'RightHandThumb'

	RightInHandIndex = 'RightInHandIndex'
	RightHandIndex = 'RightHandIndex'
	RightInHandMiddle = 'RightInHandMiddle'
	RightHandMiddle = 'RightHandMiddle'
	RightInHandRing = 'RightInHandRing'
	RightHandRing = 'RightHandRing'
	RightInHandPinky = 'RightInHandPinky'
	RightHandPinky = 'RightHandPinky'

	RightLeg = 'RightLeg'
	RightUpLeg = 'RightUpLeg'


BIPED_TO_HIK = {
	Biped_Definition.cog              : HIK_Definition.Reference,
	Biped_Definition.hip              : HIK_Definition.Hips,
	Biped_Definition.spine            : HIK_Definition.Spine,
	Biped_Definition.neck             : HIK_Definition.Neck,
	Biped_Definition.head             : HIK_Definition.Head,

	Biped_Definition.leftCollar       : HIK_Definition.LeftShoulder,
	Biped_Definition.leftShoulder     : HIK_Definition.LeftArm,
	Biped_Definition.leftFoot         : HIK_Definition.LeftFoot,
	Biped_Definition.leftToe          : HIK_Definition.LeftToeBase,
	Biped_Definition.leftElbow        : HIK_Definition.LeftForeArm,
	Biped_Definition.leftHand         : HIK_Definition.LeftHand,
	Biped_Definition.leftThumb        : HIK_Definition.LeftHandThumb,

	Biped_Definition.leftIndexFinger  : HIK_Definition.LeftHandIndex,
	Biped_Definition.leftMiddleFinger : HIK_Definition.LeftHandMiddle,
	Biped_Definition.leftRingFinger   : HIK_Definition.LeftHandRing,
	Biped_Definition.leftPinkyFinger  : HIK_Definition.LeftHandPinky,

	Biped_Definition.rightCollar      : HIK_Definition.RightShoulder,
	Biped_Definition.rightShoulder    : HIK_Definition.RightArm,
	Biped_Definition.rightFoot        : HIK_Definition.RightFoot,
	Biped_Definition.rightToe         : HIK_Definition.RightToeBase,
	Biped_Definition.rightElbow       : HIK_Definition.RightForeArm,
	Biped_Definition.rightHand        : HIK_Definition.RightHand,
	Biped_Definition.rightThumb       : HIK_Definition.RightHandThumb,

	Biped_Definition.rightIndexFinger : HIK_Definition.RightHandIndex,
	Biped_Definition.rightMiddleFinger: HIK_Definition.RightHandMiddle,
	Biped_Definition.rightRingFinger  : HIK_Definition.RightHandRing,
	Biped_Definition.rightPinkyFinger : HIK_Definition.RightHandPinky,
}


class SkeletonDefinition(object):
	def __init__(self):
		self.__dict__.update(
				{SkeletonType.biped: [x for x in vars(Biped_Definition).iterkeys() if not x.startswith('__')]})

	def __getitem__(self, key):
		return self.__dict__[key]

	def __setitem__(self, key, value):
		self.__dict__[key] = value

	def __delitem__(self, key):
		del self.__dict__[key]

	def __contains__(self, key):
		return key in self.__dict__

	def __len__(self):
		return len(self.__dict__)

	def __repr__(self):
		return repr(self.__dict__)


########################################################################################################################
#
#
#	Selection
#
#
########################################################################################################################

def getSkeletonChildren(root, kind=None):
	return


def getSkeletonBindJointsOnSelected(kind='bind', *args, **kwargs):
	selected = getSelected()

	result = []

	if selected:
		cmds.select(d=True)

		for item in selected:
			query = getSkeletonBindJoints(item, kind)
			if query:
				result += query
		if result:
			cmds.select(result)

	return result if result else None


def getSkeletonBindJoints(root, kind='bind'):
	if nodeType(root) != 'joint':
		raise NodeTypeError('Must provide a root joint.')

	result = []

	# By Connection
	if attributeExist(root, kind):
		conn = cmds.listConnections(attributeName(root, kind))
		result += conn if isinstance(conn, list) else []

	# By Type | Name
	children = getAllJointChildren(root)
	if children:
		for child in children:

			if getJointLabelOtherType(child).lower() == kind or kind in child:
				if kind != 'joint':
					if child not in result:
						result.append(child)

			# By Kind
			elif attributeExist(child, 'kind'):
				if getAttribute(child, 'kind').lower() == kind:
					if child not in result:
						result.append(child)

	return result if result else None


########################################################################################################################
#
#
#	Query
#
#
########################################################################################################################


class Query:
	def __init__(self, root=None):
		self.root = root
		self.children = getAllJointChildren(root) if root else None
		self.joints = self.getAllJoints()
		self.data = {}
		self.armLabels = ['Collar', 'Shoulder', 'Elbow', 'Hand']
		self.fingerLabels = ['Thumb', 'Index Finger', 'Middle Finger', 'Ring Finger', 'Pinky Finger']
		self.legLabels = ['Hip', 'Knee', 'Foot', 'Toe']
		self.toeLabels = ['Big Toe', 'Index Toe', 'Middle Toe', 'Ring Toe', 'Pinky Toe']
		self.limbLabels = self.armLabels + self.fingerLabels + self.legLabels + self.toeLabels

		if self.joints:
			self.populate()
			self.populateLimbs()

	def __str__(self):
		return str(json.dumps(self.data, indent=8))

	def getAllJoints(self):
		joints = []
		if self.root:
			joints.append(self.root)
		if self.children:
			joints = joints + self.children
		return joints

	def getLimbLabels(self, limb):
		if limb == 'Arms':
			return self.armLabels
		elif limb == 'Legs':
			return self.legLabels
		else:
			return limb

	def populateLimbs(self):
		dataList = []
		limbDict = {}
		for limb in ['Arms', 'Legs'] + self.fingerLabels + self.toeLabels:

			sideDict = {}
			for side in ['Left', 'Right']:
				limbLabels = self.getLimbLabels(limb)
				indexList = {}

				for joint in self.joints:
					label = getJointLabel(joint)
					labelSide = label[0]
					labelType = label[1]
					jointIndex = getJointIndex(joint)

					if side == labelSide:
						if limb in ['Arms', 'Legs']:
							if labelType in limbLabels:
								if jointIndex in indexList:
									indexList[jointIndex].append(joint)
								else:
									indexList[jointIndex] = [joint]
						else:
							if labelType == limb:
								if jointIndex in indexList:
									indexList[jointIndex].append(joint)
								else:
									indexList[jointIndex] = [joint]

				for x in indexList:
					indexList[x] = sortJointHierarchy(indexList[x])

				sideDict[side] = indexList
			limbDict[limb] = sideDict

		dataList.append(limbDict)

		dataDict = {}
		for x in dataList:
			for label, labelData in x.items():
				dataDict[label] = labelData

		self.data['Limbs'] = dataDict

	def populate(self):
		dataList = []

		for jointLabel in jointLabelGlobalList:
			if jointLabel not in self.limbLabels:
				labelList = []
				for joint in self.joints:
					label = getJointLabel(joint)
					labelSide = label[0]
					labelType = label[1]
					jointIndex = getJointIndex(joint)

					if labelType == jointLabel:
						labelList.append(joint)

				if jointLabel not in ['None', 'Bind']:
					dataList.append({jointLabel: sortJointHierarchy(labelList) if labelList else labelList})

		for x in dataList:
			for label, labelData in x.items():
				self.data[label] = labelData
		return

	def get(self, typ, limbType=None, side=None, index=0):
		typ = typ.title()
		if typ in self.data:
			if limbType:
				limbType = limbType.title()
				side = side.title()
				return self.data[typ][limbType][side][index]
			else:
				return self.data[typ]
		else:
			print 'Cannot find "{}".'.format(typ)
			return None


########################################################################################################################
#
#
#	Network
#
#
########################################################################################################################


def createSkeletonNetworkNode(name='skeletonNetwork'):
	node = cmds.createNode('network', name=name)
	cmds.addAttr(node, ln='networkType', dt='string')
	cmds.setAttr('{}.networkType'.format(node), 'skeleton', type='string', lock=True)
	return node


def createSkeletonNetwork(root=None, name='skeletonNetwork'):
	skeletonNetwork = None
	if not root:
		selected = getSelected()
		if selected:
			root = getJointRoot(selected[0])
	if root:
		query = Query(root)
		skeletonNetwork = createSkeletonNetworkNode(name)

		for attribute, attributeData in query.data.items():
			for side, sideList in attributeData.items():
				if sideList:
					attrName = '{}{}{}'.format(attribute[0].lower(),
					                           attribute.replace(' ', '').strip(attribute[0]),
					                           side
					                           )
					cmds.addAttr(skeletonNetwork, ln=attrName, dt='string', m=True)
					for obj in sideList:
						i = sideList.index(obj)
						if not cmds.attributeQuery('skeletonNetwork', node=obj, ex=True):
							cmds.addAttr(obj, ln='skeletonNetwork', at='message')
						cmds.connectAttr('{}.{}[{}]'.format(skeletonNetwork,
						                                    attrName,
						                                    i),
						                 '{}.skeletonNetwork'.format(obj))

	return skeletonNetwork


########################################################################################################################
#
#
#	Templates
#
#
########################################################################################################################


def forceTPose(root):
	"""
	Assumes skeleton is same as default imported skeleton (Axis Direction, Joint Position, Etc..).

	:param root:    Root of the Skeleton to sort through.
	:return:        None
	"""
	children = getAllJointChildren(root)
	if children:
		for child in children:
			childType = ''.join(getJointLabel(child))
			attribute = '{}.jointOrient'.format(child)

			for axis in ['x', 'y', 'z']:
				attr = '{}{}'.format(attribute, axis.upper())
				attrValue = 0

				# Foot Correction
				if 'Foot' in childType:
					if axis == 'y':
						attrValue = cmds.getAttr(attr)

				# Finger Correction
				if 'Finger' in childType:
					cmds.setAttr('{}.ty'.format(child), 0)

				try:
					cmds.setAttr(attr, attrValue)
				except:
					print 'Unable to set {}. Skipped.'.format(attr)

			if childType == 'LeftCollar':
				cmds.setAttr('{}Z'.format(attribute), -90)
			elif childType == 'RightCollar':
				cmds.setAttr('{}X'.format(attribute), -180)
				cmds.setAttr('{}Z'.format(attribute), -90)
			elif 'Spine' in childType:
				spineRoot = getJointRootByLabel(child, label='Spine')
				attribute = '{}.jointOrient'.format(spineRoot)
				cmds.setAttr('{}Z'.format(attribute), 90)
			elif childType == 'LeftHip':
				cmds.setAttr('{}Z'.format(attribute), -90)
			elif childType == 'RightHip':
				cmds.setAttr('{}X'.format(attribute), 180)
				cmds.setAttr('{}Z'.format(attribute), 90)
			elif 'Thumb' in childType:
				thumbRoot = getJointRootByLabel(child, label='Thumb')
				thumbAxis = {
					'x': 90,
					'y': -45,
					'z': 0,
				}

				for axis in thumbAxis:
					cmds.setAttr('{}.jointOrient{}'.format(thumbRoot, axis.upper()), thumbAxis[axis])
					cmds.setAttr('{}.ty'.format(thumbRoot), 0)

	return


@onSelected
def forceTPoseOnSelected(joint):
	root = getJointRoot(joint)
	forceTPose(root)
	return


@onSelected
def mirrorSelectedSkeleton(joint):
	'''
	Uses Namespaces only. Need a better way of mirroring.
	:param joint: Start joint to query from.
	:return:
	'''
	root = getJointRoot(joint)
	joints = getAllJointChildren(root)
	cleanUp = []
	for jnt in joints:
		if 'Left' in jnt:
			op = jnt.replace('Left', 'Right')
			if cmds.objExists(op):
				attributes = getJointAttributes(jnt)
				skip = ['side', 'type', 'radius']

				for axis in ['x', 'y', 'z']:
					value = cmds.getAttr('{}.r{}'.format(jnt, axis))
					cmds.setAttr('{}.r{}'.format(op, axis), value)

				loc = cmds.spaceLocator()
				grp = cmds.group(loc)
				snap(jnt, loc, t=True)
				cmds.setAttr('{}.sx'.format(grp), -1)
				pc = cmds.pointConstraint(loc, op)[0]
				cleanUp.append(grp)
				cleanUp.append(pc)

			else:
				print 'Joint "{}" does not exist. Skipped.'.format(op)
	cmds.delete(cleanUp)
	return


########################################################################################################################
#
#
#	HIK
#
#
########################################################################################################################
'''
HIK Definition File: XML

Notes:
	- Joints have character message attribute -> character node
	- Value is joint in scene
	- Key is HIK Definition
	- When connections are made - HIK updates the joint labels (only while using UI?)

<config_root>
    <match_list>
        <item value="joint" key="Reference"/>
        <item value="" key="Hips"/>
        <item value="" key="Spine"/>
        <item value="" key="Head"/>
        <item value="" key="Neck"/>
    </match_list>
</config_root>
'''


def loadHIKPlugin():
	plugin = 'mayaHIK.mll'
	isLoaded = cmds.pluginInfo(plugin, q=True, l=True)
	isAutoLoaded = cmds.pluginInfo(plugin, q=True, a=True)

	if not isLoaded:
		try:
			cmds.loadPlugin(plugin)
			isLoaded = True
			print 'Plugin "{}" was loaded successfully.'.format(plugin)
		except:
			raise PluginError('Unable to load plugin "{}".'.format(plugin))

	if isLoaded:
		if not isAutoLoaded:
			try:
				cmds.pluginInfo(plugin, e=True, a=True)
			except:
				cmds.warning('Unable to set plugin "{}" to auto load.'.format(plugin))
	return isLoaded


def createHIKCharacter(name='Character'):
	characterNode = cmds.createNode('HIKCharacterNode', n=name)
	propertyNode = cmds.createNode('HIKProperty2State', n='{}Properties'.format(name))
	cmds.connectAttr('{}.message'.format(propertyNode), '{}.propertyState'.format(characterNode))
	return [characterNode, propertyNode]


def addCharacterAttr(selected):
	cmds.addAttr(selected, ln='character', at='message')
	return


########################################################################################################################
#
#
#	Skeleton Class
#
#
########################################################################################################################


class Skeleton(Axml):
	def __init__(self, root=None, filepath=None, kind=SkeletonType.biped):
		'''
		<character>
        	<Spine name="spine_C_0_joint"/>
        		<Neck name="neck_C_0_joint"/>
		</character>

		:param root:
		:param filepath:
		:param kind:
		'''
		Axml.__init__(self, filepath=filepath)

		self.kind = kind
		self.skeletonRoot = root

		if self.skeletonRoot:
			self.buildXMLTree()

	def __repr__(self):
		return self.skeletonRoot

	def write(self, filepath=None, root=None):
		try:
			Axml.write(self, filepath=filepath, root=root)
			print 'Skeleton exported successfully: "{}"'.format(self.filepath),
		except RuntimeError:
			raise RuntimeError('Skeleton Export Failed.')
		return

	def read(self, filepath=None):
		try:
			Axml.read(self, filepath=filepath)
			print 'Skeleton File Read successfully: "{}"'.format(self.filepath)
		except RuntimeError:
			raise RuntimeError('Skeleton Import Failed.')
		return

	def isValid(self):
		if not self.skeletonRoot:
			return False
		else:
			if nodeExists(self.skeletonRoot) and nodeType(self.skeletonRoot) == Component.joint:
				return True
		return False

	def validate(self):
		return

	def buildXMLTree(self, debug=False):
		if not self.isValid():
			raise RuntimeError('No valid Skeleton Root provided.')
		else:
			self.root = 'skeleton'

			if self.kind:
				self.addAttr(element=self.root, name='kind', value=self.kind)

			self.recursiveHierarchyToXML(self.skeletonRoot)
			return

	def recursiveHierarchyToXML(self, joint, **kwargs):
		parent = kwargs.get('parent', self.root)

		# Create Element
		node = Joint(name=joint)
		side = node.side
		kind = node.type
		otherType = node.otherType

		element = self.createElement(parent=parent, name=node.definition)
		self.addAttr(element=element, name='name', value=joint)

		# Add Attributes
		for attr in SKELETON_JOINT_ATTRIBUTES:
			if hasattr(node, attr):
				value = getattr(node, attr)

				if isinstance(value, float):
					value = 0 if 'e-' in str(value) else round(value, 3)
				elif isinstance(value, int):
					value = float(value)

				if value:
					self.addAttr(element=element, name=attr, value=value)

		# Get Children and Loop
		for child in node.children:
			self.recursiveHierarchyToXML(joint=child, parent=element)
		return

	#TODO: Break this method into chucks and update the import process (importing is currently a bit slow.)
	def setupSkeletonRoot(self):
		if not self.skeletonRoot or nodeType(self.skeletonRoot) != 'joint':
			raise RuntimeError('No valid Skeleton Root provided.')
		elif not nodeExists(self.skeletonRoot):
			raise RuntimeError('Skeleton Root does not exist.')
		else:
			dataBase = SkeletonDefinition()

			if not self.kind:
				raise ValueError('No definition provided.')
			elif self.kind not in dataBase:
				raise KeyError('{} is not a valid definition.'.format(self.kind))
			else:
				dataBase = dataBase[self.kind]

				# Add Attributes To Root
				if not attributeExist(self.skeletonRoot, 'skeletonKind'):
					addAttribute(node=self.skeletonRoot,
					             attribute='skeletonKind',
					             kind=MayaAttrType.string,
					             value=self.kind,
					             lock=True,
					             )
				else:
					setAttribute(node=self.skeletonRoot,
					             attribute='skeletonKind',
					             value=self.kind,
					             lock=True,
					             force=True,
					             )

				for attr in ['children', 'joint', 'bind', 'leaf']:
					if not attributeExist(self.skeletonRoot, attr):
						addAttribute(node=self.skeletonRoot, attribute=attr, kind=MayaAttrType.string, lock=True)

				for definition in dataBase:
					if not attributeExist(self.skeletonRoot, definition):
						addAttribute(node=self.skeletonRoot, attribute=definition, kind=MayaAttrType.message)

				# Loop through Children
				children = [Joint(x) for x in getAllJointChildren(self.skeletonRoot)]

				for child in children:
					childName = child.longName

					if child.otherType in ['bind', 'leaf']:
						child.kind = child.otherType
					else:
						child.kind = 'joint'

					for attr in ['parent', 'skeleton']:
						if not attributeExist(childName, attr):
							addAttribute(node=childName, attribute=attr, kind=MayaAttrType.message)

					# Make connections
					connectAttribute(attributeName(self.skeletonRoot, 'children'),
					                 attributeName(childName, 'parent'),
					                 )

					for definition in dataBase:
						if child.definition == definition:
							connectAttribute(attributeName(self.skeletonRoot, definition),
							                 attributeName(childName, 'skeleton')
							                 )
							break

					if not attributeConnected(childName, 'skeleton'):
						if 'bind' in child.definition.lower():
							connectAttribute(attributeName(self.skeletonRoot, 'bind'),
							                 attributeName(childName, 'skeleton')
							                 )

						elif 'leaf' in child.definition.lower():
							connectAttribute(attributeName(self.skeletonRoot, 'leaf'),
							                 attributeName(childName, 'skeleton')
							                 )

						else:
							connectAttribute(attributeName(self.skeletonRoot, 'joint'),
							                 attributeName(childName, 'skeleton')
							                 )

		return

	def buildSkeletonFromXML(self, root=None):
		if not root:
			if self._root is None:
				raise RuntimeError('No Root Element provided specified.')
			else:
				pass
		else:
			self._root = root

		self.kind = self.getAttr(self.root, 'kind')
		elementRoot = self.root.getchildren()[0]
		self.skeletonRoot = self.getAttr(elementRoot, 'name')

		self.recursiveXMLToHierarchy(elementRoot)
		self.setupSkeletonRoot()
		return

	def recursiveXMLToHierarchy(self, element, **kwargs):
		parent = kwargs.get('parent', None)
		name = self.getAttr(element, 'name')
		definition = element.tag
		attributes = element.attrib

		# Create the Joint
		if nodeExists(name):
			name = replacementNodeName(name)

		joint = Joint(name)

		# Hierarchy
		if parent:
			joint.parent = self.getAttr(parent, 'name')

		joint.disableSegmentScale()

		# FIXME: Maybe not a good idea saving label as lowercase - Camelcase workaround
		# Attributes
		for attr in SKELETON_JOINT_ATTRIBUTES:
			if attr in attributes:
				if attr == 'type':
					setattr(joint, attr, camelCase(self.getAttr(element, attr)))
				else:
					setattr(joint, attr, self.getAttr(element, attr))
			else:
				if attr not in ['type', 'side', 'otherType', 'kind']:
					setattr(joint, attr, 0.0)

		# Children
		children = self.getChildren(element)

		if children:
			for child in children:
				self.recursiveXMLToHierarchy(child, parent=element)
		return


def skeletonSetupCallback(kind=SkeletonType.biped, *args, **kwargs):
	selected = getSingleSelected()
	skeleton = Skeleton(root=selected)
	skeleton.setupSkeletonRoot()
	print 'Skeleton Setup successfully.',
	return


def exportSkeletonCallback(debug=False, *args, **kwargs):
	selected = getSingleSelected()
	skeleton = Skeleton(root=selected)

	if debug:
		print skeleton
		return
	else:
		filepath = xfer.mayaFileBrowse(label='Export Skeleton Template',
		                               fileMode=0,
		                               okCaption='Export',
		                               fileFilter="*.xml",
		                               )

		if filepath:
			skeleton.write(filepath=filepath)
	return


def importSkeletonCallback(debug=False, *args, **kwargs):

	filepath = xfer.mayaFileBrowse(label='Import Skeleton Template',
	                               fileMode=1,
	                               okCaption='Import',
	                               fileFilter="*.xml",
	                               )

	if filepath:
		skeleton = Skeleton(filepath=filepath)
		skeleton.read()

		if debug:
			print skeleton
			return
		else:
			skeleton.buildSkeletonFromXML()
			print 'Skeleton Imported Successfully.'

	return


########################################################################################################################
#
#
#	IMPORT / EXPORT TO JSON (LEGACY)
#
#
########################################################################################################################


class createSkeletonFromImport:
	def __init__(self, data):
		self.reparentSkeletonTree(data)
		cmds.select(d=True)

	def reparentSkeletonTree(self, tree, parent=None):
		for root, rootDict in tree.items():
			children = rootDict['children']

			cmds.select(d=True)
			rootJoint = cmds.joint(name=root)

			if parent:
				cmds.parent(root, parent)
			self.setAttributes(rootJoint, rootDict['attributes'])

			if any(children):
				for child, childDict in children.items():
					cmds.select(d=True)
					childJoint = cmds.joint(name=child)
					cmds.parent(childJoint, rootJoint)
					self.setAttributes(childJoint, childDict['attributes'])

					grandChildren = childDict['children']
					if any(grandChildren):
						self.reparentSkeletonTree(grandChildren, childJoint)
		return

	def setAttributes(self, joint, attributeDict):
		for attribute in attributeDict:
			value = attributeDict[attribute]
			if attribute == 'type':
				if value in MAYAJOINTLABELS:
					setJointLabel(joint, typ=value)
				else:
					setJointLabel(joint, typ='Other', otherType=value)
			elif attribute == 'side':
				setJointLabel(joint, side=value)
			else:
				cmds.setAttr('{}.{}'.format(joint, attribute), value)
		return


def importTemplate(debug=False, *args):
	filepath = xfer.mayaFileBrowse(label='Import Skeleton Template',
	                               fileMode=1,
	                               okCaption='Import',
	                               fileFilter="*.json",
	                               )

	if filepath:
		importer = xfer.Import(filepath, isDebug=False)
		data = importer.getData()

		if debug:
			t1 = time.time()
			print 'Skeleton Template Import: Debug Mode {}\n\n'.format('-' * 100)
			print importer.getDebugInfo(), '\n\n'
			print json.dumps(data, indent=1)
			print 'Skeleton Template Import: Completed in {} seconds. {}'.format(time.time() - t1, '-' * 100)
			return
		else:
			createSkeletonFromImport(data)
			return

	else:
		print 'Skeleton Template Export: Canceled.'
		return


def buildSkeletonTree(root, tree={}):
	tree[root] = {
		'attributes': getJointAttributes(root),
		'children'  : {},
	}

	children = getJointChildren(root)
	if children:
		for child in children:
			tree[root]['children'][child] = {
				'children'  : getSkeletonTree(child, {}),
				'attributes': getJointAttributes(child),
			}
	return tree


def exportTemplate(debug=False, *args):
	selected = getSelected()
	if selected:
		selected = selected[0]
		root = getJointRoot(selected)

		if cmds.objectType(root) != 'joint':
			cmds.warning('Skeleton Template Export Failed: Must select a joint hierarchy.')
			return
		else:
			data = buildSkeletonTree(root)
			if data:
				if debug:
					t1 = time.time()
					print 'Skeleton Template Export: Debug Mode {}\n'.format('-' * 100)
					print json.dumps(data, indent=1) if data else 'Data: None'
					print '\nSkeleton Template Export: Completed in {} seconds. {}'.format(time.time() - t1, '-' * 100)
					return
				else:
					filepath = xfer.mayaFileBrowse(label='Export Skeleton Template',
					                               fileMode=0,
					                               okCaption='Export',
					                               fileFilter="*.json",
					                               )

					if filepath:
						xfer.Export(filepath, data=data, isDebug=False)
					else:
						print 'Skeleton Template Export: Canceled.',
			return
