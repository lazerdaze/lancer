# AXEL.UI
#
#
#
#
#

# AXEL Modules
from api import *
from thumbnail import *

# Lancer Modules
from library import xfer

reload(xfer)

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Python Modules
import os
import platform
import sys
import gc

# Maya Modules
MAYALOADED = True
try:
	from maya import cmds, mel, OpenMayaUI
	from shiboken2 import wrapInstance
except:
	MAYALOADED = False

########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################

WINDOWNAME = 'animLibraryWindowUI'
TITLE = 'AXEL: Animation XML Export Library'
WIDTH = 800
HEIGHT = 600

ICONSPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons')
DEFAULTTHUMBNAIL = os.path.join(DIRPATH, 'icons', 'thumbnail2.png')


# TESTSEQUENCE = collectSequenceFromFilepath(os.path.join(DIRPATH, 'test', 'testSequence', 'thumbnail.0000.jpg'))


########################################################################################################################
#
#
#	ICONS
#
#
########################################################################################################################

class Icon(object):
	directory = os.path.join(ICONSPATH, 'folder_284.png')
	animation = os.path.join(ICONSPATH, 'icon_white_256.png')
	pose = os.path.join(ICONSPATH, 'icon_white_256.png')


########################################################################################################################
#
#
#	DATA MODELS
#
#
########################################################################################################################

class Item(AbstractItem):
	def __init__(self, filepath):

		AbstractItem.__init__(self,
							  filepath=filepath,
							  )

		self.rootItem = None
		self.loaded = False
		self.children = []
		self.index = None

		if directoryExist(self.filepath):
			if isAxelFilepath(self.filepath):
				self.readMetadata()
			else:
				name = xfer.splitPath(self.filepath)
				self.name = name[1]
				self.kind = component.directory

	def getRootItem(self):
		return self.rootItem

	def setRootItem(self, item):
		self.rootItem = item
		return

	def getLoaded(self):
		return self.loaded

	def setLoaded(self, bool):
		self.loaded = bool
		return

	def addChild(self, child):
		if child not in self.children:
			self.children.append(child)
		return

	def removeChild(self, child):
		if child in self.children:
			self.children.remove(child)
			del child
		return

	def getIndex(self):
		return self.index

	def setIndex(self, index):
		self.index = index
		return


class ItemModel(QStandardItemModel):
	def __init__(self, rootPath=DEFAULTLIBRARY):
		QStandardItemModel.__init__(self)

		self.rootPath = rootPath
		self.rootItem = Item(self.rootPath)
		self.parentItem = self.invisibleRootItem()
		self.items = []

		# Columns
		self.setColumnCount(0)

		# Headers
		# headers = ['File', 'Kind', 'Path']
		# self.setHorizontalHeaderLabels(headers)

		# Load Default Directory
		self.parentItem.appendRow(self.createRow(self.rootItem))

	def setRootPath(self, path):
		self.rootPath = path
		return

	def createRow(self, instance):
		root = QStandardItem(instance.getName())
		root.setData(instance)
		instance.setRootItem(root)

		# Icons
		icon = None
		if instance.getKind() == component.directory:
			icon = Icon.directory
		elif instance.getKind() == component.animation:
			icon = Icon.animation
		elif instance.getKind() == component.pose:
			icon = Icon.pose

		if icon:
			root.setIcon(QIcon(icon))

		if instance.getKind() == component.directory:
			root.appendRow(QStandardItem())
		return root

	def loadChildrenFromInstance(self, instance, index):
		filepath = instance.getFilepath()
		root = instance.getRootItem()

		if not instance.getLoaded():
			self.removeChildrenFromIndex(index)
			instance.setLoaded(True)

			for d in getDirectoriesInPath(filepath):
				dirItem = Item(d)
				root.appendRow(self.createRow(dirItem))
				self.items.append(dirItem)

			for f in getFilesInPath(filepath):
				fileItem = Item(f)
				root.appendRow(self.createRow(fileItem))
				self.items.append(fileItem)
		return

	def removeChildrenFromIndex(self, index):
		rowCount = self.rowCount(index)

		for x in range(0, rowCount + 1):
			childIndex = self.index(0, 0, index)
			item = self.itemFromIndex(childIndex)
			instance = item.data()
			if instance in self.items:
				self.items.remove(instance)
				del instance

		self.removeRows(0, rowCount, index)
		return


