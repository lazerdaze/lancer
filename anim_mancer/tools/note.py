# LANCER.PIPELINE.NOTE
#
#
#
#
#


# Maya Modules
from maya import cmds, mel

########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################


PADDING = 5
WINDOWHEIGHT = 10
WINDOWWIDTH = 390


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################

def createNode(*args):
	node = cmds.createNode('network', name='sceneNote0')
	cmds.addAttr(node, ln='type', dt='string')
	cmds.setAttr('{}.type'.format(node), 'note', type='string', lock=True)
	cmds.addAttr(node, ln='notes', dt='string')
	cmds.lockNode(node, lock=True)
	return node


def listNodesInScene(*args):
	noteNodes = []
	nodes = cmds.ls(type='network')
	for node in nodes:
		if cmds.attributeQuery('type', node=node, ex=True):
			if cmds.getAttr('{}.type'.format(node)) == 'note':
				noteNodes.append(node)

	return noteNodes if noteNodes else None


def getNotes(node, *args):
	notes = None
	if cmds.attributeQuery('notes', node=node, ex=True):
		notes = cmds.getAttr('{}.notes'.format(node))
	return notes if notes else ''


def deleteNode(node, *args):
	cmds.lockNode(node, lock=False)
	cmds.delete(node)
	return


########################################################################################################################
#
#
#	UI
#
#
########################################################################################################################

WINDOWNAME = 'notewinUI'
WINDOWLAYOUT = 'notelayUI'
DEBUGMODE = False


def menu(*args):
	ui = cmds.menuBarLayout()
	cmds.menu(l='Add')
	cmds.menuItem(l='Edit')
	cmds.menuItem(l='Remove')
	cmds.setParent('..')
	return ui


class widget:
	def __init__(self):
		self.node = self.getAllInScene()
		self.control = cmds.scrollField(font='plainLabelFont', text=self.get(), cc=self.edit)
		cmds.scriptJob(p=self.control, protected=True,
		               e=['NewSceneOpened', self.updateOnNewScene])
		cmds.scriptJob(p=self.control, protected=True,
		               e=['PostSceneRead', self.updateOnOpenScene])

	def add(self):
		nodes = listNodesInScene()
		if nodes:
			return nodes[0]
		else:
			return createNode()

	def get(self):
		if self.node:
			return getNotes(self.node)
		else:
			return ''

	def getAllInScene(self):
		nodes = listNodesInScene()
		return nodes[0] if nodes else None

	def edit(self, *args):
		text = cmds.scrollField(self.control, q=True, text=True)
		if text:
			self.node = self.add()
			cmds.setAttr('{}.notes'.format(self.node), text, type='string')
		return

	def update(self, *args):
		self.node = self.add()
		cmds.scrollField(self.control, e=True, text=self.get())
		return

	def remove(self):
		return

	def updateOnNewScene(self, *args):
		self.node = None
		cmds.scrollField(self.control, e=True, text='')
		self.prompt()
		return

	def updateOnOpenScene(self, *args):
		nodes = listNodesInScene()
		if nodes:
			self.update()
			self.prompt()
		else:
			cmds.scrollField(self.control, e=True, text='')
		return

	def prompt(self):
		text = self.get()
		if text:
			cmds.confirmDialog(title='Scene Notes', ma='left', message='{}\n\n{}'.format('-' * 50, text), button=['OK'],
			                   defaultButton='OK')
		return


def ui():
	form = cmds.formLayout()
	col = widget().control
	cmds.setParent('..')

	cmds.formLayout(form,
	                e=True,
	                attachForm=[
		                [col, 'top', PADDING],
		                [col, 'left', PADDING],
		                [col, 'bottom', PADDING],
		                [col, 'right', PADDING],
	                ],
	                )
	return form


########################################################################################################################
#
#
#	WINDOW
#
#
########################################################################################################################


def window():
	if cmds.window(WINDOWNAME, q=True, ex=True):
		cmds.deleteUI(WINDOWNAME)

	winPref = cmds.windowPref(WINDOWNAME, exists=True)
	if winPref:
		cmds.windowPref(WINDOWNAME, e=True, h=WINDOWHEIGHT, w=WINDOWWIDTH)

	cmds.window(WINDOWNAME,
	            t='Note',
	            rtf=True,
	            h=WINDOWHEIGHT,
	            w=WINDOWWIDTH,
	            )

	ui()

	cmds.showWindow(WINDOWNAME)
	return
