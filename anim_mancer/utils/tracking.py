# Project Modules

# Python Modules

# ======================================================================================================================
#
#
# Global
#
#
# ======================================================================================================================

# ======================================================================================================================
#
#
# Function
#
#
# ======================================================================================================================
import os
import time
import json
import errno
import getpass
import maya.cmds as cmds


def createDir(path):
	try:
		os.makedirs(path)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise


def mayaLogger():
	mainFolder = '/your/path/logs/'
	userLogin = getpass.getuser()
	with open(mainFolder + 'users.json') as f:
		userDictionary = json.load(f)
	if userLogin in userDictionary:
		project = 'UberMovieTitle'
		mayaVersion = cmds.about(version=True)
		folderYearMonth = time.strftime("%Y-%m")
		timeNow = time.strftime("%Y-%m-%d_%H:%M:%S")
		folderPath = os.path.join(mainFolder, project, userLogin, folderYearMonth)
		fileName = timeNow + '__maya' + mayaVersion.replace(" ", "-") + '.log'
		filePath = os.path.join(folderPath, fileName).replace('''\'''', '''/''')  # Bad
		createDir(folderPath)
		cmds.cmdFileOutput(open=filePath)


# ======================================================================================================================
#
#
# Class
#
#
# ======================================================================================================================


# ======================================================================================================================
#
#
# Execute
#
#
# ======================================================================================================================

if __name__ == '__main__':
	pass
