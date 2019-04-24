# Project Modules
from utils import *

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import shiboken2 as shiboken

# Maya Modules
from maya import cmds, OpenMayaUI

UI_NAME = 'stop_motion_UI'
UI_TITLE = 'Stop Motion Tool'


def maya_to_qt(name, *args, **kwargs):
	"""
	Maya to QWidget

	:param str name:    Maya name of an ui object
	:return:            QWidget of parsed Maya name
	:rtype:             QWidget
	"""
	ptr = OpenMayaUI.MQtUtil.findControl(name)
	if ptr is None:
		ptr = OpenMayaUI.MQtUtil.findLayout(name)
	if ptr is None:
		ptr = OpenMayaUI.MQtUtil.findMenuItem(name)
	if ptr is not None:
		return shiboken.wrapInstance(long(ptr), QWidget)
	return ptr


def qt_to_maya(widget, *args, **kwargs):
	"""
	QWidget to Maya name

	:param QWidget widget:  QWidget of a maya ui object
	:return:                Maya name of parsed QWidget
	:rtype:                 str
	"""
	return OpenMayaUI.MQtUtil.fullName(long(shiboken.getCppPointer(widget)[0]))


def get_maya_window(*args, **kwargs):
	ptr = OpenMayaUI.MQtUtil.mainWindow()
	if ptr is not None:
		return shiboken.wrapInstance(long(ptr), QWidget)


class FloatSlider(QWidget):
	valueChanged = Signal(float)

	def __init__(self, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)

		self.currentValue = 0.5

		# Layout
		self.setLayout(QHBoxLayout())

		# Label
		self.label = QLabel('Ratio Control')
		self.layout().addWidget(self.label)

		# Float Field
		self.float_field = QDoubleSpinBox()
		self.float_field.setMinimum(0.0)
		self.float_field.setMaximum(1.0)
		self.float_field.setValue(0.5)
		self.float_field.setSingleStep(0.01)
		self.float_field.setFocusPolicy(Qt.ClickFocus)
		self.layout().addWidget(self.float_field)

		# Float Slider
		self.float_slider = QSlider(Qt.Horizontal)
		self.float_slider.setMinimum(0)
		self.float_slider.setMaximum(100)
		self.float_slider.setValue(50)
		self.layout().addWidget(self.float_slider)

		# Slots
		self.float_field.valueChanged.connect(self.field_callback)
		self.float_slider.valueChanged.connect(self.slider_callback)

	def slider_callback(self, *args, **kwargs):
		value = self.float_slider.value()
		self.float_field.setValue(float(value) / 100.0)
		self.currentValue = float(value)
		self.valueChanged.emit(float(value))
		return

	def field_callback(self, *args, **kwargs):
		value = self.float_field.value()
		self.float_slider.setValue(int(value * 100.0))
		self.currentValue = float(value)
		self.valueChanged.emit(float(value))
		return


class ProgressButton(QWidget):
	def __init__(self, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)


