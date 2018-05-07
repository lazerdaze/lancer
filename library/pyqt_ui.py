# Qt Modules
from library.Qt import QtGui, QtCore, QtWidgets
import shiboken2

# Maya Modules
from maya import cmds
import maya.OpenMayaUI as mui


########################################################################################################################
#
#
#	WINDOW CLASS
#
#
########################################################################################################################


def getMayaWindow():
	pointer = mui.MQtUtil.mainWindow()
	return shiboken2.wrapInstance(long(pointer), QtWidgets.QWidget)


def deleteExistingWindow(winName='Window'):
	if cmds.window(winName, exists=True):
		cmds.deleteUI(winName, wnd=True)
	return


class Window:
	def __init__(self, name='Window'):
		self.name = name
		self.parent = getMayaWindow()
		self.window = QtWidgets.QMainWindow(self.parent)

		deleteExistingWindow(self.name)
		self.window.setObjectName(self.name)
		self.window.setWindowTitle(self.name)

		self.widget = QtWidgets.QWidget()
		self.window.setCentralWidget(self.widget)

		self.layout = QtWidgets.QVBoxLayout(self.widget)

	def show(self):
		self.window.show()


########################################################################################################################
#
#
#	FONT CLASS
#
#
########################################################################################################################


class Font:
	def __init__(self, size=12, bold=True):
		self.widget = QtGui.QFont()
		self.widget.setPointSize(size)
		self.widget.setBold(bold)


########################################################################################################################
#
#
#	BUTTON CLASS
#
#
########################################################################################################################


class Button:
	def __init__(self, parent, name='Button', width=200, height=40, command=None, font=None):
		self.parent = parent
		self.name = name
		self.widget = width
		self.height = height
		self.command = command
		self.font = font
		self.widget = QtWidgets.QPushButton(name)

		self.parent.addWidget(self.widget)
		# self.widget.setMinimumSize(width, height)
		# self.widget.setMaximumSize(width, height)
		# self.widget.setStyleSheet("background-color: rgb(128,128,128); color: rgb(0,0,0)")

		if self.command:
			self.widget.clicked.connect(self.command)

		if self.font:
			self.widget.setFont(self.font)
