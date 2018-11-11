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
#	USER INTERFACE
#
#
########################################################################################################################


class InfoWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		spacing = 5
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
		self.layout().addLayout(self.formLayout)

		for meta in METAATTRIBUTES:
			if meta not in ['comment', 'tags']:
				label = '{}Label'.format(meta)
				info = '{}Info'.format(meta)

				qlabel = QLabel(convertStrToNiceStr(meta))
				qlabel.setAccessibleName('info')
				qlabel.setMinimumWidth(column)
				qlabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

				setattr(self, label, qlabel)
				setattr(self, info, QLabel())
				self.formLayout.addRow(getattr(self, label), getattr(self, info))

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

		self.setStyleSheet('''
QGroupBox {
border-top: none;
margin-top: 0; /* leave space at the top for the title */
padding-top:30;
}

QGroupBox::title {
border:none;
padding:5px 8px 5px 0;
}
QGroupBox:hover{
}
		''')

	def loadData(self, data):
		for d in data:
			info = '{}Info'.format(d)

			if d == 'comment':
				self.commentWidget.setText(data[d])

			elif d == 'tags':
				if type(data[d]) is list:
					for tag in data[d]:
						# self.tagsWidget.add(tag)
						pass

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


class LibraryWidget(QWidget):
	selectedInstance = Signal(object)

	def __init__(self, debug=True, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)

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


