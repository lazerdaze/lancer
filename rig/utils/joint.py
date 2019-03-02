# Lancer Modules
from general import *
from naming import *
from node import *
from customError import *
from attribute import *
from constraint import *

# Python Modules
import json

# Maya Modules
from maya import cmds, mel

'''
Notes:
	- segment scale compensate should be turned off.
	- default rotation order should be xyz.
	- Spline IK solvers require X down the joint chain for Advanced Twist.

	Unreal Engine:
		- doens't care about the rotate orders
		- don't use non-uniform scale between chains (only leaf joints)
		- don't use negative scale
		
	Unity:
		-doesn't support Rotate Axis (per-rotation)
'''

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


def zeroJointOrient(joint, *args, **kwargs):
	if nodeType(joint) != 'joint':
		raise TypeError('Must provide a joint.')

	for axis in ['x', 'y', 'z']:
		setAttribute(node=joint, attribute='jointOrient{}'.format(axis.upper()), value=0, force=True)
	return


@onSelected
def zeroJointOrientSelected(item, *args, **kwargs):
	return zeroJointOrient(item)


class estimateBoundsByJoint:
	def __init__(self, jnt):
		self.verts = []
		self.minX = []
		self.maxX = []
		self.minY = []
		self.maxY = []
		self.minZ = []
		self.maxZ = []

		value = []
		vertDict = {}

		if cmds.objectType(jnt, isType='joint'):
			query = queryJoint(jnt)
			verts = query.verts

			if not verts:
				children = cmds.listRelatives(jnt, children=True, type='joint')
				if children:
					for child in children:
						childVerts = queryJoint(child).verts
						if childVerts:
							verts = childVerts
							break

			if verts:
				for vert in verts:
					pos = cmds.xform(vert, ws=True, q=True, t=True)
					vertDict[str(vert)] = pos

			for axis in range(3):
				minValue = min(vertDict.iterkeys(), key=(lambda key: vertDict[key][axis]))
				maxValue = max(vertDict.iterkeys(), key=(lambda key: vertDict[key][axis]))

				value.append([vertDict[minValue], vertDict[maxValue]])

			self.verts = value
			self.minX = value[0][0]
			self.maxX = value[0][1]
			self.minY = value[1][0]
			self.maxY = value[1][1]
			self.minZ = value[2][0]
			self.maxZ = value[2][1]

		else:
			cmds.warning('Object is not a joint.')

	def __str__(self):
		return str(self.__dict__)


# TODO: Create Joint on selection
# TODO: Add Parent, Skeleton, Kind, Children Attributes | Side, Type, OtherType arguments
def createJoint(obj=None, n='joint_0', *args):
	cmds.select(d=True)
	jnt = cmds.joint(n=n)

	if obj:
		snap(obj, jnt, t=True, r=True)
		freezeTransform(jnt)
	return jnt


# TODO: Add OtherType 'bind'
def createBindJoint(*args, **kwargs):
	return


# TODO: Add OtherType 'leaf'
def createLeafJoint(*args, **kwargs):
	return


def orientJointChain(*args):
	return


def getJointHierarchy(*args):
	return cmds.select(hi=True)


def createBindChain(selected, *args):
	selected = listCheck(selected)
	bindJnt = createJointChain(selected, name=Component.bind)
	for jnt in bindJnt:
		i = bindJnt.index(jnt)
		cmds.parentConstraint(jnt, selected[i], mo=True)
	return bindJnt


def jointHierarchy(root, jointList=[], *args):
	if not jointList:
		jointList = []

	children = cmds.listRelatives(root, c=True, type='joint')

	if children:
		if len(children) == 1:
			if children[0] not in jointList:
				jointList.append(children[0])
				jointHierarchy(children[0], jointList)

		if root not in jointList:
			jointList.insert(0, root)
		return jointList


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


def toggleJointLabel(*args):
	joints = cmds.ls(type='joint')

	drawList = []

	for jnt in joints:
		var = cmds.getAttr('{}.drawLabel'.format(jnt))
		drawList.append(var)

	t = drawList.count(1)
	f = drawList.count(0)

	if f > len(joints) / 2:

		# Show
		mel.eval('displayJointLabels 4;')

	else:
		# Hide
		mel.eval('displayJointLabels 3;')


