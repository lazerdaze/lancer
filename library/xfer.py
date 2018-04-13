#
#
#
# xfer.py
#
#
#


import os
import sys
import collections
from contextlib import contextmanager

import json

import xml
import xml.dom
from xml.dom import minidom
from xml.dom.minidom import Document
from xml.dom.minidom import parse
from xml.etree import ElementTree as etree

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
	for x in [path, fileName, fileType]:
		if x:
			if x not in newPath:
				newPath = pathJoin(newPath, x)
	return newPath


def prettyXML(root):
	return minidom.parseString(etree.tostring(root)).toprettyxml()


def write(path, data=None, isDebug=False):
	fileType = splitPath(path)[2]

	with open(path, 'w') as writeFile:
		if isDebug:
			print''
			print'Start writing to file: "{}"'.format(path)

		if fileType == FileType.json:
			if isDebug:
				print data
			else:
				json.dump(data, writeFile)
		elif fileType == FileType.xml:
			if isDebug:
				print data
			else:
				writeFile.write(prettyXML(data))
		else:
			if isDebug:
				print data
			else:
				writeFile.write(data)

	writeFile.close()
	if isDebug:
		print'End writing to file.'
		print''
	return


def read(path, isDebug=False):
	data = None
	fileType = splitPath(path)[2]

	with open(path, 'r') as readFile:
		if isDebug:
			print''
			print'Start reading from file: "{}"'.format(path)

		if fileType == FileType.json:
			data = json.load(readFile)
			if isDebug:
				print json.dumps(data, indent=4)

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

	if isDebug:
		print'End reading from file.'
		print''

	return data if data else None


def importFile(path):
	pathQuery = splitPath(path)
	fileDir = pathQuery[0]
	fileName = pathQuery[1]
	fileType = pathQuery[2]
	return read(path)


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

		if self.isDebug:
			self.getDebugInfo()

		if self.fileDirectoryExists:
			self.run()
		else:
			print None

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
		for x in sorted(vars(self).iterkeys()):
			print '{}: {}'.format(x, vars(self)[x])
		return vars(self)

	def __str__(self):
		return 'filepath: {}'.format(str(self.filePath))


class Export(Base):
	def __init__(self, filePath, data, fileName=None, fileType=None):
		Base.__init__(self, filePath, data, fileName, fileType)

	def run(self):
		write(self.filePath, self.data, self.isDebug)
		return


class Import(Base):
	def __init__(self, filePath, data, fileName=None, fileType=None):
		Base.__init__(self, filePath, data, fileName, fileType)

	def run(self):
		read(self.filePath, isDebug=self.isDebug)
		return
