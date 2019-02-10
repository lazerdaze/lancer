# Lancer Modules
from library.mathUtils import setRange

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


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
#	ComboBox
#
#
########################################################################################################################

class ComboBox(QComboBox):
	def __init__(self, *args, **kwargs):
		QComboBox.__init__(self, *args, **kwargs)

		self.listView = QListView()
		self.listView.setFocusPolicy(Qt.NoFocus)
		self.setView(QListView())
		self.setFocusPolicy(Qt.NoFocus)
		self.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)


########################################################################################################################
#
#
#	ToolButton
#
#
########################################################################################################################

class ToolButton(QToolButton):
	def __init__(self, offFilepath=None, onFilepath=None, isCheckable=False, *args, **kwargs):
		QToolButton.__init__(self, *args, **kwargs)
		self.onFilepath = onFilepath
		self.offFilepath = offFilepath if offFilepath else iconsPath.logoSmall
		self.isCheckable = isCheckable
		self.isActive = False
		self.defaultOpacity = 0.75
		self.hoverOpacity = 1
		self.painter = None

		self.offPixmap = QPixmap(self.offFilepath)
		if self.onFilepath:
			self.onPixmap = QPixmap(self.onFilepath)
		self.pixmap = self.offPixmap
		self.updatePaintEvent(self.defaultOpacity)

		self.clicked.connect(self.setActive)

	def getIsActive(self):
		return self.isActive

	def setIsActive(self, value):
		self.isActive = value
		return

	def getIsCheckable(self):
		return self.isCheckable

	def setIsCheckable(self, value):
		self.isCheckable = value
		return

	def setActive(self):
		if self.offFilepath and self.onFilepath:
			if self.isCheckable:
				self.isActive = not self.isActive

				if self.isActive:
					self.pixmap = self.onPixmap
				else:
					self.pixmap = self.offPixmap

				self.updatePaintEvent(self.defaultOpacity)
		return self.isActive

	def updatePaintEvent(self, opacity):
		result = QPixmap(self.pixmap.size())
		result.fill(Qt.transparent)

		self.painter = QPainter(result)
		self.painter.setOpacity(opacity)
		self.painter.drawPixmap(0, 0, self.pixmap)
		self.painter.end()
		self.setIcon(QIcon(result))
		self.setIconSize(QSize(25, 25))
		return

	def enterEvent(self, event):
		self.updatePaintEvent(self.hoverOpacity)
		return

	def leaveEvent(self, event):
		self.updatePaintEvent(self.defaultOpacity)
		return


########################################################################################################################
#
#
#	TIMELINE
#
#
########################################################################################################################

class TimeLine(QTimeLine):
	def __init__(self, *args, **kwargs):
		QTimeLine.__init__(self, *args, **kwargs)

		self.startFrame = 0
		self.endFrame = 100
		self.frameRate = 41.667
		self.currentFrame = 0

		self.setRange(self.startFrame, self.endFrame)
		self.setCurveShape(QTimeLine.LinearCurve)
		self.setEasingCurve(QEasingCurve.Linear)
		self.setUpdateInterval(0)
		self.setLoopCount(0)

	def play(self):
		self.resume()
		return

	def pause(self):
		self.setPaused(True)
		return

	def setRange(self, start, end):
		self.startFrame = start
		self.endFrame = end
		self.setFrameRange(self.startFrame, self.endFrame)
		self.setDuration(float(self.endFrame) * float(self.frameRate))
		return


########################################################################################################################
#
#
#	ProgressBar
#
#
########################################################################################################################

