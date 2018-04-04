import maya.cmds as cmds
import maya.OpenMayaUI as mui
import PySide.QtGui as qt
import shiboken


########################################################################################################################
#																													   #
#																													   #
#	DEFAULT THEME																									   #
#																													   #
#																													   #
########################################################################################################################


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


########################################################################################################################
#																													   #
#																													   #
#	WIDGET CLASS																									   #
#																													   #
#																													   #
########################################################################################################################


def testFunction(value=None):
	print('Test Command Value: {}'.format(value))
	return value


def listCheck(var):
	if type(var) is str or type(var) is unicode:
		var = [str(var)]
	return var


def longName(var):
	return var.replace(' ', '').replace('\t', '').replace('\n', '')


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
	             name='widget1',
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
		self.name = longName(name)
		self.label = label if label else name
		self.width = width
		self.height = height
		self.margin = defaultSpacing(margin)
		self.padding = defaultSpacing(padding)
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

	def setParameters(self, item):
		self.setBackgroundColor(item) if self.backgroundColor else None

	def addName(self, item):
		item.setObjectName(self.name) if self.name else None

	def addWidget(self, parent):
		parent.layout.addWidget(self.widget)

	def addLayout(self, parent):
		parent.addLayout(self.layout)

	def setSize(self, item):
		item.setContentsMargins(
				self.padding[0],
				self.padding[1],
				self.padding[2],
				self.padding[3]
		)

	def setBackgroundColor(self, item):
		item.setStyleSheet('background-color: rgb({}, {}, {})'.format(self.backgroundColor[0],
		                                                              self.backgroundColor[1],
		                                                              self.backgroundColor[2],
		                                                              ))


########################################################################################################################
#																													   #
#																													   #
#	WINDOW CLASS																									   #
#																													   #
#																													   #
########################################################################################################################


def getMayaWindow():
	pointer = mui.MQtUtil.mainWindow()
	return shiboken.wrapInstance(long(pointer), qt.QWidget)


class window(widget):

	def __init__(self,
	             name='window1',
	             label=None,
	             width=0,
	             height=0,
	             padding=0,
	             backgroundColor=None
	             ):
		widget.__init__(self,
		                name=name,
		                label=label,
		                width=width,
		                height=height,
		                padding=padding,
		                backgroundColor=backgroundColor
		                )

		self.setBackgroundColor(self.ui) if self.backgroundColor else None

	def deleteExisting(self):
		if cmds.window(self.name, q=True, exists=True):
			cmds.deleteUI(self.name, window=True)

	def create(self):
		# Remove Existing Window
		self.deleteExisting()

		parent = getMayaWindow()
		self.ui = qt.QMainWindow(parent)
		self.ui.setObjectName(self.name)
		self.ui.setWindowTitle(self.label)

		# Main Widget
		self.widget = qt.QWidget()
		self.ui.setCentralWidget(self.widget)

		# Layout

		self.layout = qt.QVBoxLayout()
		self.layout.setContentsMargins(
				self.padding[0],
				self.padding[1],
				self.padding[2],
				self.padding[3])

		self.widget.setLayout(self.layout)

	def show(self):
		self.ui.show()


########################################################################################################################
#																													   #
#																													   #
#	LAYOUT CLASS																							           #
#																													   #
#																													   #
########################################################################################################################

class layout(widget):
	def __init__(self,
	             parent,
	             name='layout1',
	             width=0,
	             height=0,
	             padding=0,
	             margin=0,
	             backgroundColor=None,
	             ):
		widget.__init__(self,
		                parent=parent,
		                name=name,
		                width=width,
		                height=height,
		                padding=padding,
		                margin=margin,
		                backgroundColor=backgroundColor,
		                )
		self.addName(self.layout)
		self.addWidget(self.parent)
		#self.setSize(self.layout)


class column(layout):
	def __init__(self,
	             parent,
	             name='column1',
	             width=0,
	             height=0,
	             padding=0,
	             margin=0,
	             backgroundColor=None,
	             ):
		layout.__init__(self,
		                parent=parent,
		                name=name,
		                width=width,
		                height=height,
		                padding=padding,
		                margin=margin,
		                backgroundColor=backgroundColor,
		                )

	def create(self):
		self.widget = qt.QFrame()
		self.layout = qt.QVBoxLayout()
		self.widget.setLayout(self.layout)
		self.setBackgroundColor(self.widget) if self.backgroundColor else None



class row(layout):
	def __init__(self, parent, name='row1', width=0, height=0, padding=0, margin=0):
		layout.__init__(self, parent=parent, name=name, width=width, height=height, padding=padding, margin=margin)

	def create(self):
		self.layout = qt.QHBoxLayout()


class grid(layout):
	def __init__(self, parent, name='grid1', width=0, height=0, padding=0, margin=0):
		layout.__init__(self, parent=parent, name=name, width=width, height=height, padding=padding, margin=margin)

	def create(self):
		self.layout = qt.QGridLayout()


class form(layout):
	def __init__(self, parent, name='form1', width=0, height=0, padding=0, margin=0):
		layout.__init__(self, parent=parent, name=name, width=width, height=height, padding=padding, margin=margin)

	def create(self):
		self.layout = qt.QFormLayout()


class frame(layout):
	pass


class pane(layout):
	def __init__(self, parent, name='pane1', width=0, height=0, padding=0, margin=0):
		layout.__init__(self, parent=parent, name=name, width=width, height=height, padding=padding, margin=margin)

	def create(self):
		self.layout = qt.QSplitter()


class spacer(widget):
	def __init__(self, parent, name='spacer', width=0, height=0):
		widget.__init__(self, parent=parent, name=name, width=width, height=height)
		self.addSpacer(self.parent.layout)

	def create(self):
		self.widget = qt.QSpacerItem()

	def addSpacer(self, parent):
		parent.addSpacerItem(self.widget)


########################################################################################################################
#																													   #
#																													   #
#	CONTROL CLASS																							           #
#																												       #
#																													   #
########################################################################################################################


class control(widget):
	def __init__(self,
	             parent,
	             name='control1',
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
		#setSize(self.control, minW=self.width, maxW=self.width, minH=self.height, maxH=self.height)

	def addFont(self, item):
		font = qt.QFont()
		font.setPointSize(self.fontSize)
		item.setFont(font)


class menuBar(control):
	def __init__(self, parent, name='menuBar1', height=18):
		self.menu = listCheck(menu)
		control.__init__(self, parent=parent, name=name, height=height)

	def create(self):
		self.control = qt.QMenuBar()


class menu(control):
	def __init__(self, parent, name='menu1', label=None):
		control.__init__(self, parent=parent, name=name, label=label)

	def create(self):
		self.control = qt.QMenu(self.label)

	def addWidget(self, parent):
		parent.control.addMenu(self.control)


class menuItem(control):
	def __init__(self, parent, name='menuItem1', label=None, command=testFunction):
		control.__init__(self, parent=parent, name=name, label=label, command=command)

	def create(self):
		self.control = qt.QAction(self.label, None)
		self.control.triggered.connect(self.command)

	def addWidget(self, parent):
		parent.control.addAction(self.control)


class text(control):
	def __init__(
			self,
			parent,
			name='text1',
			label=None,
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
	             name='button1',
	             label=None,
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
	             name='checkBox1',
	             label=None,
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
	             name='textField1',
	             label=None,
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
