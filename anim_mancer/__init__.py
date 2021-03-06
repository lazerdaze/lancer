# Project Modules
from ui.main import Anim_Mancer, UI_MainWindow
from utils import *

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Maya Modules
from maya import cmds

# ======================================================================================================================
#
#
# Global
#
#
# ======================================================================================================================



# ======================================================================================================================
#
#
# Function
#
#
# ======================================================================================================================


def install(*args, **kwargs):
	uninstall()
	
	am = Anim_Mancer()
	am.install()
	return


def uninstall(*args, **kwargs):
	am = Anim_Mancer()
	am.uninstall()
	clean_up_instances()
	return


def clean_up_instances(*args, **kwargs):
	for _object in Anim_Mancer.getinstances():
		try:
			_object.uninstall()
		except RuntimeError:
			pass
		del _object
	return


def show(name=UI.window, *args, **kwargs):
	if cmds.window(name, exists=True):
		cmds.deleteUI(name, wnd=True)
	
	# Window
	window = UI_MainWindow(get_maya_window())
	window.setObjectName(name)
	window.show()
	return


# ======================================================================================================================
#
#
# Execute
#
#
# ======================================================================================================================


if __name__ == '__main__':
	pass
