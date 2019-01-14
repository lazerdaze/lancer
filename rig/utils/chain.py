# Lancer Modules
from naming import *
from wire import *
from attribute import *
from node import *
from joint import *
from control import *

# Maya Modules
from maya import cmds

'''
Chain Class represents a list of objects.
'''


def jointChain(*args, **kwargs):
	children = kwargs.get('children', [])

	for arg in args:
		if isinstance(arg, (list, dict, tuple)):
			for item in arg:
				jointChain(item, children=children)
		elif isinstance(arg, str):
			if cmds.nodeType(arg) == 'joint':
				children.append(Joint(name=arg))
	return children


def jointLeafChain(*args, **kwargs):
	children = kwargs.get('children', [])

	for arg in args:
		if isinstance(arg, (list, dict, tuple)):
			for item in arg:
				jointLeafChain(item, children=children)
		elif isinstance(arg, str):
			if cmds.nodeType(arg) == 'joint':
				children.append(cmds.listRelatives(arg, children=True, type='joint'))
	return children


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

		if isinstance(children, list):
			self.children = children
		elif isinstance(children, (dict, tuple)):
			self.children = [x for x in children]
		elif isinstance(children, str):
			self.children = [children]
		elif children is None:
			self.children = []
		else:
			raise TypeError('Must pass iter or str.')

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

	def append(self, child):
		self.children.append(child)
		return

	def remove(self, joint):
		if joint in self.children:
			self.children.remove(joint)
		return


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
	             prefix=None,
	             name='rig',
	             axis=None,
	             scale=1,
	             index=None,
	             side=None,
	             sector=None,
	             ):
		Chain.__init__(self, children=jointChain(children))

		self.name = name
		self.prefix = prefix
		self.axis = axis
		self.scale = scale
		self.index = index
		self.side = side
		self.sector = sector

		self.control = []
		self.master = None

		self.createMasterControl()

	def create(self, item):
		return

	def createMasterControl(self):
		lastChild = self.children[-1]
		self.master = Control(prefix=self.prefix,
		                      name=self.name,
		                      kind=Component.master,
		                      wire=WireType.lollipop,
		                      axis=[0, 1, 1],
		                      scale=self.scale,
		                      index=self.index,
		                      side=self.side,
		                      sector=self.sector,
		                      color=WireColor.purple,
		                      )

		self.master.snapTo(lastChild, translation=True, rotation=True)
		lockKeyableAttributes(self.master.transform, hide=True)
		return