class LibraryDataModel(QStandardItemModel):
	def __init__(self,
				 filepath=DEFAULTLIBRARY,
				 ):
		QStandardItemModel.__init__(self)

		self.filepath = filepath
		self.instance = Item(self.filepath)
		self.name = self.instance.getName()
		self.items = []
		self.loaded = False
		self.kind = component.directory

		# Row
		self.row = QStandardItem(self.name)
		self.row.setData(self.instance)
		self.row.setIcon(QIcon(Icon.directory))
		self.row.appendRow(QStandardItem())

		# Append To Parent
		self.invisibleRootItem().appendRow(self.row)
		self.rowIndex = self.indexFromItem(self.row)

	def getInstance(self):
		return self.instance

	def getFilepath(self):
		return self.filepath

	def setFilepath(self, filepath):
		self.filepath = filepath
		return

	def getItems(self):
		return self.items

	def addItem(self, item):
		if item not in self.items:
			self.items.append(item)
		return

	def removeItem(self, item):
		if item in self.items:
			self.items.remove(item)
			del item

	def getLoaded(self):
		return self.loaded

	def setLoaded(self, bool):
		self.loaded = bool
		return

	def getKind(self):
		return self.kind

	def createRow(self, instance):
		root = QStandardItem(instance.getName())
		root.setData(instance)
		instance.setRootItem(root)

		# Icons
		icon = None
		if instance.getKind() == component.directory:
			icon = Icon.directory
		elif instance.getKind() == component.animation:
			icon = Icon.animation
		elif instance.getKind() == component.pose:
			icon = Icon.pose

		if icon:
			root.setIcon(QIcon(icon))

		if instance.getKind() == component.directory:
			root.appendRow(QStandardItem())
		return root

	def loadChildren(self, index):
		if not self.loaded:
			self.removeChildrenFromIndex(index)
			self.setLoaded(True)

			for d in getDirectoriesInPath(self.filepath):
				dirItem = Item(d)
				self.row.appendRow(self.createRow(dirItem))
				self.items.append(dirItem)

			for f in getFilesInPath(self.filepath):
				fileItem = Item(f)
				self.row.appendRow(self.createRow(fileItem))
				self.items.append(fileItem)
		return

	def removeChildrenFromIndex(self, index):
		rowCount = self.rowCount(index)

		for x in range(0, rowCount + 1):
			childIndex = self.index(0, 0, index)
			item = self.itemFromIndex(childIndex)
			instance = item.data()
			if instance in self.items:
				self.items.remove(instance)
				del instance

		self.removeRows(0, rowCount, index)
		return


########################################################################################################################
#
#
#	CLASS
#
#
########################################################################################################################


