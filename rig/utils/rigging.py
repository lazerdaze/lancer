# Lancer Modules
from naming import *
from control import *
from curve import *
from constraint import *
from joint import *
from wire import *
from curve import *
from library import mathUtils

# Maya Modules
import maya.cmds as cmds

'''
Notes:
	- "Math is fun solving triangles"
		- Law of Cosines

	- There's six elements to a triangle (3 sides / 3 amgles).
'''


def createTriangleSolver(*args, **kwargs):
	'''

	chain start (locator)
	chain end (locator)
	distance (distanceBetween)
	aim (angleBetween)
	sides (addDoubleLinear)
	chain buffer
	'''
	return


class queryIK():
	def __init__(self, obj, *args):
		ik = None
		sj = None
		ee = None
		ej = None
		par = None

		if cmds.objectType(obj) == 'joint':
			for axis in ['x', 'y', 'z']:
				x = cmds.listConnections('{}.t{}'.format(obj, axis))

				if x:
					if ee != x:
						ee = x[0]

			if ee:
				ik = cmds.listConnections('{}.handlePath'.format(ee))

				if ik:
					ik = [0]
					sj = cmds.listConnections('{}.startJoint'.format(ik))[0]
					par = getParentByType(ik, typ='nurbsCurve')
					for axis in ['x', 'y', 'z']:
						nj = cmds.listConnections('{}.t{}'.format(ee, axis))[0]
						if ej != nj:
							ej = nj

		elif cmds.objecType(ik) == 'ikHandle':
			ik = obj
			sj = cmds.listConnections('{}.startJoint'.format(ik))[0]
			ee = cmds.listConnections('{}.endEffector'.format(ik))[0]
			par = getParentByType(ik, typ='nurbsCurve')

			ej = ''
			for axis in ['x', 'y', 'z']:
				nj = cmds.listConnections('{}.t{}'.format(ee, axis))[0]
				if ej != nj:
					ej = nj

		self.ikHandle = ik
		self.ikEffector = ee
		self.startJoint = sj
		self.endJoint = ej
		self.parent = par


def createFKIK(items, fkControls, ikControls, parent, attrName=Component.fkik):
	# Add Attribute
	if not attributeExist(parent, attrName):
		cmds.addAttr(parent, ln=attrName, min=0, max=1, dv=0, k=True)

	# Error Checks
	items = flatList(items)
	fkControls = flatList(fkControls)
	ikControls = flatList(ikControls)

	# Main Loop
	pcList = []
	reList = []

	i = 0
	for item in items:
		pc = cmds.parentConstraint(fkControls[i],
		                           ikControls[i],
		                           item,
		                           n='{}_{}_pc0'.format(item, attrName),
		                           mo=True)[0]

		pcAttr = cmds.parentConstraint(pc, q=True, wal=True)
		cmds.connectAttr('{}.{}'.format(parent, attrName), '{}.{}'.format(pc, pcAttr[-1]), f=True)

		sc = cmds.scaleConstraint(fkControls[i],
		                          ikControls[i],
		                          item,
		                          n='{}_{}_sc0'.format(item, attrName),
		                          mo=True)[0]

		pcAttr = cmds.scaleConstraint(sc, q=True, wal=True)
		cmds.connectAttr('{}.{}'.format(parent, attrName), '{}.{}'.format(sc, pcAttr[-1]), f=True)

		reverse = cmds.createNode('reverse', n='{}_{}_re1'.format(item, attrName))
		cmds.connectAttr('{}.{}'.format(parent, attrName), '{}.inputX'.format(reverse), f=True)
		cmds.connectAttr('{}.outputX'.format(reverse), '{}.{}'.format(pc, pcAttr[0]), f=True)
		cmds.connectAttr('{}.outputX'.format(reverse), '{}.{}'.format(sc, pcAttr[0]), f=True)

		pcList.append(pc)
		reList.append(reverse)
		i += 1

	# Return

	return [pcList, reList]