def handJointHierarchy(root, *args):
	jointList = []
	children = cmds.listRelatives(root, c=True, type='joint')

	if children:
		for child in children:
			c = cmds.listRelatives(child, ad=True, type='joint')
			if c:
				jointList.append(jointHierarchy(child))

	# Sort
	if jointList:
		handsort = ['thumb', 'index', 'middle', 'ring', 'pinky']
		newList = []
		for h in handsort:
			i = handsort.index(h)

			for finger in jointList:
				if any(h in x for x in finger):
					newList.append(finger)

		jointList = newList

	return jointList


class queryJoint():
	def __init__(self, jnt):
		skinCluster = getConnectedNode(jnt, 'objectColorRGB')
		verts = []

		if skinCluster:
			skinInfluences = cmds.skinCluster(skinCluster, q=True, inf=True)

			for influence in skinInfluences:
				if jnt == influence:
					cmds.select(d=True)
					cmds.skinCluster(skinCluster, e=True, selectInfluenceVerts=influence)
					verts = cmds.ls(sl=True, fl=True)
					cmds.select(d=True)

		child = cmds.listRelatives(jnt, c=True, typ='joint')
		parent = cmds.listRelatives(jnt, p=True, typ='joint')

		if child:
			child = child[0]
		else:
			child = None

		if parent:
			parent = parent[0]
		else:
			parent = None

		self.child = child
		self.parent = parent
		self.skinCluster = skinCluster
		self.verts = verts

	def __str__(self):
		return str(self.__dict__)


class jointLabel():
	def __init__(self, joints=[], isDebug=False, *args):

		self.masterDict = {}
		self.masterList = [
			'None',
			'Root',
			'COG',
			'Spine',
			'Neck',
			'Head',
			'Collar',
			'Shoulder',
			'Shoulder Bind',
			'Elbow',
			'Elbow Bind',
			'Hand',
			'Hand Bind',
			'Thumb',
			'Index Finger',
			'Middle Finger',
			'Ring Finger',
			'Pinky Finger',
			'Hip',
			'Hip Bind',
			'Knee',
			'Knee Bind',
			'Foot',
			'Foot Bind',
			'Toe',
			'Big Toe',
			'Index Toe',
			'Middle Toe',
			'Ring Toe',
			'Pinky Toe',
		]
		if joints:
			self.populate(joints)

		if isDebug:
			self.isDebug()

	def get(self, typ, side='center'):
		chain = []

		if typ == Part.root:
			chain.append(self.masterDict['Root'][side.capitalize()][0])

		elif typ == Part.cog:
			chain.append(self.masterDict['COG'][side.capitalize()][0])

		elif typ == Part.hip:
			chain.append(self.masterDict['Hip'][side.capitalize()][0])

		elif typ == Part.spine:
			chain = self.masterDict['Spine'][side.capitalize()]

		elif typ == Part.head:
			for x in ['Neck', 'Head']:
				chain.append(self.masterDict[x][side.capitalize()][0])

		elif typ == Part.arm:
			for x in ['Collar', 'Shoulder', 'Elbow', 'Hand']:
				chain.append(self.masterDict[x][side.capitalize()][0])

		elif typ == Part.hand:
			for x in ['Thumb', 'Index Finger', 'Middle Finger', 'Ring Finger', 'Pinky Finger']:
				chain.append(self.masterDict[x][side.capitalize()])

		elif typ == Part.leg:
			for x in ['Hip', 'Knee', 'Foot', 'Toe']:
				chain.append(self.masterDict[x][side.capitalize()][0])

		elif typ == Part.foot:
			for x in ['Big Toe', 'Index Toe', 'Middle Toe', 'Ring Toe', 'Pinky Toe']:
				chain.append(self.masterDict[x][side.capitalize()][0])

		return chain

	def populate(self, joints, *args):
		joints = listCheck(joints)

		for x in self.masterList:
			leftList = []
			rightList = []
			centerList = []
			noneList = []

			for jnt in joints:

				typ = self.getType(jnt)
				if typ[0] == x:
					if typ[1] == 'Left':
						leftList.append(jnt)
					elif typ[1] == 'Right':
						rightList.append(jnt)
					elif typ[1] == 'Center':
						centerList.append(jnt)
					else:
						noneList.append(jnt)

			if x != 'None':
				self.masterDict[x] = {
					'None': noneList, 'Left': sortJointHierarchy(leftList),
					'Center': sortJointHierarchy(centerList),
					'Right': sortJointHierarchy(rightList, )
				}
			else:
				self.masterDict[x] = {
					'None': noneList, 'Left': leftList,
					'Center': centerList,
					'Right': rightList
				}

	def isDebug(self):
		print(json.dumps(self.masterDict, indent=8))

	def addTypeFromUI(self, index, *args):
		selected = getSelected()

		if selected:
			for obj in selected:
				side = getPositionSide(obj)

				if cmds.objectType(obj, isType='joint'):
					if self.masterList[index - 1] in ['COG', 'Shoulder Bind', 'Elbow Bind', 'Hand Bind', 'Hip Bind',
													  'Knee Bind', 'Foot Bind']:
						setEnumByString(obj, 'type', 'Other')
						cmds.setAttr('{}.otherType'.format(obj), self.masterList[index - 1], type='string')
					else:
						setEnumByString(obj, 'type', self.masterList[index - 1])

					setEnumByString(obj, 'side', side.capitalize())

	def getType(self, obj, *arg):
		side = cmds.getAttr('{}.side'.format(obj), asString=True)
		typ = cmds.getAttr('{}.type'.format(obj), asString=True)

		if typ == 'Other':
			typ = cmds.getAttr('{}.otherType'.format(obj), asString=True)

		return [typ, side]


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
	selected = getSelected()

	for joint in selected:
		allJoints.append(joint)
		children = getAllJointChildren(joint)
		if children:
			for child in children:
				if child not in allJoints:
					allJoints.append(child)
	cmds.select(allJoints)
	return allJoints


