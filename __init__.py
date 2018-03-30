# LANCER. Copyright 2018 Justin Tirado. All Rights Reserved.
#
#
#
#
#


# Python Modules

import os
import sys
import platform
import datetime
import time

# Maya Modules

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as api
import maya.OpenMayaAnim as anim

# Operating System

OSPLATFORM = platform.system()

# Script Paths

DIRPATH = os.path.dirname(os.path.abspath(__file__))
MAYAVERSION = 'Maya {}'.format(cmds.about(v=True))
SUBDIR = os.walk(DIRPATH)


# Functions

def addToSysPath():
	global DIRPATH
	if DIRPATH not in sys.path:
		sys.path.append(DIRPATH)


if __name__ == 'lancer':

	addToSysPath()

	print '\n\n\n{0} LANCER {0}\n\n\n'.format('-' * 50)
	print '{}\n{}\n{}\n'.format(MAYAVERSION, OSPLATFORM, DIRPATH)
	for x in SUBDIR:
		print x[0]

	print '\n\n\n{0}\n\n\n'.format('-' * 111)
