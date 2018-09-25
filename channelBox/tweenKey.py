# LANCER.CHANNELBOX.TWEENKEY
#
#
#
#
#

# Qt Modules
QTLOADED = False

try:
	from PySide2.QtCore import *
	from PySide2.QtGui import *
	from PySide2.QtWidgets import *
	from shiboken2 import wrapInstance
	QTLOADED = True
except ImportError:
	try:
		from library.Qt.QtCore import *
		from library.Qt.QtGui import *
		from library.Qt.QtWidgets import *
		from shiboken import wrapInstance
		QTLOADED = True
	except ImportError:
		raise ImportError('Unable to load Qt.')

# Python Modules
import sys
from functools import partial


# Maya Modules
from maya import cmds, mel, OpenMayaUI

########################################################################################################################
#
#
#	Global Variables
#
#
########################################################################################################################

VALUERANGE = [
	0.0,
	.0833,
	.1666,
	.2499,
	.3332,
	.4165,
	.5,
	.5833,
	.6666,
	.7499,
	.8332,
	.9165,
	1.0,
]

SPECIALVALUES = [
	0.0,
	.2499,
	.5,
	.7499,
	1.0,
]

ROUNDOFF = 100


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################

def undoable(function):
	def decoratorCode(*args, **kwargs):
		cmds.undoInfo(openChunk=True)
		functionReturn = None
		try:
			functionReturn = function(*args, **kwargs)
		except:
			print sys.exc_info()[1]

		finally:
			cmds.undoInfo(closeChunk=True)
			return functionReturn

	return decoratorCode


def getKeyable(obj):
	var = []
	cbb = cmds.channelBox('mainChannelBox', q=True, sma=True)
	if cbb:
		var = cbb
	else:
		var = cmds.listAttr(obj, k=True)
	return var


@undoable
def tween(percent, *args):
	selected = cmds.ls(sl=True)

	if selected:
		for obj in selected:
			attributes = getKeyable(obj)
			if attributes:
				for attr in attributes:
					query = '{}.{}'.format(obj, attr)
					nextTime = cmds.findKeyframe(query, which='next')
					nextValue = cmds.getAttr(query, time=nextTime)

					previousTime = cmds.findKeyframe(query, which='previous')
					previousValue = cmds.getAttr(query, time=previousTime)
					newValue = (nextValue - previousValue) * percent + previousValue

					try:
						cmds.setAttr(query, newValue)
					except:
						print 'TweenKey: Unable to set "{}.{}". Skipped.'.format(obj, attr)
	return


########################################################################################################################
#
#
#	UI
#
#
########################################################################################################################

class stretchedButton(QPushButton):
	def __init__(self, *args):
		QPushButton.__init__(self, *args)
		self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

	def resizeEvent(self, evt):
		font = self.font()
		font.setPixelSize(self.width() * 0.5)
		self.setFont(font)
		return


class toolTipSlider(QSlider):
	def __init__(self, offset=QPoint(0, -40), *args):
		QSlider.__init__(self, *args)

		self.offset = offset
		self.style = QApplication.style()
		self.opt = QStyleOptionSlider()
		self.valueChanged.connect(self.show_tip)

	def show_tip(self, _):
		self.initStyleOption(self.opt)
		rectHandle = self.style.subControlRect(self.style.CC_Slider, self.opt, self.style.SC_SliderHandle)
		pos_local = rectHandle.topLeft() + self.offset
		pos_global = self.mapToGlobal(pos_local)
		QToolTip.showText(pos_global, str(self.value()), self)


def slider(min=0, max=100, default=50):
	control = toolTipSlider()
	control.setOrientation(Qt.Horizontal)
	control.setRange(min, max)
	control.setValue(default)
	control.sliderReleased.connect(lambda *x: tween(float(control.value()) / float(ROUNDOFF)))
	return control


