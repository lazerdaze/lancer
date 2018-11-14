# AXEL.ITEM
#
#
#
#
#

# Axel Modules
from anim.axel.core.api import collectSequenceFromFilepath

# Python Modules
import os
import sys

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################

DIRPATH = os.path.dirname(os.path.abspath(__file__))
TESTPATH = os.path.join(os.path.dirname(DIRPATH), 'test')
TEMPPATH = os.path.join(os.path.dirname(DIRPATH), 'temp')
ICONSPATH = os.path.join(os.path.dirname(DIRPATH), 'resource', 'icons')
THUMBPATH = os.path.join(os.path.dirname(DIRPATH), 'resource', 'thumbnail')
DEFAULTTHUMBNAIL = os.path.join(ICONSPATH, 'thumbnail2.png')
TESTTHUMBNAIL = os.path.join(THUMBPATH, 'thumbnail.0000.jpg')

WINNAME = 'axelItemWindowUI'
THUMBWIDTH = 256
THUMBHEIGHT = 256


class Componet(object):
	animation = 'animation'
	pose = 'pose'
	thumbnail = 'thumbnail'
	sequence = 'sequence'


class Icon(object):
	default = os.path.join(ICONSPATH, 'ic_leak_remove_white_48dp.png')
	animation = os.path.join(ICONSPATH, 'image.png')
	pose = os.path.join(ICONSPATH, 'icon_white_256.png')


########################################################################################################################
#
#
#	DELEGATES
#
#
########################################################################################################################

class ItemDelegate(QItemDelegate):
	def __init__(self, *args, **kwargs):
		QItemDelegate.__init__(self, *args, **kwargs)

		self.thumbnailRole = Qt.UserRole + 100
		self.headerRole = Qt.UserRole + 101
		self.textRole = Qt.UserRole + 102
		self.iconRole = Qt.UserRole + 103

	def sizeHint(self, option, index):
		icon = QIcon(index.data(self.iconRole))
		iconsize = QSize(icon.actualSize(option.decorationSize))

		font = QFont()
		fm = QFontMetrics(font)
		return QSize(iconsize.width(), iconsize.height() + fm.height() + 8)

	def paint(self, painter, option, index):
		super(ItemDelegate, self).paint(painter, option, index)
		painter.save()

		font = QFont()
		subFont = QFont()
		fm = QFontMetrics(font)

		icon = QIcon(index.data(self.iconRole))
		iconsize = QSize(icon.actualSize(option.decorationSize))

		headerText = index.data(self.headerRole)
		subText = index.data(self.textRole)

		headerRect = QRect(option.rect)
		subheaderRect = QRect(option.rect)
		iconRect = QRect(subheaderRect)
		iconRect.setRight(iconsize.width() + 30)
		iconRect.setTop(iconRect.top() + 5)
		headerRect.setLeft(iconRect.right())
		subheaderRect.setLeft(iconRect.right())
		headerRect.setTop(headerRect.top() + 5)
		headerRect.setBottom(headerRect.top() + fm.height())
		subheaderRect.setTop(headerRect.bottom() + 2)

		painter.drawPixmap(
				QPoint(iconRect.left() + iconsize.width() / 2 + 2, iconRect.top() + iconsize.height() / 2 + 3),
				icon.pixmap(iconsize.width(), iconsize.height()))
		painter.setFont(font)
		painter.drawText(headerRect, headerText)
		painter.setFont(subFont)
		painter.drawText(subheaderRect.left(), subheaderRect.top() + 17, subText)
		painter.restore()
		return


########################################################################################################################
#
#
#	MODEL
#
#
########################################################################################################################

class ItemModel(QStandardItemModel):
	def __init__(self, *args, **kwargs):
		QStandardItemModel.__init__(self, *args, **kwargs)

		self.items = {}

	def add(self):
		return

	def remove(self):
		return

	def getItems(self):
		return [x for x in self.items]


