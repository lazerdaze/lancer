# Project Modules
from anim_mancer.ui.widgets import Header_Widget
from widgets import Sliding_Stacked_Widget
from anim_mancer.utils import *
from settings import Settings_Widget

# Python Modules
import os
from os import path

# Maya Modules
from maya import cmds

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

# ======================================================================================================================
#
#
# Global
#
#
# ======================================================================================================================
'''
ChannelBoxLayerEditor|MainChannelsLayersLayout
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelButtonForm
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelButtonForm|cbManipsButton
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelButtonForm|cbSpeedButton
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelButtonForm|cbHyperbolicButton
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|ChannelBoxForm
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|ChannelBoxForm|menuBarLayout1
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|ChannelBoxForm|menuBarLayout1|frameLayout1
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|ChannelBoxForm|menuBarLayout1|frameLayout1|mainChannelBox
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|DisplayLayerTab
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|DisplayLayerTab|formLayout2
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|DisplayLayerTab|formLayout2|moveDispLayerUp
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|DisplayLayerTab|formLayout2|moveDispLayerDown
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|DisplayLayerTab|formLayout2|emptyDispLayer
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|DisplayLayerTab|formLayout2|selectedDispLayer
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|DisplayLayerTab|formLayout2|DisplayLayerScrollLayout|LayerEditorDisplayLayerLayout
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|DisplayLayerTab|formLayout2|DisplayLayerScrollLayout
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|AnimLayerTab
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|AnimLayerTab|formLayout3
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|AnimLayerTab|formLayout3|symbolButton1
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|AnimLayerTab|formLayout3|symbolButton2
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|AnimLayerTab|formLayout3|symbolButton3
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|AnimLayerTab|formLayout3|symbolButton4
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|AnimLayerTab|formLayout3|symbolButton5
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|AnimLayerTab|formLayout3|AnimLayerTabMoveUpButton
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|AnimLayerTab|formLayout3|AnimLayerTabMoveDownButton
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|AnimLayerTab|formLayout3|AnimLayerTabWeightText
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|AnimLayerTab|formLayout3|AnimLayerTabWeightField
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|AnimLayerTab|formLayout3|AnimLayerTabWeightSlider
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|AnimLayerTab|formLayout3|AnimLayerTabWeightButton
ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout|AnimLayerTab|formLayout3|AnimLayerTabanimLayerEditor
'''

ANIM_MANCER = 'anim_mancer_ui'
DIR_PATH = path.dirname(os.path.abspath(__file__))
RESOURCE_PATH = path.join(DIR_PATH, 'resource')
THEME_CSS = path.join(RESOURCE_PATH, 'theme.css')
CHANNELBOX_WINDOW = 'ChannelBoxLayerEditor'
CHANNELBOX_LAYOUT = 'ChannelBoxLayerEditor|MainChannelsLayersLayout'
CHANNELBOX_BUTTON_LAYOUT = 'ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelButtonForm'
CHANNELBOX_PANE_LAYOUT = 'ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout'
CHANNELBOX_MENU = 'ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|ChannelBoxForm|menuBarLayout1'
CHANNELBOX_MAIN = 'mainChannelBox'
CHANNELBOX_LAYER_LAYOUT = 'ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm'
CHANNELBOX_LAYER_TAB = 'ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout'

ANIM_MANCER_EXISTS = False


# ======================================================================================================================
#
#
# Function
#
#
# ======================================================================================================================

def set_channelbox_label(name, *args, **kwargs):
	return cmds.workspaceControl('ChannelBoxLayerEditor', e=True, label=name)


# ======================================================================================================================
#
#
# Class
#
#
# ======================================================================================================================