class control:
	def __init__(self):
		self.widget = QWidget()
		self.layout = QVBoxLayout(self.widget)

		self.slider = slider()
		self.layout.addWidget(self.slider)
		self.layout.addWidget(self.buttonRow())

	def onButtonPress(self, value):
		tween(value)
		self.slider.setValue(int(value * ROUNDOFF))
		return

	def button(self, value=0, width=5, height=15, labelVisibility=False):
		control = QPushButton()
		control.setMinimumSize(width, height / 2)
		control.setToolTip(str(int(value * ROUNDOFF)))
		control.clicked.connect(lambda *x: self.onButtonPress(value))

		if labelVisibility:
			control.setText(str(int(value * ROUNDOFF)))
		return control

	def buttonRow(self):
		widget = QWidget()
		layout = QHBoxLayout(widget)
		layout.setMargin(0)

		for value in VALUERANGE:
			i = VALUERANGE.index(value)
			control = self.button(value=value)
			layout.addWidget(control)

			if value in SPECIALVALUES:
				control.setStyleSheet('background-color: red;')

		return widget


def formRow(items=[], exclude=[], special=[], specialColor=[1, 0, 0], roundOff=1, command=[], *args):
	form = cmds.formLayout(nd=100)

	length = float(len(items))
	step = 100 / length

	masterList = []

	i = 0
	for v in items:

		if type(v) == float or type(v) == int:
			label = int(v * roundOff)

		elif type(v) == str:
			label = v.capitalize()

		if v in exclude:
			x = cmds.text(l=label, enable=False)

		else:
			x = cmds.button(l=label, c=partial(command, v), )

		if special:
			if v in special:
				cmds.button(x, e=True, bgc=specialColor)

		masterList.append(x)

		if i == 0:
			cmds.formLayout(form, edit=True, attachForm=[(x, 'left', 0), (x, 'top', 0), (x, 'bottom', 0), ],
			                attachPosition=[(x, 'right', 1, step), ], )

		else:
			cmds.formLayout(form, edit=True, attachForm=[(x, 'top', 0), (x, 'bottom', 0), ],
			                attachControl=[(x, 'left', 2, masterList[i - 1]), ],
			                attachPosition=[(x, 'right', 1, step), ])

		step += 100 / length
		i += 1

	cmds.setParent('..')
	return


def ui():
	column = cmds.columnLayout(adj=True)
	cmds.frameLayout(lv=False, bgs=True)
	tweenInt = cmds.intField(minValue=0, maxValue=100, value=50, ed=False)
	tweenSlide = cmds.floatSlider(minValue=0.0, maxValue=1.0, value=.5, dc=tween)

	formRow(items=VALUERANGE,
	        special=SPECIALVALUES,
	        roundOff=ROUNDOFF,
	        command=tween)

	# column = cmds.columnLayout('Keys', adj=True)
	# widget = wrapInstance(long(OpenMayaUI.MQtUtil.findControl(column)), QWidget)
	# control = tweenKey.tweenControl(True, True)
	# control.setParent(widget)
	# cmds.setParent('..')

	cmds.setParent('..')
	cmds.setParent('..')
	return column


########################################################################################################################
#
#
#	Window
#
#
########################################################################################################################


# def getMayaWindow():
# 	app = QApplication.instance()
# 	return {o.objectName(): o for o in app.topLevelWidgets()}["MayaWindow"]

def getMayaWindow():
	mayaPtr = OpenMayaUI.MQtUtil.mainWindow()
	mayaWindow = wrapInstance(long(mayaPtr), QWidget)
	return mayaWindow


def windowQt(*args):
	winName = 'tweenKeyWindowUI'
	if cmds.window(winName, exists=True):
		cmds.deleteUI(winName, wnd=True)

	# Window
	window = QMainWindow(getMayaWindow())
	window.setObjectName(winName)
	window.setWindowTitle('Tween Key')

	# Widget
	widget = QWidget()
	layout = QVBoxLayout(widget)
	window.setCentralWidget(widget)

	# Controls
	layout.addWidget(control().widget)

	# Show UI
	window.show()
	return


def windowMaya(*args):
	winName = 'tweenKeyWindowUI'
	if cmds.window(winName, exists=True):
		cmds.deleteUI(winName, wnd=True)

	cmds.window(winName, t='Tween Key')
	ui()
	cmds.showWindow(winName)
	return
