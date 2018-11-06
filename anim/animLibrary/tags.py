# AXEL.TAGS
#
#
#
#
#

# Python Modules
import os
import sys
import json

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance

# Maya Modules
from maya import cmds, mel, OpenMayaUI

########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################

WINNAME = 'axelTagsWindowUI'

PEOPLE = ['male',
		  'female',
		  'adult',
		  'child',
		  'elderly',
		  'baby',
		  ]

CHARACTER = ['biped',
			 'quadruped'
			 'monster',
			 'creature',
			 'zombie',
			 'hero',
			 'villian',
			 'robot',
			 ]

ANIMAL = ['bird',
		  'cat',
		  'dog',
		  'horse',
		  'mammal',
		  'fish',
		  'reptile',
		  'rabbit',
		  'fox',
		  'wolf',
		  'bear',
		  'tiger'
		  ]

ACTION = ['walk',
		  'run',
		  'sit',
		  'climb',
		  'jump',
		  'crawl',
		  'fall',
		  'die',
		  'hit',
		  'punch',
		  'kick',
		  'attack',
		  'block',
		  'eat',
		  'talk',
		  'interact',
		  'exercise',
		  'flip',
		  'push',
		  'pull',
		  'pick up',
		  'put down',
		  'drop',
		  'roll',
		  'shoot',
		  'hurt',
		  'laugh',
		  'cry',
		  'swim',
		  'reload',
		  ]

SPORT = ['hockey',
		 'baseball',
		 'basketball',
		 'football',
		 'soccer',
		 'tennis',
		 ]

ALLTAGS = ['character', 'animal', 'people', 'sport', 'action'] + PEOPLE + CHARACTER + ANIMAL + ACTION + SPORT


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################


def buildDefaultList():
	var = {}

	for tag in PEOPLE:
		var[tag] = 'people'

	for tag in ANIMAL:
		var[tag] = 'animal'

	for tag in CHARACTER:
		var[tag] = 'character'

	for tag in ACTION:
		var[tag] = 'action'

	for tag in SPORT:
		var[tag] = 'sport'

	return var


########################################################################################################################
#
#
#	USER INTERFACE
#
#
########################################################################################################################



def getMayaWindow():
	mayaPtr = OpenMayaUI.MQtUtil.mainWindow()
	mayaWindow = wrapInstance(long(mayaPtr), QWidget)
	return mayaWindow




########################################################################################################################
#
#
#	Line Edit
#
#
########################################################################################################################


class TagLineEdit(QFrame):
	added = Signal(str)

	def __init__(self, *args, **kwargs):
		QFrame.__init__(self, *args, **kwargs)

		# Layout
		self.setLayout(QHBoxLayout())
		self.layout().setContentsMargins(0, 0, 0, 0)
		self.layout().setSpacing(0)

		# Line Edit
		self.lineEdit = QLineEdit()
		self.lineEdit.setPlaceholderText('Tags')
		self.lineEdit.setFocusPolicy(Qt.ClickFocus)
		self.completer = QCompleter()
		self.lineEdit.setCompleter(self.completer)
		self.model = QStringListModel()
		self.model.setStringList(ALLTAGS)
		self.completer.setModel(self.model)


		self.layout().addWidget(self.lineEdit)
		self.lineEdit.returnPressed.connect(self.callback)

		# Add Button
		self.addButton = QToolButton()
		self.addButton.setText('+')
		self.addButton.clicked.connect(self.callback)
		self.layout().addWidget(self.addButton)

	def callback(self):
		text = self.lineEdit.text()

		if text:
			self.append(text)
			self.added.emit(text)
			self.clear()
		return

	def clear(self):
		self.lineEdit.clear()
		return

	def append(self, text):
		tags = self.model.stringList()
		tags.append(text)
		self.model.setStringList(tags)
		return

########################################################################################################################
#
#
#	Flow Layout
#
#
########################################################################################################################


class FlowLayout(QLayout):
	def __init__(self, *args, **kwargs):
		QLayout.__init__(self, *args, **kwargs)
		self.itemList = []

	def __del__(self):
		item = self.takeAt(0)
		while item:
			item = self.takeAt(0)
		return

	def addItem(self, item):
		self.itemList.append(item)

	def count(self):
		return len(self.itemList)

	def itemAt(self, index):
		if index >= 0 and index < len(self.itemList):
			return self.itemList[index]
		return None

	def takeAt(self, index):
		if index >= 0 and index < len(self.itemList):
			return self.itemList.pop(index)
		return None

	def expandingDirections(self):
		return Qt.Orientations(Qt.Orientation(0))

	def hasHeightForWidth(self):
		return True

	def heightForWidth(self, width):
		height = self.doLayout(QRect(0, 0, width, 0), True)
		return height

	def setGeometry(self, rect):
		super(FlowLayout, self).setGeometry(rect)
		self.doLayout(rect, False)

	def sizeHint(self):
		return self.minimumSize()

	def minimumSize(self):
		size = QSize()

		for item in self.itemList:
			size = size.expandedTo(item.minimumSize())

		size += QSize(2 * self.margin(), 2 * self.margin())
		return size

	def minimumSize(self):
		w = self.geometry().width()
		h = self.doLayout(QRect(0, 0, w, 0), True)
		return QSize(w + 2 * self.margin(), h + 2 * self.margin())

	def doLayout(self, rect, testOnly=False):
		"""
		"""
		x = rect.x()
		y = rect.y()
		lineHeight = 0

		for item in self.itemList:
			wid = item.widget()
			spaceX = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton,
																Qt.Horizontal)
			spaceY = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton,
																Qt.Vertical)
			nextX = x + item.sizeHint().width() + spaceX
			if nextX - spaceX > rect.right() and lineHeight > 0:
				x = rect.x()
				y = y + lineHeight + spaceY
				nextX = x + item.sizeHint().width() + spaceX
				lineHeight = 0

			if not testOnly:
				item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

			x = nextX
			lineHeight = max(lineHeight, item.sizeHint().height())

		return y + lineHeight - rect.y()