class createFlexiPlane:
	def __init__(self, name='felxi', amount=5, width=10, side=Position.left, debug=False):
		"""
		:param name:    Name of component.
		:param amount:  Amount of follicles to be created.
		:param width:   Total length of the plane.
		"""
		# Global Node
		globalGrp = cmds.group(name='{}_global_grp'.format(name), em=True)
		masterGrp = cmds.group(globalGrp, name='{}_grp'.format(name))

		# Nurbs Plane
		axis = [0, 1, 0]
		plane = cmds.nurbsPlane(name='{}_plane'.format(name), ax=axis, w=width, lr=0.1, d=3, u=amount, v=1, ch=0)[0]
		planeShape = cmds.listRelatives(plane, shapes=True)[0]
		cmds.parent(plane, globalGrp)

		# BlendShape
		dup = cmds.duplicate(plane, name='{}_twist_blend'.format(plane))
		blendshape = cmds.blendShape(dup, plane, name='{}_blendShape0'.format(name), weight=[0, 1])

		step = 1.0 / float(amount - 1)
		uPos = 0
		vPos = 0.5
		posList = []

		for x in range(amount):
			posList.append(uPos)
			uPos += step

		if side == Position.right:
			posList = list(reversed(posList))

		# Follicles
		follicleList = []
		follicleScale = []
		for x in range(amount):
			follicle = createFollicle('{}_{}_follicle'.format(name, x), debug=debug)
			follicleTransform = follicle[0]
			follicleShape = follicle[1]

			cmds.connectAttr('{}.local'.format(planeShape), '{}.inputSurface'.format(follicleShape))
			cmds.connectAttr('{}.worldMatrix[0]'.format(planeShape), '{}.inputWorldMatrix'.format(follicleShape))
			cmds.setAttr('{}.parameterU'.format(follicleShape), posList[x])
			cmds.setAttr('{}.parameterV'.format(follicleShape), vPos)
			cmds.setAttr('{}.v'.format(follicleShape), 0)
			follicleScale.append(cmds.scaleConstraint(globalGrp, follicleTransform, mo=True)[0])
			follicleList.append(follicleTransform)

		# Locators
		pos = [width / 2 * -1, 0, width / 2]
		if side == Position.right:
			pos = list(reversed(pos))

		locList = []
		locGrpList = []
		i = 0
		for x in pos:
			loc = cmds.spaceLocator(name='{}_{}_locator'.format(name, i))[0]
			cmds.xform(loc, ws=True, t=[x, 0, 0])
			freezeTransform(loc)
			cmds.parent(loc, globalGrp)
			locList.append(loc)
			i += 1

		# Curve
		clusterList = []
		clusterGrp = cmds.group(name='{}_cluster_grp'.format(name), em=True)
		curve = makeNurbsCurve(locList, n='{}_curve'.format(name), d=2)
		i = 0
		for x in ['0:1', '1', '1:2']:
			cluster = cmds.cluster('{}.cv[{}]'.format(curve, x), rel=True, name='{}_{}_cluster'.format(name, i))
			clusterShape = cluster[0]
			cluster = cluster[1]
			cmds.xform(cluster, ws=True, rp=[pos[i], 0, 0])
			cmds.setAttr('{}.v'.format(cluster), 0)
			cmds.connectAttr('{}.t'.format(locList[i]), '{}.t'.format(cluster))
			cmds.parent(cluster, clusterGrp)
			clusterList.append(clusterShape)
			i += 1

		cmds.percent(clusterList[0], '{}.cv[1]'.format(curve), v=.5)
		cmds.percent(clusterList[-1], '{}.cv[1]'.format(curve), v=.5)

		# TwistDeformer
		twist = cmds.nonLinear(dup, type='twist', name='{}_twist'.format(name))
		twistShape = cmds.rename(twist[0], '{}_twist'.format(name))
		twistTransform = cmds.rename(twist[1], '{}_twistHandle'.format(name))
		cmds.setAttr('{}.rz'.format(twistTransform), -90 if side == Position.left else 90)

		rangeNode = cmds.createNode('setRange', name='{}_twist_setRange0'.format(name))
		addList = []
		for axis in ['x', 'y', 'z']:
			cmds.setAttr('{}.oldMax{}'.format(rangeNode, axis.upper()), 1)

		cmds.addAttr(globalGrp, ln='startTwist', min=0, max=1, dv=1, k=True)
		cmds.addAttr(globalGrp, ln='endTwist', min=0, max=1, dv=1, k=True)
		cmds.addAttr(globalGrp, ln='startTwistAmount', k=True, at='doubleAngle')
		cmds.addAttr(globalGrp, ln='endTwistAmount', k=True, at='doubleAngle')
		cmds.addAttr(globalGrp, ln='startTwistAdd', k=True, at='doubleAngle')
		cmds.addAttr(globalGrp, ln='endTwistAdd', k=True, at='doubleAngle')
		cmds.addAttr(globalGrp, ln='twistSide',
		             min=-1,
		             max=1,
		             dv=-1 if side == Position.left else 1,
		             k=True,
		             )

		mirror = cmds.createNode('multiplyDivide', name='{}_mirror_mult0'.format(name))

		axis = 'X'
		for attr in ['start', 'end']:
			add = cmds.createNode('addDoubleLinear', name='{}_{}_add0'.format(name, attr))
			cmds.connectAttr('{}.{}TwistAmount'.format(globalGrp, attr), '{}.input1'.format(add))
			cmds.connectAttr('{}.{}TwistAdd'.format(globalGrp, attr), '{}.input2'.format(add))

			cmds.connectAttr('{}.output'.format(add), '{}.max{}'.format(rangeNode, axis))
			cmds.connectAttr('{}.{}Twist'.format(globalGrp, attr), '{}.value{}'.format(rangeNode, axis))

			cmds.connectAttr('{}.twistSide'.format(globalGrp), '{}.input1{}'.format(mirror, axis))
			cmds.connectAttr('{}.outValue{}'.format(rangeNode, axis), '{}.input2{}'.format(mirror, axis))
			cmds.connectAttr('{}.output{}'.format(mirror, axis), '{}.{}Angle'.format(twistShape, attr))
			axis = 'Y'

		# Wire Deformer
		wire = cmds.wire(dup, wire=curve, name='{}_wire0'.format(name))
		wireShape = wire[0]
		wireBaseTransform = cmds.listConnections('{}.baseWire[0]'.format(wireShape))[0]
		cmds.setAttr('{}.dropoffDistance[0]'.format(wire[0]), 20)

		# SnS
		cmds.addAttr(globalGrp, ln='sns', min=0, max=1, dv=1, k=True)
		cmds.addAttr(globalGrp, ln='snsAdd', k=True)
		# cmds.addAttr(globalGrp, ln='snsHighBound', k=True, min=0, max=1, dv=1)
		# cmds.addAttr(globalGrp, ln='snsLowBound', k=True, min=0, max=1, dv=1)

		curveInfo = createCurveInfo(curve)
		divideA = cmds.createNode('multiplyDivide', name='{}_divide0'.format(name))
		cmds.setAttr('{}.operation'.format(divideA), 2)
		cmds.setAttr('{}.input2X'.format(divideA), width)
		divideB = cmds.createNode('multiplyDivide', name='{}_divide0'.format(name))
		cmds.setAttr('{}.operation'.format(divideB), 2)
		cmds.setAttr('{}.input1X'.format(divideB), 1)

		cmds.connectAttr('{}.arcLength'.format(curveInfo), '{}.input1X'.format(divideA))
		cmds.connectAttr('{}.outputX'.format(divideA), '{}.input2X'.format(divideB))

		setRange = cmds.createNode('setRange', name='{}_sns_setRange0'.format(name))
		cmds.setAttr('{}.minX'.format(setRange), 1)
		cmds.setAttr('{}.oldMaxX'.format(setRange), 1)
		cmds.connectAttr('{}.sns'.format(globalGrp), '{}.valueX'.format(setRange))
		cmds.connectAttr('{}.outputX'.format(divideB), '{}.maxX'.format(setRange))

		add = cmds.createNode('addDoubleLinear', name='{}_add0'.format(name))
		cmds.connectAttr('{}.outValueX'.format(setRange), '{}.input1'.format(add))
		cmds.connectAttr('{}.snsAdd'.format(globalGrp), '{}.input2'.format(add))

		var = 0
		step = 1.0 / float(amount - 1)
		stepRangePos = []

		for x in range(amount):
			if x == 0:
				stepRangePos.append(.1)
			else:
				stepRangePos.append(var)
			var += step

		stepRangeNeg = list(reversed(stepRangePos))

		for scale in follicleScale:
			i = follicleScale.index(scale)
			for axis in ['y', 'z']:
				cmds.connectAttr('{}.output'.format(add), '{}.offset{}'.format(scale, axis.upper()))

		# Hierarchy
		extrasGrp = cmds.group(clusterGrp, curve, twistTransform, dup, wireBaseTransform,
		                       name='{}_extras_grp'.format(name))
		cmds.setAttr('{}.v'.format(extrasGrp), 0)
		cmds.setAttr('{}.inheritsTransform'.format(extrasGrp), 0)

		follicleGrp = cmds.group(follicleList, name='{}_follicle_grp'.format(name))
		cmds.setAttr('{}.inheritsTransform'.format(follicleGrp), 0)
		cmds.parent(extrasGrp, follicleGrp, masterGrp)

		for x in [follicleGrp, clusterGrp, extrasGrp, plane]:
			lockKeyableAttributes(x)

		setVisibility(globalGrp)
		lockScale(globalGrp)

		# Return
		self.plane = plane
		self.planeShape = planeShape
		self.planeBlend = dup
		self.planeBlendShape = blendshape
		self.follicle = follicleList
		self.curve = curve
		self.twist = twistTransform
		self.twistShape = twistShape
		self.wire = wire
		self.wireBase = wireBaseTransform
		self.control = locList
		self.group = locGrpList
		self.parent = globalGrp
		self.masterGroup = masterGrp
		self.extra = extrasGrp