# TODO: Preview Mode
class Window(QMainWindow):
	def __init__(self, *args, **kwargs):
		QMainWindow.__init__(self, *args, **kwargs)

		# Variables
		self.progress_min = 0
		self.progress_max = 100
		self.progress_current = 0

		# Layout
		self.widget_main = QWidget()
		self.widget_main.setLayout(QVBoxLayout())
		self.setCentralWidget(self.widget_main)
		self.setMinimumWidth(400)
		self.setMaximumWidth(400)

		# Options
		self.group_options = QGroupBox('Options')
		self.group_options.setLayout(QVBoxLayout())
		self.widget_main.layout().addWidget(self.group_options)

		# Ratio Slider
		self.ratio_slider = FloatSlider()
		self.group_options.layout().addWidget(self.ratio_slider)

		# Row Layout
		rowLayout = QHBoxLayout()
		self.group_options.layout().addLayout(rowLayout)

		# Dynamics
		self.checkbox_stepped = QCheckBox('Simulate Stepped')
		self.checkbox_stepped.setChecked(True)
		rowLayout.addWidget(self.checkbox_stepped)

		# New Anim Layer
		self.checkbox_layer = QCheckBox('New Anim Layer')
		self.checkbox_layer.setChecked(True)
		rowLayout.addWidget(self.checkbox_layer)

		# Dynamics
		self.checkbox_dyn = QCheckBox('Bake Dynamics')
		self.checkbox_dyn.setChecked(False)
		rowLayout.addWidget(self.checkbox_dyn)

		# Spacer
		spacer = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)
		self.group_options.layout().addItem(spacer)

		# Button
		self.button_simulate = QPushButton('Simulate')
		self.widget_main.layout().addWidget(self.button_simulate)

		# Progress Bar
		# self.progress_bar = QProgressBar()
		# self.progress_bar.setRange(self.progress_min, self.progress_max)
		# self.widget_main.layout().addWidget(self.progress_bar)

		# Thread
		# self.task_thread = SimulateThread()

		# Slots
		self.button_simulate.clicked.connect(self.simulate_callback)

	# self.task_thread.notifyProgress.connect(self.onProgress)

	def onStart(self):
		self.task_thread.update_vars(nodes=cmds.ls(sl=True),
									 ratio=self.ratio_slider.currentValue,
									 is_layer=self.checkbox_layer.isChecked(),
									 is_dynamic=self.checkbox_dyn.isChecked(),
									 )

		self.task_thread.start()

	def onProgress(self, index, *args, **kwargs):
		self.progress_bar.setValue(index)
		return

	@undo
	def simulate_callback(self, *args, **kwargs):
		is_simulate = self.checkbox_stepped.isChecked()
		is_layer = self.checkbox_layer.isChecked()
		is_dynamic = self.checkbox_dyn.isChecked()
		ratio = self.ratio_slider.currentValue
		time_range = get_time_range()

		selected = cmds.ls(sl=True)

		if not selected:
			raise RuntimeError('Nothing Selected')

		layer_name = None
		layer_exceptions = []
		rig = None
		rig_names = []
		new_items = []

		for item in selected:
			namespace = item.split(':')[0]

			if namespace:
				rig = Apex_Rig(namespace=namespace)

				if rig.main_controls:
					for control in rig.main_controls:
						if control not in selected:
							new_items.append(control)

				if rig.dyn_controls:
					layer_exceptions += rig.dyn_controls

				if hasattr(Apex_Name, namespace):
					rig_name = getattr(Apex_Name, namespace)

					if rig_name not in rig_names:
						rig_names.append(rig_name)

		if new_items:
			selected += new_items

		if rig_names:
			layer_name = 'stopMotion_layer1'
			for rig_name in rig_names:
				layer_name = '{}_{}'.format(rig_name, layer_name)

		# Dynamics
		if is_dynamic and rig:
			if rig.dyn_joints:
				rig.transfer_dyn_to_controls()

		# Animation Layers
		if is_layer:
			clean_anim_layers()

			if not layer_name:
				layer_name = 'stoppedMotion1'

			layer_name = create_anim_layer(layer_name)

			# Bake
			bake_to_layer(selected, layer_name)

		# Simulate
		if is_simulate:
			generate_stop_motion(selected,
								 ratio=ratio,
								 randomness=0.0,
								 start=int(time_range[0]),
								 end=int(time_range[-1]),
								 layer=layer_name,
								 )

		# Exceptions
		if is_layer and layer_exceptions:
			for item in layer_exceptions:
				remove_from_anim_layer(item, layer_name)
		return


def show(name=UI_NAME, title=UI_TITLE, *args, **kwargs):
	if cmds.window(name, exists=True):
		cmds.deleteUI(name, wnd=True)

	# Window
	window = Window(get_maya_window())
	window.setObjectName(name)
	window.setWindowTitle(title)
	window.show()
	return
