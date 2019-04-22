# Project Modules
from widgets import Icon_Tool_Button, Settings_Tool_Button, VGroupBox, HLine

# Python Modules
import os

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Maya Modules
from maya import cmds

# ======================================================================================================================
#
#
# Function
#
#
# ======================================================================================================================
'MAYA_DISABLE_CLIC_IPM 1'
'MAYA_DISABLE_CER 1'
'MAYA_NO_CONSOLE_WINDOW 1'


def set_defaults(*args, **kwargs):
	cmds.undoInfo(state=True, infinity=True)
	cmds.optionVar(iv=("useSaveScenePanelConfig", 0))
	cmds.optionVar(iv=("useScenePanelConfig", 0))
	cmds.optionVar(iv=("undoIsInfinite", 1))
	cmds.optionVar(iv=("isIncrementalSaveEnabled", 1))
	cmds.optionVar(iv=("RecentBackupsMaxSize", 10))
	cmds.optionVar(iv=("RecentFilesMaxSize", 10))
	cmds.optionVar(iv=("RecentProjectsMaxSize", 10))
	cmds.optionVar(iv=("firstLaunch", 1))
	return


def setAllPanelsToRenderer(renderer, reset=True):
	"""Possible values: base_OpenGL_Renderer, hwRender_OpenGL_Renderer, vp2Renderer"""
	modelPanels = cmds.getPanel(type='modelPanel')
	for panel in modelPanels:
		cmds.modelEditor(panel, edit=True, rendererName=renderer)
	if reset or os.environ.get('MAYA_DISABLE_VP2_WHEN_POSSIBLE', False):
		cmds.ogs(reset=True)

def channelbox_selection_change():
	cmds.optionVar(iv=('ChannelBox_ClearSelectionOnObjectSelectionChange', 1))
	

# ======================================================================================================================
#
#
# Class
#
#
# ======================================================================================================================


class Interface_Group(VGroupBox):
	def __init__(self, *args, **kwargs):
		VGroupBox.__init__(self, *args, **kwargs)
		
		self.checkbox_viewport = QCheckBox('Make Copy of Viewport')
		self.layout().addWidget(self.checkbox_viewport)
		
		self.checkbox_toolbox = QCheckBox('Toolbox')
		self.layout().addWidget(self.checkbox_toolbox)
		
		self.checkbox_graph = QCheckBox('Graph Editor +')
		self.layout().addWidget(self.checkbox_graph)


class Performance_Group(VGroupBox):
	def __init__(self, *args, **kwargs):
		VGroupBox.__init__(self, *args, **kwargs)
		
		self.checkbox_viewport = QCheckBox('Force Viewport 2.0')
		self.layout().addWidget(self.checkbox_viewport)
		
		self.layout().addWidget(HLine())
		
		self.radioGroup = QButtonGroup(self)
		self.radio_dg = QRadioButton('DG')
		self.radioGroup.addButton(self.radio_dg)
		self.layout().addWidget(self.radio_dg)
		
		self.radio_parallel = QRadioButton('Parallel')
		self.radioGroup.addButton(self.radio_parallel)
		self.layout().addWidget(self.radio_parallel)
		
		self.layout().addWidget(HLine())
		
		self.checkbox_gpu = QCheckBox('GPU Acceleration')
		self.layout().addWidget(self.checkbox_gpu)


class Tangent_Group(VGroupBox):
	def __init__(self, *args, **kwargs):
		VGroupBox.__init__(self, *args, **kwargs)
		
		self.checkbox_weighted = QCheckBox('Weight Tangents')
		self.layout().addWidget(self.checkbox_weighted)
		
		self.layout().addWidget(HLine())
		
		self.radioGroup = QButtonGroup(self)
		
		for item in ['auto', 'stepped', 'linear', 'spline']:
			item_name = 'radio_{}'.format(item)
			setattr(self, item_name, QRadioButton(item.capitalize()))
			button = getattr(self, item_name)
			self.radioGroup.addButton(button)
			self.layout().addWidget(button)


