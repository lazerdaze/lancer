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
import inspect

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

try:
	MAYAVERSION = int(cmds.about(v=True))
except TypeError:
	MAYAVERSION = None

MAYAPLUGINPATH = mel.eval('getenv "MAYA_PLUG_IN_PATH"')


# Functions
def refreshModules():
	toDelete = []
	for key, module in sys.modules.iteritems():
		try:
			moduleFilePath = inspect.getfile(module).lower()

			if moduleFilePath == __file__.lower():
				continue

			if moduleFilePath.startswith(DIRPATH.lower()):
				print "Removing {}".format(key)
				toDelete.append(key)
		except:
			pass

	for module in toDelete:
		del (sys.modules[module])


def reloadModules():
	for x in sys.modules.values():
		print x
	return

reloadModules()

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
getSubDirectory()

if OSPLATFORM in ['Linux', 'Darwin']:
	pass
else:
	pass
	addToMayaPluginPath()
	loadPlugins()


if __name__ == '__main__':
	print '{0}LANCER START{0}'.format('-' * 50)
	print 'Operating System: {}'.format(OSPLATFORM)
	print 'Directory Path: {}'.format(DIRPATH)
	print 'External Tools Path: {}'.format(EXTERNALDIR)
	print 'Maya Version: {}'.format(MAYAVERSION)
	print 'Maya Plugins Loaded: {}'.format(EXTERNALPLUGINS)
	# print 'Lancer Sub Directories'
	# for x in SUBDIR:
	# 	print x
	print '{0}LANCER END--{0}'.format('-' * 50)