class createIKTwist:
	def __init__(self, start, end, name='ikTwist'):
		cmds.select(d=True)

		ikJoint = []
		i = 0
		for x in [end, start]:
			joint = cmds.joint(name='{}_{}_joint'.format(name, i))
			cmds.setAttr('{}.drawStyle'.format(joint), 2)
			snap(x, joint, t=True, r=True)
			ikJoint.append(joint)
			i += 1

		globalGrp = createGroup(ikJoint[0], name='{}_grp'.format(name))
		cmds.parent(globalGrp, start)
		freezeTransform(ikJoint[0])

		ik = cmds.ikHandle(sj=ikJoint[0], ee=ikJoint[1], sol='ikSCsolver', name='{}_ik'.format(name))[0]
		setVisibility(ik)
		parent = cmds.listRelatives(start, parent=True)
		if parent:
			cmds.parent(ik, parent[0])

		self.joint = ikJoint
		self.ikHandle = ik
		self.parent = globalGrp


def createNullChain(nullNames):
	nullNames = listCheck(nullNames)
	nullList = []
	for null in nullNames:
		i = nullNames.index(null)
		grp = cmds.group(name='{}_null0'.format(null), em=True)
		if len(nullNames) > 1 and i != 0:
			cmds.parent(grp, nullList[i - 1])
		nullList.append(grp)
	return nullList


