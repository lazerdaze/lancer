# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lancer_ui_001.ui',
# licensing of 'lancer_ui_001.ui' applies.
#
# Created: Sun Jan 06 13:13:57 2019
#      by: pyside2-uic  running on PySide2 5.11.0a1.dev1528378291
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(768, 558)
		MainWindow.setStyleSheet("QWidget{\n"
		                         "color:white;\n"
		                         "font-family: \"Arial\";\n"
		                         "background-color: rgb(25, 25, 25);\n"
		                         "}\n"
		                         "\n"
		                         "QPushButton{\n"
		                         "height:30;\n"
		                         "margin:0;\n"
		                         "padding:0 10;\n"
		                         "border:none;\n"
		                         "background-color:rgb(50, 150, 255);\n"
		                         "font-weight:bold;\n"
		                         "}\n"
		                         "\n"
		                         "QListView {\n"
		                         "border:none;\n"
		                         "}\n"
		                         "\n"
		                         "QListView::item {\n"
		                         "height:40px;\n"
		                         "color: rgb(95,95,95);\n"
		                         "border:none;\n"
		                         "padding-left:10;\n"
		                         "}\n"
		                         "\n"
		                         "QListView::item:selected {\n"
		                         "background-color: rgb(35, 35, 35);\n"
		                         "color:white;\n"
		                         "border-left:3px solid rgb(44,151,222);\n"
		                         "}\n"
		                         "QListView::item:hover {\n"
		                         "background-color: rgb(35, 35, 35);\n"
		                         "color:white;\n"
		                         "}\n"
		                         "QListView::item:selected:hover {\n"
		                         "background-color: rgb(35, 35, 35);\n"
		                         "}\n"
		                         "\n"
		                         "QScrollBar:vertical {\n"
		                         " width: 10px; \n"
		                         "}\n"
		                         " QScrollBar::handle:vertical {\n"
		                         "     background: rgb(80, 80, 80);\n"
		                         "     min-height: 20px;\n"
		                         " }\n"
		                         " QScrollBar::add-line:vertical {\n"
		                         "    border: none;\n"
		                         "      background: none;\n"
		                         " }\n"
		                         "\n"
		                         " QScrollBar::sub-line:vertical {\n"
		                         "     border: none;\n"
		                         "      background: none;\n"
		                         " }\n"
		                         "\n"
		                         " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
		                         "     background: none;\n"
		                         " }\n"
		                         "\n"
		                         "QTabWidget::pane {\n"
		                         "border-top: 2px solid rgb(38,38,38);\n"
		                         "}\n"
		                         "QTabBar::tab {\n"
		                         "border:none;\n"
		                         "padding: 0 20;\n"
		                         "margin:0;\n"
		                         "color: rgb(95,95,95);\n"
		                         "height:40;\n"
		                         "}\n"
		                         "QTabBar::tab:selected {\n"
		                         "color:rgb(44,151,222);\n"
		                         "}\n"
		                         "QTabBar::tab:hover {\n"
		                         "color:white;\n"
		                         "}\n"
		                         "QTabBar::tab:selected:hover {\n"
		                         "color:rgb(44,151,222);\n"
		                         "}\n"
		                         "\n"
		                         "\n"
		                         "QGroupBox  {\n"
		                         "border-top: 2px solid rgb(45,45,45);\n"
		                         "margin-top: 40px;\n"
		                         "font-size: 16px;\n"
		                         "font-weight:bold;\n"
		                         "}\n"
		                         "\n"
		                         "QGroupBox::title  {\n"
		                         "subcontrol-origin: margin;\n"
		                         "subcontrol-position: top left;\n"
		                         "padding:10;\n"
		                         "}\n"
		                         "\n"
		                         "\n"
		                         "")
		MainWindow.setAnimated(False)
		MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.centralLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.centralLayout.setSpacing(10)
		self.centralLayout.setContentsMargins(0, 0, 0, 0)
		self.centralLayout.setObjectName("centralLayout")
		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(10)
		font.setWeight(75)
		font.setBold(True)
		self.tabWidget.setFont(font)
		self.tabWidget.setStyleSheet("\n"
		                             "")
		self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
		self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
		self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
		self.tabWidget.setUsesScrollButtons(True)
		self.tabWidget.setDocumentMode(False)
		self.tabWidget.setTabsClosable(False)
		self.tabWidget.setObjectName("tabWidget")
		self.tab_1 = QtWidgets.QWidget()
		self.tab_1.setEnabled(True)
		self.tab_1.setObjectName("tab_1")
		self.tab_1_layout = QtWidgets.QHBoxLayout(self.tab_1)
		self.tab_1_layout.setSpacing(0)
		self.tab_1_layout.setContentsMargins(0, 0, 0, 0)
		self.tab_1_layout.setObjectName("tab_1_layout")
		self.listWidget = QtWidgets.QListWidget(self.tab_1)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
		self.listWidget.setSizePolicy(sizePolicy)
		self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
		self.listWidget.setStyleSheet("\n"
		                              "\n"
		                              "")
		self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.listWidget.setProperty("showDropIndicator", False)
		self.listWidget.setAlternatingRowColors(False)
		self.listWidget.setIconSize(QtCore.QSize(30, 30))
		self.listWidget.setObjectName("listWidget")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/images/icon_01_100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		item = QtWidgets.QListWidgetItem(self.listWidget)
		item.setIcon(icon)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/images/icon_02_100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		item = QtWidgets.QListWidgetItem(self.listWidget)
		item.setIcon(icon1)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(":/images/icon_03_100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		item = QtWidgets.QListWidgetItem(self.listWidget)
		item.setIcon(icon2)
		QtWidgets.QListWidgetItem(self.listWidget)
		QtWidgets.QListWidgetItem(self.listWidget)
		QtWidgets.QListWidgetItem(self.listWidget)
		QtWidgets.QListWidgetItem(self.listWidget)
		QtWidgets.QListWidgetItem(self.listWidget)
		QtWidgets.QListWidgetItem(self.listWidget)
		QtWidgets.QListWidgetItem(self.listWidget)
		self.tab_1_layout.addWidget(self.listWidget)
		self.tab_1_infoFrame = QtWidgets.QFrame(self.tab_1)
		self.tab_1_infoFrame.setStyleSheet("QFrame{\n"
		                                   "background-color:rgb(35,35,35);\n"
		                                   "}\n"
		                                   "\n"
		                                   "QFrame > QWidget{\n"
		                                   "background:none;\n"
		                                   "}\n"
		                                   "\n"
		                                   "QFrame > QPushButton{\n"
		                                   "background-color:rgb(50, 150, 255);\n"
		                                   "}")
		self.tab_1_infoFrame.setObjectName("tab_1_infoFrame")
		self.tab_1_bodyLayout = QtWidgets.QVBoxLayout(self.tab_1_infoFrame)
		self.tab_1_bodyLayout.setSpacing(0)
		self.tab_1_bodyLayout.setContentsMargins(0, 0, 0, 0)
		self.tab_1_bodyLayout.setObjectName("tab_1_bodyLayout")
		self.tab_1_info = QtWidgets.QGroupBox(self.tab_1_infoFrame)
		self.tab_1_info.setObjectName("tab_1_info")
		self.tab_1_infoLayout = QtWidgets.QVBoxLayout(self.tab_1_info)
		self.tab_1_infoLayout.setSpacing(10)
		self.tab_1_infoLayout.setContentsMargins(10, 10, 10, 10)
		self.tab_1_infoLayout.setObjectName("tab_1_infoLayout")
		self.tab_1_infoText = QtWidgets.QLabel(self.tab_1_info)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.tab_1_infoText.sizePolicy().hasHeightForWidth())
		self.tab_1_infoText.setSizePolicy(sizePolicy)
		self.tab_1_infoText.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ")
		self.tab_1_infoText.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.tab_1_infoText.setWordWrap(True)
		self.tab_1_infoText.setObjectName("tab_1_infoText")
		self.tab_1_infoLayout.addWidget(self.tab_1_infoText)
		self.tab_1_bodyLayout.addWidget(self.tab_1_info)
		self.tab_1_options = QtWidgets.QGroupBox(self.tab_1_infoFrame)
		self.tab_1_options.setTitle("Options")
		self.tab_1_options.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.tab_1_options.setFlat(False)
		self.tab_1_options.setCheckable(False)
		self.tab_1_options.setObjectName("tab_1_options")
		self.tab_1_optionsLayout = QtWidgets.QVBoxLayout(self.tab_1_options)
		self.tab_1_optionsLayout.setSpacing(10)
		self.tab_1_optionsLayout.setContentsMargins(10, 10, 10, 10)
		self.tab_1_optionsLayout.setObjectName("tab_1_optionsLayout")
		self.tab_1_optionsText = QtWidgets.QLabel(self.tab_1_options)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.tab_1_optionsText.sizePolicy().hasHeightForWidth())
		self.tab_1_optionsText.setSizePolicy(sizePolicy)
		self.tab_1_optionsText.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.tab_1_optionsText.setWordWrap(True)
		self.tab_1_optionsText.setObjectName("tab_1_optionsText")
		self.tab_1_optionsLayout.addWidget(self.tab_1_optionsText)
		self.tab_1_bodyLayout.addWidget(self.tab_1_options)
		self.applyButton = QtWidgets.QPushButton(self.tab_1_infoFrame)
		self.applyButton.setStyleSheet("")
		self.applyButton.setAutoDefault(False)
		self.applyButton.setDefault(False)
		self.applyButton.setFlat(False)
		self.applyButton.setObjectName("applyButton")
		self.tab_1_bodyLayout.addWidget(self.applyButton)
		self.tab_1_layout.addWidget(self.tab_1_infoFrame)
		self.tabWidget.addTab(self.tab_1, "New")
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.tabWidget.addTab(self.tab_2, "")
		self.centralLayout.addWidget(self.tabWidget)
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.actionNew = QtWidgets.QAction(MainWindow)
		self.actionNew.setObjectName("actionNew")
		self.actionModidy = QtWidgets.QAction(MainWindow)
		self.actionModidy.setObjectName("actionModidy")

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
		self.listWidget.setSortingEnabled(False)
		__sortingEnabled = self.listWidget.isSortingEnabled()
		self.listWidget.setSortingEnabled(False)
		self.listWidget.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "CA Soft IK", None, -1))
		self.listWidget.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "Noise", None, -1))
		self.listWidget.item(2).setText(QtWidgets.QApplication.translate("MainWindow", "Reduce", None, -1))
		self.listWidget.item(3).setText(QtWidgets.QApplication.translate("MainWindow", "Ribbon", None, -1))
		self.listWidget.item(4).setText(QtWidgets.QApplication.translate("MainWindow", "Simple Doft IK", None, -1))
		self.listWidget.item(5).setText(QtWidgets.QApplication.translate("MainWindow", "Sine", None, -1))
		self.listWidget.item(6).setText(QtWidgets.QApplication.translate("MainWindow", "Spline Sine", None, -1))
		self.listWidget.item(7).setText(QtWidgets.QApplication.translate("MainWindow", "Spring", None, -1))
		self.listWidget.item(8).setText(QtWidgets.QApplication.translate("MainWindow", "Tail Dynamics", None, -1))
		self.listWidget.item(9).setText(QtWidgets.QApplication.translate("MainWindow", "Transform Noise", None, -1))
		self.listWidget.setSortingEnabled(__sortingEnabled)
		self.tab_1_info.setTitle(QtWidgets.QApplication.translate("MainWindow", "Info.", None, -1))
		self.tab_1_optionsText.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
		self.applyButton.setText(QtWidgets.QApplication.translate("MainWindow", "APPLY", None, -1))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
		                          QtWidgets.QApplication.translate("MainWindow", "Page", None, -1))
		self.actionNew.setText(QtWidgets.QApplication.translate("MainWindow", "New", None, -1))
		self.actionModidy.setText(QtWidgets.QApplication.translate("MainWindow", "Modify", None, -1))


if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
