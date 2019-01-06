# LANCER.API.UTILS.JOINT
#
#
#
#
#

# Lancer Modules
from general import *
from attribute import *

# Python Modules
import json

# Maya Modules
from maya import cmds, mel

from rig.api.utils import Component, Part


def zeroJointOrient(jnt, *args):
	for axis in ['x', 'y', 'z']:
		try:
			cmds.setAttr('{}.jointOrient{}'.format(jnt, axis.upper()), 0)
		except:
			pass
	return


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


def createJoint(obj=None, n='joint_0', *args):
	cmds.select(d=True)
	jnt = cmds.joint(n=n)

	if obj:
		snap(obj, jnt, t=True, r=True)
		freezeTransform(jnt)

	return jnt


def orientJointChain(*args):
	pass
	return


def getJointHierarchy(*args):
	return cmds.select(hi=True)


def createJointChain(selected=[], typ='bind', world=False, *args):
	selected = listCheck(selected)

	if not selected:
		selected = getSelected()

	if selected:
		jntList = []

		cmds.select(d=True)
		for obj in selected:
			jntName = '{}_{}_jnt'.format(removeJointStr(str(obj)), typ)

			jnt = cmds.joint(n=jntName)
			cmds.setAttr('{}.drawStyle'.format(jnt), 2)

			snap(obj, jnt, t=True, r=True)

			if cmds.objectType(obj, isType='joint'):
				radius = cmds.getAttr('{0}.radius'.format(obj))
				cmds.setAttr('{}.radius'.format(jnt), radius)

			jntList.append(jnt)
			cmds.select(d=True)

		for jnt in jntList:
			i = jntList.index(jnt)
			freezeTransform(jnt)

			if i != 0:
				if not world:
					cmds.parent(jnt, jntList[i - 1])

		return jntList

	else:
		return []


def createBindChain(selected, *args):
	selected = listCheck(selected)
	bindJnt = createJointChain(selected, typ=Component.bind)
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


def sortJointHierarchy(jointList=[], *args):
	newList = []
	root = None

	if len(jointList) > 1:
		for jnt in jointList:
			parent = cmds.listRelatives(jnt, parent=True, type='joint')

			if parent:
				parent = parent[0]

				if parent == None:
					root = jnt
					break

				elif parent not in jointList:
					root = jnt
					break

		newList.append(root)

		children = cmds.listRelatives(root, c=True, type='joint')

		if children:
			for child in children:
				c = cmds.listRelatives(child, ad=True, type='joint')
				if c:
					for j in jointHierarchy(child):
						newList.append(j)

		return newList


	else:
		return jointList


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
		skinCluster = getConnectedObj(jnt, 'objectColorRGB')
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
					'None'  : noneList, 'Left': sortJointHierarchy(leftList),
					'Center': sortJointHierarchy(centerList),
					'Right' : sortJointHierarchy(rightList, )
				}
			else:
				self.masterDict[x] = {
					'None'  : noneList, 'Left': leftList,
					'Center': centerList,
					'Right' : rightList
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


########################################################################################################################
#
#
#	Joint Class
#
#
########################################################################################################################


class Joint(Node):
	def __int__(self, name='joint1'):
		Node.__init__(self, name=name, kind=Component.joint)

	def create(self):
		return
