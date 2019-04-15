# Project Modules
from ui.main import Anim_Mancer, UI_MainWindow, ANIM_MANCER_EXISTS
from utils import *

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Maya Modules
from maya import cmds

WINDOW_NAME = 'anim_mancer_UI_window'


def install(*args, **kwargs):
	am = Anim_Mancer()
	
	if ANIM_MANCER_EXISTS:
		am.uninstall()
		
	am.install()
	return


def uninstall(*args, **kwargs):
	am = Anim_Mancer()
	am.uninstall()
	return


def show(name=WINDOW_NAME, *args, **kwargs):
	if cmds.window(name, exists=True):
		cmds.deleteUI(name, wnd=True)
	
	# Window
	MainWindow = UI_MainWindow(get_maya_window())
	MainWindow.setObjectName(name)
	MainWindow.show()
	return


if __name__ == '__main__':
	pass
