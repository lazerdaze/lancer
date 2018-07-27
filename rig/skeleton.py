# LANCER.RIG.SKELETON
#
#
#
#
#

# Lancer Modules
import ults
import library.xfer as xfer
import network

reload(ults)
reload(xfer)
reload(network)

# Maya Modules
import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om

# Python Modules
import os
from math import *
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
#	Utilities
#
#
########################################################################################################################

def onSelected(function):
	def wrapper(*args):
		selected = ults.getSelected()
		if selected:
			for obj in selected:
				return function(obj)
		else:
			return None

	return wrapper


def getJointRoot(joint, child=None):
	parent = cmds.listRelatives(joint, parent=True)
	if parent:
		parent = parent[0]
		return getJointRoot(parent, child=joint)
	else:
		if cmds.objectType(joint) == 'joint':
			return joint
		else:
			return child


def getAllJointChildren(root):
	return cmds.listRelatives(root, ad=True, type='joint')


def getJointChildren(root):
	return cmds.listRelatives(root, c=True, type='joint')


def getAllBindJoints(root):
	joints = []
	children = cmds.listRelatives(root, ad=True, type='joint')
	if children:
		for child in children:
			if getJointLabel(child)[1] == 'Bind':
				joints.append(child)
	return joints if joints else None


def selectJointHierarchy(*args):
	allJoints = []
	selected = ults.getSelected()
	if selected:
		for joint in selected:
			joints = getAllJointChildren(joint) + [joint]
			for jnt in joints:
				allJoints.append(jnt)
	cmds.select(allJoints)
	return allJoints


def selectAllBindJoints(*args):
	allJoints = []
	selected = ults.getSelected()
	if selected:
		for joint in selected:
			joints = getAllBindJoints(joint) + [joint]
			for jnt in joints:
				allJoints.append(jnt)
	cmds.select(allJoints)
	return allJoints


def selectAllNonBindJoints(joint):
	allJoints = []
	selected = ults.getSelected()
	if selected:
		for joint in selected:
			joints = getAllJointChildren(joint)
			bindJoints = getAllBindJoints(joint)
			allJoints += [jnt for jnt in joints if jnt not in bindJoints] + [joint]
	cmds.select(allJoints)
	return allJoints


@onSelected
def setSegmentScaleCompensate(joint):
	root = getJointRoot(joint)
	children = getAllJointChildren(root)
	joints = [root] + children if children else []
	for joint in joints:
		cmds.setAttr('{}.segmentScaleCompensate'.format(joint), 0)
	cmds.select(joints)
	return joints


def getJointAttributes(joint):
	data = {}
	attributes = ['translate', 'rotate', 'jointOrient']
	for attr in attributes:
		for axis in ['x', 'y', 'z']:
			axisStr = '{}{}'.format(attr, axis.upper())
			axisAttr = '{}.{}'.format(joint, axisStr)
			data[axisStr] = cmds.getAttr(axisAttr)

	jointLabel = getJointLabel(joint)
	data['side'] = jointLabel[0]
	data['type'] = jointLabel[1]

	attributes = ['radius']
	for attr in attributes:
		value = cmds.getAttr('{}.{}'.format(joint, attr))
		data[attr] = value

	return data


def getSkeletonTree(root, tree={}):
	children = getJointChildren(root)
	if children:
		for child in children:
			tree[child] = {
				'children'  : getSkeletonTree(child, {}),
				'attributes': getJointAttributes(child),
			}

	return tree


def reparentSkeletonTree(tree, parent=None):
	for root, rootDict in tree.items():
		if parent:
			cmds.parent(root, parent)
		if any(rootDict):
			for child, childDict in rootDict.items():
				cmds.parent(child, root)
				if any(childDict):
					reparentSkeletonTree(childDict, child)
	return


def getJointOrder(root):
	joints = [root]
	children = sortJointHierarchy(getAllJointChildren(root))
	return joints + children