def selectAllBindJoints(*args):
	allJoints = []
	selected = getSelected()
	if selected:
		for joint in selected:
			joints = getAllBindJoints(joint) + [joint]
			for jnt in joints:
				allJoints.append(jnt)
	cmds.select(allJoints)
	return allJoints


def selectAllNonBindJoints(joint):
	allJoints = []
	selected = getSelected()
	if selected:
		for joint in selected:
			joints = getAllJointChildren(joint)
			bindJoints = getAllBindJoints(joint)
			allJoints += [jnt for jnt in joints if jnt not in bindJoints] + [joint]
	cmds.select(allJoints)
	return allJoints


@onSelected
def removeSegmentScaleSelected(joint, *args, **kwargs):
	return removeJointSegmentScale(joint)


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
				'children': getSkeletonTree(child, {}),
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
	selected = getSelected()
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
	selected = getSelected()
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
	selected = getSelected()
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
		scale = float(max(posList))

	return scale


def setJointLabel(joint, side=None, typ=None, otherType=None):
	if typ == 'Bind':
		otherType = typ
		typ = 'Other'

	if side:
		sideAttr = setEnumByString(joint, 'side', side)

	if typ:
		if typ == 'Other':
			typeAttr = '{}.type'.format(joint)
			cmds.setAttr(typeAttr, 18)
			cmds.setAttr('{}.otherType'.format(joint), otherType, type='string')

		else:
			typeAttr = setEnumByString(joint, 'type', typ)
	return


def getJointLabelSide(joint):
	return cmds.getAttr(attributeName(joint, MayaAttr.side), asString=True)


def getJointLabelType(joint):
	return cmds.getAttr(attributeName(joint, MayaAttr.type), asString=True)


def getJointLabelOtherType(joint):
	return cmds.getAttr(attributeName(joint, MayaAttr.otherType), asString=True)


def setJointLabelSide(joint, side):
	if isinstance(side, str):
		side = side.lower()

		if hasattr(JointLabelSide, side):
			cmds.setAttr(attributeName(joint, MayaAttr.side), getattr(JointLabelSide, side))
		else:
			raise ValueError('Joint does not have side "{}".'.format(side))
	elif isinstance(side, int):
		cmds.setAttr(attributeName(joint, MayaAttr.side), side)
	else:
		raise TypeError('Side must be int or str.')
	return


