# AXEL.ALPHA_UI
#
#
#
#
#

# AXEL Modules
from api import *
import ui
from ui import *
import tags

reload(ui)
reload(tags)

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


WINNAME = 'axelAlphaWindowUI'
MARGIN = 0
PADDING = 0
SPACING = 10
COLUMN = 60

DEBUGMODE = True


########################################################################################################################
#
#
#	MENU WIDGET
#
#
########################################################################################################################

class FileMenu(QMenu):
	newFolder = Signal()
	importFolder = Signal()
	newPose = Signal()
	newAnimation = Signal()

	def __init__(self, *args, **kwargs):
		QMenu.__init__(self, *args, **kwargs)

		self.setWindowFlags(Qt.Popup | Qt.NoDropShadowWindowHint)

		self.actionNewDir = self.addAction('New Folder')
		self.actionNewDir.triggered.connect(self.newFolder.emit)
		self.addSeparator()

		self.actionImportDir = self.addAction('Import Folder')
		self.actionImportDir.triggered.connect(self.importFolder.emit)
		self.addSeparator()

		self.actionPose = self.addAction('New Pose')
		self.actionPose.triggered.connect(self.newPose.emit)

		self.actionAnim = self.addAction('New Animation')
		self.actionAnim.triggered.connect(self.newAnimation.emit)


class ContextMenu(FileMenu):
	rename = Signal()
	delete = Signal()
	show = Signal()

	def __init__(self, *args, **kwargs):
		FileMenu.__init__(self, *args, **kwargs)

		self.addSeparator()
		self.actionRename = self.addAction('Rename')
		self.actionRename.triggered.connect(self.rename.emit)

		self.actionDelete = self.addAction('Delete')
		self.actionDelete.triggered.connect(self.delete.emit)

		self.addSeparator()
		self.actionShow = self.addAction('Show In Explorer')
		self.actionShow.triggered.connect(self.show.emit)



########################################################################################################################
#
#
#	RATING WIDGET
#
#
########################################################################################################################

class RatingWidget(QWidget):
	selected = Signal(int)

	def __init__(self, default=0, max=5, iconSize=20):
		QWidget.__init__(self)

		self.default = default
		self.min = 1
		self.max = max
		self.current = default
		self.iconSize = iconSize
		self.buttonName = 'button'

		# Settings
		self.setMouseTracking(True)

		# Layout
		self.setLayout(QHBoxLayout())
		self.layout().setSpacing(0)
		self.layout().setContentsMargins(0, 0, 0, 0)
		self.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum))

		# Labels
		for x in range(self.min, self.max + 1):
			label = QLabel('-')
			label.setMinimumSize(iconSize, iconSize)
			label.setMaximumSize(iconSize, iconSize)
			label.setAlignment(Qt.AlignCenter)
			label.setStyleSheet('color:grey;')
			setattr(self, '{}{}'.format(self.buttonName, x), label)
			self.layout().addWidget(label)

	def convertPositionToValue(self, position):
		width = self.size().width()
		return int((float(self.max) / float(width)) * float(position))

	def getMax(self):
		return self.max

	def setMax(self, max):
		self.max = max
		return

	def getCurrent(self):
		return self.current

	def setCurrent(self, value):
		self.current = value
		for x in range(self.min, value + 1):
			label = getattr(self, '{}{}'.format(self.buttonName, x))
			label.setText('+')
			label.setStyleSheet('color:white;')

		if value != self.max:
			for x in range(value + 1, self.max + 1):
				label = getattr(self, '{}{}'.format(self.buttonName, x))
				label.setText('-')
				label.setStyleSheet('color:grey;')

		self.selected.emit(self.current)
		return

	def mousePressEvent(self, event):
		value = self.convertPositionToValue(event.pos().x())
		self.setCurrent(value + 1)
		return

	def clear(self):
		self.current = 0
		for x in range(self.min, self.max + 1):
			label = getattr(self, '{}{}'.format(self.buttonName, x))
			label.setStyleSheet('color:grey;')
		return


########################################################################################################################
#
#
#	INFO WIDGET
#
#
########################################################################################################################