class createIKFootRollNulls:
	def __init__(self, foot, toe, control=None, name='ik_footPivot'):
		'''
		Global
		Swivel
			Heel
			Toe
			Ball
		Bank
			Inner
			Outter
		Rock
			Heel
			Toe
		Ball XYZ
			(Ik Handle)
		Toe Raise
			(Toe Joint Orient)

		:param foot:
		:param toe:
		:param ik:
		:param control:
		:param name:
		'''
		self.start = foot
		self.end = toe
		self.control = control
		self.name = name

		self.side = getPositionSide(foot)
		self.parent = None
		self.swivel = None
		self.bank = None
		self.rock = None
		self.ball = None
		self.toe = None

		self.wire = None

		self.create()
		self.defaultPositions()

	def create(self):
		partName = ['heel', 'ball', 'toe']
		globalGrp = cmds.group(name='{}_global_grp0'.format(self.name), em=True)
		self.control = self.control if self.control else globalGrp

		# Swivel
		swivelName = ['{}_swivel_{}'.format(self.name, x) for x in partName]
		swivelList = createNullChain(swivelName)
		cmds.parent(swivelList[0], globalGrp)
		addEmptyAttr(self.control, n='swivelControl')
		for null in swivelList:
			i = swivelList.index(null)
			attrName = 'swivel{}'.format(partName[i].capitalize())
			cmds.addAttr(self.control, ln=attrName, k=True, at='doubleAngle')
			cmds.connectAttr('{}.{}'.format(self.control, attrName), '{}.ry'.format(null))

		# Bank
		bankName = ['{}_bank_{}'.format(self.name, x) for x in ['inner', 'outter']]
		bankList = createNullChain(bankName)
		cmds.parent(bankList[0], swivelList[-1])
		addEmptyAttr(self.control, n='bankControl')
		cmds.addAttr(self.control, ln='bank', k=True, min=-180, max=180, dv=0)
		bankCon = cmds.createNode('condition', name='{}_bank_condition0'.format(self.name))
		cmds.setAttr('{}.operation'.format(bankCon), 2)
		cmds.setAttr('{}.colorIfFalseR'.format(bankCon), 0)
		cmds.setAttr('{}.colorIfFalseG'.format(bankCon), 0)
		cmds.setAttr('{}.colorIfFalseB'.format(bankCon), 0)
		cmds.connectAttr('{}.bank'.format(self.control), '{}.firstTerm'.format(bankCon))
		cmds.connectAttr('{}.bank'.format(self.control), '{}.colorIfTrueR'.format(bankCon))
		cmds.connectAttr('{}.bank'.format(self.control), '{}.colorIfFalseG'.format(bankCon))

		if self.side == 'left':
			cmds.connectAttr('{}.outColorR'.format(bankCon), '{}.rz'.format(bankList[0]))
			cmds.connectAttr('{}.outColorG'.format(bankCon), '{}.rz'.format(bankList[1]))
		if self.side == 'right':
			cmds.connectAttr('{}.outColorR'.format(bankCon), '{}.rz'.format(bankList[1]))
			cmds.connectAttr('{}.outColorG'.format(bankCon), '{}.rz'.format(bankList[0]))

		# Rock
		rockName = ['{}_rock_{}'.format(self.name, x) for x in ['heel', 'toe']]
		rockList = createNullChain(rockName)
		cmds.parent(rockList[0], bankList[-1])

		# Ball
		ballOffset = cmds.group(name='{}_ball_offset_null0'.format(self.name), em=True)
		ballGrp = cmds.group(ballOffset, name='{}_ball_null0'.format(self.name))
		cmds.parent(ballGrp, rockList[-1])
		addEmptyAttr(self.control, n='ballControl')
		for attr in ['x', 'y', 'z']:
			cmds.addAttr(self.control, ln='ball{}'.format(attr.upper()), k=True, at='doubleAngle')
			cmds.connectAttr('{}.ball{}'.format(self.control, attr.upper()), '{}.r{}'.format(ballOffset, attr))

		# Toe
		toeGrp = cmds.group(name='{}_toe_grp0'.format(self.name), em=True)
		cmds.parent(toeGrp, rockList[-1])
		addEmptyAttr(self.control, n='toeControl')
		for attr in ['x', 'y', 'z']:
			cmds.addAttr(self.control, ln='toe{}'.format(attr.upper()), k=True, at='doubleAngle')
			cmds.connectAttr('{}.toe{}'.format(self.control, attr.upper()), '{}.r{}'.format(toeGrp, attr))

		# Foot Roll
		rollAngle = [90, 45, 90]
		addEmptyAttr(self.control, n='rollControl')
		cmds.addAttr(self.control, ln='roll', k=True, dv=0)
		for attr in partName:
			i = partName.index(attr)
			cmds.addAttr(self.control,
			             ln='angle{}'.format(attr.capitalize()),
			             k=True,
			             min=-180,
			             max=180,
			             dv=rollAngle[i],
			             )

		# Foot Roll - Heel
		mul = cmds.createNode('multDoubleLinear', name='{}_heel_multiply0'.format(self.name))
		cmds.setAttr('{}.input2'.format(mul), -1)
		cmds.connectAttr('{}.angleHeel'.format(self.control), '{}.input1'.format(mul))
		range = cmds.createNode('setRange', name='{}_heel_range0'.format(self.name))
		cmds.setAttr('{}.oldMinX'.format(range), -10)
		cmds.connectAttr('{}.output'.format(mul), '{}.minX'.format(range))
		cmds.connectAttr('{}.roll'.format(self.control), '{}.valueX'.format(range))
		cmds.connectAttr('{}.outValueX'.format(range), '{}.rx'.format(rockList[0]))

		# Foot Roll - Toe
		range = cmds.createNode('setRange', name='{}_toe_range0'.format(self.name))
		cmds.setAttr('{}.oldMinX'.format(range), 10)
		cmds.setAttr('{}.oldMaxX'.format(range), 20)
		cmds.connectAttr('{}.angleToe'.format(self.control), '{}.maxX'.format(range))
		cmds.connectAttr('{}.roll'.format(self.control), '{}.valueX'.format(range))
		cmds.connectAttr('{}.outValueX'.format(range), '{}.rx'.format(rockList[1]))

		# Foot Roll - Ball
		range = cmds.createNode('setRange', name='{}_ball_range0'.format(self.name))
		cmds.setAttr('{}.oldMaxX'.format(range), 10)
		cmds.setAttr('{}.oldMinY'.format(range), 10)
		cmds.setAttr('{}.oldMaxY'.format(range), 20)
		cmds.connectAttr('{}.angleBall'.format(self.control), '{}.maxX'.format(range))
		cmds.connectAttr('{}.angleBall'.format(self.control), '{}.minY'.format(range))
		cmds.connectAttr('{}.roll'.format(self.control), '{}.valueX'.format(range))
		cmds.connectAttr('{}.roll'.format(self.control), '{}.valueY'.format(range))
		con = cmds.createNode('condition', name='{}_ball_condition0'.format(self.name))
		cmds.setAttr('{}.secondTerm'.format(con), 10)
		cmds.setAttr('{}.operation'.format(con), 2)
		cmds.connectAttr('{}.roll'.format(self.control), '{}.firstTerm'.format(con))
		cmds.connectAttr('{}.outValueX'.format(range), '{}.colorIfFalseR'.format(con))
		cmds.connectAttr('{}.outValueY'.format(range), '{}.colorIfTrueR'.format(con))
		cmds.connectAttr('{}.outColorR'.format(con), '{}.rx'.format(ballGrp))

		# Return
		self.parent = globalGrp
		self.swivel = swivelList
		self.bank = bankList
		self.rock = rockList
		self.ball = [ballOffset, ballGrp]
		self.toe = listCheck(toeGrp)
		return

	def defaultPositions(self):
		locators = getDefaultIKFootRollPositions(foot=self.start, toe=self.end)
		snap(locators.parent, self.parent, t=True, r=True)
		snap(self.end, self.toe[0], t=True, r=True)

		for x in [self.swivel[0], self.rock[0]]:
			moveRotatePivot(locators.heel, x)

		for x in [self.swivel[1]]:
			moveRotatePivot(locators.ball, x)

		for x in [self.swivel[2], self.rock[1]]:
			moveRotatePivot(locators.toe, x)

		moveRotatePivot(locators.inner, self.bank[0])
		moveRotatePivot(locators.outter, self.bank[1])

		for x in self.ball:
			moveRotatePivot(self.end, x)

		cmds.delete(locators.parent)
		return

	def accuratePositions(self):
		startBounds = estimateBoundsByJoint(self.start)
		endBounds = estimateBoundsByJoint(self.end)

		if self.side == 'left':
			minX = [startBounds.minX[0], 0, startBounds.minX[2]]
			maxX = [startBounds.maxX[0], 0, startBounds.maxX[2]]
		else:
			minX = [startBounds.maxX[0], 0, startBounds.maxX[2]]
			maxX = [startBounds.minX[0], 0, startBounds.minX[2]]

		# moveRotatePivot(minX, self.bank[0])
		moveRotatePivot(maxX, self.bank[1])

		for x in [self.swivel[0], self.rock[0]]:
			moveRotatePivot([startBounds.minZ[0], 0, startBounds.minZ[2]], x)

		for x in [self.swivel[2], self.rock[1]]:
			moveRotatePivot([endBounds.maxZ[0], 0, endBounds.maxZ[2]], x)
		return

	def createWire(self):
		self.wire = createWire(kind=WireType.cubeSpecial, axis=[0, 0, 0])
		snap(self.rock[0], self.wire, r=True, t=True)

		var = [getDistance(self.bank[0], self.bank[1]),
		       getDistance(self.parent, self.start),
		       getDistance(self.rock[0], self.rock[1])]

		i = 0
		for axis in ['x', 'y', 'z']:
			cmds.setAttr('{}.s{}'.format(self.wire, axis), var[i])
			i += 1
		presetWireColor(self.wire, typ=Component.ik)
		freezeTransform(self.wire)
		return