class Key_Group(VGroupBox):
	def __init__(self, *args, **kwargs):
		VGroupBox.__init__(self, *args, **kwargs)
		
		self.checkbox_layer_weight = QCheckBox('Show Layer Weight')
		self.layout().addWidget(self.checkbox_layer_weight)
		
		self.layout().addWidget(HLine())
		
		self.radioGroup_cb = QButtonGroup(self)
		
		for item in ['active', 'channelbox', 'none']:
			item_name = 'radio_cb_{}'.format(item)
			setattr(self, item_name, QRadioButton(item.capitalize()))
			button = getattr(self, item_name)
			self.radioGroup_cb.addButton(button)
			self.layout().addWidget(button)
		
		self.layout().addWidget(HLine())
		
		self.radioGroup_layer = QButtonGroup(self)
		
		for item in ['from layer editor', 'all', 'active', 'selected', 'active and selected']:
			item_name = 'radio_layer_{}'.format(item.replace(' ', '_'))
			setattr(self, item_name, QRadioButton(item.capitalize()))
			button = getattr(self, item_name)
			self.radioGroup_layer.addButton(button)
			self.layout().addWidget(button)


class Anim_Layer_Group(VGroupBox):
	def __init__(self, *args, **kwargs):
		VGroupBox.__init__(self, *args, **kwargs)
		
		self.checkbox_translate = QCheckBox('Translate')
		self.layout().addWidget(self.checkbox_translate)
		
		self.checkbox_rotate = QCheckBox('Rotate')
		self.layout().addWidget(self.checkbox_rotate)
		
		self.checkbox_scale = QCheckBox('Scale')
		self.layout().addWidget(self.checkbox_scale)
		
		self.checkbox_user = QCheckBox('User Defined')
		self.layout().addWidget(self.checkbox_user)


class Grid_Group(VGroupBox):
	def __init__(self, *args, **kwargs):
		VGroupBox.__init__(self, *args, **kwargs)
		
		self.checkbox_show = QCheckBox('Visible')
		self.layout().addWidget(self.checkbox_show)
		
		self.layout().addWidget(HLine())
		
		self.radioGroup = QButtonGroup(self)
		
		for item in ['centimeters', 'meters', 'inches', 'feet']:
			item_name = 'radio_grid_{}'.format(item)
			setattr(self, item_name, QRadioButton(item.capitalize()))
			button = getattr(self, item_name)
			self.radioGroup.addButton(button)
			self.layout().addWidget(button)


class Settings_Widget(QFrame):
	def __init__(self, *args, **kwargs):
		QFrame.__init__(self, *args, **kwargs)
		
		# Size Policy
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)
		
		# Layout
		self.setLayout(QVBoxLayout())
		self.layout().setSpacing(0)
		self.layout().setContentsMargins(0, 0, 0, 0)
		
		# Scroll
		self.scroll = QScrollArea(self)
		self.scroll.setWidgetResizable(True)
		self.layout().addWidget(self.scroll)
		
		self.widget_contents = QWidget()
		self.widget_contents.setLayout(QVBoxLayout())
		self.scroll.setWidget(self.widget_contents)
		
		# Interface
		self.group_interface = Interface_Group('Interface')
		self.widget_contents.layout().addWidget(self.group_interface)
		
		# Performance
		self.group_performance = Performance_Group('Performance')
		self.widget_contents.layout().addWidget(self.group_performance)
		
		# Tangents
		self.group_tangents = Tangent_Group('Default Tangent')
		self.widget_contents.layout().addWidget(self.group_tangents)
		
		# Key Ticks
		self.group_key = Key_Group('Key Ticks')
		self.widget_contents.layout().addWidget(self.group_key)
		
		# Anim Layer
		self.group_anim_layer = Anim_Layer_Group('New Animation Layers')
		self.widget_contents.layout().addWidget(self.group_anim_layer)
		
		# Grid
		self.group_grid = Grid_Group('Grid')
		self.widget_contents.layout().addWidget(self.group_grid)
		
		# Spacer
		spacerItem = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)
		self.widget_contents.layout().addItem(spacerItem)
		
		# StyleSheet
		# self.setStyleSheet('background:black;')
		pass


if __name__ == "__main__":
	pass
