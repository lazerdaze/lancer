# LANCER.RIG.UI.WINDOW
#
#
#
#
#

# Lancer Modules
from rig import utils

# Python Modules
import sys

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Maya Modules
from maya import cmds, mel, OpenMayaUI
from shiboken2 import wrapInstance


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################


def getMayaWindow():
	mayaPtr = OpenMayaUI.MQtUtil.mainWindow()
	mayaWindow = wrapInstance(long(mayaPtr), QWidget)
	return mayaWindow


########################################################################################################################
#
#
#	Joint TreeView
#
#
########################################################################################################################


class JointItemDelegate(QItemDelegate):
	def __init__(self, *args, **kwargs):
		QItemDelegate.__init__(self, *args, **kwargs)


class JointItem(object):
	def __init__(self):
		pass


class JointModel(QAbstractItemModel):
	def __init__(self, *args, **kwargs):
		QAbstractItemModel.__init__(self, *args, **kwargs)


class JointTreeViewContextMenu(QMenu):
	def __init__(self, *args, **kwargs):
		QMenu.__init__(self, *args, **kwargs)
		pass


class JointTreeView(QTreeView):
	def __init__(self, *args, **kwargs):
		QTreeView.__init__(self, *args, **kwargs)


########################################################################################################################
#
#
#	GroupBox
#
#
########################################################################################################################


class OptionsGroupBox(QGroupBox):
	def __init__(self, *args, **kwargs):
		QGroupBox.__init__(self, *args, **kwargs)

		self.setTitle('Options')

		layout = QVBoxLayout()
		self.setLayout(layout)

		# Prefix
		prefixLayout = QHBoxLayout()
		prefixLayout.setSpacing(0)
		layout.addLayout(prefixLayout)

		self.prefixLabel = QLabel()
		self.prefixLabel.setText('Type')
		self.prefixLabel.setMinimumSize(QSize(60, 0))
		prefixLayout.addWidget(self.prefixLabel)

		self.prefixOptions = QComboBox()
		self.prefixOptions.setEditable(True)
		sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.prefixOptions.sizePolicy().hasHeightForWidth())
		self.prefixOptions.setSizePolicy(sizePolicy)

		for param in sorted(vars(utils.Part).iterkeys()):
			if not param.startswith('__'):
				self.prefixOptions.addItem(param.capitalize())

		self.prefixOptions.setCurrentText('Rig')

		prefixLayout.addWidget(self.prefixOptions)

		# Side
		sideLayout = QHBoxLayout()
		sideLayout.setSpacing(0)
		layout.addLayout(sideLayout)

		self.sideLabel = QLabel()
		self.sideLabel.setText('Side')
		self.sideLabel.setMinimumSize(QSize(60, 0))
		sideLayout.addWidget(self.sideLabel)

		self.sideOptions = QComboBox()
		sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sideOptions.sizePolicy().hasHeightForWidth())
		self.sideOptions.setSizePolicy(sizePolicy)
		self.sideOptions.setEditable(False)
		self.sideOptions.setFrame(True)
		self.sideOptions.addItem('Center')
		self.sideOptions.addItem('Left')
		self.sideOptions.addItem('Right')
		self.sideOptions.addItem('None')
		sideLayout.addWidget(self.sideOptions)

		# Extras
		extrasLayout = QHBoxLayout()
		extrasLayout.setSpacing(0)
		layout.addLayout(extrasLayout)

		# Twist
		self.twistCheckBox = QCheckBox()
		self.twistCheckBox.setText('Twist')
		self.twistCheckBox.setChecked(True)
		extrasLayout.addWidget(self.twistCheckBox)

		# Stretch
		self.stretchCheckBox = QCheckBox()
		self.stretchCheckBox.setText('Stretch')
		self.stretchCheckBox.setChecked(True)
		extrasLayout.addWidget(self.stretchCheckBox)

	@property
	def prefix(self):
		return self.prefixOptions.currentText().lower()

	@property
	def side(self):
		return self.sideOptions.currentText().lower()

	@property
	def twist(self):
		return self.twistCheckBox.isChecked()

	@property
	def stretch(self):
		return self.stretchCheckBox.isChecked()