def setJointLabelType(joint, kind):
	if isinstance(kind, str):
		if hasattr(JointLabelSide, kind):
			cmds.setAttr(attributeName(joint, MayaAttr.type), getattr(JointLabelType, kind))
		else:
			raise ValueError('Joint does not have type "{}".'.format(kind))

	elif isinstance(kind, int):
		cmds.setAttr(attributeName(joint, MayaAttr.type), kind)
	else:
		raise TypeError('Type must be int or str.')
	return


def setJointLabelOtherType(joint, kind):
	if isinstance(kind, str):
		cmds.setAttr(attributeName(joint, MayaAttr.type), JointLabelType.other)
		cmds.setAttr(attributeName(joint, MayaAttr.otherType), kind, type=MayaAttrType.string)
	else:
		raise TypeError('Type must be str.')
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


def getBindJointLegacy(joint):
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
						posBefore = getDistance(joint, bindJoints[i - 1])
						posAfter = getDistance(joint, child)

						# Negetive Values

						if posAfter < posBefore:
							bindJoints.insert(i - 1, child)
						else:
							bindJoints.append(child)

					else:
						bindJoints.append(child)

					i += 1

	return bindJoints if bindJoints else None


def getBindJoint(joint):
	bindJoints = []
	bindDict = {}

	children = cmds.listRelatives(joint, children=True)
	if children:
		for child in children:
			if cmds.objectType(child) == 'joint':
				label = getJointLabel(child)[1]
				if label == JointLabelOtherType.bind:
					bindDict[child] = getDistance(joint, child)

	for key, value in sorted(bindDict.iteritems(), key=lambda (k, v): (v, k)):
		bindJoints.append(key)

	return bindJoints if bindJoints else None


def getJointChainByLabel(joint, label):
	chain = [joint]
	chainDict = {}

	children = cmds.listRelatives(joint, ad=True, type='joint')
	if children:
		for child in children:
			childLabel = getJointLabel(child)[1]
			if childLabel == label:
				chainDict[child] = getDistance(joint, child)

	for key, value in sorted(chainDict.iteritems(), key=lambda (k, v): (v, k)):
		chain.append(key)

	return chain if chain else None


def createJointChain(objects, name=Component.joint):
	jointList = []
	cmds.select(d=True)

	for obj in objects:
		jntName = '{}_{}'.format(removeJointStr(str(obj)), name)
		jnt = cmds.joint(n=jntName)
		cmds.setAttr('{}.drawStyle'.format(jnt), 2)

		snap(obj, jnt, t=True, r=True)

		if cmds.objectType(obj, isType='joint'):
			radius = cmds.getAttr('{0}.radius'.format(obj))
			cmds.setAttr('{}.radius'.format(jnt), radius)

		jointList.append(jnt)
		cmds.select(d=True)

	for jnt in jointList:

		i = jointList.index(jnt)
		freezeTransform(jnt)

		if i != 0:
			cmds.parent(jnt, jointList[i - 1])

	return jointList


def removeJointSegmentScale(joint):
	if nodeType(joint) != 'joint':
		raise TypeError('Must provide a joint.')

	setAttribute(joint, 'segmentScaleCompensate', 0)

	destination = '{}.inverseScale'.format(joint)
	if cmds.connectionInfo(destination, isDestination=True):
		source = cmds.connectionInfo('{}.inverseScale'.format(joint), sourceFromDestination=True)
		cmds.disconnectAttr(source, destination)
		return True
	return False


def repositionMiddleJoint(*args, **kwargs):
	if len(args) != 3:
		raise ValueError('Must provide 3 objects')
	else:
		cmds.delete(cmds.pointConstraint(args))
	return


def repositionMiddleJointSelected(*args, **kwargs):
	selected = getSelected()
	repositionMiddleJoint(selected[0], selected[1], selected[2])
	return


