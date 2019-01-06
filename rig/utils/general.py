# Lancer Modules

# Python Modules
from math import *

# Maya Modules
from maya import cmds
import maya.api.OpenMaya as om


########################################################################################################################
#
#
#	Functions
#
#
########################################################################################################################


def selected():
	return cmds.ls(sl=True)


def getSelected(*args):
	selected = cmds.ls(sl=True)

	if not selected:
		cmds.warning('Nothing selected.')

	return selected


def getChild(root, typ='joint', *args):
	child = cmds.listRelatives(root, c=True, type=typ)
	if len(child) == 1:
		return child[0]


def listCheck(var, *args):
	if type(var) is str or type(var) is unicode:
		var = [str(var)]
	return var


def freezeTransform(obj, t=True, r=True, s=True):
	if t:
		cmds.makeIdentity(obj, apply=True, t=True)
	if r:
		cmds.makeIdentity(obj, apply=True, r=True)
	if s:
		cmds.makeIdentity(obj, apply=True, s=True)
	return


def forwardAxis(obj, axis=[0, 0, 0], *args):
	x = axis[0] * 90
	y = axis[1] * 90
	z = axis[2] * 90
	var = [z, y, x]
	cmds.xform(obj, ro=var)
	freezeTransform(obj)
	return


def snap(par, child, t=False, r=False):
	parPosition = cmds.xform(par, q=True, ws=True, rp=True)
	parRotation = cmds.xform(par, q=True, ws=True, ro=True)

	if t:
		cmds.xform(child, t=parPosition, ws=True)
	if r:
		cmds.xform(child, ro=parRotation, ws=True)
	return


def createGroup(obj, n='grp'):
	grp = cmds.group(n=n, em=True)
	snap(obj, grp, t=True, r=True)
	par = cmds.listRelatives(obj, parent=True)

	if par:
		par = par[0]
		cmds.parent(grp, par)

	cmds.parent(obj, grp)

	return grp


def getPositionSide(obj, *args):
	if type(obj) is list:
		position = cmds.xform(obj[0], q=True, ws=True, rp=True)[0]

	else:
		position = cmds.xform(obj, q=True, ws=True, rp=True)[0]

	if 'e' in str(position):
		return Position.center

	else:

		if position > 0:
			return Position.left

		elif position < 0:
			return Position.right

		elif position == 0:
			if type(obj) is list:
				if len(obj) > 1:
					obj.remove(obj[0])
					newObj = []
					for o in obj:
						newObj.append(o)
					getPositionSide(newObj)
				else:
					return Position.center
			else:
				return Position.center


def getSide(obj):
	if type(obj) is list:
		position = cmds.xform(obj[0], q=True, ws=True, rp=True)[0]

	else:
		position = cmds.xform(obj, q=True, ws=True, rp=True)[0]

	if 'e' in str(position):
		return Position.center

	else:
		if position > 0:
			return Position.left

		elif position < 0:
			return Position.right

		elif position == 0:
			if type(obj) is list:
				if len(obj) > 1:
					obj.remove(obj[0])
					newObj = []
					for o in obj:
						newObj.append(o)
					getPositionSide(newObj)
				else:
					return Position.center
			else:
				return Position.center


def getParentByType(obj, typ='nurbsCurve', *args):
	par = cmds.listRelatives(obj, p=True, type='transform')

	if par:
		shape = cmds.listRelatives(par, shapes=True)[0]

		if cmds.objectType(shape) == typ:
			return par[0]

		else:
			par = getParentByType(par[0], typ)

	else:
		return None


def getDistance(start, end):
	if type(start) is list:
		startPos = start
	else:
		startPos = cmds.xform(start, q=True, ws=True, rp=True)

	if type(end) is list:
		endPos = end
	else:
		endPos = cmds.xform(end, q=True, ws=True, rp=True)
	distance = sqrt(
			pow((startPos[0] - endPos[0]), 2) + pow((startPos[1] - endPos[1]), 2) + pow((startPos[2] - endPos[2]), 2))
	return distance


def moveRotatePivot(parent, child):
	if type(parent) is list:
		cmds.xform(child, ws=True, rp=parent)
	else:
		pos = cmds.xform(parent, q=True, ws=True, rp=True)
		cmds.xform(child, ws=True, rp=pos)
	return

def getLocalVecToWorldSpace(node, vec=om.MVector.kXaxisVector):
	matrix = om.MGlobal.getSelectionListByName(node).getDagPath(0).inclusiveMatrix()
	vec = (vec * matrix).normal()
	return vec


def axisVectorColinearity(node, vec):
	vec = om.MVector(vec)
	x = getLocalVecToWorldSpace(node, vec=om.MVector.kXaxisVector)
	y = getLocalVecToWorldSpace(node, vec=om.MVector.kYaxisVector)
	z = getLocalVecToWorldSpace(node, vec=om.MVector.kZaxisVector)
	return {'x': vec * x, 'y': vec * y, 'z': vec * z}


def getClosestAxisToWorld(node, axis='z'):
	if axis == 'x':
		axis = [1, 0, 0]
	elif axis == 'y':
		axis = [0, 1, 0]
	elif axis == 'z':
		axis = [0, 0, 1]
	var = axisVectorColinearity(node, axis)
	return max(var.iterkeys(), key=(lambda key: var[key]))


def getPoleVectorPosition(start, mid, end):
	start = cmds.xform(start, q=True, ws=True, t=True)
	mid = cmds.xform(mid, q=True, ws=True, t=True)
	end = cmds.xform(end, q=True, ws=True, t=True)

	startVec = om.MVector(start[0], start[1], start[2])
	midVec = om.MVector(mid[0], mid[1], mid[2])
	endVec = om.MVector(end[0], end[1], end[2])

	line = (endVec - startVec)
	point = (midVec - startVec)

	scaleVar = (line * point) / (line * line)
	projVec = line * scaleVar + startVec

	startToMid = (midVec - startVec).length()
	midToEnd = (endVec - midVec).length()
	total = startToMid + midToEnd

	poleVecPos = (midVec - projVec).normal() * total + midVec

	return poleVecPos


def createDistanceNode(start, end, n='distanceBetween1', *args):
	node = cmds.createNode('distanceBetween', n=n)

	i = 1
	for x in [start, end]:
		cmds.connectAttr('{}.worldMatrix[0]'.format(x), '{}.inMatrix{}'.format(node, i), f=True)
		cmds.connectAttr('{}.rotatePivotTranslate'.format(x), '{}.point{}'.format(node, i), f=True)
		i += 1

	distance = cmds.getAttr('{}.distance'.format(node))

	return [node, distance]