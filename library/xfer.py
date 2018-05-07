# LANCER.LIBRARY.XFER
#
#
#
#
#


import os
import sys
import collections
from contextlib import contextmanager
import time
import json

import xml
import xml.dom
from xml.dom import minidom
from xml.dom.minidom import Document
from xml.dom.minidom import parse
from xml.etree import ElementTree as etree

import maya.cmds as cmds

########################################################################################################################
#
#
#	Utilities
#
#
########################################################################################################################


debugMode = True


class FileType:
	json = 'json'
	xml = 'xml'
	ma = 'ma'
	mb = 'mb'
	fbx = 'fbx'
	txt = 'txt'
	py = 'py'
	obj = 'obj'


def pathJoin(*args):
	return os.path.join(*args)


def pathDirName(path):
	return os.path.dirname(path)


def pathBaseName(path):
	base = os.path.basename(path)
	return base if base else None


def doesPathExist(path):
	return os.path.exists(path)


def doesFileExists(path):
	return os.path.isfile(path)


def splitPath(path, fileName=None, fileType=None):
	dir = pathDirName(path)
	base = pathBaseName(path)
	fileName = fileName if fileName else base
	fileType = fileType if fileType else None

	if fileName:
		fileType = fileName.split('.')[-1] if '.' in fileName else None

	if fileType:
		fileName = fileName.replace('.{}'.format(fileType), '')
		fileType = fileType.replace('.', '')

	return [dir, fileName, fileType]


def makePath(path, fileName=None, fileType=None):
	newPath = ''
	for x in [path, fileName]:
		if x:
			if x not in newPath:
				newPath = pathJoin(newPath, x)
	if fileType:
		newPath = '{}.{}'.format(newPath, fileType)
	return newPath


def prettyXML(root):
	return minidom.parseString(etree.tostring(root)).toprettyxml()


def write(path, data=None, isDebug=False):
	t1 = time.time()
	fileType = splitPath(path)[2]

	with open(path, 'w') as writeFile:

		if fileType == FileType.json:
			json.dump(data, writeFile, indent=1)

		elif fileType == FileType.xml:
			writeFile.write(prettyXML(data))
		else:
			if isDebug:
				print data
			else:
				writeFile.write(data)

	writeFile.close()
	print'File written to path: "{}" successfully in {} seconds.'.format(path, time.time() - t1)
	return


def read(path, isDebug=False):
	t1 = time.time()
	data = None
	fileType = splitPath(path)[2]

	with open(path, 'r') as readFile:

		if fileType == FileType.json:
			data = json.load(readFile)

		elif fileType == FileType.xml:
			data = xml.dom.minidom.parse(path)
			root = etree.parse(path).getroot()
			if isDebug:
				print prettyXML(root)

		else:
			data = readFile.read()
			if isDebug:
				print data

	readFile.close()
	print'File read from path "{}" successfully in {} seconds.'.format(path, time.time() - t1)
	return data if data else None


def importFile(path):
	pathQuery = splitPath(path)
	fileDir = pathQuery[0]
	fileName = pathQuery[1]
	fileType = pathQuery[2]
	return read(path)


basicFilter = "*.mb"
singleFilter = "All Files (*.*)"
multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"


def mayaFileBrowse(label='File Browse', fileMode=3, okCaption='OK', fileFilter='directory', *args):
	filepath = cmds.fileDialog2(cap=label, fm=fileMode, okc=okCaption, ff=fileFilter, ds=2)
	if filepath:
		filepath = str(filepath[0])
		return filepath
	else:
		return None


def mayaImportFile(filePath, *args):
	try:
		cmds.file(filePath, i=True)
		print 'File "{}" imported successfuly.'.format(filePath)
	except:
		cmds.error('Unable to import file: "{}".'.format(filePath))
	return filePath


########################################################################################################################
#
#
#	Components
#
#
########################################################################################################################


class Base:
	def __init__(self, filePath, data=None, fileName=None, fileType=None, isDebug=debugMode):
		self.data = data
		self.filePath = filePath
		self.fileDirectory = filePath
		self.fileName = fileName
		self.fileType = fileType
		self.isDebug = isDebug
		self.fileDirectoryExists = False
		self.fileExists = False

		self.organizePaths()
		self.queryExist()

		if self.fileDirectoryExists:
			self.run()

		if self.isDebug:
			self.getDebugInfo()

	def run(self):
		pass

	def organizePaths(self):
		path = splitPath(self.filePath, self.fileName, self.fileType)
		self.fileDirectory = path[0]
		self.fileName = path[1]
		self.fileType = path[2]
		self.filePath = makePath(self.fileDirectory, self.fileName, self.fileType)
		return

	def queryExist(self):
		if self.filePath:
			self.fileExists = os.path.exists(self.filePath)

		if self.fileDirectory:
			self.fileDirectoryExists = os.path.exists(self.fileDirectory)
		return

	def getDebugInfo(self):
		print ''
		for x in sorted(vars(self).iterkeys()):
			print '{}: {}'.format(x, vars(self)[x])
		return vars(self)

	def __str__(self):
		return 'filepath: {}'.format(str(self.filePath))


class Export(Base):
	def __init__(self, filePath, data, fileName=None, fileType=None, isDebug=debugMode):
		Base.__init__(self, filePath, data, fileName, fileType, isDebug)

	def run(self):
		write(self.filePath, self.data, self.isDebug)
		return


class Import(Base):
	def __init__(self, filePath, isDebug=debugMode):
		Base.__init__(self, filePath=filePath, isDebug=isDebug)

	def run(self):
		self.data = read(self.filePath, isDebug=self.isDebug)
		return
