# Project Modules

# Python Modules

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


# ======================================================================================================================
#
#
# Class
#
#
# ======================================================================================================================

class Custom_Widget(QWidget):
	def __init__(self, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)
		
		self.setLayout(QVBoxLayout())
		
		# Test
		button = QPushButton('Test')
		self.layout().addWidget(button)



if __name__ == '__main__':
	pass