class getDefaultIKFootRollPositions:
	def __init__(self, foot, toe):
		side = getPositionSide(foot)
		distance = getDistance(foot, toe)

		self.parent = cmds.spaceLocator(name='foot0')[0]
		snap(foot, self.parent, t=True)
		cmds.setAttr('{}.ty'.format(self.parent), 0)

		self.ball = cmds.spaceLocator(name='ball0')[0]
		snap(toe, self.ball, t=True)
		cmds.setAttr('{}.ty'.format(self.ball), 0)

		cmds.delete(cmds.aimConstraint(self.ball, self.parent, aimVector=[0, 0, 1]))
		snap(self.parent, self.ball, r=True)
		cmds.parent(self.ball, self.parent)

		self.toe = cmds.spaceLocator(name='toe0')[0]
		cmds.parent(self.toe, self.parent)
		zeroAttrs(self.toe)
		cmds.setAttr('{}.tz'.format(self.toe), distance + (distance / 4))

		self.heel = cmds.spaceLocator(name='heel0')[0]
		cmds.parent(self.heel, self.parent)
		zeroAttrs(self.heel)
		cmds.setAttr('{}.tz'.format(self.heel), (distance / 4) * -1)

		if side == 'left':
			innerM = -1
			outterM = 1
		else:
			innerM = 1
			outterM = -1

		self.inner = cmds.spaceLocator(name='inner0')[0]
		cmds.parent(self.inner, self.parent)
		zeroAttrs(self.inner)
		cmds.setAttr('{}.tx'.format(self.inner), (distance / 3) * innerM)

		self.outter = cmds.spaceLocator(name='outter0')[0]
		cmds.parent(self.outter, self.parent)
		zeroAttrs(self.outter)
		cmds.setAttr('{}.tx'.format(self.outter), (distance / 3) * outterM)


