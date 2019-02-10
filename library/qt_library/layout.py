# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

########################################################################################################################
#
#
#	Global Variables
#
#
########################################################################################################################

SPACING = 3
MARGIN = 10
COLUMN = 60


########################################################################################################################
#
#
#	Base Widget Classes
#
#
########################################################################################################################

class BaseWidget(object):

	def addWidget(self, widget):
		return self.layout().addWidget(widget)

	def addLayout(self, layout):
		return self.layout().addLayout(layout)


class Widget(BaseWidget, QWidget):
	def __init__(self, *args, **kwargs):
		BaseWidget.__init__(self)
		QWidget.__init__(self, *args, **kwargs)


class Frame(BaseWidget, QFrame):
	def __init__(self, *args, **kwargs):
		BaseWidget.__init__(self)
		QFrame.__init__(self, *args, **kwargs)


class GroupBox(BaseWidget, QGroupBox):
	def __init__(self, *args, **kwargs):
		BaseWidget.__init__(self)
		QGroupBox.__init__(self, *args, **kwargs)


########################################################################################################################
#
#
#	VERTICAL
#
#
########################################################################################################################

class VerticalWidget(Widget):
	def __init__(self, *args, **kwargs):
		Widget.__init__(self, *args, **kwargs)

		# Layout
		self.setLayout(QVBoxLayout())
		self.layout().setSpacing(0)
		self.layout().setContentsMargins(0, 0, 0, 0)


class VerticalFrame(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)

		# Layout
		self.setLayout(QVBoxLayout())
		self.layout().setSpacing(SPACING)
		self.layout().setContentsMargins(MARGIN, MARGIN, MARGIN, MARGIN)


class VerticalGroupBox(GroupBox):
	def __init__(self, *args, **kwargs):
		GroupBox.__init__(self, *args, **kwargs)

		# Layout
		self.setLayout(QVBoxLayout())
		self.layout().setSpacing(0)
		self.layout().setContentsMargins(0, 0, 0, 0)


########################################################################################################################
#
#
#	HORIZONTAL
#
#
########################################################################################################################

class HorizontalWidget(Widget):
	def __init__(self, *args, **kwargs):
		Widget.__init__(self, *args, **kwargs)

		# Layout
		self.setLayout(QHBoxLayout())
		self.layout().setSpacing(0)
		self.layout().setContentsMargins(0, 0, 0, 0)


class HorizontalFrame(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)

		# Layout
		self.setLayout(QHBoxLayout())
		self.layout().setSpacing(SPACING)
		self.layout().setContentsMargins(MARGIN, MARGIN, MARGIN, MARGIN)


class HorizontalGroupBox(GroupBox):
	def __init__(self, *args, **kwargs):
		GroupBox.__init__(self, *args, **kwargs)

		# Layout
		self.setLayout(QHBoxLayout())
		self.layout().setSpacing(0)
		self.layout().setContentsMargins(0, 0, 0, 0)


########################################################################################################################
#
#
#	TAB
#
#
########################################################################################################################

class TabWidget(QTabWidget):
	def __init__(self, *args, **kwargs):
		QTabWidget.__init__(self, *args, **kwargs)

		# Settings
		self.setCurrentIndex(0)
