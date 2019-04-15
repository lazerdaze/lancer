# LANCER.ANIM.REFPLAYER
#
#
#
#
#

# Qt Modules
QTLOADED = False
CANSYNC = False

try:
	from PySide2.QtCore import *
	from PySide2.QtGui import *
	from PySide2.QtWidgets import *
	from PySide2.QtMultimedia import *

	QTLOADED = True
except ImportError:
	try:
		from library.Qt.QtCore import *
		from library.Qt.QtGui import *
		from library.Qt.QtWidgets import *
		from library.Qt.QtMultimedia import *

		QTLOADED = True
	except ImportError:
		raise ImportError('Unable to load Qt.')

if QTLOADED:
	try:
		from shiboken2 import wrapInstance
		CANSYNC = True
	except ImportError:
		try:
			from shiboken import wrapInstance
			CANSYNC = True
		except ImportError:
			raise ImportError('Unable to sync.')

# Python Modules
import os
import sys

# Maya Modules
from maya import cmds, OpenMayaUI

########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################

DIRPATH = os.path.dirname(os.path.abspath(__file__))
IMAGEPATH = os.path.join(DIRPATH, 'icons')
WINDOWNAME = 'refPlayerWindowUI'


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################

def getAllFilesInDirectory(filepath):
	return [os.path.abspath(os.path.join(filepath, f)) for f in os.listdir(filepath) if
	        os.path.isfile(os.path.join(filepath, f))]


def collectSequenceFromFilepath(filepath):
	sequence = []
	directory = os.path.dirname(filepath)
	filename, extension = os.path.splitext(filepath)

	basename = os.path.basename(filepath).replace(extension, '')

	if '.' in basename:
		basename = basename.split('.')[0]

		for f in os.listdir(directory):
			if basename in f:
				sequence.append(os.path.join(directory, f))

	return sorted(sequence) if sequence else None


def convertToQt(mayaName, objectType):
	"""
	Given the name of a Maya UI element of any type, return the corresponding QT Type object.
	"""
	ptr = OpenMayaUI.MQtUtil.findControl(mayaName)
	if ptr is None:
		ptr = OpenMayaUI.MQtUtil.findLayout(mayaName)
		if ptr is None:
			ptr = OpenMayaUI.MQtUtil.findMenuItem(mayaName)
	if ptr is not None:
		return wrapInstance(long(ptr), objectType)


class scriptJob(object):
	"""
	A context manager for creating script jobs
	"""

	def __init__(self):
		self.id = None

	def createJob(self, *args, **kwargs):
		self.id = cmds.scriptJob(*args, **kwargs)
		return self.id

	def killJob(self):
		if self.id:
			cmds.scriptJob(kill=self.id, force=True)
			self.id = None

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_type is not None:
			self.killJob()


########################################################################################################################
#
#
#	COMPONENTS
#
#
########################################################################################################################

class iconButton(QToolButton):
	def __init__(self, parent, offFilepath, onFilepath=None):
		QToolButton.__init__(self, parent)
		self.onFilepath = onFilepath
		self.offFilepath = offFilepath
		self.defaultOpacity = 0.75
		self.hoverOpacity = 1
		self.painter = None
		self.active = False

		self.offPixmap = QPixmap(self.offFilepath)
		if self.onFilepath:
			self.onPixmap = QPixmap(self.onFilepath)
		self.pixmap = self.offPixmap
		self.updatePaintEvent(self.defaultOpacity)

	def setActive(self, value):
		if self.offFilepath:
			if value:
				self.pixmap = self.onPixmap
			else:
				self.pixmap = self.offPixmap
			self.active = value
			self.updatePaintEvent(self.defaultOpacity)
		return

	def updatePaintEvent(self, opacity):
		result = QPixmap(self.pixmap.size())
		result.fill(Qt.transparent)

		self.painter = QPainter(result)
		self.painter.setOpacity(opacity)
		self.painter.drawPixmap(0, 0, self.pixmap)
		self.painter.end()
		self.setIcon(QIcon(result))

	def enterEvent(self, event):
		self.updatePaintEvent(self.hoverOpacity)
		return

	def leaveEvent(self, event):
		self.updatePaintEvent(self.defaultOpacity)
		return