def revertJointToBindPose(*args):
	selected = ults.getSelected()
	if selected:
		conn = cmds.listConnections('{}.bindPose'.format(selected[0]))
		root = getJointRoot(selected[0])
		allJoints = [root] + getAllJointChildren(root)
		jointData = {}

		for joint in allJoints:
			jointData[joint] = getJointAttributes(joint)

		cmds.dagPose(conn, restore=True)

		skip = ['radius', 'type', 'side']

		for joint, jointDict in jointData.items():
			for attr, value in jointDict.items():
				if joint not in selected:
					if attr not in skip:
						cmds.setAttr('{}.{}'.format(joint, attr), value)
	return


def createBindPose(root, name='skeletonPose0'):
	pose = cmds.dagPose(root, name=name, save=True)
	return pose


def restoreBindPose(poseName):
	cmds.dagPose(poseName, restore=True, g=True)
	return


def createBindPosePrompt(*args):
	selected = ults.getSelected()
	if selected:
		root = selected[0]

		if cmds.objectType(root) != 'joint':
			cmds.warning('Create Joint Pose Failed: Must select a joint hierarchy.')
			return
		else:
			result = cmds.promptDialog(
					title='Create Joint Pose'.format(root),
					message='Enter Name:',
					button=['OK', 'Cancel'],
					defaultButton='OK',
					cancelButton='Cancel',
					dismissString='Cancel')

			if result == 'OK':
				name = cmds.promptDialog(query=True, text=True)
				if not name:
					cmds.warning('Create Joint Pose Failed: Must specify a name.')
					return
				else:
					createBindPose(root, name)
			return


def restoreBindPoseUI(poseList):
	cmds.columnLayout(adj=True)
	textVar = cmds.textScrollList(append=poseList)
	cmds.button(l='Select',
	            c=lambda x: cmds.layoutDialog(dismiss=str(cmds.textScrollList(textVar, q=True, si=True)[0])))
	cmds.setParent('..')
	return


def restoreBindPosePrompt():
	selected = ults.getSelected()
	if selected:
		root = selected[0]

		if cmds.objectType(root) != 'joint':
			cmds.warning('Restore Joint Pose Failed: Must select a joint hierarchy.')
			return
		else:
			pose = []
			hasPose = []
			conn = cmds.listConnections('{}.message'.format(root))

			for con in conn:
				if cmds.objectType(con) == 'dagPose':
					hasPose.append(True)
					pose.append(con)
				else:
					hasPose.append(False)

			if not pose or True not in hasPose:
				cmds.warning('Restore Joint Pose Failed: No bind poses found.')
				return
			else:
				if len(pose) > 1:
					pose = cmds.layoutDialog(t='Restore Joint Pose', ui=lambda: restoreBindPoseUI(pose))
				else:
					pose = pose[0]

				restoreBindPose(pose)
			return
	return


def sortJointHierarchy(joints):
	# Find the root
	for joint in joints:
		i = joints.index(joint)
		parent = cmds.listRelatives(joint, parent=True, type='joint')
		parent = parent[0] if parent else None

		if not parent or parent not in joints:
			joints[0], joints[i] = joints[i], joints[0]
			break

	# Sort others in list except root
	for joint in joints:
		i = joints.index(joint)
		if i != 0:
			parent = cmds.listRelatives(joint, parent=True, type='joint')
			parent = parent[0] if parent else None

			if parent and parent in joints:
				parentI = joints.index(parent) + 1
				joints[i], joints[parentI] = joints[parentI], joints[i]

	return joints


def setJointIndex(joint, indexValue=0):
	attrName = 'index'
	query = cmds.attributeQuery(attrName, node=joint, exists=True)
	if not query:
		cmds.addAttr(joint, ln=attrName, at='long')
	cmds.setAttr('{}.{}'.format(joint, attrName), lock=False)
	cmds.setAttr('{}.{}'.format(joint, attrName), indexValue)
	return indexValue