class LibraryTreeView(QTreeView):
	selectedInstance = Signal(object)

	def __init__(self,
				 rootPath=DEFAULTLIBRARY,
				 debug=True,
				 ):
		QTreeView.__init__(self,
						   )
		self.rootPath = rootPath
		self.debug = debug

		# Model
		self.model = QStandardItemModel()
		self.setModel(self.model)

		# Root
		self.root = self.model.invisibleRootItem()
		self.setupRoot()

		# Settings
		self.setAnimated(False)
		self.setSortingEnabled(True)
		self.setHeaderHidden(True)
		self.setFocusPolicy(Qt.NoFocus)
		self.setDragDropMode(QAbstractItemView.InternalMove)
		self.setContextMenuPolicy(Qt.CustomContextMenu)

		# Slots
		self.clicked[QModelIndex].connect(self.getSelected)
		self.expanded[QModelIndex].connect(self.getExpanded)
		self.collapsed[QModelIndex].connect(self.getCollapsed)
		self.customContextMenuRequested.connect(self.popupMenu)

	def popupMenu(self, position):
		indexes = self.selectedIndexes()

		if len(indexes) > 0:
			index = indexes[0]

			menu = QMenu(self)
			menu.setWindowFlags(Qt.Popup | Qt.NoDropShadowWindowHint)
			actionRename = menu.addAction('Rename')
			menu.addSeparator()
			actionRemove = menu.addAction('Remove')
			menu.exec_(self.viewport().mapToGlobal(position))
		return

	def setupRoot(self):
		item = Item(self.rootPath)
		self.root.appendRow(self.createRow(item))
		return

	def getDataFromIndex(self, index):
		return self.getItemFromIndex(index).data()

	def getItemFromIndex(self, index):
		return self.model.itemFromIndex(index)

	def getIndexFromItem(self, item):
		return self.model.indexFromItem(item)

	def getSelected(self, index):
		item = self.getItemFromIndex(index)
		instance = item.data()

		if instance.getKind == component.directory:
			self.loadChildren(instance, index)

		self.selectedInstance.emit(instance)

		if self.debug:
			print 'Selected', item
		return

	def getExpanded(self, index):
		item = self.getItemFromIndex(index)
		instance = item.data()
		self.loadChildren(instance, index)

		if self.debug:
			print 'Expanded', item
		return

	def getCollapsed(self, index):
		item = self.getItemFromIndex(index)

		if self.debug:
			print 'Collpased', item
		return

	def createRow(self, item):
		row = QStandardItem(item.getName())
		row.setData(item)

		# Icons
		if item.getKind() == component.directory:
			icon = Icon.directory
		elif item.getKind() == component.animation:
			icon = Icon.animation
		elif item.getKind() == component.pose:
			icon = Icon.pose
		else:
			icon = Icon.directory

		row.setIcon(QIcon(icon))

		if item.getKind() == component.directory:
			row.appendRow(QStandardItem())
		return row

	def loadChildren(self, item, index):
		if not item.getLoaded():
			filepath = item.getFilepath()
			root = self.model.itemFromIndex(index)
			self.removeChildrenFromIndex(index)
			item.setLoaded(True)

			for d in getDirectoriesInPath(filepath):
				dirItem = Item(d)
				root.appendRow(self.createRow(dirItem))
				item.addChild(dirItem)

			for f in getFilesInPath(filepath):
				fileItem = Item(f)
				root.appendRow(self.createRow(fileItem))
				item.addChild(fileItem)
		return

	def removeChildrenFromIndex(self, index):
		rowCount = self.model.rowCount(index)
		self.model.removeRows(0, rowCount, index)
		return


class App(QMainWindow):
	def __init__(self,
				 parent=None,
				 name=WINDOWNAME,
				 title=TITLE,
				 width=WIDTH,
				 height=HEIGHT,
				 ):
		QMainWindow.__init__(self, parent=parent)

		self.setObjectName(name)
		self.setWindowTitle(title)
		self.setMinimumSize(width, height)

		# Widget
		self.mainWidget = QWidget()
		self.layout = QVBoxLayout(self.mainWidget)
		self.setCentralWidget(self.mainWidget)

		# Tree View
		self.tree = DirTreeView()
		self.layout.addWidget(self.tree)

		# Show UI
		self.show()


########################################################################################################################
#
#
#	THUMBNAIL WIDGET
#
#
########################################################################################################################


