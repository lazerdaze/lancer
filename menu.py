# LANCER.MENU
#
#
#
#
#

# Lancer Modules
import lancer
import channelBox.ui
import channelBox.tweenKey
import rig.ui
import rig.skeleton
import rig.skin
import rig.control
import rig.parts
import rig.auto
import anim.stickyFeet
import external

reload(lancer)
reload(rig.skeleton)
reload(rig.skin)
reload(rig.control)
reload(rig.parts)
reload(rig.auto)
reload(channelBox.ui)
reload(channelBox.tweenKey)
reload(anim.stickyFeet)
reload(external)

# Python Modules
import os

# Maya Modules
from maya import cmds, mel


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


def externalMeshSymmetry(*args):
	PATH = os.path.join(lancer.DIRPATH, 'external', 'abSymMesh.mel').replace('\\', '/')
	mel.eval('source "{}";'.format(PATH))
	mel.eval('abSymMesh;')
	return


def externalSmoothSkinWeight(*args):
	from external import averageVertexSkinWeightBrush
	reload(averageVertexSkinWeightBrush)
	averageVertexSkinWeightBrush.paint()
	# from external import tf_smoothSkinWeight
	# reload(tf_smoothSkinWeight)
	# tf_smoothSkinWeight.paint()
	return


def externalNGSkinTools(*args):
	from external.ngSkinTools.ui.mainwindow import MainWindow
	MainWindow.open()
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

	cmds.menuItem(d=True, l='Animation')
	cmds.menuItem(l='Tween Key', c=channelBox.tweenKey.windowQt)
	cmds.menuItem(l='Sticky Feet', c=anim.stickyFeet.ui)

	cmds.menuItem(d=True, l='External')
	cmds.menuItem(l='Mesh Symmetry', c=externalMeshSymmetry)
	cmds.menuItem(l='Smooth Weights Tool', c=externalSmoothSkinWeight, enable=lancer.EXTERNALPLUGINS)
	cmds.menuItem(l='NG Skin Weights Tool', c=externalNGSkinTools, enable=lancer.EXTERNALPLUGINS)

	return ui
