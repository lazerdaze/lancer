# Python
import pickle
import json
from os import path

# PySide
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Maya
from maya import cmds

########################################################################################################################
#
#
#	Global Variables
#
#
########################################################################################################################

WINDOWUI = None


########################################################################################################################
#
#
#	Utilities
#
#
########################################################################################################################


def getSelected():
    selected = cmds.ls(sl=True)
    if selected:
        return selected[0]
    else:
        return None


def snap(parent, child, transform=False, rotation=False):
    parPosition = getWorldTranslation(parent)
    parRotation = getWorldRotation(parent)

    if type(transform) is not bool:
        raise TypeError('Argument transform must be bool.')
    else:
        cmds.xform(child, t=parPosition, ws=True)

    if type(rotation) is not bool:
        raise TypeError('Argument rotation must be bool.')
    else:
        cmds.xform(child, ro=parRotation, ws=True)
    return


def getWorldTranslation(item):
    return cmds.xform(item, q=True, ws=True, rp=True)


def getWorldRotation(item):
    return cmds.xform(item, q=True, ws=True, ro=True)


def fk_to_ik(bone, fk, ik):
    return


def ik_to_fk(bone, fk, ik):
    return


def getMayaWindow():
    app = QApplication.instance()
    return {o.objectName(): o for o in app.topLevelWidgets()}["MayaWindow"]


########################################################################################################################
#
#
#	Class
#
#
########################################################################################################################

class Item(object):
    def __init__(self, bone, ik, fk):
        self.bone = bone
        self.ik = ik
        self.fk = fk


########################################################################################################################
#
#
#	Interface
#
#
########################################################################################################################

class Model(QStandardItemModel):
    def __init__(self, *args, **kwargs):
        QStandardItemModel.__init__(self, *args, **kwargs)


class View(QListView):
    def __init__(self, *args, **kwargs):
        QListView.__init__(self, *args, **kwargs)


class Widget(QFrame):
    def __init__(self, *args, **kwargs):
        QFrame.__init__(self, *args, **kwargs)


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)


def show(name='fkikMatchWindowUI', title='FK IK Match', *args, **kwargs):
    global WINDOWUI

    try:
        WINDOWUI.close()
        WINDOWUI.deleteLater()
    except:
        pass

    # Window
    WINDOWUI = Window(getMayaWindow())
    WINDOWUI.setObjectName(name)
    WINDOWUI.setWindowTitle(title)

    # Widget
    WINDOWUI.setCentralWidget(Widget())

    # Show UI
    WINDOWUI.show()
    return
