# Project Modules
from utils import *

# Python Modules
from os import path
import threading, sys, traceback, logging

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import shiboken2 as shiboken

# Maya Modules
from maya import cmds, mel
from maya.api import OpenMaya, OpenMayaAnim, OpenMayaUI
import maya.utils as mayaUtils

# ======================================================================================================================
#
#
# Global
#
#
# ======================================================================================================================

__version__ = '1.0.4'
__author__ = 'Justin Tirado'

UI_NAME = 'stop_motion_UI'
UI_TITLE = 'Stop Motion Tool - {}'.format(__version__)

DIRECTORY = path.dirname(path.abspath(__file__))
IMAGE_HEADER = path.join(DIRECTORY, 'image_header.png')


# ======================================================================================================================
#
#
# Function
#
#
# ======================================================================================================================

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


# ======================================================================================================================
#
#
# Class
#
#
# ======================================================================================================================

class WorkerSignals(QObject):
	finished = Signal()
	error = Signal(tuple)
	result = Signal(object)
	progress = Signal(int)
	running = Signal(bool)
	status = Signal(str)


class WorkerRunnable(QRunnable):
	"""
	Worker Thread
	"""
	
	def __init__(self, fn, *args, **kwargs):
		QRunnable.__init__(self)
		self.fn = fn
		self.args = args
		self.kwargs = kwargs
		self.signals = WorkerSignals()
		self.kwargs['progress_callback'] = self.signals.progress
		self.kwargs['progress_status'] = self.signals.status
	
	@Slot()
	def run(self):
		try:
			result = self.fn(*self.args, **self.kwargs)
		
		except:
			traceback.print_exc()
			exctype, value = sys.exc_info()[:2]
			self.signals.error.emit((exctype, value, traceback.format_exc()))
		else:
			self.signals.result.emit(result)
		
		finally:
			self.signals.finished.emit()
		return


class WorkerThread(QThread):
	"""
	Worker Thread
	"""
	
	def __init__(self, fn, *args, **kwargs):
		super(WorkerThread, self).__init__()
		self.fn = fn
		self.args = args
		self.kwargs = kwargs
		self.signals = WorkerSignals()
		self.kwargs['progress_callback'] = self.signals.progress
		self.kwargs['progress_status'] = self.signals.status
	
	@Slot()
	def run(self):
		try:
			result = self.fn(*self.args, **self.kwargs)
		
		except:
			traceback.print_exc()
			exctype, value = sys.exc_info()[:2]
			self.signals.error.emit((exctype, value, traceback.format_exc()))
		else:
			self.signals.result.emit(result)
		
		finally:
			self.signals.finished.emit()
		return


class FloatSlider(QWidget):
	valueChanged = Signal(float)
	
	def __init__(self, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)
		
		self.currentValue = 0.5
		
		# Layout
		self.setLayout(QHBoxLayout())
		
		# Label
		self.label = QLabel('Favor Keys')
		self.layout().addWidget(self.label)
		
		# Float Field
		self.float_field = QDoubleSpinBox()
		self.float_field.setMinimum(1.0)
		self.float_field.setMaximum(2.0)
		self.float_field.setValue(1.5)
		self.float_field.setSingleStep(0.25)
		self.float_field.setFocusPolicy(Qt.ClickFocus)
		self.layout().addWidget(self.float_field)
		
		# Float Slider
		label_layout = QGridLayout()
		self.layout().addLayout(label_layout)
		
		self.float_slider = QSlider(Qt.Horizontal)
		self.float_slider.setMinimum(100)
		self.float_slider.setMaximum(200)
		self.float_slider.setValue(150)
		self.float_slider.setMinimumWidth(225)
		
		label_layout.addWidget(self.float_slider, 0, 0, 1, 2)
		
		label1 = QLabel("1's")
		label1.setAlignment(Qt.AlignLeft)
		label_layout.addWidget(label1, 1, 0, 1, 1)
		
		label2 = QLabel("2's")
		label2.setAlignment(Qt.AlignCenter)
		label_layout.addWidget(label2, 1, 2, 1, 1)
		
		# Slots
		self.float_field.valueChanged.connect(self.field_callback)
		self.float_slider.sliderReleased.connect(self.slider_callback)
	
	def slider_callback(self, *args, **kwargs):
		value = self.float_slider.value()
		self.float_field.setValue(float(value) / 100.0)
		self.currentValue = float(value - 100.0) / 100.0
		self.valueChanged.emit(float(value - 100.0) / 100.0)
		return
	
	def field_callback(self, *args, **kwargs):
		value = self.float_field.value()
		self.float_slider.setValue(int(value * 100.0))
		self.currentValue = float(value - 1.0)
		self.valueChanged.emit(float(value - 1.0))
		return


