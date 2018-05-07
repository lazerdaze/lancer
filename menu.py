# LANCER.MENU
#
#
#
#
#

# Lancer Modules
import rig.ui
import channelBox.ui
import rig.skeleton
import rig.skin
import rig.control
import rig.parts
import rig.auto

reload(rig.skeleton)
reload(rig.skin)
reload(rig.control)
reload(rig.parts)
reload(rig.auto)

# Maya Modules
import maya.cmds as cmds


def rigUI(*args):
	reload(rig.ui)
	rig.ui.show()
	return


def channelBoxUI(*args):
	reload(channelBox.ui)
	channelBox.ui.show()
	return


def refresh(*args):
	import lancer.menu
	reload(lancer.menu)
	lancer.menu.show()
	return


def deletUI(name):
	if cmds.menu(name, q=True, ex=True):
		cmds.evalDeferred(lambda *_: cmds.deleteUI(name))
	return


def show(*args):
	name = 'LancerMenu'
	deletUI(name)

	ui = cmds.menu(name, label='Lancer', parent='MayaWindow', tearOff=True)
	cmds.menuItem(d=True, l='UI')
	cmds.menuItem(l='Refresh', c=refresh)
	cmds.menuItem(label='Channel Box +', c=channelBoxUI)
	cmds.menuItem(d=True, l='Rigging')
	cmds.menuItem(label='Rig Tools', c=rigUI)
	cmds.menuItem(l='Skeleton', subMenu=True, to=True)
	rig.skeleton.menu()
	cmds.setParent('..', menu=True)
	cmds.menuItem(l='Skin', subMenu=True, to=True)
	rig.skin.menu()
	cmds.setParent('..', menu=True)
	cmds.menuItem(l='Control', subMenu=True, to=True)
	rig.control.menu()
	cmds.setParent('..', menu=True)
	cmds.menuItem(l='Parts', subMenu=True, to=True)
	rig.parts.menu()
	cmds.setParent('..', menu=True)
	cmds.menuItem(l='Auto', subMenu=True, to=True)
	rig.auto.menu()
	cmds.setParent('..', menu=True)

	return ui
