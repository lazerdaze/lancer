# Project Modules
from widgets import Icon_Tool_Button, Settings_Tool_Button, Header_Widget

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Settings_Widget(QWidget):
	def __init__(self, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)
		
		# Size Policy
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)
		
		# Layout
		self.setLayout(QVBoxLayout())
		self.layout().setSpacing(0)
		self.layout().setContentsMargins(0, 0, 0, 0)
		
		# Header Widget
		self.widget_header = Header_Widget()
		self.layout().addWidget(self.widget_header)
		
		
		#
		self.scrollArea = QScrollArea(self)
		self.scrollArea.setWidgetResizable(True)
		self.scrollAreaWidgetContents = QWidget()
		self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 402, 552))
		self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
	
		spacerItem = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)
		self.verticalLayout_5.addItem(spacerItem)
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.layout().addWidget(self.scrollArea)


if __name__ == "__main__":
	pass