class playbackWidget(QWidget):
	stateChanged = Signal(str)
	play = Signal()
	pause = Signal()
	prevFrame = Signal()
	nextFrame = Signal()
	goToStart = Signal()
	goToEnd = Signal()
	loopState = Signal(bool)
	connectState = Signal(bool)

	def __init__(self, parent=None, size=20, margins=10, spacing=5):
		QWidget.__init__(self, parent)

		self.state = 'stopped'
		self.loop = True
		self.connected = False

		# Settings
		sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)
		self.setStyleSheet('''QToolButton{
				                background:none !important;
				                border:none !important;
				                margin:0 !important;
				                padding:0 !important;
				                }
				                QToolButton:checked{
				                background-color:black !important;
				                border:none !important;
				                margin:0 !important;
				                padding:0 !important;
				                }
				                QToolButton:menu-indicator{
				                image:none !important;
				                }
				                ''')

		# Layout
		self.mainLayout = QHBoxLayout(self)
		self.mainLayout.setSpacing(spacing)
		self.mainLayout.setContentsMargins(margins, margins, margins, margins)
		spacerItem = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
		self.mainLayout.addItem(spacerItem)

		# Start Button
		self.buttonStart = iconButton(self, os.path.join(IMAGEPATH, 'start_100.png'))
		self.buttonStart.setIconSize(QSize(size, size))
		self.buttonStart.clicked.connect(lambda: self.jump('start'))
		self.mainLayout.addWidget(self.buttonStart)

		# Previous Frame Button
		self.buttonPrevFrame = iconButton(self, os.path.join(IMAGEPATH, 'prevFrame_100.png'))
		self.buttonPrevFrame.setIconSize(QSize(size, size))
		self.mainLayout.addWidget(self.buttonPrevFrame)
		self.buttonPrevFrame.clicked.connect(lambda: self.jump('prev'))

		# Play Button
		self.buttonPlay = iconButton(self, os.path.join(IMAGEPATH, 'play_100.png'),
		                             os.path.join(IMAGEPATH, 'paused_100.png'))
		self.buttonPlay.setIconSize(QSize(size, size))
		self.buttonPlay.clicked.connect(self.playClicked)
		self.mainLayout.addWidget(self.buttonPlay)

		# Next Frame Button
		self.buttonNextFrame = iconButton(self, os.path.join(IMAGEPATH, 'nextFrame_100.png'))
		self.buttonNextFrame.setIconSize(QSize(size, size))
		self.buttonNextFrame.clicked.connect(lambda: self.jump('next'))
		self.mainLayout.addWidget(self.buttonNextFrame)

		# End Button
		self.buttonEnd = iconButton(self, os.path.join(IMAGEPATH, 'end_100.png'))
		self.buttonEnd.setIconSize(QSize(size, size))
		self.buttonEnd.clicked.connect(lambda: self.jump('end'))
		self.mainLayout.addWidget(self.buttonEnd)

		# Loop Button
		self.buttonLoop = iconButton(self, os.path.join(IMAGEPATH, 'loop_100.png'),
		                             os.path.join(IMAGEPATH, 'loopOnce_100.png'))
		self.buttonLoop.setIconSize(QSize(size, size))
		self.buttonLoop.clicked.connect(self.setLoop)
		self.mainLayout.addWidget(self.buttonLoop)

		# Connect Button
		self.buttonConnect = iconButton(self, os.path.join(IMAGEPATH, 'disconnect_100.png'),
		                                os.path.join(IMAGEPATH, 'connect_100.png'))
		self.buttonConnect.setIconSize(QSize(size, size))
		self.mainLayout.addWidget(self.buttonConnect)
		self.buttonConnect.clicked.connect(self.setConnect)

		spacerItem = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
		self.mainLayout.addItem(spacerItem)

	def setState(self, state):
		self.state = state
		self.stateChanged.emit(self.state)
		return

	def playClicked(self):
		if self.state in ['paused', 'stopped']:
			self.setState('playing')
			self.buttonPlay.setActive(True)
			self.play.emit()
		elif self.state == 'playing':
			self.buttonPlay.setActive(False)
			self.pause.emit()
			self.setState('paused')
		return

	def jump(self, typ):
		self.setState('paused')
		self.buttonPlay.setChecked(False)
		if typ == 'next':
			self.nextFrame.emit()
		elif typ == 'prev':
			self.prevFrame.emit()
		elif typ == 'start':
			self.goToStart.emit()
		elif typ == 'end':
			self.goToEnd.emit()
		return

	def setLoop(self):
		self.loop = False if self.loop else True
		self.buttonLoop.setActive(self.loop)
		self.loopState.emit(self.loop)
		return

	def setConnect(self):
		self.connected = False if self.connected else True
		self.buttonConnect.setActive(self.connected)
		self.connectState.emit(self.connected)
		return


