import sys
from Qt import QtCore, QtWidgets, QtGui


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(639, 426)
		MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);\n"
		                         "color:rgb(255, 255, 255);")
		MainWindow.setAnimated(False)
		MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
		                             "border-top: 2px solid rgb(28,28,28);\n"
		                             "}\n"
		                             "QTabBar::tab {\n"
		                             "    border-top: 2px solid rgb(28,28,28);\n"
		                             "     border-right: 2px solid rgb(28,28,28);\n"
		                             "    padding: 10px 25px 10px 25px;\n"
		                             "}\n"
		                             "QTabBar::tab:selected {\n"
		                             "    background-color: rgb(255, 66, 3)\n"
		                             "}\n"
		                             "QTabBar::tab:hover {\n"
		                             "    background-color:rgb(80, 80, 80)\n"
		                             "}\n"
		                             "QTabBar::tab:selected:hover {\n"
		                             "    background-color: rgb(254, 92, 33)\n"
		                             "}\n"
		                             "")
		self.tabWidget.setObjectName("tabWidget")
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.widget = QtWidgets.QWidget(self.tab)
		self.widget.setMinimumSize(QtCore.QSize(260, 0))
		self.widget.setMaximumSize(QtCore.QSize(260, 16777215))
		self.widget.setObjectName("widget")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setSpacing(0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.lineEdit = QtWidgets.QLineEdit(self.widget)
		self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
		self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
		self.lineEdit.setStyleSheet("background-color:rgb(25, 25, 25);\n"
		                            "border:0;")
		self.lineEdit.setText("")
		self.lineEdit.setFrame(True)
		self.lineEdit.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
		self.lineEdit.setReadOnly(False)
		self.lineEdit.setObjectName("lineEdit")
		self.verticalLayout_2.addWidget(self.lineEdit)
		self.listWidget = QtWidgets.QListWidget(self.widget)
		self.listWidget.setStyleSheet("QListView {\n"
		                              "border: 1px solid rgb(28,28,28);\n"
		                              "background-color: rgb(42,42,42);\n"
		                              "alternate-background-color: rgb(38,38,38);\n"
		                              "}\n"
		                              "\n"
		                              "QListView::item {\n"
		                              "height:30px;\n"
		                              "}\n"
		                              "QListView::item:selected {\n"
		                              "    background-color: rgb(255, 66, 3);\n"
		                              "    color:white;\n"
		                              "}\n"
		                              "QListView::item:hover {\n"
		                              "    background-color:rgb(80, 80, 80)\n"
		                              "}\n"
		                              "QListView::item:selected:hover {\n"
		                              "    background-color: rgb(254, 92, 33)\n"
		                              "}\n"
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
		                              "")
		self.listWidget.setProperty("showDropIndicator", False)
		self.listWidget.setAlternatingRowColors(True)
		self.listWidget.setObjectName("listWidget")
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		self.verticalLayout_2.addWidget(self.listWidget)
		self.applyButton = QtWidgets.QPushButton(self.widget)
		self.applyButton.setStyleSheet("background-color:rgb(28, 28, 28);")
		self.applyButton.setAutoDefault(False)
		self.applyButton.setDefault(False)
		self.applyButton.setFlat(False)
		self.applyButton.setObjectName("applyButton")
		self.verticalLayout_2.addWidget(self.applyButton)
		self.horizontalLayout.addWidget(self.widget)
		self.widget_2 = QtWidgets.QWidget(self.tab)
		self.widget_2.setObjectName("widget_2")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
		self.verticalLayout_3.setContentsMargins(9, 9, 9, 0)
		self.verticalLayout_3.setSpacing(0)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.headerText = QtWidgets.QLabel(self.widget_2)
		self.headerText.setMinimumSize(QtCore.QSize(0, 25))
		self.headerText.setMaximumSize(QtCore.QSize(16777215, 25))
		font = QtGui.QFont()
		font.setPointSize(13)
		font.setBold(True)
		font.setUnderline(False)
		font.setWeight(75)
		font.setKerning(True)
		self.headerText.setFont(font)
		self.headerText.setStyleSheet("color:rgb(250, 70, 1)")
		self.headerText.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.headerText.setObjectName("headerText")
		self.verticalLayout_3.addWidget(self.headerText)
		self.infoText = QtWidgets.QLabel(self.widget_2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.infoText.sizePolicy().hasHeightForWidth())
		self.infoText.setSizePolicy(sizePolicy)
		self.infoText.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.infoText.setWordWrap(True)
		self.infoText.setObjectName("infoText")
		self.verticalLayout_3.addWidget(self.infoText)
		self.groupBox = QtWidgets.QGroupBox(self.widget_2)
		self.groupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.groupBox.setFlat(True)
		self.groupBox.setCheckable(False)
		self.groupBox.setObjectName("groupBox")
		self.verticalLayout_3.addWidget(self.groupBox)
		self.horizontalLayout.addWidget(self.widget_2)
		self.tabWidget.addTab(self.tab, "")
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.tabWidget.addTab(self.tab_2, "")
		self.tab_3 = QtWidgets.QWidget()
		self.tab_3.setObjectName("tab_3")
		self.tabWidget.addTab(self.tab_3, "")
		self.verticalLayout.addWidget(self.tabWidget)
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
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search..."))
		self.listWidget.setSortingEnabled(False)
		__sortingEnabled = self.listWidget.isSortingEnabled()
		self.listWidget.setSortingEnabled(False)
		item = self.listWidget.item(0)
		item.setText(_translate("MainWindow", "CA Soft IK"))
		item = self.listWidget.item(1)
		item.setText(_translate("MainWindow", "Noise"))
		item = self.listWidget.item(2)
		item.setText(_translate("MainWindow", "Reduce"))
		item = self.listWidget.item(3)
		item.setText(_translate("MainWindow", "Ribbon"))
		item = self.listWidget.item(4)
		item.setText(_translate("MainWindow", "Simple Doft IK"))
		item = self.listWidget.item(5)
		item.setText(_translate("MainWindow", "Sine"))
		item = self.listWidget.item(6)
		item.setText(_translate("MainWindow", "Spline Sine"))
		item = self.listWidget.item(7)
		item.setText(_translate("MainWindow", "Spring"))
		item = self.listWidget.item(8)
		item.setText(_translate("MainWindow", "Tail Dynamics"))
		item = self.listWidget.item(9)
		item.setText(_translate("MainWindow", "Transform Noise"))
		self.listWidget.setSortingEnabled(__sortingEnabled)
		self.applyButton.setText(_translate("MainWindow", "Apply"))
		self.headerText.setText(_translate("MainWindow", "TextLabel"))
		self.infoText.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "))
		self.groupBox.setTitle(_translate("MainWindow", "Options"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "New"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Applied"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Help"))
		self.actionNew.setText(_translate("MainWindow", "New"))
		self.actionModidy.setText(_translate("MainWindow", "Modify"))


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
