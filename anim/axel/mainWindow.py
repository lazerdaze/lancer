# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui',
# licensing of 'mainWindow.ui' applies.
#
# Created: Mon Nov 05 21:48:12 2018
#      by: pyside2-uic  running on PySide2 5.11.0a1.dev1528378291
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 747)
        MainWindow.setStyleSheet("/*QMainWindow*/\n"
"\n"
"QMainWindow{\n"
"background:rgb(100, 100, 100);\n"
"color: white;\n"
"border:none;\n"
"border-radius:0;\n"
"}\n"
"\n"
"/*QWidget*/\n"
"QWidget{\n"
"margin:0;\n"
"padding:0;\n"
"background:rgb(100, 100, 100);\n"
"color:white;\n"
"border-radius:0;\n"
"border:none;\n"
"}\n"
"\n"
"/*QMenuBar*/\n"
"\n"
"QMenuBar{\n"
"background-color:#111517;\n"
"border-bottom:1px solid black;\n"
"border-radius:0;\n"
"margin:0;\n"
"padding:0;\n"
"}\n"
"\n"
"\n"
"QMenuBar::item {\n"
"padding: 5px 10px 5px 10px;\n"
"border-radius:0;\n"
"border:none;\n"
"margin-bottom:-1px\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected {\n"
"background-color:#0b0e0f;\n"
"border-top: 2px solid #33839f;\n"
"padding-top:3px;\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed {\n"
"background-color:#0b0e0f;\n"
"border-top: 2px solid #33839f;\n"
"padding-top:3px;\n"
"}\n"
"\n"
"\n"
"QMenu{\n"
"padding:0;\n"
"margin:0;\n"
"outline:8px solid red;\n"
"background-color:#0b0e0f;\n"
"}\n"
"\n"
"/*QStatusBar*/\n"
"\n"
"QStatusBar{\n"
"background:rgb(125, 125,125);\n"
"}\n"
"\n"
"/*QPushButton*/\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"background-color:rgb(161, 230, 255);\n"
"border:none;\n"
"padding:5;\n"
"margin:0;\n"
"height:15;\n"
"font:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgb(197, 238, 255);\n"
"}\n"
"\n"
"/*QToolButton*/\n"
"\n"
"QToolButton{\n"
"background:none;\n"
"border:none;\n"
"height:19;\n"
"width:19;\n"
"margin:0;\n"
"padding:1;\n"
"color:white;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"border:1px solid white;\n"
"}\n"
"\n"
"/*QLineEdit*/\n"
"\n"
"QLineEdit{\n"
"background:rgb(50, 50, 50);\n"
"color:white;\n"
"border:none;\n"
"padding:5;\n"
"margin:0;\n"
"height:15;\n"
"}\n"
"\n"
"QTabWidget QWidget QLineEdit{\n"
"background:rgb(50, 50, 50);\n"
"color:white;\n"
"border:none;\n"
"padding:5;\n"
"margin:0;\n"
"height:15;\n"
"}\n"
"\n"
"/*QTabWidgett*/\n"
"\n"
"QTabWidget{\n"
"background:rgb(75, 75, 75);\n"
"border:none;\n"
"}\n"
"\n"
"QTabWidget QWidget{\n"
"background:rgb(75, 75, 75);\n"
"border:none;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"border-top: 40px solid rgb(75, 75, 75);\n"
"position: absolute;\n"
"top: -40px;\n"
"}\n"
"\n"
"QTabWidget::pane > QWidget{\n"
"background:rgb(75, 75, 75);\n"
"}\n"
"\n"
"QTabBar{\n"
"border:none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"color:rgb(120, 120, 120);\n"
"padding:10 10 10 15;\n"
"border:0;\n"
"background:rgb(75, 75, 75);\n"
"height:15;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected{\n"
"color:white;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:hover {\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected:hover {\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"/*QScrollBar*/\n"
"\n"
"QScrollBar {\n"
"width: 5px;\n"
"height: 5px;\n"
"background-color: #0b0e0f;\n"
"border:0;\n"
"border-radius:0;\n"
"}\n"
"\n"
"QScrollBar::groove {\n"
"background:none;\n"
"border:0;\n"
"border-radius:0;\n"
"}\n"
"\n"
"QScrollBar::handle{\n"
"background-color:rgb(161, 230, 255);\n"
"min-height: 20px;\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line{\n"
"border: none;\n"
"background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line{\n"
"border: none;\n"
"background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"background: none;\n"
"border: none;\n"
"}\n"
"\n"
"/* QListView*/\n"
"\n"
"QListView {\n"
"border: 0;\n"
"}\n"
"\n"
"\n"
"QListView::item {\n"
"background:none;\n"
"color:white;\n"
"border:none;\n"
"padding:5 5 5 12;\n"
"}\n"
"\n"
"\n"
"QListView::item:selected {\n"
"background-color:rgb(160, 160, 160);\n"
"color:white;\n"
"}\n"
"\n"
"\n"
"QListView::item:hover {\n"
"background:none;\n"
"border:none;\n"
"color:white;\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:hover {\n"
"background-color:rgb(160, 160, 160);\n"
"color:white;\n"
"}\n"
"\n"
"/* Line*/\n"
"QFrame[frameShape=\"4\"],\n"
"QFrame[frameShape=\"5\"]\n"
"{\n"
"border: none;\n"
"background:rgb(75, 75, 75);\n"
"}\n"
"\n"
"/* QTreeView*/\n"
"QTreeView{\n"
"padding:0;\n"
"margin:0;\n"
"show-decoration-selected: 1;\n"
"border:0;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: black;\n"
"border:none;\n"
"margin:0;\n"
"padding:0;\n"
"}\n"
"\n"
"\n"
"QTreeView::item {\n"
"background:none;\n"
"color:white;\n"
"border:none;\n"
"padding:5 5 5 12;\n"
"margin:0;\n"
"}\n"
"\n"
"\n"
"QTreeView::item:hover {\n"
"border:none;\n"
"background-color:rgb(160, 160, 160);\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected {\n"
"color:white;\n"
"border:none;\n"
"background-color:rgb(160, 160, 160);\n"
"}\n"
"\n"
"/*QSplitter*/\n"
"\n"
"\n"
"QSplitter::handle:horizontal{\n"
"width: 10px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical{\n"
" height: 10px;\n"
"}\n"
"\n"
"QSplitter::handle:pressed{\n"
"background-color:rgb(161, 230, 255);\n"
"}\n"
"\n"
"QSplitter::handle:hover{\n"
"background-color:rgb(161, 230, 255);\n"
"}\n"
"\n"
"QSplitterHandle:hover{\n"
"}  \n"
"\n"
"QSplitter::handle:horizontal:hover{\n"
"}\n"
"")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setMouseTracking(True)
        self.centralWidget.setObjectName("centralWidget")
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.centralLayout.setSpacing(10)
        self.centralLayout.setContentsMargins(0, 10, 0, 3)
        self.centralLayout.setObjectName("centralLayout")
        self.headerWidget = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerWidget.sizePolicy().hasHeightForWidth())
        self.headerWidget.setSizePolicy(sizePolicy)
        self.headerWidget.setObjectName("headerWidget")
        self.headerLayout = QtWidgets.QHBoxLayout(self.headerWidget)
        self.headerLayout.setSpacing(5)
        self.headerLayout.setContentsMargins(0, 0, 0, 0)
        self.headerLayout.setObjectName("headerLayout")
        self.refreshButton = QtWidgets.QToolButton(self.headerWidget)
        self.refreshButton.setObjectName("refreshButton")
        self.headerLayout.addWidget(self.refreshButton)
        self.backButton = QtWidgets.QToolButton(self.headerWidget)
        self.backButton.setObjectName("backButton")
        self.headerLayout.addWidget(self.backButton)
        self.forwardButton = QtWidgets.QToolButton(self.headerWidget)
        self.forwardButton.setObjectName("forwardButton")
        self.headerLayout.addWidget(self.forwardButton)
        self.directoryLabel = QtWidgets.QLabel(self.headerWidget)
        self.directoryLabel.setText("I:\\lancer\\anim\\axel")
        self.directoryLabel.setObjectName("directoryLabel")
        self.headerLayout.addWidget(self.directoryLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.headerLayout.addItem(spacerItem)
        self.searchLineEdit = QtWidgets.QLineEdit(self.headerWidget)
        self.searchLineEdit.setInputMask("")
        self.searchLineEdit.setText("Search")
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.headerLayout.addWidget(self.searchLineEdit)
        self.centralLayout.addWidget(self.headerWidget)
        self.centralSplitter = QtWidgets.QSplitter(self.centralWidget)
        self.centralSplitter.setCursor(QtCore.Qt.ArrowCursor)
        self.centralSplitter.setStyleSheet("")
        self.centralSplitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.centralSplitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.centralSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.centralSplitter.setOpaqueResize(True)
        self.centralSplitter.setHandleWidth(3)
        self.centralSplitter.setObjectName("centralSplitter")
        self.leftWidget = QtWidgets.QWidget(self.centralSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftWidget.sizePolicy().hasHeightForWidth())
        self.leftWidget.setSizePolicy(sizePolicy)
        self.leftWidget.setObjectName("leftWidget")
        self.leftLayout = QtWidgets.QVBoxLayout(self.leftWidget)
        self.leftLayout.setSpacing(5)
        self.leftLayout.setContentsMargins(0, 0, 0, 0)
        self.leftLayout.setObjectName("leftLayout")
        self.leftSplitter = QtWidgets.QSplitter(self.leftWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftSplitter.sizePolicy().hasHeightForWidth())
        self.leftSplitter.setSizePolicy(sizePolicy)
        self.leftSplitter.setMouseTracking(False)
        self.leftSplitter.setOrientation(QtCore.Qt.Vertical)
        self.leftSplitter.setHandleWidth(3)
        self.leftSplitter.setObjectName("leftSplitter")
        self.collectionsTabWidget = QtWidgets.QTabWidget(self.leftSplitter)
        self.collectionsTabWidget.setMouseTracking(True)
        self.collectionsTabWidget.setAcceptDrops(True)
        self.collectionsTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.collectionsTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.collectionsTabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.collectionsTabWidget.setUsesScrollButtons(True)
        self.collectionsTabWidget.setDocumentMode(False)
        self.collectionsTabWidget.setMovable(True)
        self.collectionsTabWidget.setObjectName("collectionsTabWidget")
        self.favoriteWidget = QtWidgets.QWidget()
        self.favoriteWidget.setObjectName("favoriteWidget")
        self.favoriteLayout = QtWidgets.QVBoxLayout(self.favoriteWidget)
        self.favoriteLayout.setSpacing(5)
        self.favoriteLayout.setContentsMargins(0, 0, 0, 0)
        self.favoriteLayout.setObjectName("favoriteLayout")
        self.favoriteListWidget = QtWidgets.QListWidget(self.favoriteWidget)
        self.favoriteListWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.favoriteListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.favoriteListWidget.setProperty("showDropIndicator", False)
        self.favoriteListWidget.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.favoriteListWidget.setAlternatingRowColors(False)
        self.favoriteListWidget.setObjectName("favoriteListWidget")
        QtWidgets.QListWidgetItem(self.favoriteListWidget)
        QtWidgets.QListWidgetItem(self.favoriteListWidget)
        QtWidgets.QListWidgetItem(self.favoriteListWidget)
        QtWidgets.QListWidgetItem(self.favoriteListWidget)
        self.favoriteLayout.addWidget(self.favoriteListWidget)
        self.collectionsTabWidget.addTab(self.favoriteWidget, "Favorite")
        self.tagsWidget = QtWidgets.QWidget()
        self.tagsWidget.setObjectName("tagsWidget")
        self.tagsLayout = QtWidgets.QVBoxLayout(self.tagsWidget)
        self.tagsLayout.setSpacing(5)
        self.tagsLayout.setContentsMargins(0, 0, 0, 0)
        self.tagsLayout.setObjectName("tagsLayout")
        self.tagsTreeWidget = QtWidgets.QTreeWidget(self.tagsWidget)
        self.tagsTreeWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tagsTreeWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tagsTreeWidget.setObjectName("tagsTreeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.tagsTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.tagsTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.tagsTreeWidget)
        self.tagsTreeWidget.header().setVisible(False)
        self.tagsLayout.addWidget(self.tagsTreeWidget)
        self.tagsExtrasLayout = QtWidgets.QHBoxLayout()
        self.tagsExtrasLayout.setSpacing(0)
        self.tagsExtrasLayout.setObjectName("tagsExtrasLayout")
        self.tagsLineEdit = QtWidgets.QLineEdit(self.tagsWidget)
        self.tagsLineEdit.setText("Add Tags Separated by Commas.")
        self.tagsLineEdit.setObjectName("tagsLineEdit")
        self.tagsExtrasLayout.addWidget(self.tagsLineEdit)
        self.tagsButton = QtWidgets.QToolButton(self.tagsWidget)
        self.tagsButton.setText("+")
        self.tagsButton.setObjectName("tagsButton")
        self.tagsExtrasLayout.addWidget(self.tagsButton)
        self.tagsLayout.addLayout(self.tagsExtrasLayout)
        self.collectionsTabWidget.addTab(self.tagsWidget, "Tags")
        self.libraryTabWidget = QtWidgets.QTabWidget(self.leftSplitter)
        self.libraryTabWidget.setMouseTracking(True)
        self.libraryTabWidget.setAcceptDrops(True)
        self.libraryTabWidget.setDocumentMode(False)
        self.libraryTabWidget.setTabsClosable(False)
        self.libraryTabWidget.setMovable(True)
        self.libraryTabWidget.setObjectName("libraryTabWidget")
        self.libraryWidget = QtWidgets.QWidget()
        self.libraryWidget.setObjectName("libraryWidget")
        self.libraryLayout = QtWidgets.QVBoxLayout(self.libraryWidget)
        self.libraryLayout.setSpacing(0)
        self.libraryLayout.setContentsMargins(0, 0, 0, 0)
        self.libraryLayout.setObjectName("libraryLayout")
        self.libraryTreeView = QtWidgets.QTreeView(self.libraryWidget)
        self.libraryTreeView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.libraryTreeView.setObjectName("libraryTreeView")
        self.libraryLayout.addWidget(self.libraryTreeView)
        self.libraryTabWidget.addTab(self.libraryWidget, "Library")
        self.leftLayout.addWidget(self.leftSplitter)
        self.middleWidget = QtWidgets.QWidget(self.centralSplitter)
        self.middleWidget.setStyleSheet("background:rgb(75, 75, 75);")
        self.middleWidget.setObjectName("middleWidget")
        self.middleLayout = QtWidgets.QVBoxLayout(self.middleWidget)
        self.middleLayout.setSpacing(5)
        self.middleLayout.setContentsMargins(0, 0, 0, 0)
        self.middleLayout.setObjectName("middleLayout")
        self.middleExtrasLayout = QtWidgets.QHBoxLayout()
        self.middleExtrasLayout.setSpacing(5)
        self.middleExtrasLayout.setObjectName("middleExtrasLayout")
        self.toolButton_2 = QtWidgets.QToolButton(self.middleWidget)
        self.toolButton_2.setObjectName("toolButton_2")
        self.middleExtrasLayout.addWidget(self.toolButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.middleExtrasLayout.addItem(spacerItem1)
        self.toolButton = QtWidgets.QToolButton(self.middleWidget)
        self.toolButton.setObjectName("toolButton")
        self.middleExtrasLayout.addWidget(self.toolButton)
        self.horizontalSlider = QtWidgets.QSlider(self.middleWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.middleExtrasLayout.addWidget(self.horizontalSlider)
        self.toolButton_3 = QtWidgets.QToolButton(self.middleWidget)
        self.toolButton_3.setObjectName("toolButton_3")
        self.middleExtrasLayout.addWidget(self.toolButton_3)
        self.middleLayout.addLayout(self.middleExtrasLayout)
        self.middleScrollArea = QtWidgets.QScrollArea(self.middleWidget)
        self.middleScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.middleScrollArea.setWidgetResizable(True)
        self.middleScrollArea.setObjectName("middleScrollArea")
        self.middleScrollWidget = QtWidgets.QWidget()
        self.middleScrollWidget.setGeometry(QtCore.QRect(0, 0, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middleScrollWidget.sizePolicy().hasHeightForWidth())
        self.middleScrollWidget.setSizePolicy(sizePolicy)
        self.middleScrollWidget.setMaximumSize(QtCore.QSize(150, 150))
        self.middleScrollWidget.setObjectName("middleScrollWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.middleScrollWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.middleScrollArea.setWidget(self.middleScrollWidget)
        self.middleLayout.addWidget(self.middleScrollArea)
        self.rightWidget = QtWidgets.QWidget(self.centralSplitter)
        self.rightWidget.setObjectName("rightWidget")
        self.rightLayout = QtWidgets.QVBoxLayout(self.rightWidget)
        self.rightLayout.setSpacing(5)
        self.rightLayout.setContentsMargins(0, 0, 0, 0)
        self.rightLayout.setObjectName("rightLayout")
        self.rightStackedWidget = QtWidgets.QStackedWidget(self.rightWidget)
        self.rightStackedWidget.setObjectName("rightStackedWidget")
        self.importWidget = QtWidgets.QWidget()
        self.importWidget.setObjectName("importWidget")
        self.importLayout = QtWidgets.QVBoxLayout(self.importWidget)
        self.importLayout.setSpacing(0)
        self.importLayout.setContentsMargins(0, 0, 0, 0)
        self.importLayout.setObjectName("importLayout")
        self.importSplitter = QtWidgets.QSplitter(self.importWidget)
        self.importSplitter.setMouseTracking(True)
        self.importSplitter.setOrientation(QtCore.Qt.Vertical)
        self.importSplitter.setHandleWidth(3)
        self.importSplitter.setObjectName("importSplitter")
        self.previewTabWidget = QtWidgets.QTabWidget(self.importSplitter)
        self.previewTabWidget.setMouseTracking(True)
        self.previewTabWidget.setAcceptDrops(True)
        self.previewTabWidget.setDocumentMode(False)
        self.previewTabWidget.setTabsClosable(False)
        self.previewTabWidget.setMovable(True)
        self.previewTabWidget.setObjectName("previewTabWidget")
        self.previewWidget = QtWidgets.QWidget()
        self.previewWidget.setObjectName("previewWidget")
        self.previewLayout = QtWidgets.QVBoxLayout(self.previewWidget)
        self.previewLayout.setSpacing(0)
        self.previewLayout.setContentsMargins(0, 0, 0, 0)
        self.previewLayout.setObjectName("previewLayout")
        self.thumbnailLabel = QtWidgets.QLabel(self.previewWidget)
        self.thumbnailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.thumbnailLabel.setObjectName("thumbnailLabel")
        self.previewLayout.addWidget(self.thumbnailLabel)
        self.previewTabWidget.addTab(self.previewWidget, "")
        self.infoTabWidget = QtWidgets.QTabWidget(self.importSplitter)
        self.infoTabWidget.setMouseTracking(True)
        self.infoTabWidget.setAcceptDrops(True)
        self.infoTabWidget.setDocumentMode(False)
        self.infoTabWidget.setMovable(True)
        self.infoTabWidget.setObjectName("infoTabWidget")
        self.infoWidget = QtWidgets.QWidget()
        self.infoWidget.setObjectName("infoWidget")
        self.infoLayout = QtWidgets.QVBoxLayout(self.infoWidget)
        self.infoLayout.setSpacing(0)
        self.infoLayout.setContentsMargins(0, 0, 0, 0)
        self.infoLayout.setObjectName("infoLayout")
        self.infoScrollArea = QtWidgets.QScrollArea(self.infoWidget)
        self.infoScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.infoScrollArea.setWidgetResizable(True)
        self.infoScrollArea.setObjectName("infoScrollArea")
        self.infoScrollWidget = QtWidgets.QWidget()
        self.infoScrollWidget.setGeometry(QtCore.QRect(0, 0, 207, 275))
        self.infoScrollWidget.setObjectName("infoScrollWidget")
        self.infoScrollLayout = QtWidgets.QVBoxLayout(self.infoScrollWidget)
        self.infoScrollLayout.setSpacing(0)
        self.infoScrollLayout.setContentsMargins(0, 0, 0, 0)
        self.infoScrollLayout.setObjectName("infoScrollLayout")
        self.infoLabel = QtWidgets.QLabel(self.infoScrollWidget)
        self.infoLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.infoLabel.setObjectName("infoLabel")
        self.infoScrollLayout.addWidget(self.infoLabel)
        self.infoScrollArea.setWidget(self.infoScrollWidget)
        self.infoLayout.addWidget(self.infoScrollArea)
        self.infoTabWidget.addTab(self.infoWidget, "")
        self.importLayout.addWidget(self.importSplitter)
        self.rightStackedWidget.addWidget(self.importWidget)
        self.rightLayout.addWidget(self.rightStackedWidget)
        self.callbackButton = QtWidgets.QPushButton(self.rightWidget)
        self.callbackButton.setText("Import")
        self.callbackButton.setObjectName("callbackButton")
        self.rightLayout.addWidget(self.callbackButton)
        self.centralLayout.addWidget(self.centralSplitter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setTitle("File")
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setTitle("Help")
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setTitle("View")
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setText("New")
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setText("Open")
        self.actionOpen.setObjectName("actionOpen")
        self.actionModify = QtWidgets.QAction(MainWindow)
        self.actionModify.setText("Modify")
        self.actionModify.setObjectName("actionModify")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuEdit.addAction(self.actionModify)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.collectionsTabWidget.setCurrentIndex(1)
        self.libraryTabWidget.setCurrentIndex(0)
        self.rightStackedWidget.setCurrentIndex(0)
        self.previewTabWidget.setCurrentIndex(0)
        self.infoTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.refreshButton.setText(QtWidgets.QApplication.translate("MainWindow", "O", None, -1))
        self.backButton.setText(QtWidgets.QApplication.translate("MainWindow", "<", None, -1))
        self.forwardButton.setText(QtWidgets.QApplication.translate("MainWindow", ">", None, -1))
        self.favoriteListWidget.setSortingEnabled(False)
        __sortingEnabled = self.favoriteListWidget.isSortingEnabled()
        self.favoriteListWidget.setSortingEnabled(False)
        self.favoriteListWidget.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "HUD", None, -1))
        self.favoriteListWidget.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "Space", None, -1))
        self.favoriteListWidget.item(2).setText(QtWidgets.QApplication.translate("MainWindow", "Yellow", None, -1))
        self.favoriteListWidget.item(3).setText(QtWidgets.QApplication.translate("MainWindow", "Sports", None, -1))
        self.favoriteListWidget.setSortingEnabled(__sortingEnabled)
        self.tagsTreeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "Name", None, -1))
        __sortingEnabled = self.tagsTreeWidget.isSortingEnabled()
        self.tagsTreeWidget.setSortingEnabled(False)
        self.tagsTreeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "People", None, -1))
        self.tagsTreeWidget.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "Characters", None, -1))
        self.tagsTreeWidget.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "Animals", None, -1))
        self.tagsTreeWidget.setSortingEnabled(__sortingEnabled)
        self.toolButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.toolButton.setText(QtWidgets.QApplication.translate("MainWindow", "-", None, -1))
        self.toolButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.thumbnailLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Thumbnail", None, -1))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.previewWidget), QtWidgets.QApplication.translate("MainWindow", "Preview", None, -1))
        self.infoLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Info Text", None, -1))
        self.infoTabWidget.setTabText(self.infoTabWidget.indexOf(self.infoWidget), QtWidgets.QApplication.translate("MainWindow", "Info", None, -1))
        self.menuEdit.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))

import axel_resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