########################################################################################################################
#
#
#	TIMELINE
#
#
########################################################################################################################

class timelineWidget(QWidget):
	bufferUpdate = Signal(int)
	stateChanged = Signal(str)
	frameChanged = Signal(int)

	def __init__(self, parent=None):
		QWidget.__init__(self, parent)

		self.sequence = None
		self.currentState = None
		self.isPlaying = False
		self.start = 0
		self.duration = 100
		self.frameRate = 41.667
		self.currentFrame = 0
		self.currentPixmap = None
		self.isLoop = True
		self.imageCache = []

		# Settings
		self.setStyleSheet('background: black;')
		self.setMinimumHeight(100)

		# Display
		self.movieLabel = QLabel(self)
		self.movieLabel.setAlignment(Qt.AlignCenter)
		self.movieLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

		# Timeline for Sequences
		self.movie = QTimeLine(1000, self)
		self.movie.setFrameRange(self.start, self.duration)
		self.movie.setCurveShape(QTimeLine.LinearCurve)
		self.movie.setEasingCurve(QEasingCurve.Linear)
		self.movie.setUpdateInterval(0)
		self.movie.setLoopCount(0)

		self.movie.frameChanged.connect(self.setSequence)
		self.movie.stateChanged.connect(self.setState)

		# Layout
		self.mainLayout = QVBoxLayout(self)
		self.mainLayout.addWidget(self.movieLabel)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)
		self.mainLayout.setSpacing(0)
		self.setLayout(self.mainLayout)

	def setState(self, state):
		self.currentState = state
		self.stateChanged.emit(state)
		self.fitToWindow()
		return

	def loadSequence(self, sequence):
		self.sequence = sequence
		end = len(sequence) - 1
		self.setRange(0, end)
		self.movie.setDuration(end * self.frameRate)
		self.imageCache = []

		for item in sequence:
			self.imageCache.append(QPixmap(item))

		return

	def updatePixmap(self, pixmap):
		self.movieLabel.setPixmap(pixmap)
		self.currentPixmap = pixmap
		return

	def setSequence(self, frame):
		self.setCurrentFrame(frame)
		if self.imageCache:
			pixmap = self.imageCache[frame]
			self.updatePixmap(pixmap)
			self.fitToWindow()
		self.frameChanged.emit(frame)
		return

	def setFrameRate(self, rate):
		self.frameRate = rate
		return

	def setDuration(self, duration):
		self.duration = float(duration) * float(self.frameRate)
		self.movie.setDuration(self.duration)
		return

	def setStartFrame(self, value):
		self.start = value
		self.movie.setStartFrame(value)
		return

	def setCurrentFrame(self, frame):
		self.currentFrame = frame
		return

	def setEndFrame(self, end):
		self.duration = end
		self.movie.setEndFrame(end)
		return

	def setRange(self, start, end):
		self.start = start
		self.duration = end
		self.movie.setFrameRange(start, end)
		return

	def valueChanged(self, value):
		print value
		return

	def jumpToFrame(self, frame):
		if self.currentState != QTimeLine.Paused:
			self.movie.setPaused(True)
		self.setSequence(frame)
		self.movie.frameChanged.emit(frame)
		return

	def jumpToPrevFrame(self):
		frame = self.currentFrame - 1
		if frame > self.start:
			self.jumpToFrame(frame)
		return

	def jumpToNextFrame(self):
		frame = self.currentFrame + 1
		if frame < self.duration:
			self.jumpToFrame(frame)
		return

	def fitToWindow(self):
		if self.currentPixmap:
			w = self.movieLabel.width()
			h = self.movieLabel.height()
			pixmap = self.currentPixmap
			self.movieLabel.setPixmap(pixmap.scaled(w, h, Qt.KeepAspectRatio))
		return

	def playPause(self):
		if self.currentState in [QTimeLine.NotRunning, QTimeLine.Paused]:
			self.movie.setPaused(False)
		else:
			self.movie.setPaused(True)
		return

	def resizeEvent(self, event):
		self.fitToWindow()
		return