########################################################################################################################
#
#
#	VIEW
#
#
########################################################################################################################

class ItemListView(QListView):
	def __init__(self, *args, **kwargs):
		QListView.__init__(self, *args, **kwargs)

		# Variables
		self.items = {}

		# Model
		self.setModel(ItemModel())

		# Delegate
		self.delegate = ItemDelegate()
		self.setItemDelegate(self.delegate)

		# Settings
		# self.setFocusPolicy(Qt.NoFocus)
		self.setFrameShape(QFrame.NoFrame)
		self.setEditTriggers(False)
		self.setContextMenuPolicy(Qt.CustomContextMenu)
		# self.setViewMode(QListView.IconMode)

		# Slots
		# self.clicked[QModelIndex].connect(self.getSelected)
		# self.customContextMenuRequested.connect(self.popupMenu)
		# self.model().itemChanged.connect(self.rename)

		for x in range(10):
			name = 'Name {}'.format(x)
			kind = Componet.animation
			text = 'Info'
			self.add(name, kind, text)

	def add(self, name, kind=Componet.animation, text=''):
		item = QStandardItem()

		if kind == Componet.animation:
			icon = QIcon(Icon.animation)
		elif kind == Componet.pose:
			icon = QIcon(Icon.pose)
		else:
			icon = QIcon(Icon.default)

		thumbnail = QIcon(TESTTHUMBNAIL)

		item.setData(name, self.delegate.headerRole)
		item.setData(icon, self.delegate.iconRole)
		item.setData(text, self.delegate.textRole)
		item.setData(thumbnail, self.delegate.thumbnailRole)
		self.model().appendRow(item)
		return

	def remove(self):
		return

	def getItems(self):
		return [x for x in self.items]


########################################################################################################################
#
#
#	LABEL
#
#
########################################################################################################################

class ElidedLabel(QLabel):
	def paintEvent(self, event):
		painter = QPainter(self)
		metrics = QFontMetrics(self.font())
		elided = metrics.elidedText(self.text(), Qt.ElideRight, self.width())
		painter.drawText(self.rect(), self.alignment(), elided)


########################################################################################################################
#
#
#	THUMBNAIL
#
#
########################################################################################################################

