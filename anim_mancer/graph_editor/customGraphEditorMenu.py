"""
List Of Tools For Graph Editor

- Filter By Attributes
- Infinity
- Smooth Keys
- Add Noise

"""

# Project Modules
from anim_mancer.ui.widgets import *
from anim_mancer.utils import *
from anim_mancer.tools import keys
from anim_mancer.tools import animFilters

# Python Modules
import weakref
from functools import partial

# Maya Modules
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from maya import cmds, mel, OpenMayaUI

# Qt Modules
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from shiboken2 import wrapInstance

# ======================================================================================================================
#
#
# Global
#
#
# ======================================================================================================================

MENU_NAME = '{}_graph_editor_menu'.format(UI.name)


class Outliner_Filter(object):
	all = '0'
	translate = 'translateFilter'
	rotate = 'rotateFilter'
	scale = 'scaleFilter'
	translate_rotate = 'objectAttrFilter'
	translate_rotate_scale = 'scaleRotateTranslateFilter'
	user = 'dynamicFilter'


class Infinity_Type(object):
	constant = 'constant'
	cycle = 'cycle'
	offset = 'cycleRelative'
	lienar = 'linear'
	oscillate = 'oscillate'


# ======================================================================================================================
#
#
# Function
#
#
# ======================================================================================================================

def test_callback(*args, **kwargs):
	print args
	return


def deletUI(name, *args, **kwargs):
	if cmds.menu(name, q=True, ex=True):
		cmds.evalDeferred(lambda *_: cmds.deleteUI(name))
	return


def set_curve_infinity(kind='constant', *args, **kwargs):
	return cmds.setInfinity(postInfinite=kind, preInfinite=kind)


# Fixme: Curve Filter - Translate & Rotate
def set_curve_filter(kind=Outliner_Filter.all, *args, **kwargs):
	return cmds.outlinerEditor(UI.graph_editor_outliner, e=True, attrFilter=kind)


# ======================================================================================================================
#
#
# Execute
#
#
# ======================================================================================================================

def show(*args, **kwargs):
	cmds.menuItem(label='Filter', divider=True)
	cmds.radioMenuItemCollection()
	cmds.menuItem(label='All', command=partial(set_curve_filter, Outliner_Filter.all))
	cmds.menuItem(label='Translate Rotate', command=partial(set_curve_filter, Outliner_Filter.translate_rotate))
	cmds.menuItem(label='User', command=partial(set_curve_filter, 'user'))
	
	cmds.menuItem(label='Infinity', divider=True)
	cmds.menuItem(label='Constant', command=partial(set_curve_infinity, Infinity_Type.constant))
	cmds.menuItem(label='Linear', command=partial(set_curve_infinity, Infinity_Type.lienar))
	cmds.menuItem(label='Cycle', command=partial(set_curve_infinity, Infinity_Type.cycle))
	cmds.menuItem(label='Offset', command=partial(set_curve_infinity, Infinity_Type.offset))
	
	cmds.menuItem(label='Keys', divider=True)
	cmds.menuItem(l='Delete Redundant', c=keys.deleteRedundant)
	cmds.menuItem(l='Delete Static Channels', c=keys.deleteStaticAllChannels)
	
	cmds.menuItem(label='Noise', divider=True)
	# cmds.menuItem(label='Add Noise', command=test_callback)
	cmds.menuItem(label='Smooth', command=animFilters.main)
	return


if __name__ == '__main__':
	pass