def mirrorJoint(joint, *args, **kwargs):
	if nodeType(joint) != 'joint':
		raise TypeError('Must Provide a joint.')

	# Query Joint Name
	source = None
	destination = None

	data = {
		'left': 'right',
		'Left': 'Right',
		'_l_': '_r_',
		'_L_': '_R_',
	}

	for x in data:
		if x in joint:
			source = x
			destination = data[x]
			break
		elif data[x] in joint:
			source = data[x]
			destination = x
			break

	# Run Mirror Function
	if source and destination:
		mirrored = cmds.mirrorJoint(joint, mirrorYZ=True, mirrorBehavior=True, searchReplace=[source, destination])
	else:
		mirrored = cmds.mirrorJoint(joint, mirrorYZ=True, mirrorBehavior=True)

	# Get and Set Side Joint Label
	sourceSide = getJointLabelSide(joint).lower()
	destinationSide = None

	if sourceSide == 'left':
		destinationSide = JointLabelSide.right
	elif sourceSide == 'right':
		destinationSide = JointLabelSide.left

	if destinationSide:
		for item in mirrored:
			setJointLabelSide(item, destinationSide)
	return mirrored


@onSelected
def mirrorJointSelected(joint, *args, **kwargs):
	return mirrorJoint(joint)


def aimAtObject(*args, **kwargs):
	if len(args) != 2:
		raise ValueError('Must provide 2 objects.')
	else:
		parent = args[0]
		child = args[1]

		reparent = False

		if child == nodeParent(parent):
			cmds.parent(parent, world=True)
			reparent = True

		cmds.delete(cmds.aimConstraint(parent,
									   child,
									   aimVector=[1, 0, 0],
									   upVector=[0, 1, 0],
									   worldUpType='none',
									   worldUpVector=[0, 1, 0],
									   )
					)
		freezeTransform(args[1])

		if reparent:
			cmds.parent(parent, child)
	return


def aimAtSelected(*args, **kwargs):
	selected = getSelected()
	aimAtObject(selected[0], selected[1])
	return


########################################################################################################################
#
#
#	Joint Class
#
#
########################################################################################################################