class ThumbnailWidget(QFrame):
	stateChanged = Signal(str)
	frameChanged = Signal(int)
	clicked = Signal(bool)
	pressed = Signal(bool)
	released = Signal(bool)
	toggled = Signal(bool)

	def __init__(self, *args, **kwargs):
		QFrame.__init__(self, *args, **kwargs)

		self.createEnabled = False
		self.sequence = None
		self.currentState = None
		self.isPlaying = False
		self.start = 0
		self.duration = 100
		self.frameRate = 41.667
		self.currentFrame = 0
		self.defaultPixmap = QPixmap(DEFAULTTHUMBNAIL)
		self.currentPixmap = self.defaultPixmap
		self.isLoop = True
		self.imageCache = []
		self.hover = False
		self.isScrubbing = False
		self.hasSequence = False

		# Widget
		self.setMouseTracking(True)
		self.setStyleSheet('''
		background:black;
		padding:0;
		margin:0;
		''')

		# Layout
		self.setLayout(QVBoxLayout())
		self.layout().setSpacing(0)
		self.layout().setContentsMargins(0, 0, 0, 0)

		# Label
		self.label = QLabel()
		self.label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
		self.label.setPixmap(self.currentPixmap)
		self.label.setAlignment(Qt.AlignCenter)
		self.layout().addWidget(self.label)

		# Progress Bar
		self.progressBar = QProgressBar()
		self.progressBar.setTextVisible(False)
		self.progressBar.setFixedHeight(5)
		self.progressBar.setStyleSheet('''QProgressBar{
										background:black;
										border:none;
										border-radius:0;
										padding:0;
										margin:0;
										}
										QProgressBar::chunk{
										background:white;
										padding:0;
										margin:0;
										border:none;
										}
										''')
		self.layout().addWidget(self.progressBar)

		# Timeline for Sequences
		self.timeline = QTimeLine(1000, self)
		self.timeline.setFrameRange(self.start, self.duration)
		self.timeline.setCurveShape(QTimeLine.LinearCurve)
		self.timeline.setEasingCurve(QEasingCurve.Linear)
		self.timeline.setUpdateInterval(0)
		self.timeline.setLoopCount(0)
		self.stop()

		self.timeline.frameChanged.connect(self.setSequence)
		self.timeline.frameChanged.connect(self.progressBar.setValue)
		self.timeline.stateChanged.connect(self.setState)

	def clear(self):
		self.updatePixmap(self.defaultPixmap)
		self.setHasSequence(False)
		self.sequence = None
		self.progressBar.setValue(0)
		return

	def getHasSequence(self):
		return self.hasSequence

	def setHasSequence(self, bool):
		self.hasSequence = bool
		return

	def convertPositionToValue(self, position):
		width = self.size().width()
		return int((float(self.duration + 1) / float(width)) * float(position))

	def play(self):
		if self.sequence:
			self.timeline.start()
		return

	def stop(self):
		self.timeline.stop()
		return

	def pause(self):
		self.timeline.setPaused(True)
		return

	def unPause(self):
		self.timeline.setPaused(False)
		return

	def scrub(self, position):
		if self.sequence:
			self.pause()
			frame = self.convertPositionToValue(position)
			self.jumpToFrame(frame)
			self.isScrubbing = True
		return

	def mousePressEvent(self, event):
		if self.hasSequence:
			self.scrub(event.pos().x())
		return

	def mouseReleaseEvent(self, event):
		if self.isScrubbing:
			self.isScrubbing = False

			frame = self.currentFrame + 1
			if frame > self.duration:
				frame = 0

			self.setSequence(frame)
			self.timeline.frameChanged.emit(frame)
			self.unPause()
		return

	def mouseMoveEvent(self, event):
		if self.hasSequence:
			xpos = event.pos().x()

			if self.size().width() >= xpos >= 0:
				self.scrub(xpos)
		return

	def enterEvent(self, event):
		self.setHover(True)
		if self.hasSequence:
			self.play()
		return

	def leaveEvent(self, event):
		self.setHover(False)
		if self.hasSequence:
			self.pause()
		return

	def getHover(self):
		return self.hover

	def setHover(self, value):
		self.hover = value
		return

	def setCreateEnabled(self, value):
		self.createEnabled = value
		return

	def getCreateEnabled(self):
		return self.createEnabled

	def getTimeline(self):
		return self.timeline

	def getLabel(self):
		return self.label

	def setState(self, state):
		self.currentState = state
		self.stateChanged.emit(state)
		self.fitToWindow()
		return

	def loadSequence(self, sequence):
		self.sequence = sequence
		end = len(sequence) - 1
		self.setRange(0, end)
		self.timeline.setDuration(end * self.frameRate)
		self.imageCache = []
		self.progressBar.setRange(0, end)

		for item in sequence:
			self.imageCache.append(QPixmap(item))

		self.setHasSequence(True)
		self.jumpToFrame(0)
		return

	def loadSequenceFromFilepath(self, filepath):
		sequence = collectSequenceFromFilepath(filepath)

		if len(sequence) > 0 :
			self.loadSequence(sequence)
		else:
			self.updatePixmap(QPixmap(sequence[0]))
		return

	def updatePixmap(self, pixmap):
		self.label.setPixmap(pixmap)
		self.currentPixmap = pixmap
		return

	def setSequence(self, frame):
		self.setCurrentFrame(frame)
		if self.imageCache:
			pixmap = self.imageCache[frame]
			self.updatePixmap(pixmap)
			self.fitToWindow()
		self.frameChanged.emit(frame)
		return

	def setFrameRate(self, rate):
		self.frameRate = rate
		return

	def setDuration(self, duration):
		self.duration = float(duration) * float(self.frameRate)
		self.timeline.setDuration(self.duration)
		return

	def setStartFrame(self, value):
		self.start = value
		self.timeline.setStartFrame(value)
		return

	def setCurrentFrame(self, frame):
		self.currentFrame = frame
		return

	def setEndFrame(self, end):
		self.duration = end
		self.timeline.setEndFrame(end)
		return

	def setRange(self, start, end):
		self.start = start
		self.duration = end
		self.timeline.setFrameRange(start, end)
		return

	def valueChanged(self, value):
		print value
		return

	def jumpToFrame(self, frame):
		self.setSequence(frame)
		self.timeline.frameChanged.emit(frame)
		return

	def jumpToPrevFrame(self):
		frame = self.currentFrame - 1
		if frame > self.start:
			self.jumpToFrame(frame)
		return

	def jumpToNextFrame(self):
		frame = self.currentFrame + 1
		if frame < self.duration:
			self.jumpToFrame(frame)
		return

	def fitToWindow(self):
		if self.currentPixmap:
			w = self.label.width()
			h = self.label.height()
			pixmap = self.currentPixmap
			self.label.setPixmap(pixmap.scaled(w, h, Qt.KeepAspectRatio))
		return

	def playPause(self):
		if self.currentState in [QTimeLine.NotRunning, QTimeLine.Paused]:
			self.timeline.setPaused(False)
		else:
			self.timeline.setPaused(True)
		return

	def resizeEvent(self, event):
		self.fitToWindow()
		return