class Window(QMainWindow):
	status_init = 'init'
	status_abort = 'abort'
	status_error = 'error'
	status_warning = 'warning'
	status_busy = 'busy'
	status_finished = 'finished'
	status_preview = 'preview'
	
	state_init = 'Initializing'
	state_analyze = 'Analyzing'
	state_bake_dyn = 'Baking Dynamics'
	state_bake_layer = 'Baking to New Animation Layer'
	state_simulate = 'Removing Keys'
	state_cleanup = 'Cleanup'
	state_finished = 'Done'
	state_busy = 'Calculating ...'
	
	progress_callback = Signal(int)
	progress_status = Signal(str)
	
	def __init__(self, *args, **kwargs):
		QMainWindow.__init__(self, *args, **kwargs)
		
		# Variables
		self.status_bar_message = 'Ready'
		self.time_range = (1001, 1200)
		self.current_progress = 0
		self.min_progress = 0
		self.max_progress = 100
		
		self.animLayer = None
		self.animCurvesBuffer = None
		self.animCurvesProcessed = None
		self.preview_active = False
		self.start = None
		self.end = None
		self.originalCurves = None
		self.bufferCurvesState = True
		
		self.is_simulate = True
		self.is_layer = True
		self.is_dynamic = False
		self.ratio = 0.5
		self.selected = []
		
		# Layout
		self.widget_main = QWidget()
		self.widget_main.setLayout(QVBoxLayout())
		self.widget_main.layout().setContentsMargins(0, 0, 0, 0)
		self.setCentralWidget(self.widget_main)
		self.setMinimumWidth(400)
		self.setMaximumWidth(400)
		
		# Status
		self.status_bar = QStatusBar()
		self.status_bar.setSizeGripEnabled(False)
		self.status_bar.showMessage(self.status_bar_message)
		self.status_bar.setStyleSheet('background:black;')
		self.setStatusBar(self.status_bar)
		
		# Progress Bar
		self.progress_bar = QProgressBar()
		self.progress_bar.setRange(0, 100)
		self.progress_bar.setValue(0)
		self.progress_bar.setMaximumWidth(50)
		self.status_bar.addPermanentWidget(self.progress_bar)
		
		# Header
		self.header = QLabel()
		self.header.setPixmap(QPixmap(IMAGE_HEADER))
		self.widget_main.layout().addWidget(self.header)
		
		# Contents
		contents_layout = QVBoxLayout()
		contents_layout.setSpacing(10)
		contents_layout.setContentsMargins(10, 10, 10, 10)
		self.widget_main.layout().addLayout(contents_layout)
		
		# Step Mode
		self.group_step = QGroupBox('Auto Stepped Mode')
		self.group_step.setCheckable(True)
		self.group_step.setChecked(True)
		self.group_step.setFocusPolicy(Qt.NoFocus)
		self.group_step.setLayout(QVBoxLayout())
		self.group_step.setStatusTip('Favor keys between on 1s and on 2s.')
		self.group_step.installEventFilter(self)
		contents_layout.addWidget(self.group_step)
		
		# Ratio Slider
		self.ratio_slider = FloatSlider()
		self.group_step.layout().addWidget(self.ratio_slider)
		
		# Options
		self.group_options = QGroupBox('Options')
		self.group_options.setLayout(QVBoxLayout())
		contents_layout.addWidget(self.group_options)
		
		# Row Layout
		rowLayout = QHBoxLayout()
		self.group_options.layout().addLayout(rowLayout)
		
		# New Anim Layer
		self.checkbox_layer = QCheckBox('Bake To Animation Layer')
		self.checkbox_layer.setChecked(True)
		self.checkbox_layer.installEventFilter(self)
		self.checkbox_layer.setStatusTip('Bake Results to a new override animation layer.')
		rowLayout.addWidget(self.checkbox_layer)
		
		# Dynamics
		self.checkbox_dyn = QCheckBox('Bake Dynamics')
		self.checkbox_dyn.setChecked(False)
		self.checkbox_dyn.installEventFilter(self)
		self.checkbox_dyn.setStatusTip('Bake Dynamics on Apex Character Rigs Only (Watson, Mirage)')
		rowLayout.addWidget(self.checkbox_dyn)
		
		# Run Buttons
		run_button_layout = QHBoxLayout()
		run_button_layout.setContentsMargins(0, 0, 0, 0)
		contents_layout.addLayout(run_button_layout)
		
		# Preview Button
		self.button_preview = QPushButton('Preview (Experimental)')
		self.button_preview.setCheckable(True)
		self.button_preview.setStatusTip('Preview Stepped Mode. UNDO is disabled in preview.')
		self.button_preview.installEventFilter(self)
		run_button_layout.addWidget(self.button_preview)
		
		# Simulate Button
		self.button_simulate = QPushButton('Apply')
		self.button_simulate.setStatusTip('Apply simulation on selected objects.')
		self.button_simulate.installEventFilter(self)
		run_button_layout.addWidget(self.button_simulate)
		
		# Spacer
		spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
		self.widget_main.layout().addItem(spacer)
		
		# Thread
		# self.thread_pool = QThreadPool()
		# self.thread_count = self.thread_pool.maxThreadCount()
		# self.set_status("Max CPUs available\t:\t{}".format(self.thread_count))
		
		# Slots
		self.ratio_slider.valueChanged.connect(self.update_preview_worker)
		
		self.button_simulate.clicked.connect(self.apply_callback)
		self.button_preview.clicked.connect(self.preview_callback)
	
	# self.simulate_thread.progress_update.connect(self.run_widget.set_progress_current)
	# self.simulate_thread.state_changed.connect(self.update_status)
	# self.simulate_thread.progress_finished.connect(self.run_widget.finished_progress)
	# self.simulate_thread.progress_finished.connect(self.status_done)
	
	# ==================================================================================================================
	# Status
	# ==================================================================================================================
	
	def update_status(self, status, kind=None, *args, **kwargs):
		self.status_bar.showMessage(status)
		
		color = 'black'
		
		if kind in [self.status_warning, self.status_error]:
			color = 'darkred'
		
		elif kind == self.status_finished:
			color = 'green'
		
		self.status_bar.setStyleSheet('background:{};'.format(color))
		return
	
	def eventFilter(self, obj, event):
		if not self.preview_active:
			if event.type() == QEvent.Enter:
				self.status_bar.showMessage(obj.statusTip(), 0)
				self.status_bar.setStyleSheet('background:black;')
		event.accept()
		return False
	
	# ==================================================================================================================
	# Preview
	# ==================================================================================================================
	
	def get_options(self):
		self.is_simulate = self.group_step.isChecked()
		self.is_layer = self.checkbox_layer.isChecked()
		self.is_dynamic = self.checkbox_dyn.isChecked()
		self.ratio = self.ratio_slider.currentValue
		self.time_range = get_time_range()
		
		# Get Selected
		self.selected = cmds.ls(sl=True)
		
		if not self.selected:
			self.abort_preview()
			self.update_status('Nothing Selected.', self.status_warning)
			raise
		return
	
	def update_progress(self, value):
		if value > self.max_progress:
			self.progress_bar.setValue(self.max_progress)
		else:
			self.progress_bar.setValue(value)
		return
	
	def preview_callback(self):
		if self.button_preview.isChecked():
			if not self.group_step.isChecked():
				self.group_step.setChecked(True)
			
			self.start_preview()
		else:
			self.cancel_preview()
		return
	
	def abort_preview(self):
		self.button_preview.setChecked(False)
		return
	
	def cancel_preview(self):
		paste_clipboard_curves(self.originalCurves, self.start, self.end)
		self.animCurvesBuffer = None
		self.animCurvesProcessed = None
		self.preview_active = False
		cmds.undoInfo(stateWithoutFlush=True)
		return
	
	def start_preview(self):
		self.update_status('Calculating...', self.state_busy)
		self.get_options()
		
		# Original Curves
		self.originalCurves, self.start, self.end = copy_original_curves(self.selected)
		
		if self.originalCurves is None:
			self.abort_preview()
			self.update_status('No animation found.', self.status_error)
			return
		
		# Undo
		cmds.undoInfo(stateWithoutFlush=False)
		
		# Run
		self.preview_active = True
		self.progress_bar.setValue(0)
		self.run_buffer_worker()
		self.run_preview_worker(self.ratio_slider.currentValue)
		return
	
	def update_preview_worker(self, ratio):
		if self.preview_active:
			self.run_preview_worker(ratio)
		return
	
	def run_preview_worker(self, ratio):
		worker = WorkerThread(fn=self.refreshFilter,
		                      ratio=ratio
		                      )
		
		worker.signals.progress.connect(self.update_progress)
		worker.signals.status.connect(self.status_bar.showMessage)
		worker.run()
		return
	
	def apply_callback(self):
		self.get_options()
		
		if self.preview_active:
			# Get Original Curves Back
			cmds.undoInfo(openChunk=True)
			
			try:
				self.apply_curves(self.animCurvesBuffer,
				                  self.animCurvesBuffer,
				                  start=self.time_range[0],
				                  end=self.time_range[1],
				                  progress_callback=self.progress_callback,
				                  progress_status=self.progress_status,
				                  )
			finally:
				cmds.undoInfo(closeChunk=True)
			
			# apply processed curve for undo step
			cmds.undoInfo(swf=True)
			cmds.undoInfo(openChunk=True)
			
			try:
				self.apply_curves(self.animCurvesBuffer,
				                  self.animCurvesProcessed,
				                  start=self.time_range[0],
				                  end=self.time_range[1],
				                  progress_callback=self.progress_callback,
				                  progress_status=self.progress_status,
				                  )
			finally:
				cmds.undoInfo(closeChunk=True)
				
		else:
			self.run_apply_worker()
		
		self.button_preview.setChecked(False)
		self.progress_bar.setValue(0)
		self.animCurvesBuffer = None
		self.animCurvesProcessed = None
		self.preview_active = False
		return
	
	def run_apply_worker(self):
		worker = WorkerThread(fn=self.simulateFilter,
		                      )
		
		worker.signals.progress.connect(self.update_progress)
		worker.signals.status.connect(self.status_bar.showMessage)
		worker.run()
		return
	
	def refreshFilter(self, ratio, progress_callback, progress_status):
		self.animCurvesProcessed = self.generate_stop_motion_curves(self.animCurvesBuffer,
		                                                            ratio=ratio,
		                                                            start=self.time_range[0],
		                                                            end=self.time_range[1],
		                                                            progress_callback=progress_callback,
		                                                            progress_status=progress_status,
		                                                            )
		self.apply_curves(self.animCurvesBuffer,
		                  self.animCurvesProcessed,
		                  start=self.time_range[0],
		                  end=self.time_range[1],
		                  progress_callback=progress_callback,
		                  progress_status=progress_status,
		                  )
		progress_status.emit('Previewing Stop Motion Keys\t:\t{}'.format(ratio + 1.0))
		return
	
	def buffer_worker_result(self, result):
		self.animCurvesBuffer = result
		return
	
	def run_buffer_worker(self):
		worker = WorkerThread(fn=self.get_curves,
		                      nodes=cmds.ls(sl=True),
		                      start=self.time_range[0],
		                      end=self.time_range[1],
		                      )
		
		worker.signals.progress.connect(self.update_progress)
		worker.signals.status.connect(self.status_bar.showMessage)
		worker.signals.result.connect(self.buffer_worker_result)
		worker.run()
		return
	
	def get_curves(self, nodes, start, end, progress_callback, progress_status):
		# Signals
		progress_callback.emit(0)
		progress_status.emit('Getting Animation Data')
		step = 100.0 / float(len(nodes))
		current = 0.0
		
		result = {}
		curves = cmds.keyframe(nodes, q=True, name=True)
		
		for curve in curves:
			curve_dict = {}
			
			for frame in range(start, end + 1):
				curve_dict[frame] = cmds.keyframe(curve, q=True, time=(frame, frame), ev=True)[0]
			
			result[curve] = curve_dict
			
			current += step
			progress_callback.emit(current)
		
		progress_callback.emit(100)
		return result
	
	def curves_value_change(self, curves, start, end, progress_callback, progress_status):
		# Signals
		progress_status.emit('Calculating Changes in Animation')
		progress_callback.emit(0)
		step = 100.0 / float(len(curves))
		current = 0.0
		
		result = []
		
		# Get Max Values
		for frame in range(start, end):
			values = []
			
			for curve in curves:
				value2 = float(curves[curve][frame + 1])
				value1 = float(curves[curve][frame])
				
				value_change = (value2 - value1) / 100.0
				values.append(abs(value_change))
			
			result.append(max(values))
			current += step
			progress_callback.emit(current)
		
		progress_callback.emit(100)
		return result
	
	def generate_stop_motion_curves(self, curves, ratio, start, end, progress_callback, progress_status):
		# Get Counter
		counter = self.curves_value_change(curves, start, end, progress_callback, progress_status)
		counter_sorted = sorted(counter)
		
		# Threshold
		threshold = counter_sorted[0] + ((counter_sorted[-1] - counter_sorted[0]) * ratio)
		
		key = 0
		remove = 0
		step = 0
		
		remove_list = []
		
		# Loop
		for frame in range(start, end):
			if key == 1:
				key = 0
				remove_list.append(frame)
				remove = remove + 1
			
			elif key == 0:
				value_change = counter[frame - start]
				
				if value_change == 0:
					key = 1
					remove_list.append(frame)
					remove = remove + 1
				
				if value_change < threshold:
					key = 1
					step = step + 1
				
				elif value_change > threshold:
					key = 0
					step = step + 1
		
		# Signals
		progress_status.emit('Generating Stop Motion')
		progress_callback.emit(0)
		step = 100.0 / float(len(curves))
		current = 0.0
		
		result = {}
		
		for curve in curves:
			key_dict = {}
			
			for frame in curves[curve]:
				if frame not in remove_list:
					key_dict[frame] = curves[curve][frame]
			
			result[curve] = key_dict
			
			current += step
			progress_callback.emit(current)
		
		progress_callback.emit(100)
		return result
	
	def apply_curves(self, original, processed, start, end, progress_callback, progress_status):
		# Signals
		progress_status.emit('Removing Keys')
		progress_callback.emit(0)
		step = 100.0 / float(len(original))
		current = 0.0
		
		for curve in original:
			set_curve_to_step(curve)
			try:
				cmds.cutKey(curve,
				            time=(start + 0.001, end - 0.001),
				            option="keys",
				            cl=True
				            )
				self.add_keys(curve,
				              processed[curve],
				              )
			
			except RuntimeError:
				pass
			
			current += step
			progress_callback.emit(current)
		
		progress_callback.emit(100)
		return
	
	def add_keys(self, curve, anim_dict):
		"""
		Add keyframes to animation curve

		:param curve: animation curve name
		:param anim_dict: dictionary of keyframes in {frame_number (float): value (float)} format
		:return: None
		"""
		
		unit = OpenMaya.MTime.uiUnit()
		nodeNattr = cmds.listConnections(curve, d=True, s=False, p=True)[0]
		selList = OpenMaya.MSelectionList()
		selList.add(nodeNattr)
		mplug = selList.getPlug(0)
		dArrTimes = OpenMaya.MTimeArray()
		dArrVals = OpenMaya.MDoubleArray()
		
		if 'rotate' in nodeNattr:
			for i in anim_dict.keys():
				dArrTimes.append(OpenMaya.MTime(float(i), unit))
				dArrVals.append(OpenMaya.MAngle.uiToInternal(anim_dict[i]))
		else:
			for i in anim_dict.keys():
				dArrTimes.append(OpenMaya.MTime(float(i), unit))
				dArrVals.append(anim_dict[i])
		
		crvFnc = OpenMayaAnim.MFnAnimCurve(mplug)
		crvFnc.addKeys(dArrTimes, dArrVals, crvFnc.kTangentAuto, crvFnc.kTangentStep)
		return
	
	# ==================================================================================================================
	# Apply
	# ==================================================================================================================
	
	@undo
	def simulateFilter(self, progress_callback, progress_status):
		# Signals
		progress_status.emit('Simulating...')
		progress_callback.emit(0)
		step = 100.0 / float(len(self.selected))
		current = 0.0
		
		layer_name = None
		layer_exceptions = []
		rig = None
		rig_names = []
		new_items = []
		
		# Get items
		for item in self.selected:
			namespace = item.split(':')[0]
			
			if namespace:
				rig = Apex_Rig(namespace=namespace)
				
				if rig.main_controls:
					for control in rig.main_controls:
						if control not in self.selected:
							new_items.append(control)
				
				if rig.dyn_controls:
					layer_exceptions += rig.dyn_controls
				
				if hasattr(Apex_Name, namespace):
					rig_name = getattr(Apex_Name, namespace)
					
					if rig_name not in rig_names:
						rig_names.append(rig_name)
		
		if new_items:
			self.selected += new_items
		
		if rig_names:
			layer_name = 'stopMotion_layer1'
			for rig_name in rig_names:
				layer_name = '{}_{}'.format(rig_name, layer_name)
		
		# Dynamics
		if self.is_dynamic and rig:
			if rig.dyn_joints:
				rig.transfer_dyn_to_controls()
		
		# Animation Layers
		if self.is_layer:
			clean_anim_layers()
			
			if not layer_name:
				layer_name = 'stoppedMotion1'
			
			layer_name = create_anim_layer(layer_name)
			
			# Bake
			bake_to_layer(self.selected, layer_name)
		
		# Simulate
		if self.is_simulate:
			generate_stop_motion(self.selected,
			                     ratio=self.ratio,
			                     randomness=0.0,
			                     start=self.time_range[0],
			                     end=self.time_range[1],
			                     layer=layer_name,
			                     )
		
		# Exceptions
		if self.is_layer and layer_exceptions:
			for item in layer_exceptions:
				remove_from_anim_layer(item, layer_name)
		
		progress_callback.emit(0)
		progress_status.emit('Done')
		return
	
	# ==================================================================================================================
	# Close
	# ==================================================================================================================
	
	def closeEvent(self, *args, **kwargs):
		QMainWindow.closeEvent(self, *args, **kwargs)
		
		if self.preview_active:
			self.cancel_preview()
		self.deleteLater()
		return


# ======================================================================================================================
#
#
# Execute
#
#
# ======================================================================================================================


def show(name=UI_NAME, title=UI_TITLE, *args, **kwargs):
	if cmds.window(name, exists=True):
		cmds.deleteUI(name, wnd=True)
	
	# Window
	window = Window(get_maya_window())
	window.setObjectName(name)
	window.setWindowTitle(title)
	window.show()
	return


if __name__ == '__main__':
	pass