class ThumbnailWidget(QFrame):
	stateChanged = Signal(str)
	frameChanged = Signal(int)
	clicked = Signal(bool)
	pressed = Signal(bool)
	released = Signal(bool)
	toggled = Signal(bool)

	def __init__(self, filepath=DEFAULTTHUMBNAIL, *args, **kwargs):
		QFrame.__init__(self, *args, **kwargs)

		self.filepath = filepath
		self.createEnabled = False
		self.sequence = None
		self.currentState = None
		self.isPlaying = False
		self.start = 0
		self.duration = 100
		self.frameRate = 41.667
		self.currentFrame = 0
		self.defaultPixmap = QPixmap(DEFAULTTHUMBNAIL)
		self.currentPixmap = QPixmap(self.filepath)
		self.isLoop = True
		self.imageCache = []
		self.hover = False
		self.isScrubbing = False
		self.hasSequence = False

		# Widget
		self.setMouseTracking(True)
		self.setStyleSheet('''
							background:black;
							padding:0;
							margin:0;
							''')

		# Layout
		self.setLayout(QVBoxLayout())
		self.layout().setSpacing(0)
		self.layout().setContentsMargins(0, 0, 0, 0)

		# Label
		self.label = QLabel()
		self.label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
		self.label.setPixmap(self.currentPixmap)
		self.label.setAlignment(Qt.AlignCenter)
		self.layout().addWidget(self.label)

		# Progress Bar
		self.progressBar = QProgressBar()
		self.progressBar.setTextVisible(False)
		self.progressBar.setFixedHeight(5)
		self.progressBar.setRange(0, 100)
		self.progressBar.setValue(0)
		self.progressBar.setStyleSheet('''
										QProgressBar{
										background:transparent;
										border:none;
										border-radius:0;
										padding:0;
										margin:0;
										}
										QProgressBar::chunk{
										background:#269bc4;
										padding:0;
										margin:0;
										border:none;
										}
										''')
		self.layout().addWidget(self.progressBar)

		# Timeline for Sequences
		self.timeline = QTimeLine(1000, self)
		self.timeline.setFrameRange(self.start, self.duration)
		self.timeline.setCurveShape(QTimeLine.LinearCurve)
		self.timeline.setEasingCurve(QEasingCurve.Linear)
		self.timeline.setUpdateInterval(0)
		self.timeline.setLoopCount(0)
		self.stop()

		self.timeline.frameChanged.connect(self.setSequence)
		self.timeline.frameChanged.connect(self.progressBar.setValue)
		self.timeline.stateChanged.connect(self.setState)

	def getFilepath(self):
		return self.filepath

	def setFilepath(self, filepath):
		self.filepath = filepath
		return

	def clear(self):
		self.updatePixmap(self.defaultPixmap)
		self.setHasSequence(False)
		self.sequence = None
		self.progressBar.setValue(0)
		return

	def getHasSequence(self):
		return self.hasSequence

	def setHasSequence(self, bool):
		self.hasSequence = bool
		return

	def convertPositionToValue(self, position):
		width = self.size().width()
		return int((float(self.duration + 1) / float(width)) * float(position))

	def play(self):
		if self.sequence:
			self.timeline.start()
		return

	def stop(self):
		self.timeline.stop()
		return

	def pause(self):
		self.timeline.setPaused(True)
		return

	def unPause(self):
		self.timeline.setPaused(False)
		return

	def scrub(self, position):
		if self.sequence:
			self.pause()
			frame = self.convertPositionToValue(position)
			self.jumpToFrame(frame)
			self.isScrubbing = True
		return

	def mousePressEvent(self, event):
		if self.hasSequence:
			self.scrub(event.pos().x())
		return

	def mouseReleaseEvent(self, event):
		if self.isScrubbing:
			self.isScrubbing = False

			frame = self.currentFrame + 1
			if frame > self.duration:
				frame = 0

			self.setSequence(frame)
			self.timeline.frameChanged.emit(frame)
			self.unPause()
		return

	def mouseMoveEvent(self, event):
		if self.hasSequence:
			xpos = event.pos().x()

			if self.size().width() >= xpos >= 0:
				self.scrub(xpos)
		return

	def enterEvent(self, event):
		self.setHover(True)
		if self.hasSequence:
			self.play()
		return

	def leaveEvent(self, event):
		self.setHover(False)
		if self.hasSequence:
			self.pause()
		return

	def getHover(self):
		return self.hover

	def setHover(self, value):
		self.hover = value
		return

	def setCreateEnabled(self, value):
		self.createEnabled = value
		return

	def getCreateEnabled(self):
		return self.createEnabled

	def getTimeline(self):
		return self.timeline

	def getLabel(self):
		return self.label

	def setState(self, state):
		self.currentState = state
		self.stateChanged.emit(state)
		self.fitToWindow()
		return

	def loadSequence(self, sequence):
		self.sequence = sequence
		end = len(sequence) - 1
		self.setRange(0, end)
		self.timeline.setDuration(end * self.frameRate)
		self.imageCache = []
		self.progressBar.setRange(0, end)

		for item in sequence:
			self.imageCache.append(QPixmap(item))

		self.setHasSequence(True)
		self.jumpToFrame(0)
		return

	def loadSequenceFromFilepath(self, filepath):
		sequence = collectSequenceFromFilepath(filepath)

		if len(sequence) > 0:
			self.loadSequence(sequence)
		else:
			self.updatePixmap(QPixmap(sequence[0]))
		return

	def updatePixmap(self, pixmap):
		self.label.setPixmap(pixmap)
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
		self.timeline.setDuration(self.duration)
		return

	def setStartFrame(self, value):
		self.start = value
		self.timeline.setStartFrame(value)
		return

	def setCurrentFrame(self, frame):
		self.currentFrame = frame
		return

	def setEndFrame(self, end):
		self.duration = end
		self.timeline.setEndFrame(end)
		return

	def setRange(self, start, end):
		self.start = start
		self.duration = end
		self.timeline.setFrameRange(start, end)
		return

	def valueChanged(self, value):
		print value
		return

	def jumpToFrame(self, frame):
		self.setSequence(frame)
		self.timeline.frameChanged.emit(frame)
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
			w = self.label.width()
			h = self.label.height()
			pixmap = self.currentPixmap
			self.label.setPixmap(pixmap.scaled(w, h, Qt.KeepAspectRatio))
		return

	def playPause(self):
		if self.currentState in [QTimeLine.NotRunning, QTimeLine.Paused]:
			self.timeline.setPaused(False)
		else:
			self.timeline.setPaused(True)
		return

	def resizeEvent(self, event):
		self.fitToWindow()
		return