def createSplineIK(joints, prefix='rig', *args, **kwargs):
	'''

	:param joints:
	:param prefix:
	:param args:
	:param kwargs:
	:return: [ik, curve, clusterList]
	'''

	# Curve
	curve = createCurveOnPivots(items=joints, prefix=prefix)

	# Cluster
	clusters = clusterCurve(curve=curve, prefix=prefix)

	# Spline
	ik = cmds.ikHandle(n='{}_splineIK'.format(prefix),
	                   sj=joints[0],
	                   ee=joints[-1],
	                   c=curve,
	                   sol='ikSplineSolver',
	                   ccv=False,
	                   rootOnCurve=True,
	                   parentCurve=False)[0]
	cmds.setAttr('{}.v'.format(ik), 0)
	return [ik, curve, clusters]


# TODO: Custom Plug-in Node: Auto On Valve
def valveNode(prefix='rig', *args, **kwargs):
	'''
	inputNode.auto = setRangeNode.valueX
	inputNode.auto = multiplyNode.input2

	inputNode.max = setRangeNode.maxX
	Output = multiplyNode.output

	:param prefix:
	:param args:
	:param kwargs:
	:return:
	'''

	# Set Range
	rangeNode = cmds.createNode('setRange', name=longName(prefix, 'valve', 'setRange'))
	cmds.setAttr(attributeName(rangeNode, 'oldMaxX'), 1)

	# Mult
	multNode = cmds.createNode('multDoubleLinear', name=longName(prefix, 'valve', 'mutiply'))

	# Connect
	cmds.connectAttr(attributeName(rangeNode, 'outValueX'),
	                 attributeName(multNode, 'input1')
	                 )

	return [rangeNode, multNode]


