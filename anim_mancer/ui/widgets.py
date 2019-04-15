# Project Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from color import USER_COLOR, DIVIDER_COLOR
from anim_mancer.utils import *

# Python Modules
import os
from os import path

# Python Modules
import difflib

# Maya Modules
from maya import OpenMaya, OpenMayaUI, cmds

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import shiboken2 as shiboken

# ======================================================================================================================
#
#
# Global
#
#
# ======================================================================================================================

CHANNELBOX_PLUS = None

DIR_PATH = path.dirname(os.path.abspath(__file__))
RESOURCE_PATH = path.join(DIR_PATH, 'resource')
ICON_GEAR = path.join(RESOURCE_PATH, 'icon_gear.png')
ICON_LOGO = path.join(RESOURCE_PATH, 'icon_logo.png')


# ======================================================================================================================
#
#
# Function
#
#
# ======================================================================================================================

def install_channelbox_search(threshold=0.75):
	"""
	Add the search interface and colouring functionality to Maya's main
	channel box. If channelBoxPlus is already installed a RuntimeError
	exception will be thrown. A threshold can be set, this threshold
	determines when the attributes should change colour. the higher the
	threshold the more the 2 attributes will have to match up to stay the same
	colour.

	:param float threshold: Threshold for attribute colour change
	:raises RuntimeError: When the channel box plus is already installed.
	"""
	global CHANNELBOX_PLUS
	
	# validate channel box plus
	if CHANNELBOX_PLUS:
		raise RuntimeError("Channel box plus is already installed!")
	
	# get channel box
	channelBox = get_channelbox()
	
	# get channel box layout
	parent = channelBox.parent()
	layout = parent.layout()
	layout.setSpacing(0)
	
	# initialize search widget
	CHANNELBOX_PLUS = ChannelBox_Search_Widget(parent, threshold)
	
	# add search widget to layout
	if type(layout) == QLayout:
		item = layout.itemAt(0)
		widget = item.widget()
		
		layout.removeWidget(widget)
		layout.addWidget(CHANNELBOX_PLUS)
		layout.addWidget(widget)
	else:
		layout.insertWidget(0, CHANNELBOX_PLUS)


# ======================================================================================================================
#
#
# Class
#
#
# ======================================================================================================================