########################################################################################################################
#
#
#	IMPORT / EXPORT WIDGET UI
#
#
########################################################################################################################

class BaseWidget(QWidget):
	def __init__(self, kind=None, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)

		spacing = 10
		margins = 5
		padding = 10
		column = 60

		self.kind = kind

		# Layout
		self.setLayout(QVBoxLayout())
		self.layout().setSpacing(spacing)
		self.layout().setContentsMargins(padding, padding, padding, padding)

		# Header
		self.headerWidget = QLabel(str(self.kind.capitalize()))
		self.headerWidget.setAccessibleName('header')
		self.layout().addWidget(self.headerWidget)

		# Scroll: Area
		self.scrollArea = QScrollArea()
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setFrameShape(QFrame.NoFrame)
		self.scrollArea.setFrameShadow(QFrame.Plain)

		self.scrollWidget = QWidget()
		self.scrollWidget.setGeometry(QRect(0, 0, 394, 668))
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.scrollWidget.sizePolicy().hasHeightForWidth())
		self.scrollWidget.setSizePolicy(sizePolicy)
		self.scrollArea.setWidget(self.scrollWidget)

		self.layout().addWidget(self.scrollArea)

		self.scrollLayout = QVBoxLayout(self.scrollWidget)
		self.scrollLayout.setSpacing(spacing)
		self.scrollLayout.setContentsMargins(0, 0, 0, 0)

		# Thumbnail: Box
		self.thumbailBox = QGroupBox()
		self.thumbailBox.setTitle('Thumbnail')
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
		sizePolicy.setHeightForWidth(self.thumbailBox.sizePolicy().hasHeightForWidth())
		self.thumbailBox.setSizePolicy(sizePolicy)
		self.scrollLayout.addWidget(self.thumbailBox)

		self.thumbnailBoxLayout = QVBoxLayout()
		self.thumbnailBoxLayout.setSpacing(margins)
		self.thumbnailBoxLayout.setContentsMargins(padding, padding, padding, padding)
		self.thumbailBox.setLayout(self.thumbnailBoxLayout)

		# Thumbnail: Image
		self.thumbnailWidget = ThumbnailWidget()
		self.thumbnailBoxLayout.addWidget(self.thumbnailWidget)

		# Settings: Box
		self.settingsBox = QGroupBox()
		self.settingsBox.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum))
		self.settingsBox.setFlat(False)
		self.settingsBox.setCheckable(False)
		self.scrollLayout.addWidget(self.settingsBox)

		self.settingsBoxLayout = QVBoxLayout(self.settingsBox)
		self.settingsBoxLayout.setSpacing(5)
		self.settingsBoxLayout.setContentsMargins(10, 10, 10, 10)

		# Comment: Box
		self.commentBox = QGroupBox()
		self.commentBox.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum))
		self.commentBox.setMaximumSize(QSize(16777215, 150))
		self.commentBox.setTitle('Comment')
		self.scrollLayout.addWidget(self.commentBox)

		self.commentBoxLayout = QVBoxLayout(self.commentBox)
		self.commentBoxLayout.setSpacing(margins)
		self.commentBoxLayout.setContentsMargins(padding, padding, padding, padding)

		# Comment: Widget
		self.commentWidget = QTextEdit(self.commentBox)
		sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		sizePolicy.setHeightForWidth(self.commentWidget.sizePolicy().hasHeightForWidth())
		self.commentWidget.setSizePolicy(sizePolicy)
		self.commentBoxLayout.addWidget(self.commentWidget)
		self.scrollLayout.addWidget(self.commentBox)

		# Tags: Box
		self.tagBox = QGroupBox()
		self.tagBox.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum))
		self.tagBox.setTitle('Tags')
		self.scrollLayout.addWidget(self.tagBox)

		self.tagBoxLayout = QVBoxLayout(self.tagBox)
		self.tagBoxLayout.setSpacing(5)
		self.tagBoxLayout.setContentsMargins(10, 10, 10, 10)

		# Tags: Widget
		self.tagWidget = QLineEdit()
		self.tagWidget.setPlaceholderText('Tags separated by commas.')
		self.tagWidget.setMinimumSize(QSize(0, 25))
		self.tagWidget.setMaximumSize(QSize(16777215, 25))
		self.tagBoxLayout.addWidget(self.tagWidget)

		# Footer
		self.callbackButton = QPushButton()
		self.callbackButton.setText('Do Something')
		self.layout().addWidget(self.callbackButton)


