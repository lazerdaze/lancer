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
	leaf = 'leaf'

	control = 'control'
	fkControl = 'FK{}'.format(control.capitalize())
	ikControl = 'IK{}'.format(control.capitalize())
	master = 'master'
	detailControl = 'detail{}'.format(control.capitalize())
	offsetControl = 'offset{}'.format(control.capitalize())
	leafControl = 'leaf{}'.format(control.capitalize())
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
	radius = 'radius'
	drawStyle = 'drawStyle'
	side = 'side'
	type = 'type'
	otherType = 'otherType'
	segmentScaleCompensate = 'segmentScaleCompensate'
	jointOrientX = 'jointOrientX'
	jointOrientY = 'jointOrientY'
	jointOrientZ = 'jointOrientZ'


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
	outer = 'outer'


class Part(object):
	# Root
	rig = 'rig'
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


class JointDrawStyle(object):
	bone = 0
	box = 1
	none = 2


class JointLabelSide(object):
	center = 0
	left = 1
	right = 2
	none = 3


class JointLabelType(object):
	none = 0
	root = 1
	hip = 2
	knee = 3
	foot = 4
	toe = 5
	spine = 6
	neck = 7
	head = 8
	collar = 9
	shoulder = 10
	elbow = 11
	hand = 12
	finger = 13
	thumb = 14
	propA = 15
	propB = 16
	propC = 17
	other = 18
	indexFinger = 19
	middleFinger = 20
	ringFinger = 21
	pinkyFinger = 22
	extraFinger = 23
	bigToe = 24
	indexToe = 25
	middleToe = 26
	ringToe = 27
	pinkyToe = 28
	footThumb = 29


class JointLabelOtherType(object):
	bind = 'bind'
	footPivot = 'footPivot'
	cog = 'cog'
	tail = 'tail'


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
	capitalize = kwargs.get('capitalize', True)

	result = ''
	i = 0
	for arg in args:
		if ' ' in arg:
			arg = [x.strip() for x in arg.split(' ')]

		if isinstance(arg, (list, dict, tuple)):
			start = True if i == 0 else False
			for item in arg:
				result += camelCase(item, start=start)
				start = False
		else:
			if start:
				if capitalize:
					result += str(arg).strip().capitalize()
				else:
					result += str(arg).strip().lower()
				start = False
			else:
				result += str(arg).strip().title()
		i += 1
	return result


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


def enumName(*args, **kwargs):
	index = kwargs.get('index', 0)
	result = ''
	for arg in args:
		if isinstance(arg, (list, dict, tuple)):
			for item in arg:
				result += enumName(item, index=index)
				index += 1
		else:
			result += '{}={}:'.format(arg, index)
			index += 1
	return result


class TokenizeLongName(object):
	def __init__(self, string):
		'''
		:param str string: Initial string to split apart into attributes.
		:Example:

		"arm_L_shoulder_A_0_control"
		'''

		self.prefix = None
		self.side = None
		self.name = None
		self.index = None
		self.sector = None
		self.kind = None
		self.longName = string

		self.query(string)

	def __str__(self):
		return self.longName

	def __repr__(self):
		return self.longName

	def query(self, string):
		if isinstance(string, str):
			stringList = string.split('_')

			if len(stringList) == 1:
				self.name = string
			elif len(stringList) == 2:
				self.prefix, self.kind = stringList
				self.name = self.prefix
			elif len(stringList) == 6:
				self.prefix, self.side, self.name, self.sector, self.index, self.kind = stringList
			else:
				self.prefix = stringList[0]
				self.name = self.prefix
				self.kind = stringList[-1] if len(stringList[-1]) > 1 else None

				unsorted = []

				for i in range(1, len(stringList) - 1):
					x = stringList[i]

					# Get Side
					if i == 1:
						if len(x) == 1:
							if x.lower() in 'lrmc':
								self.side = x
						else:
							if x.lower() in ['left', 'right', 'center', 'middle']:
								self.side = x

					# Get Name
					else:
						try:
							self.index = int(x)
						except ValueError:
							if len(x) == 1:
								self.sector = x
							else:
								unsorted.append(x)

				self.name = longName(unsorted)

		else:
			raise TypeError('Must provide str.')
		return
