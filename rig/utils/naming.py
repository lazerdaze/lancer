'''
Naming Conventions:
	- "leg_R_..._type"
	- [Component][Side][...][Type]
	- checking for string at the beginning is fastest / end is second fastest

	- "componentSideType"
	- Camel Case

	- "_hierarchy" | "_hrc"
	- No transform values

	- "_position" | "_pos"
	- Initial position of an Object / has transform values

	- "_buffer"
	-

	- "_srt"
	- Scaling Rotation Translation

	- "arm_L_finger_A_0_fkControl"
	- [Prefix][Side][Name][Sector][Index][type]
'''

CHARACTERSTR = 'abcdefghijklmnopqrstuvwxyz'
NUMBERSTR = '0123456789'
SPECIALSTR = '_'


class MayaNodeType(object):
	transform = 'transform'
	mesh = 'mesh'
	joint = 'joint'
	nurbsCurve = 'nurbsCurve'
	control = 'control'
	null = 'null'
	blendWeighted = 'blendWeighted'
	animCurve = 'animCurve'
	unitConversion = 'unitConversion'
	distanceBetween = 'distanceBetween'
	angleBetween = 'angleBetween'
	addDoubleLinear = 'addDoubleLinear'


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
	leaf = '{}_leaf'.format(joint)

	control = 'control'
	fkControl = 'fk_{}'.format(control.capitalize())
	ikControl = 'ik_{}'.format(control)
	masterControl = 'master_{}'.format(control)
	detailControl = 'detail_{}'.format(control)
	group = 'group'
	offset = 'offset'
	origin = 'origin'
	position = 'position'
	connection = 'connection'
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
	sector = 'sector'


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
		if arg[0] in NUMBERSTR:
			raise TypeError('Argument must start with a letter.')
		else:
			if var:
				var += '.{}'.format(arg)
			else:
				var = str(arg)
	return var


def camelCase(*args, **kwargs):
	start = kwargs.get('start', True)

	var = ''
	i = 0
	for arg in args:
		if isinstance(arg, (list, dict, tuple)):
			start = True if i == 0 else False
			for item in arg:
				var += camelCase(item, start=start)
				start = False
		else:
			if start:
				var += str(arg).strip().lower()
				start = False
			else:
				var += str(arg).strip().title()
		i += 1
	return var


def splitCamelCase(string):
	root = []

	if isinstance(string, str):
		stringList = string.split('_')

		for x in stringList:
			newStr = ''
			for char in x:
				if char != ' ':
					if char in CHARACTERSTR.lower():
						newStr += char
					elif char in CHARACTERSTR.upper():
						root.append(newStr)
						newStr = char.lower()
					else:
						newStr += char
			root.append(newStr.strip())
	else:
		raise TypeError('Must provide a str.')
	return root


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
