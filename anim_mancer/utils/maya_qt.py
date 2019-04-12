# Project Modules

# Maya Modules
from maya import OpenMaya, OpenMayaUI, cmds, mel

# Qt Modules
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import shiboken2 as shiboken

# Python Modules
import difflib

# ======================================================================================================================
#
#
# Global
#
#
# ======================================================================================================================

CHANNELBOX = "mainChannelBox"
CHANNELBOX_SEARCH = "mainChannelBoxSearch"


# ======================================================================================================================
#
#
# Function
#
#
# ======================================================================================================================

def maya_to_qt(name, *args, **kwargs):
	"""
	Maya to QWidget

	:param str name:    Maya name of an ui object
	:return:            QWidget of parsed Maya name
	:rtype:             QWidget
	"""
	ptr = OpenMayaUI.MQtUtil.findControl(name)
	if ptr is None:
		ptr = OpenMayaUI.MQtUtil.findLayout(name)
	if ptr is None:
		ptr = OpenMayaUI.MQtUtil.findMenuItem(name)
	if ptr is not None:
		return shiboken.wrapInstance(long(ptr), QWidget)
	return ptr


def qt_to_maya(widget, *args, **kwargs):
	"""
	QWidget to Maya name

	:param QWidget widget:  QWidget of a maya ui object
	:return:                Maya name of parsed QWidget
	:rtype:                 str
	"""
	return OpenMayaUI.MQtUtil.fullName(long(shiboken.getCppPointer(widget)[0]))


def get_channelbox(*args, **kwargs):
	"""
	Get ChannelBox, convert the main channel box to QT.

	:return: Maya's main channel box
	:rtype: QWidget
	"""
	channelBox = maya_to_qt(CHANNELBOX)
	return channelBox


def get_channelbox_menu():
	"""
	Get ChannelBox, convert the main channel box to QT and return the QMenu
	which is part of the channel box' children.

	:return: Maya's main channel box menu
	:rtype: QMenu
	"""
	channelBox = get_channelbox()
	
	for child in channelBox.children():
		if type(child) == QMenu:
			cmd = "generateChannelMenu {0} 1".format(qt_to_maya(child))
			mel.eval(cmd)
			return child


def search_mel_variables(searchString=None, *args, **kwargs):
	"""
	Loop over all global MEL variables and if a search string is provided
	print only the global MEL variables that match the search string.

	:param str/None search_string:
	"""
	for var in sorted(mel.eval("env")):
		if not searchString or var.lower().count(searchString):
			yield var

# ======================================================================================================================
#
#
# Class
#
#
# ======================================================================================================================


# ======================================================================================================================
#
#
# Execute
#
#
# ======================================================================================================================

if __name__ == '__main__':
	pass