class ChannelBox_Search_Widget(QWidget):
	def __init__(self, parent, threshold=0.75):
		# initialize
		QWidget.__init__(self, parent)
		self.setObjectName(CHANNELBOX_SEARCH)
		
		# variable
		self.threshold = threshold
		
		# set ui
		self.setMaximumHeight(30)
		
		# create layout
		layout = QHBoxLayout(self)
		layout.setContentsMargins(3, 5, 3, 5)
		layout.setSpacing(3)
		
		# create search widget
		self.edit = QLineEdit(self)
		self.edit.textChanged.connect(self.update)
		self.edit.setPlaceholderText("Search...")
		layout.addWidget(self.edit)
		
		# create clear widget
		button = QPushButton(self)
		button.setText("x")
		button.setFlat(True)
		button.setMinimumHeight(20)
		button.setMinimumWidth(20)
		button.released.connect(self.clear)
		layout.addWidget(button)
		
		# register callback
		self.id = self.registerCallback()
		self.update()
	
	# ------------------------------------------------------------------------
	
	def registerCallback(self):
		"""
		Register a callback to run the update function every time the
		selection list is modified.

		:return: Callback id
		:rtype: int
		"""
		return OpenMaya.MModelMessage.addCallback(
				OpenMaya.MModelMessage.kActiveListModified,
				self.update
		)
	
	def removeCallback(self):
		"""
		Remove the callback that updates the ui every time the selection
		list is modified.
		"""
		OpenMaya.MMessage.removeCallback(self.id)
	
	# ------------------------------------------------------------------------
	
	def deleteLater(self):
		"""
		Subclass the deleteLater function to first remove the callback,
		this callback shouldn't be floating around and should be deleted
		with the widget.
		"""
		self.removeCallback()
		QWidget.deleteLater(self)
	
	# ------------------------------------------------------------------------
	
	def update(self, *args):
		"""
		Update the main channel box with the input data, filter attributes
		based on the search term and colour user attributes.
		"""
		# get selected nodes
		nodes = cmds.ls(sl=True, l=True) or []
		
		# colour user attributes
		self.updateColour(nodes)
		
		# filter attributes
		string = self.edit.text()
		self.updateSearch(string, nodes)
		
		QWidget.update(self)
	
	# ------------------------------------------------------------------------
	
	def clear(self):
		"""
		Clear the text in the search line edit.
		"""
		self.edit.setText("")
	
	# ------------------------------------------------------------------------
	
	def matchSearch(self, attr, searchArguments):
		"""
		Check if all search arguments exist in the attribute string.

		:param str attr: Attribute channel name
		:param list searchArguments: List of arguments to match
		:return: Does attribute match with search arguments
		:rtype: bool
		"""
		return all([s in attr.lower() for s in searchArguments])
	
	def updateSearch(self, matchString, nodes):
		"""
		Loop over all keyable attributes and match them with the search string.

		:param str matchString: Search string to match with attributes
		:param list nodes: List of nodes to process the attributes from
		"""
		# reset of search string is empty
		if not matchString:
			cmds.channelBox(CHANNELBOX, edit=True, fixedAttrList=[])
			return
		
		# split match string
		matches = []
		matchStrings = matchString.lower().split()
		
		# get matching attributes
		for node in nodes:
			attrs = cmds.listAttr(node, k=True, v=True)
			
			for attr in attrs:
				if (
						not attr in matches and
						self.matchSearch(attr, matchStrings)
				):
					matches.append(attr)
		
		# append null if not matches are found ( cannot use empty list )
		if not matches:
			matches.append("null")
		
		# filter channel box
		cmds.channelBox(CHANNELBOX, edit=True, fixedAttrList=matches)
	
	# ------------------------------------------------------------------------
	
	def updateColour(self, nodes):
		"""
		Loop over the selected objects user defined attributes, and generate
		a colour for them, nodeRegex is not used because it slows down the
		displaying of the the Channel Box in scenes with many user defined
		attributes.

		:param list nodes: list of selected nodes
		"""
		for node in nodes:
			# get user defined attributes
			attrs = cmds.listAttr(node, userDefined=True) or []
			
			# set default colour indices
			mainColour, subColour = 0, 0
			
			# loop attributes
			for i, attr in enumerate(attrs):
				# get attribute state
				isLocked = cmds.getAttr("{0}.{1}".format(node, attr), l=True)
				isKeyable = cmds.getAttr("{0}.{1}".format(node, attr), k=True)
				
				# catch divider
				if isLocked or not isKeyable:
					# update colour indices
					mainColour += 1
					subColour = 0
					
					if mainColour == len(USER_COLOR):
						mainColour = 0
					
					# update colour
					cmds.channelBox(
							CHANNELBOX,
							edit=True,
							attrRegex=attr,
							attrBgColor=DIVIDER_COLOR
					)
					
					continue
				
				# match string with previous attribute to get sub colour
				if i != 0:
					# get match ratio
					ratio = difflib.SequenceMatcher(
							None,
							attr,
							attrs[i - 1]
					).ratio()
					
					# compare match ratio with threshold
					if ratio < self.threshold:
						subColour += 1
						
						if subColour == len(USER_COLOR[mainColour]):
							subColour = 0
				
				# update colour
				colour = USER_COLOR[mainColour][subColour]
				cmds.channelBox(
						CHANNELBOX,
						edit=True,
						attrRegex=attr,
						attrBgColor=colour
				)