class InfoWidget(QFrame):
	def __init__(self):
		QFrame.__init__(self)

		spacing = 3
		column = 60
		margin = 10

		# Layout
		self.setLayout(QVBoxLayout())
		self.layout().setSpacing(margin)
		self.layout().setContentsMargins(margin, margin, margin, margin)
		self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum))

		# Info Layout
		self.formLayout = QFormLayout()
		self.formLayout.setHorizontalSpacing(margin)
		self.formLayout.setVerticalSpacing(spacing)
		self.formLayout.setContentsMargins(0, 0, 0, 0)
		self.formLayout.setLabelAlignment(Qt.AlignRight)
		self.layout().addLayout(self.formLayout)

		for meta in METAATTRIBUTES:
			if meta not in ['comment', 'tags']:
				label = '{}Label'.format(meta)
				info = '{}Info'.format(meta)

				qlabel = QLabel(convertStrToNiceStr(meta))
				qlabel.setAccessibleName('info')
				qlabel.setMinimumWidth(column)
				qlabel.setMaximumWidth(column)
				qlabel.setAlignment(Qt.AlignRight)

				if meta == 'rating':
					widget = RatingWidget()
				else:
					widget = QLabel()

				setattr(self, label, qlabel)
				setattr(self, info, widget)
				self.formLayout.addRow(qlabel, widget)

		# Comment
		self.commentBox = QGroupBox()
		self.commentBox.setTitle('Comments')
		self.commentBox.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum))
		self.commentBoxLayout = QVBoxLayout()
		self.commentBoxLayout.setSpacing(0)
		self.commentBoxLayout.setContentsMargins(0, 0, 0, 0)
		self.commentBox.setLayout(self.commentBoxLayout)
		self.layout().addWidget(self.commentBox)

		self.commentWidget = QTextEdit()
		self.commentWidget.setReadOnly(True)
		self.commentWidget.setMaximumHeight(80)
		self.commentBoxLayout.addWidget(self.commentWidget)

		# Tags
		self.tagsBox = QGroupBox()
		self.tagsBox.setTitle('Tags')
		self.tagsBox.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum))
		self.tagsBoxLayout = QVBoxLayout()
		self.tagsBoxLayout.setSpacing(0)
		self.tagsBoxLayout.setContentsMargins(0, 0, 0, 0)
		self.tagsBox.setLayout(self.tagsBoxLayout)
		self.layout().addWidget(self.tagsBox)

		self.tagsWidget = tags.AssignedTagsWidget()
		self.tagsBoxLayout.addWidget(self.tagsWidget)

	def loadData(self, data):
		for d in data:
			info = '{}Info'.format(d)

			if d == 'comment':
				self.commentWidget.setText(data[d])

			elif d == 'tags':
				if type(data[d]) is list:
					for tag in data[d]:
						#self.tagsWidget.add(tag)
						pass

			elif d == 'rating':
				widget = getattr(self, info)
				widget.setCurrent(data[d])

			elif d == 'items':
				qlabel = getattr(self, info)
				qlabel.setText(str(len(data[d])))

			else:
				try:
					qlabel = getattr(self, info)
					qlabel.setText(str(data[d]))
				except:
					pass
		return

	def clear(self):
		for v in vars(self).iterkeys():
			if 'Info' in v:
				try:
					qlabel = getattr(self, v)
					qlabel.setText('')
				except:
					pass
		self.commentWidget.setText('')
		return


########################################################################################################################
#
#
#	LIBRARY WIDGET
#
#
########################################################################################################################


class LibraryWidget(QFrame):
	selectedInstance = Signal(object)

	def __init__(self, debug=True, *args, **kwargs):
		QFrame.__init__(self, *args, **kwargs)

		self.debug = debug
		self.libraryWidget = QWidget()

		# Layout
		self.setLayout(QVBoxLayout())
		self.layout().setSpacing(SPACING)
		self.layout().setContentsMargins(MARGIN, MARGIN, MARGIN, MARGIN)

		# Tree View
		self.treeView = LibraryTreeView(debug=self.debug)
		self.treeView.setFrameShape(QFrame.NoFrame)
		self.treeView.setEditTriggers(False)
		self.layout().addWidget(self.treeView)

		# Slots
		self.treeView.selectedInstance.connect(self.selectedCallback)

	def selectedCallback(self, instance):
		self.selectedInstance.emit(instance)
		return


class RightWidget(QWidget):
	def __init__(self, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)


class ExportWidget(RightWidget):
	def __init__(self, *args, **kwargs):
		RightWidget.__init__(self, *args, **kwargs)


class ImportWidget(RightWidget):
	def __init__(self, *args, **kwargs):
		RightWidget.__init__(self, *args, **kwargs)


########################################################################################################################
#
#
#	WINDOW
#
#
########################################################################################################################

