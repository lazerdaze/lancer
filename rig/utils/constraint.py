# Lancer Modules
from general import *
from naming import *
from attribute import *

# Maya Modules
from maya import cmds


def constraint(*args, **kwargs):
	kwargs['offset'] = kwargs.get('offset', False)
	offset = kwargs['offset']
	return [parentConstraint(args, offset=offset), scaleConstraint(args, offset=offset)]


def parentConstraint(*args, **kwargs):
	kwargs['offset'] = kwargs.get('offset', False)
	offset = kwargs['offset']
	return cmds.parentConstraint(args, mo=offset)


def pointConstraint(*args, **kwargs):
	kwargs['offset'] = kwargs.get('offset', False)
	offset = kwargs['offset']
	return cmds.pointConstraint(args, mo=offset)


def orientConstraint(*args, **kwargs):
	kwargs['offset'] = kwargs.get('offset', False)
	offset = kwargs['offset']
	return cmds.orientConstraint(args, mo=offset)


def scaleConstraint(*args, **kwargs):
	kwargs['offset'] = kwargs.get('offset', False)
	offset = kwargs['offset']
	return cmds.scaleConstraint(args, mo=offset)


def aimConstraint(*args, **kwargs):
	kwargs['offset'] = kwargs.get('offset', False)
	offset = kwargs['offset']
	return cmds.aimConstraint(args, mo=offset)


def poleVectorConstraint(*args, **kwargs):
	kwargs['offset'] = kwargs.get('offset', False)
	offset = kwargs['offset']
	return


def localWorldConstraint(obj, local, world, n='localWorld', t=False, r=True):
	name = '{}_{}'.format(obj, n)

	if cmds.objExists(name):
		name = '{}0'.format(name)

	null = createGroup(obj, n=name)

	cmds.addAttr(obj, ln=n, min=0, max=1, dv=1, k=True)

	if t and r:
		pc = cmds.parentConstraint(local, world, null, mo=True)[0]
		pcAttr = cmds.parentConstraint(pc, q=True, wal=True)

	elif t and not r:
		pc = cmds.parentConstraint(local, world, null, sr=['x', 'y', 'z'], mo=True)[0]
		pcAttr = cmds.parentConstraint(pc, q=True, wal=True)

	elif r and not t:
		pc = cmds.parentConstraint(local, world, null, st=['x', 'y', 'z'], mo=True)[0]
		pcAttr = cmds.parentConstraint(pc, q=True, wal=True)

	cmds.connectAttr('{}.{}'.format(obj, n), '{}.{}'.format(pc, pcAttr[-1]))

	reverse = cmds.createNode('reverse', name='{}_re0'.format(name))
	cmds.connectAttr('{}.{}'.format(obj, n), '{}.inputX'.format(reverse))
	cmds.connectAttr('{}.outputX'.format(reverse), '{}.{}'.format(pc, pcAttr[0]))

	return [null, pc]


def clusterCurve(curve, n='cluster', *args):
	clusterList = []
	curveCVs = cmds.ls('{0}.cv[:]'.format(curve), fl=True)
	i = 1
	for cv in curveCVs:
		clusterList.append(cmds.cluster(cv, n='{0}_{1}'.format(n, i))[1])
		i += 1

	for c in clusterList:
		cmds.setAttr('{}.v'.format(c), 0)

	return clusterList


def setOnMotionPath(selected, curve, name='motionPath', uValue=0, *args):
	# Create Nodes
	mp = cmds.createNode('motionPath', n='{}_mp'.format(name))

	mpAttr = {
		'follow'      : 1,
		'fractionMode': 0,
		'worldUpType' : 3,
		'frontAxis'   : 2,
		'upAxis'      : 1,
	}
	for attr in mpAttr:
		cmds.setAttr('{}.{}'.format(mp, attr), mpAttr[attr])

	add = []
	for x in range(3):
		a = cmds.createNode('addDoubleLinear', n='{}_add{}'.format(name, x))
		add.append(a)

	# Make Connections
	cmds.connectAttr('{}.worldSpace[0]'.format(curve), '{}.geometryPath'.format(mp), f=True)
	cmds.connectAttr('{}.rotateOrder'.format(mp), '{}.rotateOrder'.format(selected), f=True)

	i = 0
	for axis in ['x', 'y', 'z']:
		cmds.connectAttr('{}.{}Coordinate'.format(mp, axis), '{}.input2'.format(add[i]), f=True)
		cmds.connectAttr('{}.output'.format(add[i]), '{}.t{}'.format(selected, axis), f=True)
		cmds.connectAttr('{}.r{}'.format(mp, axis), '{}.r{}'.format(selected, axis), f=True)
		cmds.connectAttr('{}.transMinusRotatePivot{}'.format(selected, axis.upper()), '{}.input1'.format(add[i]))
		i += 1

	cmds.setAttr('{0}.uValue'.format(mp), uValue)

	return mp