def getJointIndex(joint):
	attrName = 'index'
	indexValue = 0
	query = cmds.attributeQuery(attrName, node=joint, exists=True)
	if not query:
		indexValue = setJointIndex(joint, indexValue)
	else:
		indexValue = cmds.getAttr('{}.{}'.format(joint, attrName))
	return indexValue


def determineHeight(root):
	scale = 1
	posList = []
	children = cmds.listRelatives(root, ad=True)

	if children:
		for child in children:
			if cmds.objectType(child, isType='joint'):
				pos = cmds.xform(child, q=True, ws=True, rp=True)
				posList.append(pos[1])
	if posList:
		scale = int(max(posList))

	return scale


########################################################################################################################
#
#
#	Joint Labels
#
#
########################################################################################################################

MAYAJOINTLABELS = ['None',
                   'Root',
                   'Hip',
                   'Knee',
                   'Foot',
                   'Toe',
                   'Spine',
                   'Neck',
                   'Head',
                   'Collar',
                   'Shoulder',
                   'Elbow',
                   'Hand',
                   'Finger',
                   'Thumb',
                   'PropA',
                   'PropB',
                   'PropC',
                   'Other',
                   'Index Finger',
                   'Middle Finger',
                   'Ring Finger',
                   'Pinky Finger',
                   'Extra Finger'
                   'Big Toe',
                   'Index Toe',
                   'Middle Toe',
                   'Ring Toe',
                   'Pinky Toe',
                   'Foot Thumb',
                   ]

jointLabelGlobalList = ['None',
                        'Root',
                        'Spine',
                        'Neck',
                        'Head',
                        'Collar',
                        'Shoulder',
                        'Elbow',
                        'Hand',
                        'Thumb',
                        'Index Finger',
                        'Middle Finger',
                        'Ring Finger',
                        'Pinky Finger',
                        'Hip',
                        'Knee',
                        'Foot',
                        'Toe',
                        'Big Toe',
                        'Index Toe',
                        'Middle Toe',
                        'Ring Toe',
                        'Pinky Toe',
                        'Other',
                        'Bind',
                        'Limbs'
                        ]

jointLabelLimbGlobalList = ['arms',
                            'legs',
                            'finger',
                            'toe',
                            ]


def setJointLabel(joint, side=None, typ=None, otherType=None):
	if typ == 'Bind':
		otherType = typ
		typ = 'Other'

	if side:
		sideAttr = ults.setEnumByString(joint, 'side', side)

	if typ:
		if typ == 'Other':
			typeAttr = '{}.type'.format(joint)
			cmds.setAttr(typeAttr, 18)
			cmds.setAttr('{}.otherType'.format(joint), otherType, type='string')

		else:
			typeAttr = ults.setEnumByString(joint, 'type', typ)

	return


def getJointLabel(joint):
	side = None
	typ = None

	if cmds.attributeQuery('side', node=joint, exists=True):
		side = cmds.getAttr('{}.side'.format(joint), asString=True)

	if cmds.attributeQuery('type', node=joint, exists=True):
		typ = cmds.getAttr('{}.type'.format(joint), asString=True)

	if typ == 'Other':
		typ = cmds.getAttr('{}.otherType'.format(joint), asString=True)

	return [side, typ]


def getJointRootByLabel(joint, label, child=None):
	parent = cmds.listRelatives(joint, parent=True)
	if parent:
		parent = parent[0]
		parentLabel = getJointLabel(parent)[1]
		if label == parentLabel:
			return getJointRootByLabel(parent, label=label, child=joint)
		else:
			return joint
	else:
		if cmds.objectType(joint) == 'joint':
			return joint
		else:
			return child


