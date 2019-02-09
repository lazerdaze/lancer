# Lancer Modules
from utils import *

# Python Modules
import sys

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


@standaloneMayaWrapper
class Window(QMainWindow):
	def __init__(self, parent=None, name='QTWindowUI', title='Qt WIndow', *args, **kwargs):
		QMainWindow.__init__(self, parent=parent, *args, **kwargs)

		self.setObjectName(name)
		self.setWindowTitle(title)

	def closeEvent(self, event):
		QMainWindow.closeEvent(self, event)
		return


if __name__ == "__main__":
	Window(title='Test Window')
