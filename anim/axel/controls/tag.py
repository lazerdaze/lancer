# AXEL.TAGS
#
#
#
#
#
'''
{
tag: {parent: tag, children: [filepath]}
}
'''
# Lancer
from library import xfer

# Python Modules
import os
import sys
import json

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################

WINNAME = 'axelTagsWindowUI'
DIRPATH = os.path.dirname(os.path.abspath(__file__))
SETTINGSPATH = os.path.join(os.path.dirname(DIRPATH), 'config', 'tag_config.json')

PEOPLE = ['male',
          'female',
          'adult',
          'child',
          'elderly',
          'baby',
          'teen',
          ]

CHARACTER = ['biped',
             'quadruped',
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

	tagDict = {
		'people'   : PEOPLE,
		'animal'   : ANIMAL,
		'character': CHARACTER,
		'action'   : ACTION,
		'sport'    : SPORT,
	}
	for tag in tagDict:
		var[tag] = {'children': [], 'parent': ''}

		for child in tagDict[tag]:
			var[child] = {'children': [], 'parent': tag}
	return var


def saveSettingsToPath(filepath, data):
	xfer.write(path=filepath, data=data)
	return


def splitTags(tags):
	tagList = tags.split(',')
	return [tag.strip() for tag in tagList]


########################################################################################################################
#
#
#	Line Edit
#
#
########################################################################################################################


class TagLineEdit(QWidget):
	added = Signal(str)

	def __init__(self, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)

		# Layout
		self.setLayout(QHBoxLayout())
		self.layout().setContentsMargins(0, 0, 0, 0)
		self.layout().setSpacing(0)

		# Line Edit
		self.lineEdit = QLineEdit()
		self.lineEdit.setPlaceholderText('Tags')
		self.lineEdit.setFocusPolicy(Qt.ClickFocus)

		# Completer
		self.completer = QCompleter()
		self.lineEdit.setCompleter(self.completer)
		self.model = QStringListModel()
		self.completer.setModel(self.model)

		self.layout().addWidget(self.lineEdit)
		self.lineEdit.returnPressed.connect(self.callback)

		# Add Button
		self.addButton = QToolButton()
		self.addButton.setText('+')
		self.addButton.clicked.connect(self.callback)
		self.layout().addWidget(self.addButton)

	def setPlaceholderText(self, text):
		self.lineEdit.setPlaceholderText(text)
		return

	def setCompleterList(self, list):
		self.model.setStringList(list)
		return

	def callback(self):
		text = splitTags(self.lineEdit.text())

		if text:
			for tag in text:
				self.append(tag)
				self.clear()
		return

	def clear(self):
		self.lineEdit.clear()
		return

	def append(self, text):
		tags = self.model.stringList()
		if text not in tags:
			tags.append(text)
			self.added.emit(text)
			self.model.setStringList(tags)
		return


########################################################################################################################
#
#
#	TreeView
#
#
########################################################################################################################

class TagTreeView(QTreeView):
	selected = Signal(str)

	def __init__(self, *args, **kwargs):
		QTreeView.__init__(self, *args, **kwargs)

		self.tagDict = {}
		self.itemList = {}
		self.itemOriginName = None
		self.isRenaming = False

		# Model
		headers = ['Tag', '#']
		self.setModel(QStandardItemModel())
		self.model().setHorizontalHeaderLabels(headers)
		self.root = self.model().invisibleRootItem()
		self.setColumnWidth(0, 200)
		self.setColumnWidth(1, 1)

		# Settings
		self.setHeaderHidden(False)
		self.setDragDropMode(QAbstractItemView.InternalMove)
		self.setAlternatingRowColors(True)
		self.setDropIndicatorShown(False)
		self.setFocusPolicy(Qt.NoFocus)
		self.setAnimated(False)
		self.setFrameShape(QFrame.NoFrame)
		self.setEditTriggers(False)
		self.setContextMenuPolicy(Qt.CustomContextMenu)
		self.header().setSectionResizeMode(0, QHeaderView.Stretch)
		self.header().setSectionResizeMode(1, QHeaderView.Fixed)
		self.header().setStretchLastSection(False)

		# Slots
		self.clicked[QModelIndex].connect(self.getSelected)
		self.customContextMenuRequested.connect(self.popupMenu)
		self.model().itemChanged.connect(self.rename)

		# Loading
		self.loadSettings()
		self.setSortingEnabled(True)
		self.sortByColumn(0, Qt.AscendingOrder)
		self.resizeColumnToContents(1)

	def refresh(self):
		self.clear()
		self.loadItems()
		return

	def appendChildToTag(self, tag, child):
		if tag in self.tagDict:
			self.tagDict[tag]['children'].append(child)
		return

	def removeChildFromTag(self, tag, child):
		if tag in self.tagDict:
			self.tagDict[tag]['children'].remove(child)
		return

	def editSelected(self, index):
		self.isRenaming = True
		self.itemOriginName = self.model().itemFromIndex(index).text()
		self.edit(index)
		return

	def rename(self, item):
		if self.isRenaming:
			oldName = self.itemOriginName
			newName = item.text()

			self.itemList[newName] = self.itemList[oldName]
			del self.itemList[oldName]

			self.tagDict[newName] = self.tagDict[oldName]
			del self.tagDict[oldName]

			index = self.model().indexFromItem(item)
			rowCount = self.model().rowCount(index)

			if rowCount:
				for row in range(0, rowCount + 1):
					rowIndex = self.model().index(row, 0, index)
					rowItem = self.model().itemFromIndex(rowIndex)

					if rowItem:
						rowName = rowItem.text()
						self.tagDict[rowName]['parent'] = newName
		self.isRenaming = False
		return

	def dropEvent(self, event):
		super(QTreeView, self).dropEvent(event)

		index = self.selectedIndexes()[0]
		item = self.model().itemFromIndex(index)
		name = item.text()

		parentIndex = self.indexAt(event.pos())
		parentItem = self.model().itemFromIndex(parentIndex)
		parentName = parentItem.text() if parentItem else None

		self.tagDict[name] = {'parent': parentName, 'children': self.tagDict[name]['children']}
		return

	def popupMenu(self, position):
		indexes = self.selectedIndexes()

		if len(indexes) > 0:
			index = indexes[0]

			menu = QMenu(self)
			menu.setWindowFlags(Qt.Popup | Qt.NoDropShadowWindowHint)
			actionRename = menu.addAction('Rename')
			actionRename.triggered.connect(lambda *x: self.editSelected(index))
			menu.addSeparator()
			actionRemove = menu.addAction('Remove')
			actionRemove.triggered.connect(lambda *x: self.remove(index))
			menu.exec_(self.viewport().mapToGlobal(position))
		return

	def loadSettings(self):
		self.tagDict = xfer.read(SETTINGSPATH)
		self.loadItems()
		return

	def loadDefaultSettings(self):
		self.tagDict = buildDefaultList()
		self.loadItems()
		return

	def saveSettings(self):
		xfer.write(SETTINGSPATH, self.tagDict)
		return

	def getSelected(self, index):
		item = self.model().itemFromIndex(index)
		self.selected.emit(item.data())
		return

	def clear(self):
		self.model().clear()
		self.itemList = {}
		return

	def createItem(self, parent=None, name='tag', children=[]):
		if name not in self.itemList:
			if parent:
				if parent not in self.itemList:
					parentItem = self.createItem(parent=None, name=parent)
				else:
					parentItem = self.itemList[parent]
			else:
				parentItem = self.root

			row = [QStandardItem(name), QStandardItem(str(len(children)))]
			row[0].setData(children)

			if type(parentItem) is list:
				parentItem[0].appendRow(row)
			else:
				parentItem.appendRow(row)

			self.itemList[name] = row
			self.tagDict[name] = {'parent': parent, 'children': children}

			return row
		return self.itemList[name]

	def loadItems(self):
		if self.tagDict:
			for item in self.tagDict:

				if type(self.tagDict) is dict:
					parent = self.tagDict[item]['parent']
					children = self.tagDict[item]['children']
					self.createItem(parent=parent, name=item, children=children)

				elif type(self.tagDict) is list:
					row = QStandardItem(item)
					self.root.appendRow(row)
					self.itemList[item] = row
		return

	def add(self, name=''):
		if name and name not in self.itemList:
			selected = self.selectionModel().selectedIndexes()
			if selected:
				parent = self.model().itemFromIndex(selected[0]).text()
				self.setExpanded(selected[0], True)
			else:
				parent = None
			self.createItem(parent=parent, name=name)

		return

	def remove(self, index):
		name = self.model().itemFromIndex(index).text()
		rowCount = self.model().rowCount(index)

		if rowCount:
			for row in range(0, rowCount + 1):
				rowIndex = self.model().index(row, 0, index)
				rowItem = self.model().itemFromIndex(rowIndex)

				if rowItem:
					rowName = rowItem.text()
					if rowName in self.tagDict:
						del self.tagDict[rowName]

					if rowName in self.itemList:
						del self.itemList[rowName]

			self.model().removeRows(0, rowCount, index)
		self.removeSelected(index)
		return

	def removeSelected(self, index):
		name = self.model().itemFromIndex(index).text()
		parent = self.model().parent(index)

		for row in range(0, self.model().rowCount(parent) + 1):
			rowIndex = self.model().index(row, 0, parent)
			rowItem = self.model().itemFromIndex(rowIndex)
			rowName = rowItem.text()

			if name == rowName:
				self.model().removeRow(row, parent)
				if name in self.tagDict:
					del self.tagDict[name]
				if name in self.itemList:
					del self.itemList[name]
				break
		return

	def setTagDict(self, dict):
		self.tagDict = dict
		return

	def getTagDict(self):
		return self.tagDict


class TagEditor(QFrame):
	def __init__(self, *args, **kwargs):
		QFrame.__init__(self, *args, **kwargs)

		# Layout
		self.setLayout(QVBoxLayout())
		self.layout().setSpacing(10)
		self.layout().setContentsMargins(0, 0, 0, 0)

		# Line Edit
		self.lineEdit = TagLineEdit()
		self.lineEdit.setPlaceholderText('Add Tags (e.g., walk, run, jump)')
		self.layout().addWidget(self.lineEdit)

		# Tree
		self.tree = TagTreeView()
		self.tree.setHeaderHidden(True)
		self.layout().addWidget(self.tree)

		self.lineEdit.setCompleterList([x for x in self.tree.getTagDict()])

		# Slots
		self.lineEdit.added.connect(self.tree.add)




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

	def remove(self, label):
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
		self.tags.append(str(text))
		self.flowLayout.add(str(text))


def showStandalone(name=WINNAME, title='Tags Editor'):
	app = QApplication(sys.argv)

	# Window
	window = QMainWindow()
	window.setObjectName(name)
	window.setWindowTitle(title)

	# Widget
	widget = QWidget()
	layout = QVBoxLayout(widget)
	window.setCentralWidget(widget)

	# Tree View
	editor = TagEditor()
	layout.addWidget(editor)

	# Show UI
	window.show()
	app.exec_()
	return


if __name__ == '__main__':
	showStandalone()