class Anim_Mancer(QWidget):
	def __init__(self, title='Anim-Mancer', *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)
		# Settings
		self.title = title
		
		# Channel Box Widgets
		self.widget_central = maya_to_qt(CHANNELBOX_WINDOW)
		self.widget_main = maya_to_qt(CHANNELBOX_LAYOUT)
		self.widget_pane = maya_to_qt(CHANNELBOX_PANE_LAYOUT)
		self.widget_layer = maya_to_qt(CHANNELBOX_LAYER_LAYOUT)
		self.widget_channelbox_buttons = maya_to_qt(CHANNELBOX_BUTTON_LAYOUT)
		
		# Widgets
		self.widget_name = '{}_widget_main'.format(ANIM_MANCER)
		
		self.widget_stacked = None
		self.widget_stacked_name = '{}_widget_stacked'.format(ANIM_MANCER)
		
		self.widget_header = None
		self.widget_header_name = '{}_widget_header'.format(ANIM_MANCER)

		self.widget_settings = None
		self.widget_settings_name = '{}_widget_settings'.format(ANIM_MANCER)
		
		self.widget_custom = None
		self.widget_custom_name = '{}_widget_custom'.format(ANIM_MANCER)
		
		
	
	def install(self, *args, **kwargs):
		global ANIM_MANCER_EXISTS
		
		if ANIM_MANCER_EXISTS:
			# self.uninstall()
			pass
		
		if self.title:
			set_channelbox_label(self.title)
			
		# Hide
		self.widget_channelbox_buttons.setHidden(True)
		
		# Custom Widget
		self.setObjectName(self.widget_name)
		self.setLayout(QVBoxLayout())
		self.layout().setSpacing(0)
		self.layout().setContentsMargins(0, 0, 0, 0)
		self.widget_central.layout().insertWidget(0, self)
		
		# Header
		self.widget_header = Header_Widget()
		self.widget_header.setObjectName(self.widget_header_name)
		self.layout().addWidget(self.widget_header)
		
		# Reparent
		self.layout().addWidget(self.widget_main)
		
		# Stacked Widget
		self.widget_stacked = QStackedWidget(self.widget_central)
		self.widget_stacked.setObjectName(self.widget_stacked_name)
		self.widget_central.layout().addWidget(self.widget_stacked)
		self.widget_stacked.addWidget(self)
		
		# Settings Widget
		self.widget_settings = Settings_Widget()
		self.widget_settings.setObjectName(self.widget_settings_name)
		self.widget_stacked.addWidget(self.widget_settings)
		
		# Slots
		self.widget_header.button_settings.clicked.connect(self.settings_callback)
		self.widget_settings.widget_header.button_settings.clicked.connect(self.settings_callback)
		
		self.widget_stacked.setCurrentIndex(0)
		
		ANIM_MANCER_EXISTS = True
		return
	
	def settings_callback(self):
		current = self.widget_stacked.currentIndex()
		self.widget_stacked.setCurrentIndex(1 if current == 0 else 0)
		return
	
	def clear_layout(self, layout, *args, **kwargs):
		while layout.count():
			child = layout.takeAt(0)
			if child.widget() is not None:
				child.widget().deleteLater()
			elif child.layout() is not None:
				self.clear_layout(child.layout())
		return
	
	def uninstall(self, *args, **kwargs):
		global ANIM_MANCER_EXISTS
		
		self.widget_central.setStyleSheet('')
		set_channelbox_label('Channel Box / Layer Editor')
		
		self.widget_channelbox_buttons.setHidden(False)
		
		# Header
		try:
			cmds.deleteUI(self.widget_header_name)
		except RuntimeError:
			pass
		
		# Settings
		try:
			cmds.deleteUI(self.widget_settings_name)
		except RuntimeError:
			pass
	
		# Custom
		try:
			cmds.deleteUI(self.widget_custom_name)
		except RuntimeError:
			pass
			
		# Stacked
		self.widget_central.layout().addWidget(self.widget_main)
		
		try:
			cmds.deleteUI(self.widget_stacked_name)
		except RuntimeError:
			pass
		
		# Main
		try:
			cmds.deleteUI(self.widget_main)
		except RuntimeError:
			pass
		
		ANIM_MANCER_EXISTS = False
		return
	
	


