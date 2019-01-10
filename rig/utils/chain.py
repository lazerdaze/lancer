# Lancer Modules
from control import Control
from naming import *
from wire import *
from attribute import *

# Maya Modules
from maya import cmds

'''
Chain Class represents a list of objects.
'''


########################################################################################################################
#
#
#	Base Chain Class
#
#
########################################################################################################################

class Chain(object):
	def __init__(self, children=None):
		self.currentIndex = 0
		self.children = children if isinstance(children, list) else []

	def __str__(self):
		return self.children

	def __repr__(self):
		return self.children

	def __len__(self):
		return len(self.children)

	def __getitem__(self, item):
		return self.children[item]

	def __iter__(self):
		self.currentIndex = 0
		return self

	def __next__(self):
		if self.currentIndex > len(self.children) - 1:
			raise StopIteration
		else:
			self.currentIndex += 1
			return self.children[self.currentIndex - 1]

	def next(self):
		return self.__next__()

	def append(self, joint):
		self.children.append(joint)
		return

	def remove(self, joint):
		if joint in self.children:
			self.children.remove(joint)
		return


########################################################################################################################
#
#
#	Joint Chain Class
#
#
########################################################################################################################

class JointChain(Chain):
	def __init__(self, children):
		Chain.__init__(self, children=children)


########################################################################################################################
#
#
#	Control Chain Class
#
#
########################################################################################################################

class ControlChain(Chain):
	def __init__(self,
	             children,
	             prefix='rig',
	             name=None,
	             axis=None,
	             scale=1,
	             index=None,
	             side=None,
	             sector=None,
	             ):
		Chain.__init__(self, children=children)

		self.name = name
		self.prefix = prefix
		self.axis = axis
		self.scale = scale
		self.index = index
		self.side = side
		self.sector = sector

		self.control = []
		self.masterControl = None

		if self.children:
			self.createMasterControl()

	# for child in self.children:
	# 	self.create(child)

	def create(self, item):
		return

	def createMasterControl(self):
		lastChild = self.children[-1]
		self.masterControl = Control(prefix=self.prefix,
									 name=self.name,
									 item=None,
									 kind=Component.master,
									 wire=WireType.lollipop,
									 axis=[0, 1, 1],
									 scale=self.scale,
									 index=self.index,
									 side=self.side,
									 sector=self.sector,
									 color=WireColor.purple,
									 )

		self.masterControl.snapTo(lastChild, translation=True, rotation=True)
		lockKeyableAttributes(self.masterControl.transform, hide=True)
		return
