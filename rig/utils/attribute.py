# Lancer Modules
from naming import *

# Maya Modules
from maya import cmds


def attributeExists(node, attribute):
	return


def addAttribute(node, attribute, kind=None, value=None, min=None, max=None):
	return


def setAttribute(node, attribute, value):
	name = attributeName(node, attribute)
	kind = attributeType(node, attribute)
	try:
		cmds.setAttr(name, value, type=kind)
		return True
	except ValueError:
		return False


def getAttribute(node, attribute):
	name = attributeName(node, attribute)
	return


def attributeType(node, attribute):
	return str(cmds.getAttr(attributeName(node, attribute), type=True))


def attributeLocked(node, attribute):
	return cmds.getAttr(attributeName(node, attribute), lock=True)


def connectAttribute(parent, child):
	return


def getKeyableAttributes(node):
	result = cmds.listAttr(node, k=True)
	result = [x for x in result if attributeType(node, x) not in ['string']]
	return result if result else []


def getNonKeyableAttributes(node):
	result = cmds.listAttr(node, cb=True)
	return result if result else []


def getChannelBoxAttributes(node):
	return getKeyableAttributes(node) + getNonKeyableAttributes(node)


def attributeExist(node, attribute):
	return cmds.attributeQuery(attribute, node=node, ex=True)


def hideAttributes(node):
	attributes = cmds.listAttr(node, k=True)
	if attributes:
		for attr in attributes:
			cmds.setAttr('{}.{}'.format(node, attr), keyable=False, channelBox=False)
	return


def listAllAttributes(node):
	return cmds.listAttr(node)


def attributeConnected(node, attribute):
	longName = attributeName(node, attribute)
	return True if cmds.connectionInfo(longName, id=True) else False


def lockAttribute(node, attribute):
	return cmds.setAttr(attributeName(node, attribute), lock=True)


def unlockAttribute(node, attribute):
	return cmds.setAttr(attributeName(node, attribute), lock=False)


def lockAttributes(node, hide=False):
	hide = False if hide else True
	attributes = cmds.listAttr(node, k=True)
	if attributes:
		for attr in attributes:
			cmds.setAttr('{}.{}'.format(node, attr), lock=True, keyable=hide, channelBox=hide)
	return


def lockTranslate(node, hide=False):
	for axis in ['x', 'y', 'z']:
		cmds.setAttr('{}.t{}'.format(node, axis), lock=True, keyable=hide, channelBox=hide)
	return


def lockRotate(node, hide=False):
	for axis in ['x', 'y', 'z']:
		cmds.setAttr('{}.r{}'.format(node, axis), lock=True, keyable=hide, channelBox=hide)
	return


def lockScale(node, hide=False):
	for axis in ['x', 'y', 'z']:
		cmds.setAttr('{}.s{}'.format(node, axis), lock=True, keyable=hide, channelBox=hide)
	return


def setVisibility(node, hide=True):
	hide = False if hide else True
	attrName = '{}.v'.format(node)
	cmds.setAttr(attrName, hide, lock=False)
	return


def zeroAttrs(node, *args):
	for attr in ['t', 'r', 's']:
		value = 0

		if attr == 's':
			value = 1

		for axis in ['x', 'y', 'z']:
			try:
				cmds.setAttr('{}.{}{}'.format(node, attr, axis), value)
			except:
				pass


def addEmptyAttr(node, n='customAttr', *args):
	cmds.addAttr(node, ln=n, at='enum', en='-:', k=True)
	cmds.setAttr('{}.{}'.format(node, n), e=True, channelBox=True)
	return


def addBoolAttr(node, name):
	attrName = '{}.{}'.format(node, name)
	cmds.addAttr(node, ln=name, at='enum', en='off:on')
	cmds.setAttr(attrName, e=True, cb=True)
	return attrName


def setEnumByString(node, attr, value):
	enumString = cmds.attributeQuery(attr, node=node, listEnum=1)[0]
	enumList = enumString.split(':')
	index = enumList.index(str(value))
	attribute = '{}.{}'.format(node, attr)
	cmds.setAttr(attribute, index)
	return attribute


def addSideAttr(node):
	cmds.addAttr(node, ln='side', at='enum', en='Center:Left:Right:None:', keyable=True)
	cmds.setAttr('{}.side'.format(node), 3, keyable=False, cb=False)
	return


def getConnectedObj(node, attr):
	name = '{}.{}'.format(node, attr)

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


def addIndexValue(node, var, *args):
	if not cmds.attributeQuery('index', node=node, ex=True):
		cmds.addAttr(node, ln='index', at='long', dv=var)
	else:
		cmds.setAttr('{}.index'.format(node), var)

	return


########################################################################################################################
#
#
#	Attribute Class
#
#
########################################################################################################################


class Attribute(object):
	def __init__(self, node, name, kind=None, value=None, lock=False):
		self.name = attributeName(node, name)
		self.kind = kind
		self.value = value
		self.lock = lock

		# Connections
		self.parentConnection = None
		self.childConnection = None

	def __str__(self):
		value = ''
		for x in sorted(vars(self).iterkeys()):
			value += '{}:\t{}\n'.format(x, vars(self)[x])
		return value

	def __repr__(self):
		return self.name
