# Python Modules
import sys

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################

def mayaRunning():
	try:
		import maya.cmds as cmds
	except ImportError:
		return False
	else:
		try:
			if cmds.about(batch=True):
				return True
		except AttributeError:
			return False
		else:
			return True


def mayaWindowWrapInstance():
	from maya import cmds, mel, OpenMayaUI
	from shiboken2 import wrapInstance

	mayaPtr = OpenMayaUI.MQtUtil.mainWindow()
	mayaWindow = wrapInstance(long(mayaPtr), QWidget)
	return mayaWindow


def mayaWindowQt():
	app = QApplication.instance()
	return {o.objectName(): o for o in app.topLevelWidgets()}['MayaWindow']


def mayaWindowExists(name):
	from maya import cmds

	if cmds.window(name, exists=True):
		cmds.deleteUI(name, wnd=True)
	return


def standaloneMayaWrapper(window):
	def wrapper(*args, **kwargs):
		name = kwargs.get('name', 'QtWindowUI')

		if mayaRunning():
			mayaWindowExists(name)
			ui = window(parent=mayaWindowWrapInstance(), **kwargs)
			ui.show()
			return

		else:
			app = QApplication(sys.argv)
			ui = window(*args, **kwargs)
			ui.show()
			sys.exit(app.exec_())

	return wrapper

