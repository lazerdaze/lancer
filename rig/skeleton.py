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


def storeBindPose(*args):
	selected = ults.getSelected()
	if selected:
		pass
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


########################################################################################################################
#
#
#	Joint Labels
#
#
########################################################################################################################

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
                        ]


def setJointLabel(joint, side=None, typ=None, otherType=None):
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
	side = cmds.getAttr('{}.side'.format(joint), asString=True)
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


class Query:
	def __init__(self, root=None):
		self.root = root
		self.children = getAllJointChildren(root) if root else None
		self.joints = self.getAllJoints()
		self.data = {}

		if self.joints:
			self.populate()

	def __str__(self):
		return str(json.dumps(self.data, indent=8))

	def getAllJoints(self):
		joints = []
		if self.root:
			joints.append(self.root)
		if self.children:
			joints = joints + self.children
		return joints

	def populate(self):
		dataList = []

		for jointLabel in jointLabelGlobalList:
			leftList = []
			rightList = []
			centerList = []
			noneList = []

			for joint in self.joints:
				label = getJointLabel(joint)
				labelSide = label[0]
				labelType = label[1]

				if labelType == jointLabel:
					if labelSide == 'Left':
						leftList.append(joint)
					elif labelSide == 'Right':
						rightList.append(joint)
					elif labelSide == 'Center':
						centerList.append(joint)
					else:
						noneList.append(joint)

			if jointLabel not in ['None', 'Bind']:
				dataList.append({
					jointLabel: {
						'Left'  : sortJointHierarchy(leftList) if leftList else leftList,
						'Center': sortJointHierarchy(centerList) if centerList else centerList,
						'Right' : sortJointHierarchy(rightList) if rightList else rightList,
					}
				})

		for x in dataList:
			for label, labelData in x.items():
				self.data[label] = labelData

	def get(self, typ, side='center'):
		chain = []

		if typ == ults.componentType.root:
			chain.append(self.data['Root'][side.capitalize()][0])

		elif typ == ults.componentType.cog:
			chain.append(self.data['COG'][side.capitalize()][0])

		elif typ == ults.componentType.hip:
			chain.append(self.data['Hip'][side.capitalize()][0])

		elif typ == ults.componentType.spine:
			chain = self.data['Spine'][side.capitalize()]

		elif typ == ults.componentType.head:
			for x in ['Neck', 'Head']:
				chain.append(self.data[x][side.capitalize()][0])

		elif typ == ults.componentType.arm:
			for x in ['Collar', 'Shoulder', 'Elbow', 'Hand']:
				chain.append(self.data[x][side.capitalize()][0])

		elif typ == ults.componentType.hand:
			for x in ['Thumb', 'Index Finger', 'Middle Finger', 'Ring Finger', 'Pinky Finger']:
				chain.append(self.data[x][side.capitalize()])

		elif typ == ults.componentType.leg:
			for x in ['Hip', 'Knee', 'Foot', 'Toe']:
				chain.append(self.data[x][side.capitalize()][0])

		elif typ == ults.componentType.foot:
			for x in ['Big Toe', 'Index Toe', 'Middle Toe', 'Ring Toe', 'Pinky Toe']:
				chain.append(self.data[x][side.capitalize()][0])

		return chain


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
#	External
#
#
########################################################################################################################


def importTemplate(*args):
	path = 'templates'
	fileName = 'skeleton_biped_T.ma'
	filePath = os.path.join(DIRPATH, path, fileName)
	cmds.file(filePath, i=True)
	return filePath


def exportTemplate(*args):
	selected = ults.getSelected()
	if selected:
		selected = selected[0]
		root = getJointRoot(selected)
		data = getSkeletonTree(root)

		if data:
			filepath = xfer.mayaFileBrowse(label='Export Skeleton Weights',
			                               fileMode=0,
			                               okCaption='Export',
			                               fileFilter="*.json",
			                               )

			if filepath:
				xfer.Export(filepath, data=data, isDebug=False)

	return


########################################################################################################################
#
#
#	Menu
#
#
########################################################################################################################


def menu():
	cmds.menuItem(l='Import Skeleton Template', d=True)
	cmds.menuItem(l='Bi-Ped', c=importTemplate)
	# cmds.menuItem(l='Export Skeleton Template', c=skeleton.exportTemplate)
	cmds.menuItem(d=True)
	cmds.menuItem(l='Select Joint Hierarchy', c=selectJointHierarchy)
	cmds.menuItem(l='Select Bind Joints', c=selectAllBindJoints)
	cmds.menuItem(l='Select Non-Bind Joints', c=selectAllNonBindJoints)
	cmds.menuItem(d=True)
	cmds.menuItem(l='Remove Segment Scale', c=setSegmentScaleCompensate)
	cmds.menuItem(d=True)
	cmds.menuItem(l='Revert Joint To Bind Pose', c=revertJointToBindPose)
	cmds.menuItem(l='Store New Bind Pose', c=storeBindPose, enable=False)
	cmds.menuItem(d=True, l='Joint Labels')
	cmds.menuItem(l='Create Skeleton Network From Labels', c=createSkeletonNetwork)
	cmds.menuItem(d=True, l='Template Only')
	cmds.menuItem(l='Mirror Skeleton Positions', c=mirrorSelectedSkeleton)
	cmds.menuItem(l='Force T-Pose', c=forceTPoseOnSelected)
	return