class timelineSliderWidget(QWidget):
	sliderMoved = Signal(int)
	jumpedToFrame = Signal(int)

	inMarkerMoved = Signal(int)
	outMarkerMoved = Signal(int)
	stop = Signal()
	prevFrame = Signal()
	nextFrame = Signal()
	rangeChanged = Signal(int, int)
	doubleClick = Signal()
	bufferProgress = Signal(int)

	def __init__(self, parent=None):
		QWidget.__init__(self, parent)

		self.width = 1
		self.height = 20
		self.lineWidth = 1
		self.topMargin = 6
		self.bottomMargin = self.topMargin * 2
		self.bufferMargin = 2
		self.handleWidth = 2
		self.divisions = 100
		self.min = 0
		self.max = 100
		self.scale = self.max - self.min
		self.currentValue = 50
		self.bufferValue = 0
		self.bufferMin = 0
		self.bufferMax = 100
		self.inMark = self.min
		self.outMark = self.max
		self.totalRange = self.outMark - self.inMark
		self.hasReachedEnd = False
		self.loop = True
		self.emitWhileMoving = True
		self.isMoving = None
		self.currentHandle = None
		self.oldMousePosition = 0
		self.oldMinPosition = self.inMark
		self.oldMaxPosition = self.outMark

		self.outlineColor = QColor(0, 0, 0)
		self.backgroundColor = QColor(60, 60, 60)
		self.rangeColor = QColor(150, 150, 150)
		self.inOutColor = QColor(150, 150, 150)
		self.bufferColor = QColor(0, 120, 40)
		self.handleColor = QColor(250, 250, 250)
		self.hightlightColor = QColor(170, 170, 170)
		self.divisionColor = QColor(10, 10, 10)

		self.painter = None
		self.inOutRect = None
		self.bufferRect = None
		self.mainHandleRect = None
		self.inHandleRect = None
		self.outHandleRect = None
		self.backgroundRect = None
		self.setMinimumSize(self.width, self.height)
		self.setMouseTracking(True)
		self.updateDisplayValues()

		# Settings
		self.setMinimumSize(0, self.height)
		self.setMaximumSize(16777215, self.height)
		sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)

	def paintEvent(self, event):
		self.painter = QPainter()
		# self.painter.setRenderHints(QPainter.Antialiasing)
		self.painter.begin(self)
		self.drawWidget(self.painter)
		self.painter.end()
		return

	def drawWidget(self, widget):
		size = self.size()
		width = size.width()
		height = size.height()

		till = int((float(width) / float(self.max)) * self.currentValue)

		inMark = int((float(width) / float(self.max)) * self.inMark)
		outMark = int((float(width) / float(self.max)) * self.outMark)

		current = int((float(width) / float(self.max)) * self.currentValue)
		buffer = int((float(width) / float(self.max)) * self.bufferValue)

		# Background Rect
		widget.setPen(Qt.NoPen)
		widget.setBrush(self.backgroundColor)
		self.backgroundRect = QRect(0, self.topMargin, width, height - self.bottomMargin)
		widget.drawRect(self.backgroundRect)

		# InOut Rect
		widget.setPen(Qt.NoPen)
		widget.setBrush(self.inOutColor)
		self.inOutRect = QRect(inMark, self.topMargin, outMark - inMark, height - self.bottomMargin)
		widget.drawRect(self.inOutRect)

		# Buffer Rect
		widget.setPen(Qt.NoPen)
		widget.setBrush(self.bufferColor)
		self.bufferRect = widget.drawRect(self.min, self.bufferMargin + self.topMargin, buffer,
		                                  height - self.bottomMargin - (self.bufferMargin * 2))

		# Divison Lines
		# if self.divisions > 1:
		# 	step = (float(width) / float(self.divisions * 2))
		# 	value = 0
		# 	pen = QPen(QColor(self.outlineColor), self.lineWidth, Qt.SolidLine)
		# 	widget.setPen(pen)
		# 	widget.setBrush(Qt.NoBrush)
		#
		# 	for x in range(0, int(self.divisions * 2)):
		# 		if x % 2 != 0:
		# 			widget.drawLine(value, 0, value, height)
		# 		value += step

		# Main Handle
		widget.setPen(Qt.NoPen)
		widget.setBrush(self.handleColor)
		self.mainHandleRect = QRect(current, 0, self.handleWidth, height)
		widget.drawRect(self.mainHandleRect)

		# In Handle
		widget.setPen(Qt.NoPen)
		widget.setBrush(self.handleColor)
		self.inHandleRect = QRect(inMark, self.topMargin, self.handleWidth, height - self.bottomMargin)
		widget.drawRect(self.inHandleRect)

		# Out Handle
		widget.setPen(Qt.NoPen)
		widget.setBrush(self.handleColor)
		self.outHandleRect = QRect(outMark - self.handleWidth, self.topMargin, self.handleWidth,
		                           height - self.bottomMargin)
		widget.drawRect(self.outHandleRect)
		return

	def setLooping(self, value):
		self.loop = value
		return

	def isLooping(self):
		return self.loop

	def loopPlayback(self, value):
		if self.loop:
			if value >= self.outMark:
				return self.inMark
			else:
				return value

	def emitRange(self):
		self.rangeChanged.emit(self.min, self.max)
		return

	def setValue(self, value):
		if self.min < value < self.max:
			self.currentValue = value
			self.updateDisplayValues()
		return

	def value(self):
		return self.currentValue

	def updateBuffer(self, value):
		self.bufferValue = value
		self.updateDisplayValues()
		return

	def buffer(self):
		return self.bufferValue

	def emitBuffer(self):
		self.bufferProgress.emit(int(self.bufferValue))
		return

	def setMaximum(self, value):
		self.max = value
		self.updateDisplayValues()
		return

	def maximum(self):
		return self.max

	def setMinimum(self, value):
		self.min = value
		self.updateDisplayValues()
		return

	def minimum(self):
		return self.min

	def setInMark(self, value):
		if value >= self.min:
			self.inMark = value
			self.updateDisplayValues()
		return

	def setOutMark(self, value):
		if value <= self.max:
			self.outMark = value
			self.updateDisplayValues()
		return

	def setMarkers(self, minV, maxV):
		self.setInMark(minV)
		self.setOutMark(maxV)
		return

	def setRange(self, minV, maxV):
		self.setMinimum(minV)
		self.setMaximum(maxV)
		return

	def range(self):
		return self.min, self.max

	def setDivisions(self, value):
		self.divisions = value
		self.update()
		return

	def updateDisplayValues(self):
		self.totalRange = self.outMark - self.inMark
		self.update()
		return

	def resizeEvent(self, event):
		self.updateDisplayValues()
		return

	def jumpToPrevFrame(self):
		self.setValue(self.currentValue - 1)
		return

	def jumpToNextFrame(self):
		self.setValue(self.currentValue + 1)
		return

	def mousePressEvent(self, event):
		width = self.size().width()
		if event.buttons() == Qt.LeftButton:
			self.currentHandle = self.checkMovable(event)
			self.oldMousePosition = self.convertPositionToValue(event.x())
			self.oldMinPosition = self.inMark
			self.oldMaxPosition = self.outMark

			if self.currentHandle in ['background', 'inOut']:
				frame = self.oldMousePosition
				self.setValue(frame)
				self.jumpedToFrame.emit(frame)
		return

	def mouseMoveEvent(self, event):
		width = self.size().width()
		mousePosition = self.convertPositionToValue(event.x())

		if self.checkMovable(event) == 'inOut':
			if self.inOutColor != self.hightlightColor:
				self.inOutColor = self.hightlightColor
				self.update()
		else:
			if self.inOutColor != self.rangeColor:
				self.inOutColor = self.rangeColor
				self.update()

		if event.buttons() == Qt.LeftButton:
			if self.currentHandle == 'main':
				if mousePosition >= self.min and mousePosition <= self.max:
					self.setValue(mousePosition)
					self.sliderMoved.emit(mousePosition)
			elif self.currentHandle == 'in':
				if mousePosition < self.outMark:
					self.setInMark(mousePosition)
					self.inMarkerMoved.emit(mousePosition)
			elif self.currentHandle == 'out':
				if mousePosition > self.inMark:
					self.setOutMark(mousePosition)
					self.outMarkerMoved.emit(mousePosition)
			elif self.currentHandle == 'inOut':
				diff = mousePosition - self.oldMousePosition
				minV = self.oldMinPosition + diff
				maxV = self.oldMaxPosition + diff

				if self.inOutColor != self.hightlightColor:
					self.inOutColor = self.hightlightColor

				if minV >= self.min and maxV <= self.max:
					self.setMarkers(minV, maxV)
					self.rangeChanged.emit(minV, maxV)

					self.inMarkerMoved.emit(minV)
					self.outMarkerMoved.emit(maxV)
		return

	def convertPositionToValue(self, position):
		width = self.size().width()
		return int((float(self.max) / float(width)) * float(position))

	def convertValueToPosition(self, value):
		width = self.size().width()
		return int((float(self.max) / float(width)) * float(value))

	def checkMovable(self, event):
		margin = 5
		mousePosition = QPoint(event.x(), event.y())
		x = event.x()
		y = event.y()

		mainX = self.mainHandleRect.x()
		mainY = self.mainHandleRect.y()
		main = QRectF(mainX - margin,
		              mainY - margin,
		              margin * 2 + self.handleWidth,
		              self.height + margin * 2
		              )

		inX = self.inHandleRect.x()
		inY = self.inHandleRect.y()
		inHandle = QRectF(inX - margin,
		                  inY - margin,
		                  margin * 2 + self.handleWidth,
		                  self.height + margin * 2
		                  )

		outX = self.outHandleRect.x()
		outY = self.outHandleRect.y()
		outHandle = QRectF(outX - margin,
		                   outY - margin,
		                   margin * 2 + self.handleWidth,
		                   self.height + margin * 2
		                   )

		if main.contains(mousePosition):
			return 'main'
		elif inHandle.contains(mousePosition):
			return 'in'
		elif outHandle.contains(mousePosition):
			return 'out'
		elif self.inOutRect.contains(mousePosition):
			return 'inOut'
		elif self.backgroundRect.contains(mousePosition):
			return 'background'
		else:
			return None

	def mouseReleaseEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.currentHandle = None

		mousePosition = QPoint(event.x(), event.y())
		if not self.inOutRect.contains(mousePosition):
			if self.inOutColor != self.rangeColor:
				self.inOutColor = self.rangeColor
				self.update()
		return