class CircularProgressBar(QWidget):
	valueChanged = Signal(float)
	stateChanged = Signal(str)
	currentProgress = Signal(float)

	def __init__(self, value=100, minValue=0, maxValue=100, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)

		self._value = float(value)
		self.minValue = float(minValue)
		self.maxValue = float(maxValue)

		self._state = None

		self.innerRadius = 0.6
		self.outerRadius = 1.0

		self.startColor = [255, 0, 0]
		self.midColor = [255, 255, 0]
		self.endColor = [0, 255, 0]

		self.backgroundColor = Qt.lightGray
		self.borderColor = QColor(0, 0, 0, 60)

		self.updateState(self._value)

	def abort(self, value):
		if value:
			self.state = 'abort'
		return

	def color(self):
		# Start To Mid
		start = self.startColor
		mid = self.midColor
		end = self.endColor
		result = []

		midValue = float(self.maxValue / 2.0)

		# Start To Mid
		if self.value < midValue:
			for x in range(3):
				newValue = setRange(value=self.value,
				                    oldMin=self.minValue,
				                    oldMax=midValue,
				                    newMin=start[x],
				                    newMax=mid[x]
				                    )
				result.append(newValue)

		# Mid
		elif self.value == midValue:
			result = mid

		# Mid To End
		elif self.value > midValue:
			for x in range(3):
				newValue = setRange(value=self.value,
				                    oldMin=midValue,
				                    oldMax=self.maxValue,
				                    newMin=mid[x],
				                    newMax=end[x]
				                    )
				result.append(newValue)


		return QColor(result[0], result[1], result[2])

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		value = float(value)

		if value < self.minValue:
			value = self.minValue
		elif value > self.maxValue:
			value = self.maxValue

		if self.minValue <= value <= self.maxValue:
			self._value = float(value)
			self.valueChanged.emit(self._value)
			self.updateState(self._value)
			self.update()
		return

	def updateState(self, value):
		if value == self.minValue:
			self.state = 'initalized'
		elif value == self.maxValue:
			self.state = 'finished'
		else:
			self.state = 'working'
		return

	@property
	def state(self):
		return self._state

	@state.setter
	def state(self, state):
		self._state = state
		self.stateChanged.emit(self._state)
		return

	@staticmethod
	def squared(rect):
		if rect.width() > rect.height():
			diff = float(rect.width() - rect.height())
			return rect.adjusted(diff / 2, 0, -diff / 2, 0)
		else:
			diff = float(rect.height() - rect.width())
			return rect.adjusted(0, diff / 2, 0, -diff / 2)

	def paintEvent(self, event):
		pixmap = QPixmap(self.squared(self.rect()).size())
		pixmap.fill(QColor(0, 0, 0, 0))

		painter = QPainter(pixmap)
		painter.setRenderHint(QPainter.Antialiasing)

		rect = QRectF(pixmap.rect().adjusted(1, 1, -1, -1))
		margin = float(rect.width() * (1.0 - self.outerRadius) / 2.0)
		rect.adjust(margin, margin, -margin, -margin)
		innerRadius = float(self.innerRadius * rect.width() / 2.0)

		if self.state == 'working':
			# Background
			painter.setBrush(self.backgroundColor)
			painter.setPen(self.borderColor)
			painter.drawPie(rect, 0, 360 * 16)

			# Progress
			painter.setBrush(self.color())
			painter.setPen(self.color())

			value = min(self.value, self.maxValue)
			startAngle = 90 * 16
			spanAngle = float(-value) * 360 * 16 / self.maxValue
			painter.drawPie(rect, startAngle, spanAngle)

			# inner circle and frame
			painter.setBrush(QColor(255, 255, 255))
			painter.setPen(QColor(255, 255, 255))
			painter.drawEllipse(rect.center(), innerRadius, innerRadius)

			# outer frame
			painter.drawArc(rect, 0, 360 * 16)

		elif self.state == 'abort':
			color = QColor(self.startColor[0], self.startColor[1],self.startColor[2])

			# Progress
			painter.setBrush(color)
			painter.setPen(color)

			value = min(self.value, self.maxValue)
			startAngle = 90 * 16
			spanAngle = float(-value) * 360 * 16 / self.maxValue
			painter.drawPie(rect, startAngle, spanAngle)

		elif self.state == 'initalized':
			# inner circle and frame
			painter.setBrush(self.color())
			painter.setPen(self.color())
			painter.drawEllipse(rect.center(), innerRadius, innerRadius)

		elif self.state == 'finished':
			# inner circle and frame
			painter.setBrush(self.color())
			painter.setPen(self.color())
			painter.drawPie(rect, 0, 360 * 16)

		painter = QPainter(self)
		painter.drawPixmap(0.5 * (self.width() - pixmap.width()), 0.5 * (self.height() - pixmap.height()), pixmap)
		return


if __name__ == '__main__':
	import sys

	app = QApplication(sys.argv)
	control = CircularProgressBar()
	control.abort(True)
	control.show()
	sys.exit(app.exec_())





