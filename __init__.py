# LANCER
#
#
#
#
#


# Python Modules
import os
import sys
import platform

# Maya Modules
from maya import cmds, mel

# Operating System
OSPLATFORM = platform.system()

# Script Paths
DIRPATH = os.path.dirname(os.path.abspath(__file__))
SUBDIR = os.walk(DIRPATH)
EXTERNALDIR = os.path.join(DIRPATH, 'external')
EXTERNALPLUGINDIR = os.path.join(EXTERNALDIR, 'plugins')
EXTERNALPLUGINS = False
MAYAVERSION = int(cmds.about(v=True))
MAYAPLUGINPATH = mel.eval('getenv "MAYA_PLUG_IN_PATH"')


# Functions
def splitall(path):
	allparts = []
	while 1:
		parts = os.path.split(path)
		if parts[0] == path:
			allparts.insert(0, parts[0])
			break
		elif parts[1] == path:
			allparts.insert(0, parts[1])
			break
		else:
			path = parts[0]
			allparts.insert(0, parts[1])
	return allparts


def getSubDirectory():
	global SUBDIR

	sub = []
	exception = ['.git', '.idea']

	for folder in SUBDIR:
		folder = folder[0]
		folderParts = splitall(folder)
		if '.git' not in folderParts and '.idea' not in folderParts:
			sub.append(folder)

	SUBDIR = sub
	return


def addToSysPath():
	if DIRPATH not in sys.path:
		sys.path.append(DIRPATH)
	if EXTERNALDIR not in sys.path:
		sys.path.append(EXTERNALDIR)
	return


def addToMayaPluginPath():
	global EXTERNALPLUGINS

	path = EXTERNALPLUGINDIR.replace('\\', '/')
	if MAYAVERSION:
		if EXTERNALDIR not in MAYAPLUGINPATH.split(';'):
			try:
				mel.eval('''putenv "MAYA_PLUG_IN_PATH" "{};{}";'''.format(MAYAPLUGINPATH, path))
				EXTERNALPLUGINS = True
			except:
				pass
	return


def loadPlugins():
	if EXTERNALPLUGINS and MAYAVERSION == 2018:
		for plugin in os.listdir(EXTERNALPLUGINDIR):
			if not cmds.pluginInfo(plugin, q=True, l=True):
				cmds.loadPlugin(plugin)
	return


addToSysPath()
addToMayaPluginPath()
getSubDirectory()
loadPlugins()


if __name__ == '__main__':
	print '\n\n\n{0} LANCER {0}\n\n\n'.format('-' * 50)
	print 'Operating System: {}'.format(OSPLATFORM)
	print 'Directory Path: {}'.format(DIRPATH)
	print 'External Tools Path: {}'.format(EXTERNALDIR)
	print ''
	print 'Maya Version: {}'.format(MAYAVERSION)
	print 'Maya Plugins Loaded: {}'.format(EXTERNALPLUGINS)
	print ''
	print 'Lancer Sub Directories'
	for x in SUBDIR:
		print x
	print '\n\n\n{}\n\n\n'.format('-' * 111)
