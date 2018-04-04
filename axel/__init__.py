#
#
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
import PySide

# Maya Modules

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as api
import maya.OpenMayaAnim as anim

__version__ = "1.0"
__encoding__ = sys.getfilesystemencoding()

OSPLATFORM = platform.system()
DIRPATH = os.path.dirname(os.path.abspath(__file__))
SUBDIR = os.walk(DIRPATH)
MAYAVERSION = 'Maya {}'.format(cmds.about(v=True))


def addToSysPath():
	global DIRPATH
	if DIRPATH not in sys.path:
		sys.path.append(DIRPATH)


if __name__ == "__main__":

	addToSysPath()

	print
	'\n\n\n{0} AXEL {0}\n\n\n'.format('-' * 50)
	print
	'{}\n{}\n{}\n'.format(MAYAVERSION, OSPLATFORM, DIRPATH)
	for x in SUBDIR:
		print(x[0])

	print('\n\n\n{0}\n\n\n'.format('-' * 111))
