from maya import cmds
from rig.utils import *


def replaceTextureDir(filepath):
	textures = cmds.ls(type='file')
	attr = 'fileTextureName'

	if textures:
		for texture in textures:
			attrName = '{}.{}'.format(texture, attr)

			if cmds.attributeQuery(attr, node=texture, ex=True):
				current = cmds.getAttr(attrName)
				prefix = None

				if current.startswith('T:'):
					prefix = 'T:'
				elif current.startswith('U:'):
					prefix = 'U:'

				if current and prefix:
					current = current.replace(prefix, '')

					newPath = '{}{}'.format(filepath, current)
					cmds.setAttr(attrName, newPath, type='string')
	return


def createJoints(start, end, count):
	distance = getDistance(start, end)
	startPos = cmds.xform(start, q=True, ws=True, rp=True)

	for x in range(count):
		cmds.createJoint()
	return


def matchCurveCallback(*args, **kwargs):
	selected = cmds.ls(sl=True)

	if len(selected) == 2:
		matchCurve(source=selected[0], destination=selected[1])
	return


def curveFromMotionPathCallback(*args, **kwargs):
	selected = cmds.ls(sl=True)

	if selected:
		curveFromMotionPath(selected[0])
	return


def createJointInbetween(start, end, amount):
	distance = getDistance(start, end)
	step = float(distance) / float(amount - 1.0)

	startPos = cmds.xform(start, q=True, ws=True, rp=True)

	currentStep = 0.0

	for x in range(amount):
		joint = cmds.joint()
		cmds.xform(joint, ws=True, t=[startPos[0], startPos[1], currentStep])

		if x == 0:
			cmds.setAttr('{}.jointOrientY'.format(joint), -90)

		currentStep += step
	return


def tongueRig(*args, **kwargs):
	return
