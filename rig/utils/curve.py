# Lancer Modules
from general import *

# Maya Modules
from maya import cmds


def scaleCurve(selected=[], *args):
	curveList = []

	if not selected:
		getSelected()

	if selected:
		for obj in selected:
			shape = cmds.listRelatives(obj, shapes=True)[0]

			if cmds.objectType(shape, isType='nurbsCurve'):
				curveList.append(obj)

		for obj in curveList:
			curveCVs = cmds.ls('{}.cv[:]'.format(obj), fl=True)
			cmds.scale(1.5, 1.5, 1.5, curveCVs, r=True)

		cmds.select(curveList)

	return


def swapShape(par, child):
	snap(par, child)
	parShape = cmds.listRelatives(par, shapes=True)[0]
	childShape = cmds.listRelatives(child, shapes=True)[0]
	cmds.parent(childShape, par, r=True, s=True)
	cmds.delete(child, parShape)
	cmds.rename(childShape, parShape)
	return


def getCurveCVs(curve):
	return cmds.ls('{}.cv[:]'.format(curve), fl=True)


def getCurvePoints(curve):
	pointList = []
	curveCVs = getCurveCVs(curve)
	for cv in curveCVs:
		pointList.append(cmds.xform(cv, q=True, ws=True, t=True))
	return pointList


def makeNurbsCurve(objects, n='curve_#', d=1, *args):
	# 1 == Linear / 3 == Curve
	pointList = []
	for obj in objects:
		if type(obj) == str or type(obj) == unicode:
			var = cmds.xform(obj, q=True, ws=True, rp=True)
		elif type(obj) == list:
			var = obj
		pointList.append(var)
	curve = cmds.curve(n=n, d=d, p=pointList)

	shape = cmds.listRelatives(curve, shapes=True)
	cmds.rename(shape, '{}Shape'.format(curve))

	return curve


def presetWireColor(selected, typ):
	color = [0, 0, 1]

	if typ == Component.fk:
		color = [0, 0, 1]

	elif typ == Component.ik:
		color = [1, 0, 0]

	elif typ == Position.center:
		color = [1, 1, 0]

	elif typ == Component.attr:
		color = [.75, 0, .75]

	elif typ == Component.detail:
		color = [0, .5, 0]

	overrideColor(selected, color=color)
	return


def overrideColor(selected, color=None, reset=False, index=False, *args, **kwargs):
	attrList = ['useObjectColor', 'overrideEnabled', 'overrideRGBColors']

	selected = listCheck(selected)

	if not selected:
		selected = cmds.ls(sl=True)

	if selected:
		for obj in selected:
			shapes = cmds.listRelatives(obj, shapes=True, f=True)

			if shapes:
				for shape in shapes:

					if reset:
						for attr in attrList:
							cmds.setAttr('{0}.{1}'.format(shape, attr), 0)

					else:

						cmds.setAttr('{0}.useObjectColor'.format(shape), 0)
						cmds.setAttr('{0}.overrideEnabled'.format(shape), 1)

						if index:
							if color:

								cmds.setAttr('{0}.overrideRGBColors'.format(shape), 0)
								cmds.setAttr('{0}.overrideColor'.format(shape), color)

							else:
								for attr in attrList:
									cmds.setAttr('{0}.{1}'.format(shape, attr), 0)

						else:
							if color:
								cmds.setAttr('{0}.overrideRGBColors'.format(shape), 1)

								i = 0
								for x in ['R', 'G', 'B']:
									cmds.setAttr('{0}.overrideColor{1}'.format(shape, x), color[i])
									i += 1
	return


def overrideColorFromParent(parent, child, *args, **kwargs):
	override = cmds.getAttr(attributeName(parent, MayaAttr.overrideEnabled))
	rgbOverride = cmds.getAttr(attributeName(parent, MayaAttr.overrideRGBColors))

	if override:
		cmds.setAttr(attributeName(child, MayaAttr.overrideEnabled), True)

		# RGB
		if rgbOverride:
			cmds.setAttr(attributeName(child, MayaAttr.overrideRGBColors), True)

			for hue in ['R', 'G', 'B']:
				value = cmds.getAttr('{}.overrideColor{}'.format(parent, hue))
				cmds.setAttr('{}.overrideColor{}'.format(child, hue), value)
				return True
		# INDEX
		else:
			index = cmds.getAttr(attributeName(parent, MayaAttr.overrideColor))
			cmds.setAttr(attributeName(child, MayaAttr.overrideColor), index)
			return True

	return False


def createCurveInfo(curve):
	node = cmds.createNode('curveInfo', name='{}_curveInfo0'.format(curve))
	shape = cmds.listRelatives(curve, shapes=True)[0]
	cmds.connectAttr('{}.worldSpace[0]'.format(shape), '{}.inputCurve'.format(node))
	return node


def colorIndexList(*args):
	indexColor = []
	indexColor.append([0.35, 0.35, 0.35])

	for x in range(1, 32, 1):
		c = []

		for y in cmds.colorIndex(x, q=True):
			c.append(round(y, 2))

		indexColor.append(c)

	return indexColor


def createCurveOnPivots(items, name='curve', degree=3, *args, **kwargs):
	'''
	Degree
	1 == Linear / 3 == Curve

	:param items:
	:param name:
	:param degree:
	:return:
	'''

	pointList = []
	for item in items:
		if type(item) == str or type(item) == unicode:
			var = cmds.xform(item, q=True, ws=True, rp=True)
		elif type(item) == list:
			var = item
		pointList.append(var)

	curve = cmds.curve(n=name, d=degree, p=pointList)

	shape = cmds.listRelatives(curve, shapes=True)
	cmds.rename(shape, '{}Shape'.format(curve))
	cmds.setAttr('{}.v'.format(curve), 0)
	return curve


def clusterCurve(curve, name='cluster', *args, **kwargs):
	clusterList = []
	curveCVs = cmds.ls('{}.cv[:]'.format(curve), fl=True)
	i = 1
	for cv in curveCVs:
		clusterList.append(cmds.cluster(cv, n='{}_{}'.format(name, i))[1])
		i += 1

	for c in clusterList:
		cmds.setAttr('{}.v'.format(c), 0)

	return clusterList