########################################################################################################################
#
#
#	PLAYER
#
#
########################################################################################################################

maya_window = wrapInstance(long(OpenMayaUI.MQtUtil.mainWindow()), QObject)
maya_timeline = maya_window.findChild(QWidget, "timeControl1")

class player(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)


		# Maya Sync
		# self.currentJob = scriptJob()
		# self.playbackJob = scriptJob()
		# self.playingJob = scriptJob()
		self.isSynced = False
		self.mayaStart = 0
		self.mayaEnd = 100
		self.mayaCurrent = 0
		self.mayaOffset = 0

		# Player Settings
		self.mainLayout = QVBoxLayout(self)
		self.mainLayout.setContentsMargins(10, 10, 10, 10)
		self.mainLayout.setSpacing(10)
		self.setLayout(self.mainLayout)

		# Viewer
		self.viewWidget = timelineWidget()
		self.movie = self.viewWidget.movie
		self.movieLabel = self.viewWidget.movieLabel
		self.mainLayout.addWidget(self.viewWidget)

		# Trackbar
		self.trackbar = timelineSliderWidget()
		self.trackbar.sliderMoved.connect(self.seek)
		self.trackbar.jumpedToFrame.connect(self.seek)
		self.mainLayout.addWidget(self.trackbar)
		self.trackbar.inMarkerMoved.connect(self.movie.setStartFrame)
		self.trackbar.outMarkerMoved.connect(self.movie.setEndFrame)
		self.trackbar.inMarkerMoved.connect(self.updateDuration)
		self.trackbar.outMarkerMoved.connect(self.updateDuration)
		self.movie.frameChanged.connect(self.trackbar.setValue)
		self.movie.frameChanged.connect(self.playInRange)
		self.viewWidget.bufferUpdate.connect(self.trackbar.updateBuffer)

		# Controls
		self.controls = playbackWidget()
		self.mainLayout.addWidget(self.controls)
		self.controls.play.connect(self.play)
		self.controls.pause.connect(self.pause)
		self.controls.connectState.connect(self.setSync)

	def setSync(self, value):
		if value:
			self.pause()

			self.mayaCurrent = int(cmds.currentTime(q=True))
			self.mayaStart = int(cmds.playbackOptions(q=True, min=True))
			self.mayaEnd = int(cmds.playbackOptions(q=True, max=True))
			self.mayaOffset = self.mayaCurrent - self.viewWidget.currentFrame

			self.seek(self.mayaCurrent)

			#self.currentJob.createJob(e=['timeChanged', self.mayaCurrentFrameSync])
			#self.playingJob.createJob(ct=['playingBack', self.mayaPlayingBack])

			# self.trackbar.setInMark()
			self.trackbar.setEnabled(False)
			self.isSynced = True
		else:
			self.killJobs()
			self.trackbar.setEnabled(True)
			self.isSynced = False

			print self.mayaStart, self.mayaEnd, self.mayaCurrent
		return

	def mayaCurrentFrameSync(self):
		self.mayaCurrent = int(cmds.currentTime(q=True))
		self.mayaOffset = self.mayaCurrent - self.viewWidget.currentFrame
		current = self.mayaCurrent
		minFrame = self.viewWidget.start
		maxFrame = self.viewWidget.duration

		if minFrame <= current <= maxFrame:
			self.seek(current)
		elif current > maxFrame:
			self.seek(maxFrame - 1)
		elif current < minFrame:
			self.seek(minFrame + 1)
		return

	def mayaPlayingBack(self):
		print True
		self.movie.start()
		return

	def killJobs(self):
		# self.currentJob.killJob()
		# self.playingJob.killJob()
		# self.playbackJob.killJob()
		return

	def play(self):
		if self.viewWidget.currentState == QTimeLine.Paused:
			self.movie.setPaused(False)
		else:
			self.movie.start()
		return

	def pause(self):
		self.movie.setPaused(True)
		return

	def setSequence(self, sequence):
		self.movie.stop()
		self.setRange(0, len(sequence) - 1)
		self.trackbar.setDivisions(len(sequence) - 1)
		self.viewWidget.loadSequence(sequence)
		self.seek(1)
		return

	def setRange(self, start, end):
		self.trackbar.setRange(start, end)
		self.trackbar.setMarkers(start, end)
		return

	def playInRange(self, value):
		if self.viewWidget.currentState == QTimeLine.Running:
			if self.trackbar.min <= value <= self.trackbar.max:
				if value >= self.trackbar.outMark:
					self.movie.setCurrentTime(self.viewWidget.frameRate * self.trackbar.inMark)
				elif value < self.trackbar.inMark:
					if self.movie.startFrame() != self.trackbar.inMark:
						self.movie.setStartFrame(self.trackbar.inMark)
					self.movie.setCurrentTime(self.viewWidget.frameRate * self.trackbar.inMark)
			else:
				self.movie.setCurrentTime(self.viewWidget.frameRate * self.trackbar.inMark)
		return

	def seek(self, frame):
		self.movie.setPaused(True)
		self.viewWidget.jumpToFrame(frame)
		return

	def updateDuration(self):
		start = self.trackbar.inMark
		end = self.trackbar.outMark
		value = end - start

		self.movie.setStartFrame(start)
		self.movie.setEndFrame(end)
		self.viewWidget.setDuration(value)
		return