class IKGroupBox(QGroupBox):
	def __init__(self, *args, **kwargs):
		QGroupBox.__init__(self, *args, **kwargs)

		self.setTitle('Inverse Kinematics')
		self.setCheckable(True)
		self.setChecked(False)

		layout = QVBoxLayout()
		self.setLayout(layout)

		# Solver
		solverLayout = QHBoxLayout()
		solverLayout.setSpacing(0)
		layout.addLayout(solverLayout)

		self.solverLabel = QLabel()
		self.solverLabel.setText('Solver')
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.solverLabel.sizePolicy().hasHeightForWidth())
		self.solverLabel.setSizePolicy(sizePolicy)
		self.solverLabel.setMinimumSize(QSize(60, 0))
		solverLayout.addWidget(self.solverLabel)

		self.solverGroup = QButtonGroup()
		self.solverGroup.setExclusive(True)

		self.rpRadioButton = QRadioButton()
		self.rpRadioButton.setText('Rotate Plane')
		self.rpRadioButton.setChecked(True)
		self.solverGroup.addButton(self.rpRadioButton)
		solverLayout.addWidget(self.rpRadioButton)

		self.splineRadioButton = QRadioButton()
		self.splineRadioButton.setText('Spline')
		self.solverGroup.addButton(self.splineRadioButton)
		solverLayout.addWidget(self.splineRadioButton)

	@property
	def enabled(self):
		return self.isChecked()

	@property
	def solver(self):
		return self.solverGroup.checkedButton().text().lower()


class LocalWorldGroupBox(QGroupBox):
	def __init__(self, *args, **kwargs):
		QGroupBox.__init__(self, *args, **kwargs)

		self.setTitle('Local World')
		self.setCheckable(True)
		self.setChecked(False)

		layout = QVBoxLayout()
		self.setLayout(layout)

		# Local
		localLayout = QHBoxLayout()
		localLayout.setSpacing(0)
		layout.addLayout(localLayout)

		self.localLabel = QLabel()
		self.localLabel.setText('Local')
		self.localLabel.setMinimumSize(QSize(60, 0))
		localLayout.addWidget(self.localLabel)

		self.localLineEdit = QLineEdit()
		localLayout.addWidget(self.localLineEdit)

		self.localButton = QPushButton()
		self.localButton.setText('<')
		localLayout.addWidget(self.localButton)

		# World
		worldLayout = QHBoxLayout()
		worldLayout.setSpacing(0)
		layout.addLayout(worldLayout)

		self.worldLabel = QLabel()
		self.worldLabel.setText('World')
		self.worldLabel.setMinimumSize(QSize(60, 0))
		worldLayout.addWidget(self.worldLabel)

		self.worldLineEdit = QLineEdit()
		worldLayout.addWidget(self.worldLineEdit)

		self.worldButton = QPushButton()
		self.worldButton.setText('<')
		worldLayout.addWidget(self.worldButton)

	@property
	def enabled(self):
		return self.isChecked()

	@property
	def local(self):
		return self.localLineEdit.text()

	@property
	def world(self):
		return self.worldLineEdit.text()


class JointGroupBox(QGroupBox):
	def __init__(self, *args, **kwargs):
		QGroupBox.__init__(self, *args, **kwargs)

		self.setTitle('Joint Options')

		layout = QVBoxLayout()
		self.setLayout(layout)

		# Up Axis
		upAxisLayout = QHBoxLayout()
		upAxisLayout.setSpacing(0)
		layout.addLayout(upAxisLayout)

		self.upAxisLabel = QLabel()
		self.upAxisLabel.setText('Up Axis')
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.upAxisLabel.sizePolicy().hasHeightForWidth())
		self.upAxisLabel.setSizePolicy(sizePolicy)
		self.upAxisLabel.setMinimumSize(QSize(80, 0))
		upAxisLayout.addWidget(self.upAxisLabel)

		self.upAxisButtonGroup = QButtonGroup()
		self.upAxisButtonGroup.setExclusive(True)

		upXRadioButton = QRadioButton()
		upXRadioButton.setText('X')
		upXRadioButton.setChecked(False)
		self.upAxisButtonGroup.addButton(upXRadioButton)
		upAxisLayout.addWidget(upXRadioButton)

		upYRadioButton = QRadioButton()
		upYRadioButton.setText('Y')
		upYRadioButton.setChecked(True)
		self.upAxisButtonGroup.addButton(upYRadioButton)
		upAxisLayout.addWidget(upYRadioButton)

		upZRadioButton = QRadioButton()
		upZRadioButton.setText('Z')
		upZRadioButton.setChecked(False)
		self.upAxisButtonGroup.addButton(upZRadioButton)
		upAxisLayout.addWidget(upZRadioButton)

		# Down Axis
		downAxisLayout = QHBoxLayout()
		downAxisLayout.setSpacing(0)
		layout.addLayout(downAxisLayout)

		self.downAxisLabel = QLabel()
		self.downAxisLabel.setText('Down Axis')
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.downAxisLabel.sizePolicy().hasHeightForWidth())
		self.downAxisLabel.setSizePolicy(sizePolicy)
		self.downAxisLabel.setMinimumSize(QSize(80, 0))
		downAxisLayout.addWidget(self.downAxisLabel)

		self.downAxisButtonGroup = QButtonGroup()
		self.downAxisButtonGroup.setExclusive(True)

		upXRadioButton = QRadioButton()
		upXRadioButton.setText('X')
		upXRadioButton.setChecked(True)
		self.downAxisButtonGroup.addButton(upXRadioButton)
		downAxisLayout.addWidget(upXRadioButton)

		upYRadioButton = QRadioButton()
		upYRadioButton.setText('Y')
		upYRadioButton.setChecked(False)
		self.downAxisButtonGroup.addButton(upYRadioButton)
		downAxisLayout.addWidget(upYRadioButton)

		upZRadioButton = QRadioButton()
		upZRadioButton.setText('Z')
		upZRadioButton.setChecked(False)
		self.downAxisButtonGroup.addButton(upZRadioButton)
		downAxisLayout.addWidget(upZRadioButton)

		# Extras
		extrasLayout = QHBoxLayout()
		extrasLayout.setSpacing(0)
		layout.addLayout(extrasLayout)

		self.leafJointsCheckbox = QCheckBox()
		self.leafJointsCheckbox.setText('Include Leaf Joints')
		self.leafJointsCheckbox.setChecked(True)
		extrasLayout.addWidget(self.leafJointsCheckbox)

		# Treeview
		self.treeView = JointTreeView()
		layout.addWidget(self.treeView)

	@property
	def upAxis(self):
		return self.upAxisButtonGroup.checkedButton().text().lower()

	@property
	def downAxis(self):
		return self.downAxisButtonGroup.checkedButton().text().lower()

	@property
	def leafJoints(self):
		return self.leafJointsCheckbox.isChecked()


