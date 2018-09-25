# LANCER.ANIM.ANIMLIBRARY
#
#
#
#
#

# Lancer Modules
from ... import MAYAVERSION
from library import xfer

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance

# Python Modules
import os
import platform

# Maya Modules
from maya import cmds, mel, OpenMayaUI


########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################
WIDTH = 800
HEIGHT = 600

########################################################################################################################
#
#
#	SHOW USER INTERFACE
#
#
########################################################################################################################


def getMayaWindow(*args):
	mayaPtr = OpenMayaUI.MQtUtil.mainWindow()
	mayaWindow = wrapInstance(long(mayaPtr), QWidget)
	return mayaWindow


def window(*args):
	winName = 'animLibraryWindowUI'
	if cmds.window(winName, exists=True):
		cmds.deleteUI(winName, wnd=True)

	# Window
	window = QMainWindow(getMayaWindow())
	window.setObjectName(winName)
	window.setWindowTitle('Animation Library')
	window.setMinimumSize(WIDTH, HEIGHT)

	# Widget
	widget = QWidget()
	layout = QVBoxLayout(widget)
	window.setCentralWidget(widget)

	# Controls
	# layout.addWidget(control().widget)

	# Show UI
	window.show()
	return


def show():
	if MAYAVERSION == 2018:
		window()
		return
	else:
		cmds.error('Animation Library only works with Maya Version 2018.')
		return
