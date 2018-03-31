import maya.cmds as cmds
import maya.OpenMayaUI as mui
import PySide.QtGui as qt
import shiboken


#########################################################################################################################
#																														#
#																														#
#	DEFAULT THEME																									    #
#																														#
#																														#
#########################################################################################################################


class theme:
	margin = 5
	padding = 10
	window = [.267, .267, .267]
	button = [.365, .365, .365]
	layout = [.286, .286, .286]
	vertical = [.286, .286, .286]
	border = 0
	borderColor = [.169, .169, .169]
	field = [.169, .169, .169]
	divider = [.5, .5, .5]
	header = 25
	headerColor = [.365, .365, .365]


#########################################################################################################################
#																														#
#																														#
#	WIDGET CLASS																									    #
#																														#
#																														#
#########################################################################################################################


def testFunction(value=None):
	print('Test Command Value: {}'.format(value))
	return value


def defaultSpacing(value):
	if type(value) is not list:
		value = [value, value, value, value]
	return value


def setSize(item, minW=0, maxW=0, minH=0, maxH=0, minSize=0, maxSize=0):
	item.setMinimumWidth(minW) if minW else None
	item.setMaximumWidth(maxW) if maxW else None
	item.setMinimumHeight(minH) if minH else None
	item.setMaximumHeight(maxH) if maxH else None
	item.setMinimumSize(minSize) if minSize else None
	item.setMaximumSize(maxSize) if maxSize else None


def mayaUIPointer(item):
	return mui.MQtUtil.fullName(long(shiboken.unwrapInstance(item)))


class widget(object):
	def __init__(self,
	             name=None,
	             label=None,
	             width=0,
	             height=0,
	             margin=0,
	             padding=0,
	             visible=True,
	             enable=True,
	             backgroundColor=None,
	             border=0,
	             borderColor=None,
	             parent=None,
	             children=None,
	             annotation=None,
	             ):
		self.name = name
		self.label = label if label else name
		self.width = width
		self.height = height
		self.margin = margin
		self.padding = padding
		self.visible = visible
		self.enable = enable
		self.backgroundColor = backgroundColor
		self.border = border
		self.borderColor = borderColor
		self.parent = parent
		self.children = children
		self.annotation = annotation
		self.ui = None
		self.layout = None
		self.widget = None
		self.control = None

		self.create()

	def create(self):
		pass

	def addName(self, item):
		item.setObjectName(self.name) if self.name else None


#########################################################################################################################
#																														#
#																														#
#	WINDOW CLASS																									    #
#																														#
#																														#
#########################################################################################################################


def getMayaWindow():
	pointer = mui.MQtUtil.mainWindow()
	return shiboken.wrapInstance(long(pointer), qt.QWidget)


class window(widget):

	def __init__(self, name='window1', label=None, width=0, height=0):
		widget.__init__(self, name=name, label=label, width=width, height=height)

	def deleteExisting(self):
		if cmds.window(self.name, q=True, exists=True):
			cmds.deleteUI(self.name, window=True)

	def create(self):
		# Remove Existing Window
		self.deleteExisting()

		parent = getMayaWindow()
		ui = qt.QMainWindow(parent)
		ui.setObjectName(self.name)
		ui.setWindowTitle(self.label)

		# Main Widget
		mainWidget = qt.QWidget()
		ui.setCentralWidget(mainWidget)

		# Layout
		verticalLayout = qt.QVBoxLayout(mainWidget)

		self.ui = ui
		self.widget = mainWidget
		self.layout = verticalLayout

	def show(self):
		self.ui.show()


#########################################################################################################################
#																														#
#																														#
#	LAYOUT CLASS																							            #
#																														#
#																														#
#########################################################################################################################

class layout(widget):
	def __init__(self, parent, name=None, width=0, height=0):
		widget.__init__(self, name=name, parent=parent, width=width, height=height)
		self.addName(self.layout)
		self.addLayout(self.parent.layout)

	def addLayout(self, parent):
		parent.addLayout(self.layout)