class Window(QMainWindow):
	def __init__(self, *args, **kwargs):
		QMainWindow.__init__(self, *args, **kwargs)

		self.resize(312, 695)
		self.centralwidget = QWidget(self)
		self.setCentralWidget(self.centralwidget)

		self.verticalLayout = QVBoxLayout(self.centralwidget)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.scrollArea = QScrollArea(self.centralwidget)
		self.scrollArea.setWidgetResizable(True)
		self.scrollAreaWidgetContents = QWidget()
		self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 310, 649))
		self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)

		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.verticalLayout.addWidget(self.scrollArea)

		# Global Options
		self.optionsWidget = OptionsGroupBox()
		self.verticalLayout_3.addWidget(self.optionsWidget)

		# IK
		self.ikWidget = IKGroupBox()
		self.verticalLayout_3.addWidget(self.ikWidget)

		# Local World
		self.localWorldWidget = LocalWorldGroupBox()
		self.verticalLayout_3.addWidget(self.localWorldWidget)

		# Joint Options
		self.jointWidget = JointGroupBox()
		self.verticalLayout_3.addWidget(self.jointWidget)

		# Create Button
		self.createButton = QPushButton()
		self.createButton.setText('Create')
		self.verticalLayout.addWidget(self.createButton)

		# Signals Slots
		self.createButton.clicked.connect(self.callback)

	def callback(self):
		# Global
		prefix = self.optionsWidget.prefix
		side = self.optionsWidget.side
		twist = self.optionsWidget.twist
		stretch = self.optionsWidget.stretch

		# IK
		ik = self.ikWidget.enabled
		ikSolver = self.ikWidget.solver

		# Local World
		localWorld = self.localWorldWidget.enabled
		localParent = self.localWorldWidget.local
		worldParent = self.localWorldWidget.world

		if localWorld:
			if not localParent:
				raise ValueError('Must specify a local transform node.')
			else:
				if not utils.nodeExists(localParent):
					raise utils.NodeExistsError('Node "{}" does not exist.'.format(localParent))
			if not worldParent:
				raise ValueError('Must specify a world transform node.')
			else:
				if not utils.nodeExists(worldParent):
					raise utils.NodeExistsError('Node "{}" does not exist.'.format(worldParent))

		# Joints
		upAxis = self.jointWidget.upAxis
		downAxis = self.jointWidget.downAxis
		leafJoints = self.jointWidget.leafJoints
		return


def show(name='lancer_rig_windowUI', title='Lancer Rig', *args, **kwargs):
	if cmds.window(name, exists=True):
		cmds.deleteUI(name, wnd=True)

	window = Window(getMayaWindow())
	window.setObjectName(name)
	window.setWindowTitle(title)
	window.show()
	return window
