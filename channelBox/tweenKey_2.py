# Python Modules
import sys

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


########################################################################################################################
#
#
#	Widget
#
#
########################################################################################################################

class TweenKeyWidget(QWidget):
	keyColor = Qt.red
	lineColor = Qt.darkGray

	barColor = Qt.black
	handleColor = Qt.red

	margin = 15.0
	keyWidth = 3.0

	barHeight = 5.0
	handleHeight = 10.0
	handleWidth = 10.0

	valueChanged = Signal(float)

	def __init__(self, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)

		self.keyValues = [0, 25, 50, 75, 100]
		self.values = [0, 6.25, 12.5, 25, 50, 75, 87.5, 93.75, 100]
		self.currentValue = 50

		# Setting
		self.setMouseTracking(True)
		self.setMinimumHeight(self.handleHeight + (self.margin * 2))

	def setCurrentValue(self, value):
		self.currentValue = value
		self.valueChanged.emit(float(value) / 100.0)
		return

	@staticmethod
	def convertPositionToValue(maxWidth, maxValue, position):
		return int((float(maxValue) / float(maxWidth)) * float(position))

	@staticmethod
	def convertValueToWidth(maxWidth, maxValue, value):
		return (float(maxWidth) * float(value)) / float(maxValue)

	def drawBar(self, painter):
		# Bar
		barRect = QRect(float(self.margin),
		                (self.height() / 2.0) - (float(self.barHeight) / 2.0),
		                self.width() - (float(self.margin) * 2.0),
		                self.barHeight,
		                )

		painter.setBrush(QBrush(self.barColor))
		painter.setPen(QPen(self.barColor))
		painter.drawRect(barRect)
		return

	def drawHandle(self, painter):
		xPos = self.convertValueToWidth(self.width(), max(self.values), self.currentValue)
		painter.setBrush(QBrush(self.handleColor))
		painter.setPen(QPen(self.handleColor))
		# painter.drawEllipse(QPoint(xPos,
		#                            self.height() / 2.0),
		#                     self.handleWidth,
		#                     self.handleHeight,
		#                     )

		centerX = xPos
		centerY = self.height() / 2.0

		points = [QPoint(xPos - (self.handleWidth / 2.0), centerY - (self.handleHeight / 2.0)),
		          QPoint(xPos - (self.handleWidth / 2.0), centerY + (self.handleHeight / 2.0)),
		          QPoint(xPos + (self.handleWidth / 2.0), centerY + (self.handleHeight / 2.0)),
		          QPoint(xPos + (self.handleWidth / 2.0), centerY - (self.handleHeight / 2.0)),
		          QPoint(xPos, centerY - self.handleHeight),
		          ]
		polygon = QPolygon(points)
		painter.drawPolygon(polygon)

		return

	def drawKeys(self, painter):
		for value in self.values:
			index = self.values.index(value)

			if self.values[index] == self.values[0]:
				x = self.handleWidth
			elif self.values[index] == self.values[-1]:
				x = self.width() - float(self.handleWidth) - 1
			else:
				x = self.convertValueToWidth(self.width(), max(self.values), value)

			# Text
			font = QFont('arial', 7)
			fontMetrics = QFontMetrics(font)
			fontWidth = fontMetrics.width(str(int(value)))
			fontHeight = fontMetrics.height()

			fontRect = QRect(0,
			                 0,
			                 fontWidth,
			                 fontHeight,
			                 )

			fontRect.moveCenter(QPoint(x, fontHeight / 2))

			painter.setFont(font)
			painter.setPen(QPen(Qt.white if value in self.keyValues else self.lineColor))
			painter.drawText(fontRect, str(int(value)))

			# Line
			painter.setPen(QPen(self.keyColor if value in self.keyValues else self.lineColor,
			                    3 if value in self.keyValues else 1,
			                    Qt.SolidLine,
			                    Qt.SquareCap,
			                    ))
			painter.drawLine(x, self.margin + (fontHeight / 2), x, (self.height() / 2.0) - self.margin)
			painter.drawLine(x, (self.height() / 2.0) + self.margin, x, self.height())

			# Circle
			# painter.setBrush(QBrush(self.barColor))
			# painter.setPen(QPen(self.barColor))
			# painter.drawEllipse(QPoint(x, self.height() / 2.0), self.handleWidth * 0.75, self.handleHeight * 0.75)
		return

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing)
		painter.setRenderHint(QPainter.HighQualityAntialiasing)
		#self.drawKeys(painter)
		self.drawBar(painter)
		self.drawHandle(painter)
		return

	def mousePressEvent(self, event):
		postion = event.pos()
		xPos = postion.x()

		value = self.convertPositionToValue(self.width(), max(self.values), xPos)
		self.setCurrentValue(value)
		self.update()
		return

	def mouseMoveEvent(self, event):

		if event.buttons() == Qt.LeftButton:
			postion = event.pos()
			xPos = postion.x()

			value = self.convertPositionToValue(self.width(), max(self.values), xPos)
			self.setCurrentValue(value)
			self.update()
		return


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QMainWindow()

	window.setCentralWidget(TweenKeyWidget())
	window.setStyleSheet('background:rgb(75,75,75);')

	window.show()
	sys.exit(app.exec_())
