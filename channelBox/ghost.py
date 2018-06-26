# LANCER.PIPELINE.GHOST
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

WINDOWNAME = 'ghostWinUI'
WINDOWTITLE = 'Ghost'
WINDOWHEIGHT = 10
WINDOWWIDTH = 390

GROUPNAME = 'scene_ghost_grp'

PADDING = 5
MARGIN = 10
COLUMN = 60


class component(object):
	ghost = 'ghost'


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################


def createMasterGroup(*args):
	if cmds.objExists(GROUPNAME):
		return GROUPNAME
	else:
		return cmds.group(name=GROUPNAME, em=True)


def deleteMasterGroup(*args):
	if cmds.objExists(GROUPNAME):
		cmds.delete(GROUPNAME)
	return


def createGhost(*args):
	selected = cmds.ls(sl=True)

	if selected:
		obj = selected[0]
		ghost = cmds.duplicate(obj, name='ghost#', rc=True)[0]
		cmds.setAttr('{}.template'.format(ghost), 1)
		cmds.parent(ghost, createMasterGroup())
		cmds.select(obj)
		return ghost
	else:
		return None


def autoRow(*args):
	form = cmds.formLayout(nd=100)
	cmds.setParent('..')

	length = float(len(args))
	step = 100 / length

	i = 0
	for x in args:

		if cmds.control(x, q=True, exists=True):
			x = cmds.control(x, e=True, p=form)

		elif cmds.layout(x, q=True, exists=True):
			x = cmds.layout(x, e=True, p=form)

		if i == 0:
			cmds.formLayout(form, edit=True, attachForm=[(x, 'left', 0), (x, 'top', 0), (x, 'bottom', 0), ],
			                attachPosition=[(x, 'right', 1, step), ], )

		else:
			cmds.formLayout(form, edit=True,
			                attachForm=[(x, 'top', 0), (x, 'bottom', 0), ],
			                attachControl=[(x, 'left', 2, args[i - 1]), ],
			                attachPosition=[(x, 'right', 1, step), ]
			                )

		step += 100 / length
		i += 1

	return form


########################################################################################################################
#
#
#	UI
#
#
########################################################################################################################

class ui:
	def __init__(self):

		col = cmds.columnLayout(adj=True)
		cmds.frameLayout(lv=False)
		b1 = cmds.button(l='Create', c=self.create)
		b2 = cmds.button(l='Delete All', c=self.delete)
		autoRow(b1, b2)

		self.objectUI = cmds.textScrollList(sc=lambda *x: self.select(self.objectUI))
		self.ghostUI = cmds.textScrollList(sc=lambda *x: self.select(self.ghostUI))
		listUI = autoRow(self.objectUI, self.ghostUI)

		cmds.setParent('..')
		cmds.setParent('..')

		self.startup()

	def create(self, *args):
		selected = cmds.ls(sl=True)
		if selected:
			selected = selected[0]
			allObjects = cmds.textScrollList(self.objectUI, q=True, ai=True)

			if allObjects is None or selected not in allObjects:
				cmds.textScrollList(self.objectUI, e=True, append=str(selected))

		ghost = createGhost()
		if ghost:
			cmds.textScrollList(self.ghostUI, e=True, append=str(ghost))
		return

	def select(self, ui, *args):
		obj = cmds.textScrollList(ui, q=True, si=True)
		if obj:
			obj = obj[0]

			if cmds.objExists(obj):
				cmds.select(obj)
		return

	def startup(self):
		if cmds.objExists(GROUPNAME):
			children = cmds.listRelatives(GROUPNAME, children=True)
			if children:
				for child in children:
					cmds.textScrollList(self.ghostUI, e=True, append=str(child))
		return

	def delete(self, *args):
		deleteMasterGroup()
		cmds.textScrollList(self.objectUI, e=True, ra=True)
		cmds.textScrollList(self.ghostUI, e=True, ra=True)
		return


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
	            t=WINDOWTITLE,
	            rtf=True,
	            h=WINDOWHEIGHT,
	            w=WINDOWWIDTH,
	            )

	ui()

	cmds.showWindow(WINDOWNAME)
	return