class TagButtonFlowLayout(FlowLayout):
	def __init__(self, *args, **kwargs):
		FlowLayout.__init__(self, *args, **kwargs)
		self.tags = []

	def add(self, label):
		self.tags.append(label)
		button = TagButton(label)
		button.closed.connect(self.remove)
		self.addWidget(button)
		return

	def remove(self):
		print 'something'
		return

	def clear(self):
		return


class ResizeScrollArea(QScrollArea):
	"""
	A QScrollArea that propagates the resizing to any FlowLayout children.
	"""

	def __init(self, parent=None):
		QScrollArea.__init__(self, parent)

	def resizeEvent(self, event):
		wrapper = self.findChild(QWidget)
		flow = wrapper.findChild(FlowLayout)

		if wrapper and flow:
			width = self.viewport().width()
			height = flow.heightForWidth(width)
			size = QSize(width, height)
			point = self.viewport().rect().topLeft()
			flow.setGeometry(QRect(point, size))
			self.viewport().update()

		super(ResizeScrollArea, self).resizeEvent(event)


class ScrollingFlowWidget(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent=parent)
		grid = QGridLayout(self)
		scroll = ResizeScrollArea()
		self._wrapper = QWidget(scroll)
		self.flowLayout = FlowLayout(self._wrapper)
		self._wrapper.setLayout(self.flowLayout)
		scroll.setWidget(self._wrapper)
		scroll.setWidgetResizable(True)
		grid.addWidget(scroll)

	def addWidget(self, widget):
		self.flowLayout.addWidget(widget)
		widget.setParent(self._wrapper)


class TagButton(QFrame):
	clicked = Signal(bool)
	closed = Signal(bool)

	def __init__(self, label='Button', *args, **kwargs):
		QFrame.__init__(self, *args, **kwargs)

		# Widget
		self.setObjectName('TagButton')
		self.setMouseTracking(True)
		self.setStyleSheet('''
				TagButton{
				background:red;
				border-radius:5;
				margin:0;
				padding:5;
				}
				''')

		# Layout
		self.setLayout(QHBoxLayout())
		self.layout().setContentsMargins(0, 0, 0, 0)
		self.layout().setSpacing(10)

		# Label
		self.label = QLabel()
		if label:
			self.label.setText(label)
		self.label.setStyleSheet('''
		background:none;
		border:none;
		padding:0;
		''')
		self.layout().addWidget(self.label)

		# Close Button
		self.closeButton = QPushButton('X')
		self.closeButton.setStyleSheet('''
				background:none;
				border:none;
				margin:0;
				padding:0;
				color:white;
				''')
		self.layout().addWidget(self.closeButton)
		self.closeButton.clicked.connect(self.delete)

	def mousePressEvent(self, event):
		self.clicked.emit(True)
		return

	def delete(self):
		self.closed.emit(True)
		return


class AssignedTagsWidget(QWidget):
	def __init__(self, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)
		self.items = []
		self.tags = []

		# Main Layout
		self.flowLayout = TagButtonFlowLayout()
		self.setLayout(self.flowLayout)

	def add(self, text):
		self.tags.append(text)
		self.flowLayout.add(text)


class Widget(QWidget):
	def __init__(self, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)

		# Main Layout
		self.setLayout(QVBoxLayout())

		#
		self.assignedWidget = AssignedTagsWidget()
		self.layout().addWidget(self.assignedWidget)


def showWindow(name=WINNAME, title='Tags Editor'):
	app = QApplication(sys.argv)

	# Window
	window = QMainWindow()
	window.setObjectName(name)
	window.setWindowTitle(title)

	# Widget
	widget = QWidget()
	layout = QVBoxLayout(widget)
	window.setCentralWidget(widget)

	# Controls
	lineEdit = TagLineEdit()
	layout.addWidget(lineEdit)

	assigned = AssignedTagsWidget()
	layout.addWidget(assigned)

	lineEdit.added.connect(assigned.add)

	# Show UI
	window.show()
	app.exec_()
	return


showWindow()