class Window(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent=parent)

		# Window
		self.setGeometry(100, 100, 800, 600)

		# Menu
		# self.menubar = QMenuBar(self)
		# self.menubar.setGeometry(QRect(0, 0, 795, 25))
		# self.menubar.setObjectName("menubar")
		# self.menuFile = QMenu(self.menubar)
		# self.menuFile.setTitle("File")
		# self.menuFile.setObjectName("menuFile")
		# self.menuEdit = QMenu(self.menubar)
		# self.menuEdit.setObjectName("menuEdit")
		# self.menuHelp = QMenu(self.menubar)
		# self.menuHelp.setTitle("Help")
		# self.menuHelp.setObjectName("menuHelp")
		# self.menuView = QMenu(self.menubar)
		# self.menuView.setTitle("View")
		# self.menuView.setObjectName("menuView")
		# self.actionNew = QAction(self)
		# self.actionNew.setText("New")
		# self.actionNew.setObjectName("actionNew")
		# self.actionOpen = QAction(self)
		# self.actionOpen.setText("Open")
		# self.actionOpen.setObjectName("actionOpen")
		# self.actionModify = QAction(self)
		# self.actionModify.setText("Modify")
		# self.actionModify.setObjectName("actionModify")
		# self.menuFile.addAction(self.actionNew)
		# self.menuFile.addAction(self.actionOpen)
		# self.menuEdit.addAction(self.actionModify)
		# self.menubar.addAction(self.menuFile.menuAction())
		# self.menubar.addAction(self.menuEdit.menuAction())
		# self.menubar.addAction(self.menuView.menuAction())
		# self.menubar.addAction(self.menuHelp.menuAction())
		# self.setMenuBar(self.menubar)
		# self.menuEdit.setTitle(QApplication.translate("MainWindow", "Edit", None, -1))

		# Central Widget
		self.centralWidget = QWidget(self)
		self.centralWidget.setMouseTracking(True)
		self.centralLayout = QVBoxLayout(self.centralWidget)
		self.centralLayout.setSpacing(10)
		self.centralLayout.setContentsMargins(0, 0, 0, 0)
		self.setCentralWidget(self.centralWidget)

		# Central Splitter
		self.centralSplitter = QSplitter(self.centralWidget)
		self.centralSplitter.setHandleWidth(3)

		# Left Widget
		self.leftWidget = QWidget(self.centralSplitter)

		self.leftWidgetLayout = QVBoxLayout(self.leftWidget)
		self.leftWidgetLayout.setSpacing(5)
		self.leftWidgetLayout.setContentsMargins(0, 0, 0, 0)
		self.leftWidgetLayout.setObjectName("leftWidgetLayout")

		# Library Tab
		self.libraryTabWidget = QTabWidget(self.leftWidget)
		self.libraryTabWidget.setMouseTracking(True)
		self.libraryTabWidget.setAcceptDrops(True)
		self.libraryTabWidget.setDocumentMode(False)
		self.libraryTabWidget.setTabsClosable(False)
		self.libraryTabWidget.setMovable(True)
		self.libraryTabWidget.setCurrentIndex(0)
		self.leftWidgetLayout.addWidget(self.libraryTabWidget)

		# Library Widget
		self.libraryWidget = LibraryWidget()
		self.libraryTabWidget.addTab(self.libraryWidget, "Library")
		self.libraryWidget.selectedInstance.connect(self.loadInfoFromSelected)

		# Right Widget
		self.rightWidget = QWidget(self.centralSplitter)
		self.rightWidget.setObjectName("rightWidget")
		self.rightLayout = QVBoxLayout(self.rightWidget)
		self.rightLayout.setSpacing(5)
		self.rightLayout.setContentsMargins(0, 0, 0, 0)
		self.rightLayout.setObjectName("rightLayout")
		self.rightStackedWidget = QStackedWidget(self.rightWidget)
		self.rightStackedWidget.setObjectName("rightStackedWidget")

		# Import Widget
		self.importWidget = QWidget()
		self.importWidget.setObjectName("importWidget")
		self.importLayout = QVBoxLayout(self.importWidget)
		self.importLayout.setSpacing(0)
		self.importLayout.setContentsMargins(0, 0, 0, 0)
		self.importLayout.setObjectName("importLayout")
		self.importSplitter = QSplitter(self.importWidget)
		self.importSplitter.setMouseTracking(True)
		self.importSplitter.setOrientation(Qt.Vertical)
		self.importSplitter.setHandleWidth(3)
		self.importSplitter.setObjectName("importSplitter")

		# Preview Widget
		self.previewTabWidget = QTabWidget(self.importSplitter)
		self.previewTabWidget.setMouseTracking(True)
		self.previewTabWidget.setAcceptDrops(True)
		self.previewTabWidget.setDocumentMode(False)
		self.previewTabWidget.setTabsClosable(False)
		self.previewTabWidget.setMovable(True)
		self.previewTabWidget.setObjectName("previewTabWidget")
		self.previewWidget = QWidget()
		self.previewWidget.setObjectName("previewWidget")
		self.previewLayout = QVBoxLayout(self.previewWidget)
		self.previewLayout.setSpacing(0)
		self.previewLayout.setContentsMargins(0, 0, 0, 0)
		self.previewLayout.setObjectName("previewLayout")
		self.thumbnailLabel = QLabel(self.previewWidget)
		self.thumbnailLabel.setAlignment(Qt.AlignCenter)
		self.thumbnailLabel.setObjectName("thumbnailLabel")
		self.thumbnailLabel.setText(QApplication.translate("MainWindow", "Thumbnail", None, -1))
		self.previewLayout.addWidget(self.thumbnailLabel)
		self.previewTabWidget.addTab(self.previewWidget, "")

		# Info Widget
		self.infoTabWidget = QTabWidget(self.importSplitter)
		self.infoTabWidget.setMouseTracking(True)
		self.infoTabWidget.setAcceptDrops(True)
		self.infoTabWidget.setDocumentMode(False)
		self.infoTabWidget.setMovable(True)

		self.infoScrollArea = QScrollArea()
		self.infoScrollArea.setFrameShape(QFrame.NoFrame)
		self.infoScrollArea.setWidgetResizable(True)
		self.infoTabWidget.addTab(self.infoScrollArea, 'Info')

		self.infoWidget = InfoWidget()
		self.infoScrollArea.setWidget(self.infoWidget)

		self.importLayout.addWidget(self.importSplitter)
		self.rightStackedWidget.addWidget(self.importWidget)
		self.rightLayout.addWidget(self.rightStackedWidget)
		self.callbackButton = QPushButton(self.rightWidget)
		self.callbackButton.setText("Import")
		self.callbackButton.setObjectName("callbackButton")
		self.rightLayout.addWidget(self.callbackButton)
		self.centralLayout.addWidget(self.centralSplitter)

		# Status Bar
		self.statusbar = QStatusBar(self)
		self.statusbar.setSizeGripEnabled(False)
		self.statusbar.setObjectName("statusbar")
		self.setStatusBar(self.statusbar)

		self.rightStackedWidget.setCurrentIndex(0)
		self.previewTabWidget.setCurrentIndex(0)
		self.infoTabWidget.setCurrentIndex(0)

		self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.previewWidget),
		                                 QApplication.translate("MainWindow", "Preview", None, -1))

	def loadInfoFromSelected(self, instance):
		if instance.getKind() != component.directory:
			self.infoWidget.loadData(instance.getMetadata())
		else:
			self.infoWidget.clear()
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
	# window.setStyleSheet(getStyleSheet(os.path.join(DIRPATH, 'alpha_theme.css')))
	window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	standalone()
