# LANCER.RIG.FACEPOSE.UI
#
#
#
#
#


import core
reload(core)

# Maya Modules
from maya import cmds


########################################################################################################################
#
#
#	MIRROR / DUPLICATE / COPY
#
#
########################################################################################################################


def updateTextField(ui, *args):
	selected = cmds.ls(sl=True)

	if not selected:
		cmds.textFieldButtonGrp(ui, e=True, tx='')
		return
	else:
		cmds.textFieldButtonGrp(ui, e=True, tx=selected[0])
		return


def mirrorUI(*args):
	winName = 'facePoseMirrorWindowUI'
	if cmds.window(winName, exists=True):
		cmds.deleteUI(winName, wnd=True)

	cmds.window(winName, t='Mirror SDK', s=False)
	cmds.columnLayout(adj=True)
	stex = cmds.textFieldButtonGrp(l='Source: ', bl='<<', bc=lambda *x: updateTextField(stex))
	dtex = cmds.textFieldButtonGrp(l='Destination: ', bl='<<', bc=lambda *x: updateTextField(dtex))
	cmds.separator(h=20)
	cmds.text(l='Mirror Table')
	cmds.separator(st='none', h=20)
	sString = cmds.textFieldGrp(l='Search For: ', tx='L_')
	dString = cmds.textFieldGrp(l='Replace With: ', tx='R_')

	cmds.separator(st='none', h=20)
	cmds.button(l='Apply', c=lambda *x: core.mirror(parent=cmds.textFieldButtonGrp(stex, q=True, tx=True),
	                                                child=cmds.textFieldButtonGrp(stex, q=True, tx=True),
	                                                parentString=cmds.textFieldGrp(sString, q=True, tx=True),
	                                                childString=cmds.textFieldGrp(dString, q=True, tx=True),
	                                                ))

	cmds.setParent('..')

	cmds.showWindow(winName)
	return


########################################################################################################################
#
#
#	MENU
#
#
########################################################################################################################

def menu():
	cmds.menuItem(l='Mirror SDK', c=mirrorUI)
	return
