# LANCER.API.UTILS.ATTRIBUTE
#
#
#
#
#

# Lancer Modules
from naming import *

# Maya Modules
from maya import cmds


def attributeExists(node, attribute):
	return


def addAttribute(node, attribute, kind=None, value=None, min=None, max=None):
	return


def addKindAttribute(node, kind):
	return


def setAttribute(node, attribute, value):
	name = attributeName(node, attribute)
	cmds.setAttr(name, value)
	return


def getAttribute(node, attribute):
	name = attributeName(node, attribute)
	return


def attributeType():
	return


def connectAttribute(parent, child):
	return


def hideAttributes(obj):
	attributes = cmds.listAttr(obj, k=True)
	if attributes:
		for attr in attributes:
			cmds.setAttr('{}.{}'.format(obj, attr), keyable=False, channelBox=False)
	return


def lockAttributes(obj, hide=False):
	hide = False if hide else True
	attributes = cmds.listAttr(obj, k=True)
	if attributes:
		for attr in attributes:
			cmds.setAttr('{}.{}'.format(obj, attr), lock=True, keyable=hide, channelBox=hide)
	return


def lockTranslate(obj, hide=False):
	for axis in ['x', 'y', 'z']:
		cmds.setAttr('{}.t{}'.format(obj, axis), lock=True, keyable=hide, channelBox=hide)
	return


def lockRotate(obj, hide=False):
	for axis in ['x', 'y', 'z']:
		cmds.setAttr('{}.r{}'.format(obj, axis), lock=True, keyable=hide, channelBox=hide)
	return


def lockScale(obj, hide=False):
	for axis in ['x', 'y', 'z']:
		cmds.setAttr('{}.s{}'.format(obj, axis), lock=True, keyable=hide, channelBox=hide)
	return


def setVisibility(obj, hide=True):
	hide = False if hide else True
	attrName = '{}.v'.format(obj)
	cmds.setAttr(attrName, hide, lock=False)
	return


def zeroAttrs(obj, *args):
	for attr in ['t', 'r', 's']:
		value = 0

		if attr == 's':
			value = 1

		for axis in ['x', 'y', 'z']:
			try:
				cmds.setAttr('{}.{}{}'.format(obj, attr, axis), value)
			except:
				pass


def addEmptyAttr(obj, n='customAttr', *args):
	cmds.addAttr(obj, ln=n, at='enum', en='-:', k=True)
	cmds.setAttr('{}.{}'.format(obj, n), e=True, channelBox=True)
	return


def addBoolAttr(obj, name):
	attrName = '{}.{}'.format(obj, name)
	cmds.addAttr(obj, ln=name, at='enum', en='off:on')
	cmds.setAttr(attrName, e=True, cb=True)
	return attrName


def setEnumByString(obj, attr, value):
	enumString = cmds.attributeQuery(attr, node=obj, listEnum=1)[0]
	enumList = enumString.split(':')
	index = enumList.index(str(value))
	attribute = '{}.{}'.format(obj, attr)
	cmds.setAttr(attribute, index)
	return attribute


def addSideAttr(obj):
	cmds.addAttr(obj, ln='side', at='enum', en='Center:Left:Right:None:', keyable=True)
	cmds.setAttr('{}.side'.format(obj), 3, keyable=False, cb=False)
	return


def getConnectedObj(obj, attr):
	name = '{}.{}'.format(obj, attr)

	if cmds.connectionInfo(name, id=True):
		query = cmds.listConnections(cmds.connectionInfo(name, ged=True))[0]
		return query
	else:
		query = cmds.listConnections(name)
		if query:
			query = query[0]
			return query

		else:
			return None


def addIndexValue(obj, var, *args):
	if not cmds.attributeQuery('index', node=obj, ex=True):
		cmds.addAttr(obj, ln='index', at='long', dv=var)
	else:
		cmds.setAttr('{}.index'.format(obj), var)

	return
