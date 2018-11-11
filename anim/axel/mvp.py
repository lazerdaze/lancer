# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mvp.ui',
# licensing of 'mvp.ui' applies.
#
# Created: Tue Nov 06 13:26:00 2018
#      by: pyside2-uic  running on PySide2 5.11.0a1.dev1528378291
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 671)
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
        self.leftWidgetLayout = QtWidgets.QVBoxLayout(self.leftWidget)
        self.leftWidgetLayout.setSpacing(5)
        self.leftWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.leftWidgetLayout.setObjectName("leftWidgetLayout")
        self.libraryTabWidget = QtWidgets.QTabWidget(self.leftWidget)
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
        self.leftWidgetLayout.addWidget(self.libraryTabWidget)
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
        self.infoScrollWidget.setGeometry(QtCore.QRect(0, 0, 261, 255))
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 25))
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
        self.libraryTabWidget.setCurrentIndex(0)
        self.rightStackedWidget.setCurrentIndex(0)
        self.previewTabWidget.setCurrentIndex(0)
        self.infoTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
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

