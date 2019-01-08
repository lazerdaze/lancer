class Type(object):
	transform = 'transform'
	mesh = 'mesh'
	joint = 'joint'
	nurbsCurve = 'nurbsCurve'
	control = 'control'
	null = 'null'
	blendWeighted = 'blendWeighted'
	animCurve = 'animCurve'
	unitConversion = 'unitConversion'


class Component(object):
	node = 'node'
	transform = 'transform'
	base = 'base'
	rig = 'rig'
	bind = 'bind'
	chain = 'chain'
	fk = 'fk'
	ik = 'ik'

	fkik = 'fkik'
	set = 'set'
	joint = 'joint'
	control = 'control'
	fkControl = 'fk_{}'.format(control)
	ikControl = 'ik_{}'.format(control)
	masterControl = 'master_{}'.format(control)
	detailControl = 'detail_{}'.format(control)
	group = 'group'
	offset = 'offset'
	origin = 'origin'
	position = 'position'
	zero = 'zero'
	network = 'network'
	null = 'null'
	aim = 'aim'
	ribbon = 'ribbon'

	detail = 'detail'
	attr = 'attr'
	aux = 'aux'
	parent = 'parent'
	rigNetwork = 'rigNetwork'
	rigNetworkRoot = 'rigNetworkRoot'
	skeletonNetwork = 'skeletonNetwork'
	character = 'character'
	index = 'index'
	stretch = 'stretch'
	autoStretch = 'autoStretch'
	detailControlDisplay = 'detailControlDisplay'

	constraint = 'constraint'
	ikHandle = 'ikHandle'
	poleVector = 'poleVector'
	ikPoleVector = 'ikPoleVector'
	fkPoleVector = 'fkPoleVector'
	aimVector = 'aimVector'


class MayaAttr(object):
	# Transforms
	translate = 'translate'
	translateX = 'translateX'
	translateY = 'translateY'
	translateZ = 'translateZ'

	rotate = 'rotate'
	rotateX = 'rotateX'
	rotateY = 'rotateY'
	rotateZ = 'rotateZ'

	scale = 'scale'
	scaleX = 'scaleX'
	scaleY = 'scaleY'
	scaleZ = 'scaleZ'

	visibility = 'visibility'
	rotateOrder = 'rotateOrder'

	overrideEnabled = 'overrideEnabled'
	overrideRGBColors = 'overrideRGBColors'
	useObjectColor = 'useObjectColor'

	# Joints
	drawStyle = 'drawStyle'
	side = 'side'
	type = 'type'
	otherType = 'otherType'
	segmentScaleCompensate = 'segmentScaleCompensate'
	jointOrientX = 'jointOrientX'
	jointOrientY = 'jointOrientX'
	jointOrientZ = 'jointOrientX'


class MayaAttrType(object):
	float = 'double'
	int = 'long'
	bool = 'bool'
	enum = 'enum'
	string = 'string'
	vector = 'double3'
	message = 'message'


class UserAttr(object):
	index = 'index'
	offsetVisibility = 'offsetVisibility'
	kind = 'kind'


class Position(object):
	none = 'none'
	left = 'left'
	right = 'right'
	center = 'center'
	top = 'top'
	bottom = 'bottom'
	corner = 'corner'
	inner = 'inner'
	outter = 'outter'


class Part(object):
	# Root
	root = 'root'
	cog = 'cog'

	# Spine
	spine = 'spine'
	chest = 'chest'
	neck = 'neck'
	head = 'head'

	# Face
	face = 'face'
	mouth = 'mouth'
	jaw = 'jaw'
	ear = 'ear'
	nose = 'nose'
	eye = 'eye'
	lid = 'lid'
	lip = 'lip'
	brow = 'brow'
	cheeck = 'cheeck'
	tongue = 'tongue'
	teeth = 'teeth'

	# Arm
	arm = 'arm'
	collar = 'collar'
	shoulder = 'shoulder'
	elbow = 'elbow'
	wrist = 'wrist'
	hand = 'hand'
	finger = 'finger'

	# Leg
	leg = 'leg'
	hip = 'hip'
	thigh = 'thigh'
	knee = 'knee'
	ankle = 'ankle'
	foot = 'foot'
	toe = 'toe'

	# Hand / Toe
	thumb = 'thumb'
	index = 'index'
	middle = 'middle'
	ring = 'ring'
	pinky = 'pinky'
	digit = 'digit'

	# Misc
	prop = 'prop'
	tail = 'tail'
	wing = 'wing'
	appendage = 'appendage'
	extension = 'extension'


AnimCurves = ['animCurveUL',
              'animCurveUU',
              'animCurveUA',
              'animCurveUT'
              ]


def longName(*args):
	var = ''
	for arg in args:
		if arg is not None and arg != '':
			if not isinstance(arg, (list, dict)):
				if var:
					var += '_{}'.format(arg)
				else:
					var += str(arg)
			else:
				for item in arg:
					if var:
						var += '_{}'.format(longName(item))
					else:
						var += longName(item)
	return var


def attributeName(*args):
	var = ''
	for arg in args:
		if arg[0] in '0123456789':
			raise TypeError('Argument must start with a letter.')
		else:
			if var:
				var += '.{}'.format(arg)
			else:
				var = str(arg)
	return var


def removeJointStr(obj, *args):
	var = str(obj)

	removeList = ['bind', 'joint', 'jnt', 'joints', 'jnts', ]
	exclude = []

	if '_' in var:

		var = var.split('_')

		for x in var:
			if x.lower() in removeList:
				exclude.append(x)

		for x in exclude:
			var.remove(x)

		newStr = str(var).replace("'", '').replace('[', '').replace(']', '').replace(' ', '').replace(',', '_')

		return newStr

	else:
		return var


def niceString(var, *args):
	newVar = ''
	i = 0
	for v in var:
		if i == 0:
			newVar = v.upper()
		else:
			if v.isupper():
				newVar = '{} {}'.format(newVar, v)
			else:
				newVar = ''.join([newVar, v])
		i += 1

	return newVar