# TODO: Polymer Plug-in Node
class PolymerRig(object):
	def __init__(self,
	             start,
	             end,
	             children=None,
	             twister='start',
	             prefix='rig',
	             ):
		'''
		Assumes that down axis is X.

		:param str unicode object start:
		:param str unicode object end:
		:param str prefix:
		'''

		self.start = start
		self.end = end
		self.children = children
		self.prefix = longName(prefix, 'polymer')
		self.twistOutput = []
		self.stretchOutput = []
		self.maxDistance = getDistance(self.start, self.end)

		self.twister = self.start

		if twister == 'end':
			self.twister = self.end

		# Get Side
		sideQuery = getSide(self.end)

		self.side = -1 if sideQuery == Position.right else 1

		# Create Locators
		self.startLoctor = cmds.spaceLocator(name=longName(self.prefix, 'start', 'locator'))[0]
		snap(self.start, self.startLoctor, True, True)

		self.endLocator = cmds.spaceLocator(name=longName(self.prefix, 'end', 'locator'))[0]
		snap(self.end, self.endLocator, True, True)
		cmds.parent(self.endLocator, self.end)

		# Create Distance Between
		self.distanceNode = cmds.createNode('distanceBetween', name=longName(self.prefix, 'distance'))

		cmds.connectAttr('{}.worldPosition[0]'.format(self.startLoctor),
		                 attributeName(self.distanceNode, 'point1')
		                 )

		cmds.connectAttr('{}.worldPosition[0]'.format(self.endLocator),
		                 attributeName(self.distanceNode, 'point2')
		                 )

		# Create Aim
		self.aimConstraint = cmds.aimConstraint(self.endLocator,
		                                        self.startLoctor,
		                                        aimVector=[self.side, 0, 0],
		                                        upVector=[0, 1, 0],
		                                        worldUpType='none',
		                                        )

		# Create Twist Extractor
		self.extractor = cmds.group(name=longName(self.prefix, 'extractor'), em=True)
		snap(self.start, self.extractor, True, True)
		cmds.parent(self.extractor, self.start)

		addAttribute(self.extractor, 'scaleFactor', kind=MayaAttrType.float)
		addAttribute(self.extractor, 'maxDistance', kind=MayaAttrType.float, value=self.maxDistance, lock=True)
		addAttribute(self.extractor, 'currentDistance', kind=MayaAttrType.float)
		addAttribute(self.extractor, 'twist', kind=MayaAttrType.float)
		addAttribute(self.extractor, 'twistAuto', kind=MayaAttrType.float, minValue=0, maxValue=1, value=1)
		addAttribute(self.extractor, 'twistAdd', kind=MayaAttrType.float, keyable=True, channelBox=False)
		addAttribute(self.extractor, 'twistAmount', kind=MayaAttrType.float, array=True)
		addAttribute(self.extractor, 'stretchAmount', kind=MayaAttrType.float, array=True)

		cmds.connectAttr(attributeName(self.distanceNode, 'distance'),
		                 attributeName(self.extractor, 'currentDistance')
		                 )

		# Auto / Add
		self.twistValve = valveNode(prefix=longName(self.prefix,
		                                            'twist',
		                                            ))

		self.twistAdd = cmds.createNode('addDoubleLinear', name=longName(self.prefix,
		                                                                 'twist',
		                                                                 'add'
		                                                                 ))

		cmds.connectAttr(attributeName(self.extractor, 'twistAuto'),
		                 attributeName(self.twistValve[0], 'valueX')
		                 )

		cmds.connectAttr(attributeName(self.extractor, 'twistAuto'),
		                 attributeName(self.twistValve[1], 'input2')
		                 )

		cmds.connectAttr(attributeName(self.extractor, 'rx'),
		                 attributeName(self.twistValve[0], 'maxX')
		                 )

		cmds.connectAttr(attributeName(self.twistValve[1], 'output'),
		                 attributeName(self.twistAdd, 'input1')
		                 )

		cmds.connectAttr(attributeName(self.extractor, 'twistAdd'),
		                 attributeName(self.twistAdd, 'input2')
		                 )

		cmds.connectAttr(attributeName(self.twistAdd, 'output'),
		                 attributeName(self.extractor, 'twist')
		                 )



		# Scale Extractor
		self.scaleExtractor = cmds.group(name=longName(self.prefix, 'scale_extractor'), em=True)
		cmds.setAttr(attributeName(self.scaleExtractor, 'inheritsTransform'), 0)
		cmds.parent(self.scaleExtractor, self.start)
		self.scaleConstraint = cmds.scaleConstraint(self.start, self.scaleExtractor, mo=True)

		scaleFactor = cmds.createNode('multDoubleLinear', name=longName(self.prefix,
		                                                                'multiply',
		                                                                'scaleExtractor'
		                                                                ))

		cmds.connectAttr(attributeName(self.scaleExtractor, 'sx'), attributeName(scaleFactor, 'input1'))
		cmds.connectAttr(attributeName(self.extractor, 'maxDistance'), attributeName(scaleFactor, 'input2'))
		cmds.connectAttr(attributeName(scaleFactor, 'output'), attributeName(self.extractor, 'scaleFactor'))

		# Create Orient Constraint
		self.orientConstraint = cmds.orientConstraint(self.twister, self.extractor, mo=True)

		# Children
		if self.children:
			i = 0
			for child in self.children:
				# Twist Percentage
				twistAmount = mathUtils.setRange(value=getDistance(self.twister, child),
				                                 oldMin=0,
				                                 oldMax=self.maxDistance,
				                                 newMin=1,
				                                 newMax=0
				                                 ) * self.side

				twistAttr = '{}.{}[{}]'.format(self.extractor, 'twistAmount', i)
				cmds.setAttr(twistAttr, twistAmount, lock=True)

				twistNode = cmds.createNode('multDoubleLinear', name=longName(self.prefix,
				                                                              'multiply',
				                                                              i,
				                                                              'twistOutput'
				                                                              ))

				cmds.connectAttr(twistAttr,
				                 attributeName(twistNode, 'input1'),
				                 force=True,
				                 )

				cmds.connectAttr(attributeName(self.extractor, 'twist'),
				                 attributeName(twistNode, 'input2'),
				                 force=True,
				                 )

				cmds.connectAttr(attributeName(twistNode, 'output'),
				                 attributeName(child, 'rx'))

				self.twistOutput.append(twistNode)

				# Stretch Percentage
				stretchAmount = getDistance(self.start, child) * self.side

				stretchAttr = '{}.{}[{}]'.format(self.extractor, 'stretchAmount', i)
				cmds.setAttr(stretchAttr, stretchAmount, lock=True)

				stretchRange = cmds.createNode('setRange', name=longName(self.prefix,
				                                                         'range',
				                                                         i,
				                                                         'stretchOutput'
				                                                         ))

				cmds.setAttr(attributeName(stretchRange, 'maxX'), 1)
				cmds.connectAttr(attributeName(self.extractor, 'scaleFactor'),
				                 attributeName(stretchRange, 'oldMaxX')
				                 )

				cmds.connectAttr(stretchAttr,
				                 attributeName(stretchRange, 'valueX')
				                 )

				stretchNode = cmds.createNode('multDoubleLinear', name=longName(self.prefix,
				                                                                'multiply',
				                                                                i,
				                                                                'stretchOutput'
				                                                                ))

				cmds.connectAttr(attributeName(stretchRange, 'outValueX'),
				                 attributeName(stretchNode, 'input1'),
				                 force=True,
				                 )

				cmds.connectAttr(attributeName(self.extractor, 'currentDistance'),
				                 attributeName(stretchNode, 'input2'),
				                 force=True,
				                 )

				cmds.connectAttr(attributeName(stretchNode, 'output'),
				                 attributeName(child, 'tx'))

				self.stretchOutput.append(stretchNode)
				i += 1