class Window(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent=parent)

		# Window
		self.setGeometry(100, 100, 800, 600)

		# Menu
		menubar = self.menuBar()
		menubar.setNativeMenuBar(False)
		self.menuFile = FileMenu(self)
		self.menuFile.setTitle('File')
		menubar.addMenu(self.menuFile)

		# Central Widget
		self.centralWidget = QWidget(self)
		self.centralWidget.setMouseTracking(True)
		self.centralLayout = QVBoxLayout(self.centralWidget)
		self.centralLayout.setSpacing(10)
		self.centralLayout.setContentsMargins(0, 5, 0, 5)
		self.setCentralWidget(self.centralWidget)

		# Central Splitter
		self.centralSplitter = QSplitter()
		self.centralSplitter.setHandleWidth(3)
		self.centralLayout.addWidget(self.centralSplitter)

		# Left Widget
		self.leftWidget = QWidget()
		self.leftWidgetLayout = QVBoxLayout(self.leftWidget)
		self.leftWidgetLayout.setSpacing(5)
		self.leftWidgetLayout.setContentsMargins(0, 0, 0, 0)
		self.centralSplitter.addWidget(self.leftWidget)

		# Library Tab
		self.libraryTabWidget = QTabWidget(self.leftWidget)
		self.libraryTabWidget.setCurrentIndex(0)
		self.leftWidgetLayout.addWidget(self.libraryTabWidget)

		self.libraryWidget = LibraryWidget()
		self.libraryTabWidget.addTab(self.libraryWidget, 'Folders')
		self.libraryWidget.selectedInstance.connect(self.loadInfoFromSelected)

		# Tags Widget
		self.tagsWidget = tags.TagEditor()
		self.libraryTabWidget.addTab(self.tagsWidget, 'Tags')

		# Right Widget
		self.rightWidget = QWidget()
		self.rightLayout = QVBoxLayout(self.rightWidget)
		self.rightLayout.setSpacing(5)
		self.rightLayout.setContentsMargins(0, 0, 0, 0)
		self.rightStackedWidget = QStackedWidget(self.rightWidget)
		self.centralSplitter.addWidget(self.rightWidget)
		self.rightWidget.setHidden(True)

		# Import Widget
		self.importWidget = QWidget()
		self.importLayout = QVBoxLayout(self.importWidget)
		self.importLayout.setSpacing(0)
		self.importLayout.setContentsMargins(0, 0, 0, 0)
		self.importSplitter = QSplitter(self.importWidget)
		self.importSplitter.setMouseTracking(True)
		self.importSplitter.setOrientation(Qt.Vertical)
		self.importSplitter.setHandleWidth(3)

		# Preview Widget
		self.previewTabWidget = QTabWidget()
		self.previewTabWidget.setCurrentIndex(0)
		self.importSplitter.addWidget(self.previewTabWidget)

		self.previewWidget = ThumbnailWidget()
		self.previewWidget.setMinimumHeight(150)
		self.previewTabWidget.addTab(self.previewWidget, 'Preview')

		# Info Widget
		self.infoTabWidget = QTabWidget()
		self.infoTabWidget.setMouseTracking(True)
		self.infoTabWidget.setAcceptDrops(True)
		self.infoTabWidget.setDocumentMode(False)
		self.infoTabWidget.setMovable(True)
		self.infoTabWidget.setCurrentIndex(0)
		self.importSplitter.addWidget(self.infoTabWidget)

		self.infoScrollArea = QScrollArea()
		self.infoScrollArea.setFrameShape(QFrame.NoFrame)
		self.infoScrollArea.setWidgetResizable(True)
		self.infoTabWidget.addTab(self.infoScrollArea, 'Info')

		self.infoWidget = InfoWidget()
		self.infoScrollArea.setWidget(self.infoWidget)

		self.importLayout.addWidget(self.importSplitter)
		self.rightStackedWidget.addWidget(self.importWidget)
		self.rightLayout.addWidget(self.rightStackedWidget)

		self.infoTabWidget.addTab(QFrame(), 'Items')
		self.infoTabWidget.addTab(QFrame(), 'Layers')

		# Callback Button
		self.callbackButton = QPushButton(self.rightWidget)
		self.callbackButton.setText('Import')
		self.callbackButton.setHidden(True if not MAYALOADED else False)
		self.rightLayout.addWidget(self.callbackButton)
		self.centralLayout.addWidget(self.centralSplitter)

		# Status Bar
		self.statusbar = QStatusBar(self)
		self.statusbar.setSizeGripEnabled(False)
		self.statusbar.showMessage('Status')
		self.setStatusBar(self.statusbar)

		self.rightStackedWidget.setCurrentIndex(0)


	def loadInfoFromSelected(self, instance):
		if instance.getKind() != component.directory:
			self.infoWidget.loadData(instance.getMetadata())
			self.rightWidget.setHidden(False)
		else:
			self.infoWidget.clear()
			self.rightWidget.setHidden(True)

		self.statusbar.showMessage(instance.getFilepath())
		return


def show(name=WINNAME, title='AXEL: Animation XML Export Library'):
	if cmds.window(name, exists=True):
		cmds.deleteUI(name, wnd=True)

	# Window
	window = Window(getMayaWindow())
	window.setObjectName(name)
	window.setWindowTitle(title)
	# window.setStyleSheet(api.getStyleSheet(os.path.join(DIRPATH, 'alpha_theme.css')))

	# Show UI
	window.show()
	return window


def standalone(name=WINNAME, title='AXEL: Animation XML Export Library'):
	app = QApplication(sys.argv)
	window = Window()
	window.setObjectName(name)
	window.setWindowTitle(title)
	window.setStyleSheet(getStyleSheet(os.path.join(DIRPATH, 'alpha_theme.css')))
	window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	MAYALOADED = False
	standalone()