class Joint(DagNode):
	def __init__(self,
				 prefix=None,
				 side=None,
				 name='rigJoint',
				 sector=None,
				 index=None,
				 kind=Component.joint,
				 parent=None,
				 radius=1.0,
				 drawStyle=JointDrawStyle.bone,
				 type=None,
				 otherType=None,
				 color=None,
				 *args,
				 **kwargs
				 ):

		DagNode.__init__(self,
						 name=name,
						 prefix=prefix,
						 parent=parent,
						 color=color,
						 index=index,
						 sector=sector,
						 kind=kind,
						 side=side,
						 *args,
						 **kwargs,
						 )

		'''
		Base Joint class to be used in all parts classes.

		:param float radius:    Joint radius scale.
		:param enum drawStyle:  Joint draw style visibility.
		:param enum type:       Label type.
		:param str otherType:   Label other type.
		'''

		# Joint Attributes
		self.forwardAxis = None
		self.upAxis = None

		if not self.wrapper:
			self.radius = radius
			self.drawStyle = drawStyle
			self.type = type
			self.otherType = otherType


	def create(self, *args, **kwargs):
		cmds.select(d=True)
		self.transform = cmds.joint(name=self.longName)
		self.disableSegmentScale()
		return

	@property
	def definition(self):
		if self.otherType in ['bind', 'leaf']:
			if self.side == 'none':
				return camelCase(self.otherType)
			else:
				return camelCase(self.side, self.otherType)
		else:
			if self.side == 'center':
				if self.type == 'other':
					return camelCase(self.otherType)
				else:
					return camelCase(self.type)
			elif self.side in ['left', 'right']:
				if self.type == 'other':
					return camelCase(self.side, self.otherType)
				else:
					return camelCase(self.side, self.type)
			else:
				if self.type == 'other':
					if self.otherType:
						return camelCase(self.otherType)
				else:
					return camelCase(self.type)
		return 'Joint'

	####################################################################################################################
	# Joint Orient Properties
	####################################################################################################################
	@property
	def jointOrient(self):
		if self.isValid():
			return [self.jointOrientX, self.jointOrientY, self.jointOrientZ]
		else:
			return [0.0, 0.0, 0.0]

	@jointOrient.setter
	def jointOrient(self, *args):
		if self.isValid():
			if len(args) == 1:
				if isinstance(args[0], (list, dict, tuple)) and len(args[0]) == 3:
					self.jointOrientX = args[0][0]
					self.jointOrientY = args[0][1]
					self.jointOrientZ = args[0][2]
				else:
					raise ValueError('Must provide "XYZ" values in a list, dict, or tuple.')
			elif len(args) == 3:
				self.jointOrientX = args[0]
				self.jointOrientY = args[1]
				self.jointOrientZ = args[2]
			else:
				raise ValueError('Must provide 3 values for "XYZ".')
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def jointOrientX(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.jointOrientX))
		else:
			return 0.0

	@jointOrientX.setter
	def jointOrientX(self, value):
		if self.isValid():
			setAttribute(self.longName, attribute=MayaAttr.jointOrientX, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def jointOrientY(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.jointOrientY))
		else:
			return 0.0

	@jointOrientY.setter
	def jointOrientY(self, value):
		if self.isValid():
			setAttribute(self.longName, attribute=MayaAttr.jointOrientY, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def jointOrientZ(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.jointOrientZ))
		else:
			return 0.0

	@jointOrientZ.setter
	def jointOrientZ(self, value):
		if self.isValid():
			setAttribute(self.longName, attribute=MayaAttr.jointOrientZ, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	####################################################################################################################
	# Joint Properties
	####################################################################################################################
	@property
	def radius(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.radius))
		return None

	@radius.setter
	def radius(self, radius):
		if self.isValid():
			if isinstance(radius, (int, float)):
				setAttribute(self.longName, attribute=MayaAttr.radius, value=radius)
			else:
				raise TypeError('Radius must be numeric value.')
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def drawStyle(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.drawStyle), asString=True)
		return None

	@drawStyle.setter
	def drawStyle(self, drawStyle):
		if self.isValid():
			if isinstance(drawStyle, str):
				if hasattr(JointDrawStyle, drawStyle):
					value = getattr(JointDrawStyle, drawStyle)
				else:
					raise ValueError('Draw style "{}" not valid.'.format(drawStyle))

			elif isinstance(drawStyle, (int, float)):
				value = drawStyle

			elif drawStyle is None:
				value = ''

			else:
				raise ValueError('Draw style "{}" not valid type: {}'.format(drawStyle, type(drawStyle)))

			setAttribute(self.longName, attribute=MayaAttr.drawStyle, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def type(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.type), asString=True).lower()
		return None

	@type.setter
	def type(self, typeValue):
		if self.isValid():
			if isinstance(typeValue, str):
				if hasattr(JointLabelType, typeValue):
					value = getattr(JointLabelType, typeValue)
				else:
					raise ValueError('Type "{}" not valid.'.format(typeValue))

			elif isinstance(typeValue, (int, float)):
				value = typeValue

			elif typeValue is None:
				value = JointLabelType.none
			else:
				raise ValueError('Type "{}" not valid type: {}'.format(typeValue, type(typeValue)))

			setAttribute(self.longName, attribute=MayaAttr.type, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	@property
	def otherType(self):
		if self.isValid():
			return cmds.getAttr(attributeName(self.longName, MayaAttr.otherType))
		return None

	@otherType.setter
	def otherType(self, otherType):
		if self.isValid():
			if isinstance(otherType, str):
				value = otherType
				self.type = JointLabelType.other
			elif otherType is None:
				value = ''
			else:
				raise ValueError('Other type "{}" not valid. Must be str or None.'.format(otherType))

			setAttribute(self.longName, attribute=MayaAttr.otherType, value=value, force=True)
		else:
			raise NodeExistsError('{} "{}" is not a valid object.'.format(self.__class__.__name__, self.longName))
		return

	####################################################################################################################
	# Joint Methods
	####################################################################################################################
	def disableSegmentScale(self):
		if self.isValid():
			removeJointSegmentScale(self.longName)
		return

	def zeroOrient(self):
		self.jointOrient = [0.0, 0.0, 0.0]
		return