########################################################################################################################
#
#
#	WINDOW
#
#
########################################################################################################################

class mainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		QMainWindow.__init__(self, *args, **kwargs)

		# Window
		self.setObjectName(WINDOWNAME)
		self.setWindowTitle('Reference Player')

		# Widget
		self.mainWidget = QWidget()
		self.mainLayout = QVBoxLayout(self.mainWidget)
		self.setCentralWidget(self.mainWidget)

		# Menu
		self.menubar = QMenuBar(self)
		self.fileMenu = self.menubar.addMenu('File')
		self.openAction = self.fileMenu.addAction('Open')
		self.openAction.triggered.connect(self.openFile)
		self.setMenuBar(self.menubar)

		# Player
		self.player = player()
		self.mainLayout.addWidget(self.player)

	def openFile(self):
		filepath = QFileDialog.getOpenFileName(self, 'Open Image Sequence', None, '''Image Files (*.jpg *.png)''')[0]

		if filepath:
			sequence = collectSequenceFromFilepath(filepath)
			if sequence:
				self.player.setSequence(sequence)
		return

	def closeEvent(self, event):
		try:
			self.player.killJobs()
		except:
			pass
		super(QMainWindow, self).closeEvent(event)
		return


def getMayaWindow():
	app = QApplication.instance()
	return {o.objectName(): o for o in app.topLevelWidgets()}['MayaWindow']


def windowUI():
	winName = 'refPlayerWindowUI'
	if cmds.window(winName, exists=True):
		cmds.deleteUI(winName, wnd=True)

	# Window
	window = mainWindow(getMayaWindow())

	# Show UI
	window.show()
	return


########################################################################################################################
#
#
#	STANDALONE
#
#
########################################################################################################################


if __name__ == '__main__':
	pass