class ExportWidget(BaseWidget):
	def __init__(self, kind=component.animation, *args, **kwargs):
		BaseWidget.__init__(self, kind=kind, *args, **kwargs)

		if self.kind == component.animation:
			# Thumbnail: Range
			self.rangeLayout = QHBoxLayout()
			self.thumbnailBoxLayout.addLayout(self.rangeLayout)

			self.rangeLabel = QLabel(self.thumbailBox)
			self.rangeLabel.setMinimumSize(QSize(60, 25))
			self.rangeLabel.setMaximumSize(QSize(60, 16777215))
			self.rangeLabel.setText('Range')
			self.rangeLabel.setAccessibleName('info')
			self.rangeLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
			self.rangeLayout.addWidget(self.rangeLabel)

			self.rangeStartWidget = QLineEdit(self.thumbailBox)
			self.rangeStartWidget.setMaximumSize(QSize(16777215, 25))
			self.rangeStartWidget.setValidator(QIntValidator())
			self.rangeStartWidget.setText(str(int(getStartFrame())))

			self.rangeLayout.addWidget(self.rangeStartWidget)
			self.rangeEndWidget = QLineEdit(self.thumbailBox)
			self.rangeEndWidget.setMaximumSize(QSize(16777215, 25))
			self.rangeEndWidget.setValidator(QIntValidator())
			self.rangeEndWidget.setText(str(int(getEndFrame())))
			self.rangeLayout.addWidget(self.rangeEndWidget)

			self.rangeOptionsButton = QPushButton(self.thumbailBox)
			sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.rangeOptionsButton.sizePolicy().hasHeightForWidth())
			self.rangeOptionsButton.setSizePolicy(sizePolicy)
			self.rangeOptionsButton.setMinimumSize(QSize(25, 0))
			self.rangeOptionsButton.setMaximumSize(QSize(25, 16777215))
			self.rangeOptionsButton.setText('...')
			self.rangeLayout.addWidget(self.rangeOptionsButton)

			# Thumbnail: Step
			self.frameLayout = QHBoxLayout()
			self.thumbnailBoxLayout.addLayout(self.frameLayout)

			self.frameLabel = QLabel(self.thumbailBox)
			self.frameLabel.setMinimumSize(QSize(60, 25))
			self.frameLabel.setMaximumSize(QSize(60, 16777215))
			self.frameLabel.setText('Step')
			self.frameLabel.setAccessibleName('info')
			self.frameLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
			self.frameLayout.addWidget(self.frameLabel)

			self.frameWidget = QSpinBox(self.thumbailBox)
			self.frameWidget.setMinimum(1)
			self.frameWidget.setMaximum(10000000)
			self.frameWidget.setMaximumSize(QSize(16777215, 25))
			self.frameWidget.setProperty('value', 1)
			self.frameLayout.addWidget(self.frameWidget)

		# Settings: Library
		self.libraryLayout = QHBoxLayout()
		self.settingsBoxLayout.addLayout(self.libraryLayout)

		self.libraryLabel = QLabel(self.settingsBox)
		self.libraryLabel.setMinimumSize(QSize(60, 25))
		self.libraryLabel.setMaximumSize(QSize(60, 16777215))
		self.libraryLabel.setText('Library')
		self.libraryLabel.setAccessibleName('info')
		self.libraryLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
		self.libraryLayout.addWidget(self.libraryLabel)

		self.libraryWidget = QComboBox()
		self.libraryWidget.addItem(os.path.basename(DEFAULTLIBRARY), DEFAULTLIBRARY)
		self.libraryLayout.addWidget(self.libraryWidget)

		# Settings: Name
		self.nameLayout = QHBoxLayout()
		self.settingsBoxLayout.addLayout(self.nameLayout)

		self.nameLabel = QLabel(self.settingsBox)
		self.settingsBox.setTitle('File Info.')
		self.nameLabel.setMinimumSize(QSize(60, 25))
		self.nameLabel.setMaximumSize(QSize(60, 16777215))
		self.nameLabel.setText('Name *')
		self.nameLabel.setAccessibleName('info')
		self.nameLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
		self.nameLayout.addWidget(self.nameLabel)

		self.nameWidget = QLineEdit(self.settingsBox)
		self.nameWidget.setPlaceholderText('Required ***')
		sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.nameWidget.sizePolicy().hasHeightForWidth())
		self.nameWidget.setSizePolicy(sizePolicy)
		self.nameWidget.setMaximumSize(QSize(16777215, 25))
		self.nameLayout.addWidget(self.nameWidget)

		# Settings: Extra
		self.settingsExtraLayout = QHBoxLayout()
		self.settingsBoxLayout.addLayout(self.settingsExtraLayout)

		self.shapesLayout = QHBoxLayout()
		self.settingsExtraLayout.addLayout(self.shapesLayout)

		self.shapesLabel = QLabel(self.settingsBox)
		self.shapesLabel.setMinimumSize(QSize(60, 25))
		self.shapesLabel.setMaximumSize(QSize(60, 25))
		self.shapesLabel.setText('Shapes')
		self.shapesLabel.setAccessibleName('info')
		self.shapesLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
		self.shapesLayout.addWidget(self.shapesLabel)

		self.shapesCheckBox = QCheckBox(self.settingsBox)
		self.shapesCheckBox.setTristate(False)
		self.shapesCheckBox.setObjectName('shapesCheckBox')
		self.shapesLayout.addWidget(self.shapesCheckBox)

		if self.kind == component.animation:
			self.layersLayout = QHBoxLayout()
			self.settingsExtraLayout.addLayout(self.layersLayout)

			self.layersLabel = QLabel(self.settingsBox)
			self.layersLabel.setMinimumSize(QSize(60, 25))
			self.layersLabel.setMaximumSize(QSize(60, 16777215))
			self.layersLabel.setText('Layers')
			self.layersLabel.setAccessibleName('info')
			self.layersLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
			self.layersLayout.addWidget(self.layersLabel)

			self.layersCheckBox = QCheckBox(self.settingsBox)
			self.layersCheckBox.setTristate(False)
			self.layersLayout.addWidget(self.layersCheckBox)

		# Callback
		self.callbackButton.setText('Export')
		self.callbackButton.clicked.connect(self.exportCallback)

	def exportCallback(self, isDebug=DEBUGMODE):
		name = self.nameWidget.text()
		kind = self.kind
		shapes = self.shapesCheckBox.isChecked()
		layers = self.layersCheckBox.isChecked()
		comment = self.commentWidget.toPlainText()
		tags = createTagsFromString(str(self.tagWidget.text()))
		objects = getSelectedObjects(shapes)
		library = self.libraryWidget.currentData(Qt.UserRole)

		if isDebug:
			print 'Library: \t{}'.format(library)
			print 'Name: \t{}'.format(name)
			print 'Kind: \t{}'.format(kind)
			print 'Shapes: \t{}'.format(shapes)
			print 'Layers: \t{}'.format(layers)
			print 'Comment: \t{}'.format(comment)
			print 'Tags: \t{}'.format(tags)
			print 'Objects: \t{}'.format(objects)

		if not name:
			self.nameWidget.setStyleSheet('border:1px solid red;')
			errorStr = 'Axel Export: Name not specified.'
			raise ValueError(errorStr)

		elif not objects:
			errorStr = 'Axel Export: No objects were selected.'
			cmds.warning(errorStr)
			# raise ValueError(error)
			return
		else:
			filepath = os.path.join(library, '{}.{}'.format(name, EXTENSION))

			if directoryExist(filepath):
				return
			else:
				Export(filepath=filepath,
					   kind=kind,
					   items=objects,
					   tags=tags,
					   comment=comment,
					   layers=layers,
					   )
			return

	def createThumbnailCallback(self, isDebug=True):
		start = int(self.rangeStartWidget.text())
		end = int(self.rangeEndWidget.text())
		interval = 1

		if isDebug:
			print 'Start: \t{}'.format(start)
			print 'End: \t{}'.format(end)
			print 'Step: \t{}'.format(interval)
		return