class ThumbnailButton(ThumbnailWidget):
	selected = Signal(object)

	def __init__(self,
	             name='Item',
	             filepath=DEFAULTTHUMBNAIL,
	             instance=None,
	             size=200,
	             *args,
	             **kwargs):
		ThumbnailWidget.__init__(self, filepath=filepath, *args, **kwargs)

		# Settings
		self.name = name
		self.instance = instance
		self.isSelected = False

		progressBarSize = 2
		headerSize = 20
		self.sizeOffset = progressBarSize + headerSize
		self.setSize(size)

		# Progress Bar
		self.progressBar.setFixedHeight(2)

		# Sub Widget
		self.subWidget = QFrame()
		self.subWidget.setLayout(QHBoxLayout())
		self.subWidget.layout().setSpacing(5)
		self.subWidget.layout().setContentsMargins(5, 0, 5, 5)
		self.subWidget.setMinimumSize(size - 5, headerSize)
		self.subWidget.setMaximumSize(size - 5, headerSize)
		self.layout().addWidget(self.subWidget)
		self.subWidget.setStyleSheet('background:#393939;color:white;')

		# Header
		self.header = ElidedLabel()
		self.header.setText(self.name)
		self.header.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		self.subWidget.layout().addWidget(self.header)

		# Style
		self.setStyleSheet('''
							ThumbnailButton{
							background:#393939;
							border:2 solid #393939;
							}
							ThumbnailButton[selected="true"]{
							background:#393939; 
							border:2 solid #269bc4;
							}
							''')

	def setName(self, name):
		self.header.setText(name)
		self.name = name
		return

	def setSize(self, size):
		self.setMaximumSize(size, size + self.sizeOffset)
		self.setMinimumSize(size, size + self.sizeOffset)
		return

	def mousePressEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.setSelected(True if not self.isSelected else False)
		return

	def getIsSelected(self):
		return self.isSelected

	def setSelected(self, bool):
		self.isSelected = bool
		self.setProperty('selected', self.isSelected)
		self.style().polish(self)

		if self.isSelected:
			self.selected.emit(self.instance)
		return


