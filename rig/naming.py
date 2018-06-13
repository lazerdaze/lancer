# LANCER.RIG.NAMING
#
#
#
#
#

class rig(object):
	base = 'base'
	rig = 'rig'
	bind = 'bind'
	chain = 'chain'
	fk = 'FK'
	ik = 'IK'
	ikHandle = 'ikHandle'
	poleVector = 'poleVector'
	ikPoleVector = 'ikPoleVector'
	fkPoleVector = 'fkPoleVector'
	fkik = 'FKIK'
	fkControl = 'fkControl'
	ikControl = 'ikControl'
	set = 'set'
	joint = 'joint'
	jnt = 'jnt'
	control = 'control'
	ctl = 'ctl'
	group = 'group'
	grp = 'grp'
	network = 'network'
	net = 'net'
	null = 'null'
	aim = 'aim'
	aimVector = 'aimVector'
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


class component(object):
	character = 'character'
	root = 'root'
	cog = 'cog'

	spine = 'spine'
	neck = 'neck'
	head = 'head'

	limb = 'limb'
	digit = 'digit'
	tail = 'tail'
	prop = 'prop'

	leg = 'leg'
	hip = 'hip'
	knee = 'knee'
	foot = 'foot'
	toe = 'toe'
	bigToe = 'bigToe'
	indexToe = 'indexToe'
	middleToe = 'middleToe'
	ringToe = 'ringToe'
	pinkyToe = 'pinkyToe'

	arm = 'arm'
	collar = 'collar'
	hand = 'hand'
	finger = 'finger'
	thumb = 'thumb'
	index = 'index'
	middle = 'middle'
	ring = 'ring'
	pinky = 'pinky'

	face = 'face'
	mouth = 'mouth'
	jaw = 'jaw'
	ear = 'ear'
	nose = 'nose'
	eye = 'eye'
	lid = 'lid'
	brow = 'brow'
	cheeck = 'cheeck'
	tongue = 'tongue'


class side(object):
	none = 'None'
	left = 'Left'
	right = 'Right'
	center = 'Center'


def convention(*args):
	var = ''
	for arg in args:
		if arg not in [None, [], {}]:
			i = args.index(arg)
			if i == 0:
				var = str(arg)
			else:
				var = '{}_{}'.format(var, arg)
	return var


def attribute(*args):
	var = ''
	for arg in args:
		i = args.index(arg)
		if i == 0:
			var = str(arg)
		else:
			var = '{}{}'.format(var, arg.upper())
	return var
