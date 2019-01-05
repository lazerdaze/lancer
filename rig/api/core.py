# LANCER.API.CORE
#
#
#
#
#

'''
* Rigging Goals *
- Real-time Speed
- Simple to Use
- Robust

* Rig Structure *

- Global
	- Mesh Group
	- Control Rig
		- Network
		- Skeleton Hierarchy
	- Control Set
	- Geo Cache Set


* Tools *
- Manuel Rig Builder
- Auto Rig Builder
- FKIK Switcher
- Pose Mirror
- Human IK / Mocap
- Retarget & Bake Animation
- Geo Cache Export / Alembic
- FBX Export??
'''

# Lancer Modules
import utils


########################################################################################################################
#
#
#	Globals
#
#
########################################################################################################################

class Type(object):
	transform = 'transform'
	mesh = 'mesh'
	joint = 'joint'
	nurbsCurve = 'nurbsCurve'
	control = 'control'


class Component(object):
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
	group = 'group'
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


########################################################################################################################
#
#
#	Base Node Class
#
#
########################################################################################################################

class Node(object):
	def __init__(self, parent=None, name=None, type=None, children=None):
		self.name = name
		self.type = type
		self.parent = parent
		self.children = children if children is list else []

	def __str__(self):
		value = ''
		for x in sorted(vars(self).iterkeys()):
			value += '{}:\t{}\n'.format(x, vars(self)[x])
		return value

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name
		return

	def getType(self):
		return self.type

	def setType(self, type):
		self.type = type
		return

	def getParent(self):
		return self.parent

	def setParent(self, parent):
		self.parent = parent
		return

	def getChildren(self):
		return self.children

	def setChildren(self, children):
		self.children = children
		return

	def appendChild(self, child):
		self.children.append(child)
		return

	def removeChild(self, child):
		if child in self.children:
			self.children.remove(child)
		return

	def isValid(self):
		if self.name:
			return utils.nodeExists(self.name)
		return False

	def populateFromScene(self):
		if self.isValid():
			#self.parent = utils.nodeParent(self.name)
			self.type = utils.nodeType(self.name)

			children = utils.nodeChildren(self.name)

			if children:
				for child in children:
					childNode = Node(parent=self, name=child)
					childNode.populateFromScene()
					self.appendChild(childNode)
		return
