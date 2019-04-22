"""
List of Tools:

General:
- Snap Objects - Match Transformations
- Create Locator At Position

Animation
- Motion Trail
- Ghost
- Motion Path
- Bake
- Bake To World
- Bake To Local
- Select All Animation
- Re-timer

Rigging
- FK IK Network
- FK > IK Switch
- IK < FK Switch

- Sets
- Create
- Add
- Remove

Time
- Playback Every Frame (Radio)
- Playback Realtime (Radio)
- Playback Snapping (Checkbox)

Grid (Radio)
- Centimeter
- Meter
- Inches
- Feet

Modeling
- Select All Verts

"""

# Project Modules
from widgets import *
from anim_mancer.utils import *

# Python Modules
import weakref

# Maya Modules
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from maya import cmds, mel, OpenMayaUI

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from shiboken2 import wrapInstance

# ======================================================================================================================
#
#
# Global
#
#
# ======================================================================================================================

TOOLBOX_NAME = '{}_toolbox_widget'.format(UI.name)
TOOLBOX_TITLE = 'Anim Toolbox'
TOOLBOX_ICON_SIZE = 25


# ======================================================================================================================
#
#
# Class
#
#
# ======================================================================================================================

class Toolbox_Button(Icon_Tool_Button):
	def __init__(self, *args, **kwargs):
		Icon_Tool_Button.__init__(self, *args, **kwargs)
		
		size = QSize(25, 25)
		self.setMinimumSize(size)
		self.setMaximumSize(size)
		self.setIconSize(size)
		self.setStyleSheet("""
		background:none;
		border:none;
		margin:0;
		padding:0;
		""")


class Toolbox_Widget(QWidget):
	def __init__(self, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)
		
		# Layout
		self.setLayout(QVBoxLayout())
		
		# Snap
		self.button_snap = Toolbox_Button(self, IconPath.snap)
		self.button_snap.setToolTip('Snap')
		self.layout().addWidget(self.button_snap)
		
		# Locate
		self.button_locate = Toolbox_Button(self, IconPath.locator)
		self.button_locate.setToolTip('Locator')
		self.layout().addWidget(self.button_locate)
		
		# Time
		self.button_time = Toolbox_Button(self, IconPath.time)
		self.button_time.setToolTip('Time')
		self.layout().addWidget(self.button_time)
		
		# Grid
		self.button_grid = Toolbox_Button(self, IconPath.grid)
		self.button_grid.setToolTip('Grid')
		self.layout().addWidget(self.button_grid)
		
		self.layout().addWidget(HLine())
		
		# Motion Trail
		self.button_motion = Toolbox_Button(self, IconPath.motion_trail)
		self.button_motion.setToolTip('Motion Trail')
		self.layout().addWidget(self.button_motion)
		
		# Motion Path
		self.button_path = Toolbox_Button(self, IconPath.motion_path)
		self.button_path.setToolTip('Motion Path')
		self.layout().addWidget(self.button_path)
		
		# Ghost
		self.button_ghost = Toolbox_Button(self, IconPath.ghost)
		self.button_ghost.setToolTip('Ghost')
		self.layout().addWidget(self.button_ghost)
		
		# Bake
		self.button_bake = Toolbox_Button(self, IconPath.bake)
		self.button_bake.setToolTip('Bake')
		self.layout().addWidget(self.button_bake)
		
		# Key
		self.button_key = Toolbox_Button(self, IconPath.key)
		self.button_key.setToolTip('Bake')
		self.layout().addWidget(self.button_key)
		
		self.layout().addWidget(HLine())
		
		# FK
		self.button_fk = Toolbox_Button(self, IconPath.fk)
		self.button_fk.setToolTip('FK')
		self.layout().addWidget(self.button_fk)
		
		# IK
		self.button_ik = Toolbox_Button(self, IconPath.ik)
		self.button_ik.setToolTip('IK')
		self.layout().addWidget(self.button_ik)
		
		self.layout().addWidget(HLine())
		
		# Set 
		self.button_set = Toolbox_Button(self, IconPath.set)
		self.button_set.setToolTip('Sets')
		self.layout().addWidget(self.button_set)
		
		# Spacer
		spacer = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)
		self.layout().addItem(spacer)


class Toolbox_Window(QWidget):
	instances = list()
	
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		
		Toolbox_Window.delete_instances()
		self.__class__.instances.append(weakref.proxy(self))
		
		self.window_name = TOOLBOX_NAME
		self.ui = parent
		self.main_layout = parent.layout()
		self.main_layout.setContentsMargins(0, 0, 0, 0)
		self.main_layout.setSpacing(0)
		
		self.button_widget = Toolbox_Widget()
		self.main_layout.addWidget(self.button_widget)
	
	@staticmethod
	def delete_instances():
		for _object in Toolbox_Window.instances:
			try:
				_object.setParent(None)
				_object.deleteLater()
			except RuntimeError:
				pass
			
			Toolbox_Window.instances.remove(_object)
			del _object


# ======================================================================================================================
#
#
# Execute
#
#
# ======================================================================================================================

def show(*args, **kwargs):
	try:
		cmds.deleteUI(TOOLBOX_NAME)
	except RuntimeError:
		pass
	
	main_control = cmds.workspaceControl(TOOLBOX_NAME,
	                                     ttc=['ChannelBoxLayerEditor', -1],
	                                     widthProperty='fixed',
	                                     label=TOOLBOX_TITLE,
	                                     minimumWidth=40,
	                                     initialWidth=40,
	                                     horizontal=False,
	                                     )
	
	control_widget = OpenMayaUI.MQtUtil.findControl(TOOLBOX_NAME)
	control_wrap = wrapInstance(long(control_widget), QWidget)
	control_wrap.setAttribute(Qt.WA_DeleteOnClose)
	window = Toolbox_Window(control_wrap)
	cmds.evalDeferred(lambda *args: cmds.workspaceControl(main_control, e=True, rs=True))
	return window


if __name__ == '__main__':
	pass