def locOnCurve(curve, intLoc=1, n='locator', upObject='', start=False, end=False, *args):
	locList = []
	curveLength = cmds.getAttr('{0}.maxValue'.format(curve))
	step = curveLength / float(intLoc - 1) if end else curveLength / float(intLoc + 1)
	distance = 0 if start else step

	i = 1
	for loc in range(intLoc):
		# loc = cmds.spaceLocator(n='{0}_{1}'.format(n, i))[0]
		loc = cmds.group(n='{0}_{1}'.format(n, i), em=True)
		mp = setOnMotionPath(selected=loc, name='{}_motionPath'.format(loc), curve=curve, uValue=distance)
		if upObject:
			cmds.pathAnimation(mp, e=True, wut='objectRotation', wuo=upObject)
		distance += step
		i += 1
		locList.append(loc)

	return locList


def createAimVectorHelper(start, end, name='poleVector_helper'):
	# Create Curve
	curve = cmds.curve(n=name, d=1, p=[[0, 0, 0], [0, 0, 0]])
	curveShape = cmds.rename(cmds.listRelatives(curve, shapes=True)[0],
	                         '{}Shape'.format(name))
	cmds.parent(curveShape, end, r=True, s=True)
	cmds.delete(curve)

	# Create Nodes
	mult = cmds.createNode('multMatrix', name='{}_multMatrix0'.format(name))
	dec = cmds.createNode('decomposeMatrix', name='{}_decomposeMatrix0'.format(name))

	# Create Connections
	cmds.connectAttr('{}.worldMatrix[0]'.format(start), '{}.matrixIn[0]'.format(mult))
	cmds.connectAttr('{}.worldInverseMatrix[0]'.format(end), '{}.matrixIn[1]'.format(mult))

	cmds.connectAttr('{}.matrixSum'.format(mult), '{}.inputMatrix'.format(dec))
	cmds.connectAttr('{}.outputTranslate'.format(dec), '{}.controlPoints[1]'.format(curveShape))
	return curveShape


def createPoleVector(joint, ctl, ik, name='ik_poleVector'):
	poleVector = cmds.poleVectorConstraint(ctl, ik)
	shape = createAimVectorHelper(joint, ctl, name='{}_helper'.format(name))
	return [poleVector, shape]


def createAimVector(par, child, name='aimVector', aimVector=[0, 0, 1]):
	aim = cmds.aimConstraint(par,
	                         child,
	                         name='{}_constraint0'.format(name),
	                         mo=True,
	                         aimVector=aimVector,
	                         upVector=[0, 1, 0],
	                         worldUpType='objectrotation',
	                         worldUpVector=[0, 1, 0],
	                         worldUpObject=par,
	                         )

	shape = createAimVectorHelper(child, par, name='{}_helper'.format(name))

	return [aim, shape]


def createFollicle(name='follicle0', debug=False):
	shape = cmds.createNode('follicle', name='{}Shape'.format(name))
	transform = cmds.listRelatives(shape, parent=True)[0]

	cmds.select(d=True)
	joint = cmds.joint(name='{}_joint'.format(name))
	if not debug:
		cmds.setAttr('{}.drawStyle'.format(joint), 2)
	else:
		cmds.setAttr('{}.displayLocalAxis'.format(joint), 1)
	cmds.parent(shape, joint, r=True, s=True)
	cmds.delete(transform)
	transform = cmds.listRelatives(shape, parent=True)[0]

	cmds.connectAttr('{}.outRotate'.format(shape), '{}.rotate'.format(transform))
	cmds.connectAttr('{}.outTranslate'.format(shape), '{}.translate'.format(transform))

	return [transform, shape]