class TabBarPlus(QTabBar):
	"""Tab bar that has a plus button floating to the right of the tabs."""
	
	plusClicked = Signal()
	
	def __init__(self):
		QTabBar.__init__(self)
		
		# Plus Button
		self.plusButton = QPushButton("+")
		self.plusButton.setParent(self)
		self.plusButton.setFixedSize(20, 20)  # Small Fixed size
		self.plusButton.clicked.connect(self.plusClicked.emit)
		self.movePlusButton()  # Move to the correct location
	
	# end Constructor
	
	def sizeHint(self):
		"""Return the size of the TabBar with increased width for the plus button."""
		sizeHint = QTabBar.sizeHint(self)
		width = sizeHint.width()
		height = sizeHint.height()
		return QSize(width + 25, height)
	
	# end tabSizeHint
	
	def resizeEvent(self, event):
		"""Resize the widget and make sure the plus button is in the correct location."""
		QTabBar.resizeEvent(self, event)
		
		self.movePlusButton()
	
	# end resizeEvent
	
	def tabLayoutChange(self):
		"""This virtual handler is called whenever the tab layout changes.
		If anything changes make sure the plus button is in the correct location.
		"""
		QTabBar.tabLayoutChange(self)
		
		self.movePlusButton()
	
	# end tabLayoutChange
	
	def movePlusButton(self):
		"""Move the plus button to the correct location."""
		# Find the width of all of the tabs
		size = sum([self.tabRect(i).width() for i in range(self.count())])
		# size = 0
		# for i in range(self.count()):
		#     size += self.tabRect(i).width()
		
		# Set the plus button location in a visible area
		h = self.geometry().top()
		w = self.width()
		if size > w:  # Show just to the left of the scroll buttons
			self.plusButton.move(w - 54, h)
		else:
			self.plusButton.move(size, h)


class Custom_Tab_Widget(QTabWidget):
	"""Tab Widget that that can have new tabs easily added to it."""
	
	def __init__(self):
		QTabWidget.__init__(self)
		
		# Tab Bar
		self.tab = TabBarPlus()
		self.setTabBar(self.tab)
		
		# Properties
		self.setMovable(True)
		self.setTabsClosable(True)
		
		# Signals
		self.tab.plusClicked.connect(self.addTab)
		self.tab.tabMoved.connect(self.moveTab)
		self.tabCloseRequested.connect(self.removeTab)


class Icon_Tool_Button(QToolButton):
	def __init__(self, parent, offFilepath, onFilepath=None, *args, **kwargs):
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


