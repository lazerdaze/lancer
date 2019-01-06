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


########################################################################################################################
#
#
#	User-Defined Errors
#
#
########################################################################################################################

class Error(Exception):
	pass


class NodeExistsError(Error):
	pass


########################################################################################################################
#
#
#	Base Node Class
#
#
########################################################################################################################

class Node(object):
	def __init__(self, parent=None, name=None, kind=None, children=None, exists=False):
		self.name = name
		self.kind = kind
		self.parent = parent
		self.children = children if children is list else []
		self.exists = exists

		self.transform = None
		self.shape = None

		self.translateX = 0
		self.translateY = 0
		self.translateZ = 0
		self.rotateX = 0
		self.rotateY = 0
		self.rotateZ = 0
		self.scaleX = 0
		self.scaleY = 0
		self.scaleZ = 0
		self.visibility = 1

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

	def getKind(self):
		return self.kind

	def setKind(self, kind):
		self.kind = kind
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

	def setExists(self, exists):
		self.exists = exists
		return

	def getExists(self):
		return self.exists

	def isValid(self):
		if self.name:
			self.exists = utils.nodeExists(self.name)
			return self.exists
		self.exists = False
		return self.exists

	def populateFromScene(self):
		if self.isValid():
			# self.parent = utils.nodeParent(self.name)
			self.kind = utils.nodeType(self.name)

			children = utils.nodeChildren(self.name)

			if children:
				for child in children:
					childNode = Node(parent=self, name=child)
					childNode.populateFromScene()
					self.appendChild(childNode)
		return
