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


DIRPATH = os.path.dirname(os.path.abspath(__file__))


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
			print item
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
		result += cmds.listConnections(attributeName(root, kind))

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


class HIKPart(object):
	cog = 'Reference'
	hip = 'Hips'
	spine = 'Spine'
	neck = 'Neck'
	head = 'Head'

	leftCollar = 'LeftShoulder'
	leftArm = 'LeftArm'
	leftFoot = 'LeftFoot'
	leftToe = 'LeftToeBase'
	leftElbow = 'LeftForeArm'
	leftHand = 'LeftHand'
	leftThumb = 'LeftHandThumb'

	leftIndexFingerBase = 'LeftInHandIndex'
	leftIndexFinger = 'LeftHandIndex'
	leftMiddleFingerBase = 'LeftInHandMiddle'
	leftMiddleFinger = 'LeftHandMiddle'
	leftRingFingerBase = 'LeftInHandRing'
	leftRingFinger = 'LeftHandRing'
	leftPinkyFingerBase = 'LeftInHandPinky'
	leftPinkyFinger = 'LeftHandPinky'

	leftLeg = 'LeftLeg'
	leftHip = 'LeftUpLeg'

	rightCollar = 'RightShoulder'
	rightArm = 'RightArm'
	rightFoot = 'RightFoot'
	rightToe = 'RightToeBase'
	rightElbow = 'RightForeArm'
	rightHand = 'RightHand'
	rightThumb = 'RightHandThumb'

	rightIndexFingerBase = 'RightInHandIndex'
	rightIndexFinger = 'RightHandIndex'
	rightMiddleFingerBase = 'RightInHandMiddle'
	rightMiddleFinger = 'RightHandMiddle'
	rightRingFingerBase = 'RightInHandRing'
	rightRingFinger = 'RightHandRing'
	rightPinkyFingerBase = 'RightInHandPinky'
	rightPinkyFinger = 'RightHandPinky'

	rightLeg = 'RightLeg'
	rightHip = 'RightUpLeg'


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
#	Character Class
#
#
########################################################################################################################


CHARACTER_JOINT_HANDLER = [
	'translateX',
	'translateY',
	'translateZ',
	'jointOrientY',
	'jointOrientX',
	'jointOrientZ',
	'rotateX',
	'rotateY',
	'rotateZ',
	'scaleX',
	'scaleY',
	'scaleZ',
	'radius',
	'type',
	'side',
	'otherType',
]


# TODO: Run Validator On Hierarchy: If there's warnings then skeleton is invalid.
class Character(Axml):
	def __init__(self, name='Character', root=None, filepath=None):
		'''
		<character>
        	<Spine name="spine_C_0_joint"/>
        		<Neck name="neck_C_0_joint"/>
		</character>


		:param name:
		:param root:
		:param filepath:
		'''
		Axml.__init__(self, filepath=filepath)

		self._name = name
		self.skeletonRoot = root

	def __repr__(self):
		return self._name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		if nodeExists(name):
			raise NodeExistsError('Character "{}" already exists.'.format(name))
		else:
			cmds.rename(self._name, name)
			self._name = name
		return

	def isValid(self):
		if not self.skeletonRoot:
			return False
		else:
			if nodeExists(self.skeletonRoot) and nodeType(self.skeletonRoot) == Component.joint:
				return True
		return False

	def buildTree(self, debug=False):
		if not self.isValid():
			raise RuntimeError('No valid Skeleton Root provided.')
		else:
			self.root = Component.character
			self.recursiveBuildJointTree(self.skeletonRoot)

			if debug:
				print self
			return

	def recursiveBuildJointTree(self, joint, **kwargs):
		parent = kwargs.get('parent', self.root)

		# Create Element
		node = Joint(name=joint)
		element = self.createElement(parent=parent, name=Component.joint)

		# Add Attributes
		for attr in CHARACTER_JOINT_HANDLER:
			if hasattr(node, attr):
				self.addAttr(element=element, name=attr, value=getattr(node, attr))

		# Get Children and Loop
		for child in node.children:
			self.recursiveBuildJointTree(joint=child, parent=element)

		return


########################################################################################################################
#
#
#	IMPORT
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


def importTemplateLegacy(*args):
	path = 'workfiles'
	fileName = 'skeleton_biped_T.ma'
	filePath = os.path.join(DIRPATH, path, fileName)
	cmds.file(filePath, i=True)
	return filePath


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


########################################################################################################################
#
#
#	EXPORT
#
#
########################################################################################################################


def buildSkeletonTree(root, tree={}):
	tree[root] = {
		'attributes': getJointAttributes(root),
		'children': {},
	}

	children = getJointChildren(root)
	if children:
		for child in children:
			tree[root]['children'][child] = {
				'children': getSkeletonTree(child, {}),
				'attributes': getJointAttributes(child),
			}
	return tree


# FIXME: Doesn't work properly. Need to update with Recursive solution.
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
