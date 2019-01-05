# LANCER.API.UTILS.GENERAL
#
#
#
#
#

# Maya Modules
from maya import cmds


########################################################################################################################
#
#
#	Functions
#
#
########################################################################################################################

def selected():
	return cmds.ls(sl=True)


def nodeExists(node):
	return cmds.objExists(node)


def nodeParent(node):
	parent = cmds.listRelatives(node, parent=True)
	return parent[0] if parent else None


def nodeShapes(node):
	return cmds.listRelatives(node, shapes=True)


def nodeType(node):
	shapes = nodeShapes(node)
	return cmds.nodeType(shapes[0]) if shapes else cmds.nodeType(node)


def nodeChildren(node):
	children = cmds.listRelatives(node, type='transform')
	return [str(child) for child in children] if children else None


def nodeLocalPosition(node):
	return


def nodeLocalRotation(node):
	return


def nodeWorldPosition(node):
	return


def nodeWorldRotation(node):
	return
