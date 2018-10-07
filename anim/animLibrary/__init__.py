# AXEL
#
#
#
#
#

'''
AXEL : Animation XML Export Library

Notes:
- Make Standalone (from Lancer)

Legacy Notes:
- Add Alphabetical Sorting
- Add Drag Drop / Moving files
- Add Search
- Add Rename File Function
- Add Overwrite File
- Add Select Objects from file
- Add Objects To Item
- Add Offset Animation

Future Stuff:
- Add Meta node Functionality
'''

# Lancer Modules
import ui
reload(ui)

# Python Modules
import os
import platform

# Maya Modules
from maya import cmds, mel

# Operating System
OSPLATFORM = platform.system()

# Script Paths
MAYAVERSION = int(cmds.about(v=True))
DIRPATH = os.path.dirname(os.path.abspath(__file__))
SUBDIR = os.walk(DIRPATH)
DEFAULTLIBRARY = os.path.join(DIRPATH, 'default_library')
PREFSFILEPATH = os.path.join(DIRPATH, 'user_prefs.json')


