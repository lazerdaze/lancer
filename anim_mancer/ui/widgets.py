"""
"""

# Project Modules
from color import USER_COLOR, DIVIDER_COLOR
from anim_mancer.utils import *

# Python Modules

# Python Modules
import difflib

# Maya Modules
from maya import OpenMaya, OpenMayaUI, cmds, mel

# Qt Modules
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


# ======================================================================================================================
#
#
# Execute
#
#
# ======================================================================================================================

if __name__ == '__main__':
	pass
