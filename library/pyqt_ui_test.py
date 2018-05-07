import library.pyqt_ui as pyqt

reload(pyqt)
from maya import cmds, mel
from functools import partial


def test(var=None):
	print 'Test Function: {}'.format(var)


def ui(name='QT UI Test'):
	window = pyqt.Window(name=name)
	layout = window.layout

	b1 = pyqt.Button(layout, name='Button 1', command=test)
	b2 = pyqt.Button(layout, name='Button 2', command=test)

	window.show()