class Sliding_Stacked_Widget(QStackedWidget):
	animation_finished = Signal()
	
	def __init__(self, speed=500, animation=QEasingCurve.InOutCubic, vertical=False, wrap=False, *args, **kwargs):
		QStackedWidget.__init__(self, *args, **kwargs)
		
		self.vertical = vertical
		self.speed = speed
		self.animation_type = animation
		self.current = 0
		self.next = 0
		self.wrap = wrap
		self.pnow = QPoint(0, 0)
		self.active = False
	
	class direction(object):
		left_to_right = 'left to right'
		right_to_left = 'right to left'
		top_to_bottom = 'top to bottom'
		bottom_to_top = 'bottom to top'
		automatic = 'automatic'
	
	def set_wrap(self, wrap):
		self.wrap = wrap
		return
	
	def set_vertical(self, vertical):
		self.vertical = vertical
		return
	
	def set_speed(self, speed):
		self.speed = speed
		return
	
	def slide_in_next(self, *args, **kwargs):
		current = self.currentIndex()
		
		if self.wrap and current < self.count() - 1:
			self.slide_in_index(current + 1, self.direction.automatic)
		return
	
	def slide_in_prev(self, *args, **kwargs):
		current = self.currentIndex()
		
		if self.wrap and current > 0:
			self.slide_in_index(current - 1, self.direction.automatic)
		return
	
	def slide_in_index(self, index, direction='automatic'):
		if index > self.count() - 1:
			direction = self.direction.top_to_bottom if self.vertical else self.direction.right_to_left
			index = index % self.count()
		elif index < 0:
			direction = self.direction.bottom_to_top if self.vertical else self.direction.left_to_right
			index = (index + self.count()) % self.count()
		
		self.slide_in_widget(self.widget(index), direction)
		return
	
	def slide_in_widget(self, new_widget, direction, *args, **kwargs):
		if self.active:
			return
		else:
			self.active = True
		
		direction_hint = None
		current = self.currentIndex()
		next = self.indexOf(new_widget)
		
		if current == next:
			self.active = False
			return
		
		elif current < next:
			direction_hint = self.direction.top_to_bottom if self.vertical else self.direction.right_to_left
		
		else:
			direction_hint = self.direction.bottom_to_top if self.vertical else self.direction.left_to_right
		
		if direction == self.direction.automatic:
			direction = direction_hint
		
		offsetx = self.frameRect().width()
		offsety = self.frameRect().height()
		
		self.widget(next).setGeometry(0, 0, offsetx, offsety)
		
		if direction == self.direction.bottom_to_top:
			offsetx = 0
			offsety = - offsety
		
		elif direction == self.direction.top_to_bottom:
			offsetx = 0
		
		elif direction == self.direction.right_to_left:
			offsetx = - offsetx
			offsety = 0
		
		elif direction == self.direction.left_to_right:
			offsety = 0
		
		pnext = QPoint(self.widget(next).pos())
		pnow = QPoint(self.widget(current).pos())
		self.pnow = pnow
		
		self.widget(next).move(pnext.x() - offsetx, pnext.y() - offsety)
		self.widget(next).show()
		self.widget(next).raise_()
		
		animnow = QPropertyAnimation(self.widget(current), "pos")
		
		animnow.setDuration(self.speed)
		animnow.setEasingCurve(self.animation_type)
		animnow.setStartValue(QPoint(pnow.x(), pnow.y()))
		animnow.setEndValue(QPoint(offsetx + pnow.x(), offsety + pnow.y()))
		animnext = QPropertyAnimation(self.widget(next), "pos")
		animnext.setDuration(self.speed)
		animnext.setEasingCurve(self.animation_type)
		animnext.setStartValue(QPoint(-offsetx + pnext.x(), offsety + pnext.y()))
		animnext.setEndValue(QPoint(pnext.x(), pnext.y()))
		
		animgroup = QParallelAnimationGroup()
		
		animgroup.addAnimation(animnow)
		animgroup.addAnimation(animnext)
		animgroup.finished.connect(self.animation_done)
		
		self.next = next
		self.current = current
		self.active = True
		animgroup.start()
		return
	
	def animation_done(self, *args, **kwargs):
		self.setCurrentIndex(self.next)
		self.widget(self.current).hide()
		self.widget(self.current).move(self.pnow)
		self.active = False
		self.animation_finished.emit()
		return


class Settings_Tool_Button(Icon_Tool_Button):
	def __init__(self, parent, offFilepath=ICON_GEAR, *args, **kwargs):
		Icon_Tool_Button.__init__(self, parent, offFilepath=offFilepath, onFilepath=None, *args, **kwargs)
		self.setMinimumSize(QSize(25, 25))
		self.setMaximumSize(QSize(25, 25))
		self.setIconSize(QSize(25, 25))


class Header_Widget(QFrame):
	def __init__(self, *args, **kwargs):
		QFrame.__init__(self, *args, **kwargs)
		
		# Size Policy
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)
		self.setMinimumSize(QSize(200, 20))
		self.setMaximumSize(QSize(16777215, 16777215))
		
		# Layout
		self.setLayout(QHBoxLayout())
		self.layout().setSpacing(5)
		self.layout().setContentsMargins(5, 5, 5, 5)
		
		# Logo
		self.label_logo = QLabel()
		self.label_logo.setMinimumSize(QSize(114, 14))
		self.label_logo.setPixmap(QPixmap(path.join(RESOURCE_PATH, "icon_logo.png")))
		self.layout().addWidget(self.label_logo)
		
		# Settings Button
		self.button_settings = Settings_Tool_Button(self)
		self.layout().addWidget(self.button_settings)
		
		# Style Sheet
		self.setStyleSheet('background:black;')

# ======================================================================================================================
#
#
# Execute
#
#
# ======================================================================================================================

if __name__ == '__main__':
	pass