class UI_MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		QMainWindow.__init__(self, *args, **kwargs)
		
		# Main
		self.widget_main = QWidget(self)
		self.layout_main = QVBoxLayout(self.widget_main)
		self.layout_main.setSpacing(3)
		self.layout_main.setContentsMargins(3, 3, 3, 3)
		
		# Header
		self.widget_header = Header_Widget()
		self.layout_main.addWidget(self.widget_header)
		
		# Pane
		self.widget_pane = QSplitter(self.widget_main)
		self.widget_pane.setLayoutDirection(Qt.LeftToRight)
		self.widget_pane.setFrameShape(QFrame.NoFrame)
		self.widget_pane.setFrameShadow(QFrame.Plain)
		self.widget_pane.setOrientation(Qt.Vertical)
		self.widget_pane.setHandleWidth(8)
		self.widget_channelbox = QWidget(self.widget_pane)
		self.layout_channelbox = QVBoxLayout(self.widget_channelbox)
		self.layout_channelbox.setSpacing(0)
		self.layout_channelbox.setContentsMargins(0, 0, 0, 0)
		self.widget_tab_channelbox = QTabWidget(self.widget_channelbox)
		self.tab_channelbox = QWidget()
		self.layout_tab_channelbox = QVBoxLayout(self.tab_channelbox)
		self.layout_tab_channelbox.setSpacing(3)
		self.layout_tab_channelbox.setContentsMargins(3, 3, 3, 3)
		
		self.widget_tab_channelbox.addTab(self.tab_channelbox, "")
		self.layout_channelbox.addWidget(self.widget_tab_channelbox)
		self.widget_layers = QWidget(self.widget_pane)
		self.layout_layers = QVBoxLayout(self.widget_layers)
		self.layout_layers.setSpacing(0)
		self.layout_layers.setContentsMargins(0, 0, 0, 0)
		self.widget_tab_layers = QTabWidget(self.widget_layers)
		self.tab_layers = QWidget()
		self.layout_tab_layers = QVBoxLayout(self.tab_layers)
		self.layout_tab_layers.setSpacing(3)
		self.layout_tab_layers.setContentsMargins(3, 3, 3, 3)
		
		self.widget_layers_tools = QWidget(self.tab_layers)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.widget_layers_tools.sizePolicy().hasHeightForWidth())
		self.widget_layers_tools.setSizePolicy(sizePolicy)
		self.widget_layers_tools.setLayoutDirection(Qt.RightToLeft)
		self.layout_layers_tools = QHBoxLayout(self.widget_layers_tools)
		self.layout_layers_tools.setSpacing(3)
		self.layout_layers_tools.setContentsMargins(3, 3, 3, 3)
		
		self.widget_tab_layers.addTab(self.tab_layers, "")
		self.tab_anim = QWidget()
		self.widget_tab_layers.addTab(self.tab_anim, "")
		self.layout_layers.addWidget(self.widget_tab_layers)
		
		# Custom Widget
		self.widget_custom = QWidget(self.widget_pane)
		self.layout_custom = QVBoxLayout(self.widget_custom)
		self.layout_custom.setSpacing(0)
		self.layout_custom.setContentsMargins(0, 0, 0, 0)
		self.widget_tab_custom = QTabWidget(self.widget_custom)
		self.tab_tools = QWidget()
		self.verticalLayout_7 = QVBoxLayout(self.tab_tools)
		self.verticalLayout_7.setSpacing(3)
		self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
		self.scrollArea = QScrollArea(self.tab_tools)
		self.scrollArea.setWidgetResizable(True)
		self.scrollAreaWidgetContents = QWidget()
		self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 471, 75))
		self.scrollAreaWidgetContents.setAutoFillBackground(True)
		self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
		
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.verticalLayout_7.addWidget(self.scrollArea)
		self.widget_tab_custom.addTab(self.tab_tools, "")
		self.layout_custom.addWidget(self.widget_tab_custom)
		self.layout_main.addWidget(self.widget_pane)
		
		# Settings Widget
		self.widget_settings = Settings_Widget()
		
		# Stacked Widget
		self.widget_stacked = QStackedWidget()
		self.widget_stacked.addWidget(self.widget_main)
		self.widget_stacked.addWidget(self.widget_settings)
		self.setCentralWidget(self.widget_stacked)
		self.widget_stacked.setCurrentIndex(0)
		
		# Slots
		self.widget_header.button_settings.clicked.connect(self.settings_callback)
		self.widget_settings.widget_header.button_settings.clicked.connect(self.settings_callback)
	
	def settings_callback(self):
		current = self.widget_stacked.currentIndex()
		self.widget_stacked.setCurrentIndex(1 if current == 0 else 0)
		return


