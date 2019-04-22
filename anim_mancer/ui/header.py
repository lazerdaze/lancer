# Project Modules
from anim_mancer.utils import *
from widgets import Settings_Tool_Button

# Python Modules
import os
from os import path

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


# ======================================================================================================================
#
#
# Class
#
#
# ======================================================================================================================

class Header_Widget(QWidget):
	def __init__(self, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)
		# Main
		self.setLayout(QVBoxLayout())
		self.layout().setSpacing(0)
		self.layout().setContentsMargins(0, 0, 0, 0)
		
		# Header
		self.frame_header = QFrame()
		self.frame_header.setLayout(QHBoxLayout())
		self.frame_header.layout().setSpacing(5)
		self.frame_header.layout().setContentsMargins(5, 5, 5, 5)
		self.layout().addWidget(self.frame_header)
		
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.frame_header.setSizePolicy(sizePolicy)
		self.frame_header.setMinimumSize(QSize(200, 20))
		self.frame_header.setMaximumSize(QSize(16777215, 16777215))
		
		# Logo
		self.label_logo = QLabel()
		self.label_logo.setMinimumSize(QSize(114, 14))
		self.label_logo.setPixmap(QPixmap(IconPath.logo))
		self.frame_header.layout().addWidget(self.label_logo)
		
		# Settings Button
		self.button_settings = Settings_Tool_Button(self)
		self.frame_header.layout().addWidget(self.button_settings)
		
		# Style Sheet
		self.frame_header.setStyleSheet('background:black;')
		

# ======================================================================================================================
#
#
# Execute
#
#
# ======================================================================================================================

if __name__ == '__main__':
	pass