def getBindJoint(joint):
	bindJoints = []

	children = cmds.listRelatives(joint, children=True)
	if children:
		i = 0
		for child in children:
			if cmds.objectType(child) == 'joint':
				label = getJointLabel(child)[1]
				if label == 'Bind':

					# Position in chain - Distance

					if i != 0:
						posBefore = ults.getDistance(joint, bindJoints[i - 1])
						posAfter = ults.getDistance(joint, child)

						# Negetive Values

						if posAfter < posBefore:
							bindJoints.insert(i - 1, child)
						else:
							bindJoints.append(child)

					else:
						bindJoints.append(child)

					i += 1

	return bindJoints if bindJoints else None


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
		selected = ults.getSelected()
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
				ults.snap(jnt, loc, t=True)
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


def loadHIKPlugin(plugin='mayaHIK.mll'):
	isLoaded = cmds.pluginInfo(plugin, q=True, l=True)
	isAutoLoaded = cmds.pluginInfo(plugin, q=True, a=True)

	if not isLoaded:
		try:
			cmds.loadPlugin(plugin)
			isLoaded = True
			print 'Plugin "{}" was loaded successfully.'.format(plugin)
		except:
			print 'Unable to load plugin "{}".'.format(plugin)

	# else:
	#	print 'Plugin "{}" is already loaded.'.format(plugin)

	if isLoaded:
		if not isAutoLoaded:
			try:
				cmds.pluginInfo(plugin, e=True, a=True)
			except:
				print 'Unable to set plugin "{}" to auto load.'.format(plugin)
	#	else:
	#		print 'Plugin "{}" is already set to auto load.'.format(plugin)
	return


def createHIKCharacter(name='Character0'):
	loadHIKPlugin()
	characterNode = cmds.createNode('HIKCharacterNode', n=name)
	propertyNode = cmds.createNode('HIKProperty2State', n='{}Properties'.format(name))
	cmds.connectAttr('{}.message'.format(propertyNode), '{}.propertyState'.format(characterNode))
	return [characterNode, propertyNode]


def addCharacterAttr(selected):
	cmds.addAttr(selected, ln='character', at='message')
	return


def defineCharacter():
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
	path = 'templates'
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
	tree[root] = {'attributes': getJointAttributes(root),
	              'children': {},
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
	selected = ults.getSelected()
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


########################################################################################################################
#
#
#	MENU
#
#
########################################################################################################################


def menu():
	cmds.menuItem(l='Select Joint Hierarchy', c=selectJointHierarchy)
	cmds.menuItem(l='Select Bind Joints', c=selectAllBindJoints)
	cmds.menuItem(l='Select Non-Bind Joints', c=selectAllNonBindJoints)
	cmds.menuItem(d=True)
	cmds.menuItem(l='Remove Segment Scale', c=setSegmentScaleCompensate)
	cmds.menuItem(d=True, l='Joint Labels')
	cmds.menuItem(l='Create Skeleton Network From Labels', c=createSkeletonNetwork)
	cmds.menuItem(d=True, l='Joint Pose')
	cmds.menuItem(l='Restore Joint Pose', c=restoreBindPosePrompt)
	cmds.menuItem(l='Create Joint Pose', c=createBindPosePrompt)
	cmds.menuItem(l='Template', d=True)
	cmds.menuItem(l='Import Template', c=importTemplate)
	cmds.menuItem(l='Export Template', c=exportTemplate)
	# cmds.menuItem(d=True)
	# cmds.menuItem(l='Import Biped (Simple)', c=importTemplate)
	# cmds.menuItem(l='Import Biped (Advanced)', c=importTemplate, enable=False)
	# cmds.menuItem(l='Import Quadruped (Simple)', c=importTemplate)
	# cmds.menuItem(l='Import Quadruped (Advanced)', c=importTemplate, enable=False)
	cmds.menuItem(d=True, l='Template Only')
	cmds.menuItem(l='Mirror Skeleton Positions', c=mirrorSelectedSkeleton)
	cmds.menuItem(l='Force T-Pose', c=forceTPoseOnSelected)
	return
