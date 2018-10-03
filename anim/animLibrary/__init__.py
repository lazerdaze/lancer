# LANCER.ANIM.ANIMLIBRARY
#
#
#
#
#

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
DIRPATH = os.path.dirname(os.path.abspath(__file__))
SUBDIR = os.walk(DIRPATH)
MAYAVERSION = int(cmds.about(v=True))