class UI_Slide_MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		QMainWindow.__init__(self, *args, **kwargs)
		
		animTime = 500
		
		_min = 500
		_max = 1500
		animTime = 1000
		
		# Components
		buttonNext = QPushButton("Next")
		buttonPrev = QPushButton("Prev")
		checkWrap = QCheckBox("Wrap")
		checkVertical = QCheckBox("Vertical")
		
		listAll = QComboBox()
		listAll.addItem("Page 1")
		listAll.addItem("Page 2")
		listAll.addItem("Page 3")
		listAll.addItem("Page 4")
		listAll.setMinimumHeight(40)
		
		speedLabel = QLabel("Anim. Time:")
		speedDisplay = QLCDNumber()
		
		slideSpeed = QSlider(Qt.Horizontal)
		slideSpeed.setMinimum(_min)
		slideSpeed.setMaximum(_max)
		slideSpeed.setValue(animTime)
		speedDisplay.display(animTime)
		
		# Sliding Widgets
		slideWidget1 = QWidget()
		slideWidget2 = QWidget()
		slideWidget3 = QWidget()
		slideWidget4 = QWidget()
		slideWidget1layout = QVBoxLayout()
		slideWidget1.setLayout(slideWidget1layout)
		slideWidget2layout = QVBoxLayout()
		slideWidget2.setLayout(slideWidget2layout)
		slideWidget3layout = QVBoxLayout()
		slideWidget3.setLayout(slideWidget3layout)
		slideWidget4layout = QVBoxLayout()
		slideWidget4.setLayout(slideWidget4layout)
		b11 = QPushButton("Qt")
		slideWidget1layout.addWidget(b11)
		b12 = QPushButton("is cool !")
		slideWidget1layout.addWidget(b12)
		
		b21 = QPushButton("Cool")
		slideWidget2layout.addWidget(b21)
		b22 = QPushButton("is Qt !")
		slideWidget2layout.addWidget(b22)
		
		b31 = QPushButton("Isn't")
		slideWidget3layout.addWidget(b31)
		b32 = QPushButton("Qt cool ?")
		slideWidget3layout.addWidget(b32)
		
		b41 = QPushButton("How cool")
		slideWidget4layout.addWidget(b41)
		b42 = QPushButton("is Qt !")
		slideWidget4layout.addWidget(b42)
		
		slidingStacked = Sliding_Stacked_Widget(self)
		slidingStacked.addWidget(slideWidget1)
		slidingStacked.addWidget(slideWidget2)
		slidingStacked.addWidget(slideWidget3)
		slidingStacked.addWidget(slideWidget4)
		slidingStacked.set_speed(animTime)
		
		# Main Layout
		centralWidget = QWidget()
		mainLayout = QVBoxLayout()
		centralWidget.setLayout(mainLayout)
		controlPaneLayout = QGridLayout()
		mainLayout.addWidget(slidingStacked)
		mainLayout.addLayout(controlPaneLayout)
		row = 1
		controlPaneLayout.addWidget(buttonPrev, row, 1, 1, 1)
		controlPaneLayout.addWidget(buttonNext, row, 2, 1, 1)
		controlPaneLayout.addWidget(checkWrap, row + 1, 1, 1, 1)
		controlPaneLayout.addWidget(checkVertical, row, 2, 1, 1)
		controlPaneLayout.addWidget(speedLabel, row + 2, 1, 1, 1)
		controlPaneLayout.addWidget(speedDisplay, row, 2, 1, 1)
		controlPaneLayout.addWidget(slideSpeed, row + 3, 1, 1, 2)
		controlPaneLayout.addWidget(listAll, row + 4, 1, 1, 2)
		
		self.setCentralWidget(centralWidget)
		
		buttonNext.pressed.connect(slidingStacked.slide_in_next)
		buttonPrev.pressed.connect(slidingStacked.slide_in_prev)
		checkWrap.clicked.connect(slidingStacked.set_wrap)
		checkVertical.clicked.connect(slidingStacked.set_vertical)
		slideSpeed.valueChanged.connect(slidingStacked.set_speed)
		slideSpeed.valueChanged.connect(speedDisplay.display)
		listAll.currentIndexChanged.connect(slidingStacked.slide_in_index)


# ======================================================================================================================
#
#
# Execute
#
#
# ======================================================================================================================

if __name__ == '__main__':
	pass