class column(layout):
	def __init__(self, parent, name=None, width=0, height=0):
		layout.__init__(self, name=name, parent=parent, width=width, height=height)

	def create(self):
		self.layout = qt.QVBoxLayout()


class row(layout):
	def __init__(self, parent, name=None, width=0, height=0):
		layout.__init__(self, name=name, parent=parent, width=width, height=height)

	def create(self):
		self.layout = qt.QHBoxLayout()


class grid(layout):
	def __init__(self, parent, name=None, width=0, height=0):
		layout.__init__(self, name=name, parent=parent, width=width, height=height)

	def create(self):
		self.layout = qt.QGridLayout()


class form(layout):
	def __init__(self, parent, name=None, width=0, height=0):
		layout.__init__(self, name=name, parent=parent, width=width, height=height)

	def create(self):
		self.layout = qt.QFormLayout()


class frame(layout):
	pass


class spacer(widget):
	def __init__(self, parent, name=None, width=0, height=0):
		widget.__init__(self, name=name, parent=parent, width=width, height=height)
		self.addSpacer(self.parent.layout)

	def create(self):
		self.widget = qt.QSpacerItem()

	def addSpacer(self, parent):
		parent.addSpacerItem(self.widget)


#########################################################################################################################
#																														#
#																														#
#	CONTROL CLASS																							            #
#																														#
#																														#
#########################################################################################################################


class control(widget):
	def __init__(self,
	             parent,
	             name=None,
	             label=None,
	             value=None,
	             command=None,
	             width=0,
	             height=0,
	             font=None,
	             fontSize=0,
	             enable=True,
	             ):
		self.value = value
		self.command = command
		self.font = font
		self.fontSize = fontSize
		self.enable = enable

		widget.__init__(
				self,
				name=name,
				label=label,
				parent=parent,
				width=width,
				height=height,
		)

		self.addName(self.control)
		self.addWidget(self.parent)

	def addWidget(self, parent):
		parent.layout.addWidget(self.control)

	def addFont(self, item):
		font = qt.QFont()
		font.setPointSize(self.fontSize)
		item.setFont(font)


class text(control):
	def __init__(
			self,
			parent,
			name=None,
			label='text1',
			width=0,
			height=0):
		control.__init__(
				self,
				name=name,
				label=label,
				parent=parent,
				width=width,
				height=height
		)

	def create(self):
		self.control = qt.QLabel(self.label)


class button(control):
	def __init__(self,
	             parent,
	             name=None,
	             label='button1',
	             width=0,
	             height=0,
	             command=testFunction,
	             enable=True,
	             ):
		control.__init__(self,
		                 name=name,
		                 label=label,
		                 parent=parent,
		                 width=width,
		                 height=height,
		                 command=command,
		                 enable=enable)

	def create(self):
		self.control = qt.QPushButton(self.label)
		self.control.clicked.connect(self.command)


class checkBox(control):
	def __init__(self,
	             parent,
	             name=None,
	             label='checkBox1',
	             width=0,
	             height=0,
	             value=False,
	             command=testFunction,
	             onCommand=None,
	             offCommand=None,
	             enable=True,
	             ):
		self.onCommand = onCommand
		self.offCommand = offCommand

		control.__init__(self,
		                 name=name,
		                 label=label,
		                 parent=parent,
		                 width=width,
		                 height=height,
		                 value=value,
		                 command=command,
		                 enable=enable)

	def create(self):
		self.control = qt.QCheckBox(self.label)
		self.control.setChecked(self.value)

	def get(self):
		return self.control.isChecked()


class radioButton(control):
	pass


class optionMenu(control):
	pass


class spinField(control):
	pass


class textField(control):
	def __init__(self,
	             parent,
	             name=None,
	             label='textField1',
	             width=0,
	             height=0,
	             value=None,
	             enable=True,
	             ):
		control.__init__(self,
		                 name=name,
		                 label=label,
		                 parent=parent,
		                 width=width,
		                 height=height,
		                 value=value,
		                 enable=enable)

	def create(self):
		self.control = qt.QLineEdit()
		self.control.setPlaceholderText(self.value)

	def get(self):
		return self.control.text()


class textScrollField(control):
	pass