def exportWindow(name='axelExportWindowUI', title='Axel Export'):
	if cmds.window(name, exists=True):
		cmds.deleteUI(name, wnd=True)

	# Window
	window = QMainWindow(parent=getMayaWindow())
	window.setObjectName(name)
	window.setWindowTitle(title)

	# Widget
	mainWidget = ExportWidget()
	window.setCentralWidget(mainWidget)
	window.setGeometry(300, 300, 285, 590)

	window.show()
	return window


class ImportWidget(BaseWidget):
	def __init__(self, kind=component.animation, *args, **kwargs):
		BaseWidget.__init__(self, kind=kind, *args, **kwargs)

		# File Info
		for meta in METAATTRIBUTES:
			layout = QHBoxLayout()
			self.settingsBoxLayout.addLayout(layout)

			label = QLabel(convertStrToNiceStr(meta))
			label.setAccessibleName('info')
			label.setMaximumSize(QSize(60, 13))
			label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
			layout.addWidget(label)

			info = QLabel(str(METADATA[meta]))
			info.setAccessibleName('infoData')
			info.setMaximumSize(QSize(16777215, 13))
			layout.addWidget(info)

		spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
		self.settingsBoxLayout.addItem(spacerItem)

		# Comment
		self.commentWidget.setReadOnly(True)
		self.commentWidget.setText(METADATA['comment'])

		# Callback Button
		self.callbackButton.setText('Import')

	def setComment(self, text):
		self.commentWidget.setText(text)
		return

	def setMetaData(self, data):
		return


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


def window(name=WINDOWNAME, *args):
	if cmds.window(name, exists=True):
		cmds.deleteUI(name, wnd=True)

	# Window
	window = App(parent=getMayaWindow(), name=name)
	return window


def show():
	if MAYAVERSION == 2018:
		window()
		return
	else:
		cmds.error('AXEL: Animation Library only works with Maya Version 2018.')
		return