class ThumbnailButton2(QFrame):
	selected = Signal(bool)

	def __init__(self,
	             name='Item',
	             filepath=DEFAULTTHUMBNAIL,
	             instance=None,
	             size=200,
	             *args,
	             **kwargs):
		QFrame.__init__(self, *args, **kwargs)

		# Settings
		self.name = name
		self.filepath = filepath
		self.instance = instance
		self.isSelected = False

		progressBarSize = 2
		headerSize = 20
		self.sizeOffset = progressBarSize + headerSize

		self.setMouseTracking(True)
		self.setMaximumSize(size, size + self.sizeOffset)
		self.setMinimumSize(size, size + self.sizeOffset)

		# Layout
		self.setLayout(QVBoxLayout())
		self.layout().setSpacing(0)
		self.layout().setContentsMargins(0, 0, 0, 0)

		self.thumbnail = QLabel()
		self.thumbnailPixmap = QPixmap(filepath)
		self.thumbnail.setPixmap(self.thumbnailPixmap)
		self.thumbnail.setAlignment(Qt.AlignCenter)
		self.thumbnail.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
		self.layout().addWidget(self.thumbnail)

		# Progress Bar
		self.progressBar = QProgressBar()
		self.progressBar.setTextVisible(False)
		self.progressBar.setFixedHeight(2)
		self.progressBar.setStyleSheet('''
										QProgressBar{
										background:transparent;
										border:none;
										border-radius:0;
										padding:0;
										margin:0;
										}
										QProgressBar::chunk{
										background:#269bc4;
										padding:0;
										margin:0;
										border:none;
										}
										''')
		self.progressBar.setRange(0, 100)
		self.progressBar.setValue(0)
		self.layout().addWidget(self.progressBar)

		# Sub Widget
		self.subWidget = QFrame()
		self.subWidget.setLayout(QHBoxLayout())
		self.subWidget.layout().setSpacing(5)
		self.subWidget.layout().setContentsMargins(5, 0, 5, 5)
		self.subWidget.setMinimumSize(size - 5, headerSize)
		self.subWidget.setMaximumSize(size - 5, headerSize)
		self.layout().addWidget(self.subWidget)

		# Icon
		# self.icon = QLabel('ANIM')
		# self.icon.setObjectName('itemLabel')
		# self.icon.setMaximumSize(20, 20)
		# self.icon.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
		# self.subWidget.layout().addWidget(self.icon)
		# self.icon.setStyleSheet('background:#269bc4; color:white; font-size:8px; font-style:bold; letter-spacing:3px')

		# Header
		self.header = ElidedLabel()
		self.header.setText(self.name)
		self.header.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		self.subWidget.layout().addWidget(self.header)

		# Style
		self.setStyleSheet('''
							ThumbnailButton{
							background:#393939;
							border:2 solid #393939;
							}
							ThumbnailButton[selected="true"]{
							background:#393939; 
							border:2 solid #269bc4;
							}
							''')
		self.subWidget.setStyleSheet('background:#393939;color:white;')

	def setName(self, name):
		self.header.setText(name)
		self.name = name
		return

	def setSize(self, size):
		self.setMaximumSize(size, size + self.sizeOffset)
		self.setMinimumSize(size, size + self.sizeOffset)
		return

	def fitToWindow(self):
		w = self.thumbnail.width()
		h = self.thumbnail.height()
		self.thumbnail.setPixmap(self.thumbnailPixmap.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation))
		return

	def resizeEvent(self, event):
		self.fitToWindow()
		return

	def mousePressEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.setSelected(True if not self.isSelected else False)
		return

	def getIsSelected(self):
		return self.isSelected

	def setSelected(self, bool):
		self.isSelected = bool
		self.setProperty('selected', self.isSelected)
		self.style().polish(self)
		self.selected.emit(self.isSelected)
		return


########################################################################################################################
#
#
#	WINDOW
#
#
########################################################################################################################

class Window(QMainWindow):
	def __init__(self, *args, **kwargs):
		QMainWindow.__init__(self, *args, **kwargs)

		# Layout
		self.widget = QWidget()
		self.widget.setLayout(QVBoxLayout())
		self.setCentralWidget(self.widget)

		thumbnail = ThumbnailButton()
		self.widget.layout().addWidget(thumbnail)

		thumbnail.selected.connect(self.callback)

	def callback(self, instance):
		print instance
		return


########################################################################################################################
#
#
#	STANDALONE
#
#
########################################################################################################################

def standalone(name=WINNAME, title=WINNAME):
	app = QApplication(sys.argv)
	window = Window()
	window.setObjectName(name)
	window.setWindowTitle(title)
	window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	standalone()
