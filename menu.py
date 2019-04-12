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
import rig
import rig.parts
import rig.legacy.ui
import rig.utils.skeleton
import rig.utils.joint
import rig.utils.skin
import rig.utils.control
import rig.auto
import rig.poseSDK.ui
import rig.menu
import anim.stickyFeet
import anim.refPlayer.ui
import anim.refman
import shows

# Python Modules
import os

# Qt Modules
QTLOADED = False

try:
	import PySide2
	QTLOADED = True

except ImportError:
	try:
		from library import Qt
		QTLOADED = True

	except ImportError:
		raise ImportError('Unable to load Qt.')

# Maya Modules
from maya import cmds, mel


def rigUI(*args):
	reload(rig.legacy.ui)
	rig.legacy.ui.show()
	return


def channelBoxUI(*args):
	reload(channelBox.ui)
	channelBox.ui.show()
	return


def refreshLancer(*args):
	import lancer.menu
	reload(lancer.menu)
	lancer.menu.show()

	import refresh
	refresh.resetSessionForScript()
	print 'Lancer successfully reloaded.',
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

def referencePlayer(*args):
	reload(anim.refPlayer.ui)
	anim.refPlayer.ui.windowUI()
	return

def show(*args):
	name = 'LancerMenu'
	deletUI(name)

	ui = cmds.menu(name, label='Lancer', parent='MayaWindow', tearOff=True)
	cmds.menuItem(d=True, l='UI')
	cmds.menuItem(l='Refresh', c=refreshLancer)
	cmds.menuItem(label='Channel Box +', c=channelBoxUI)
	cmds.menuItem(d=True, l='Rigging')
	cmds.menuItem(label='Rig Tools', c=rigUI)
	rig.menu.menuItems()

	cmds.menuItem(l='Facial', subMenu=True, to=True)
	rig.poseSDK.ui.menu()
	cmds.setParent('..', menu=True)

	shows.sub_menu()

	cmds.menuItem(d=True, l='Animation')
	cmds.menuItem(l='Tween Key', c=channelBox.tweenKey.windowQt)
	cmds.menuItem(l='Sticky Feet', c=anim.stickyFeet.ui)
	cmds.menuItem(l='Reference Manager', c=anim.refman.show)
	cmds.menuItem(l='Reference Player', c=referencePlayer, enable=QTLOADED)

	cmds.menuItem(d=True, l='External')
	cmds.menuItem(l='Mesh Symmetry', c=externalMeshSymmetry)
	cmds.menuItem(l='Smooth Weights Tool', c=externalSmoothSkinWeight, enable=lancer.EXTERNALPLUGINS)
	cmds.menuItem(l='NG Skin Weights Tool', c=externalNGSkinTools, enable=lancer.EXTERNALPLUGINS)
	return ui
