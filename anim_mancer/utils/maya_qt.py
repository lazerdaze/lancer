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
CHANNELBOX_EDITOR = 'ChannelBoxLayerEditor'


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


def get_channelbox_editor(*args, **kwargs):
	return maya_to_qt(CHANNELBOX_EDITOR)


def get_channelbox(*args, **kwargs):
	"""
	Get ChannelBox, convert the main channel box to QT.

	:return: Maya's main channel box
	:rtype: QWidget
	"""
	return maya_to_qt(CHANNELBOX)


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


def maya_recurse_children(root, *args, **kwargs):
	tree = kwargs.get('tree', {})
	
	children = []
	
	try:
		children = cmds.layout(root, q=True, ca=True)
	except RuntimeError:
		pass
	
	if children:
		for child in children:
			name = child
			
			try:
				name = cmds.layout(child, q=True, fpn=True)
			except RuntimeError:
				try:
					name = cmds.control(child, q=True, fpn=True)
				except RuntimeError:
					pass
			tree[name] = maya_recurse_children(child)
			print name
	
	return tree


def qt_recurse_children(root, *args, **kwargs):
	return


def get_maya_window():
	ptr = OpenMayaUI.MQtUtil.mainWindow()
	if ptr is not None:
		return shiboken.wrapInstance(long(ptr), QWidget)


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
