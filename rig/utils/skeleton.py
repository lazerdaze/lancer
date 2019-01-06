# Lancer Modules
import library.xfer as xfer
from joint import *

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
