# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class CustomItem(object):
	def __init__(self, *args, **kwargs):
		pass


class CustomItemModel(QAbstractItemModel):
	def __init__(self, *args, **kwargs):
		QAbstractItemModel.__init__(self, *args, **kwargs)
