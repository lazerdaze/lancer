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


def pathJoin(*args):
	return os.path.join(*args)


def pathEnd(path):
	return os.path.basename(path)


def pathExists(path):
	return os.path.exists(path)


def fileExists(path):
	return os.path.isfile(path)


########################################################################################################################
#
#
#	Components
#
#
########################################################################################################################


class FileType:
	ma = 'ma'
	mb = 'mb'
	fbx = 'fbx'
	txt = 'txt'
	py = 'py'
	obj = 'obj'
	json = 'json'
	xml = 'xml'

	def __init__(self):
		pass


debugMode = True


class Base:
	def __init__(self, data=None, filePath=None, fileName=None, fileType=None, isDebug=debugMode):
		self.data = data
		self.filePath = filePath
		self.fileDirectory = filePath
		self.fileName = fileName
		self.fileType = fileType
		self.fileDirectoryExists = False
		self.fileExists = False
		self.isDebug = isDebug

		self.makeFileName()
		self.makeFilePath()
		self.makeFileDirectory()
		self.queryExist()

		if self.isDebug:
			self.getDebugInfo()

	def makeFileName(self):

		end = pathEnd(self.filePath)

		if not self.fileName:
			if self.filePath:
				if '.' in end:
					self.fileName = end.split('.')[0]
					self.fileType = end.split('.')[-1]
				else:
					self.fileName = end if end else None

		else:
			if '.' in self.fileName:
				self.fileType = self.fileName.split('.')[-1]
				self.fileName = self.fileName.split('.')[0]

		if not self.fileType:
			if self.fileName:
				if '.' in self.fileName:
					self.fileType = self.fileName.split('.')[-1]

			elif self.filePath:
				if '.' in end:
					self.fileType = end.split('.')[-1]

	def makeFilePath(self):
		pathE = pathEnd(self.filePath)
		end = '{}.{}'.format(self.fileName, self.fileType)

		if self.filePath:
			if self.fileName == pathE:
				if '.' not in pathE:
					if self.fileType:
						self.filePath = '{}.{}'.format(self.filePath, self.fileType)
			else:
				if self.fileName and self.fileType:
					if end != pathE:
						self.filePath = pathJoin(self.filePath, end)
				else:
					if self.fileName:
						self.filePath = pathJoin(self.filePath, self.fileName)

	def makeFileDirectory(self):
		end = pathEnd(self.filePath)
		if self.filePath:
			if not end:
				self.fileDirectory = self.filePath
			else:
				self.fileDirectory = os.path.dirname(self.filePath)

	def queryExist(self):
		if self.filePath:
			self.fileExists = os.path.exists(self.filePath)

		if self.fileDirectory:
			self.fileDirectoryExists = os.path.exists(self.fileDirectory)

	def read(self):
		data = None

		if self.fileExists:
			if self.fileType == FileType.txt:
				readFile = open(self.filePath, 'r')
				data = readFile.readlines()
				readFile.close()
			elif self.fileType == FileType.json:
				data = json.load(open(self.filePath))

		self.data = data
		return self.data

	def write(self):
		if self.isDebug:
			return
		else:
			writeFile = open(self.filePath, 'w')
			writeFile.write(self.data)
			writeFile.close()
			return self.filePath

	def getDebugInfo(self):
		for x in sorted(vars(self).iterkeys()):
			print '{}: {}'.format(x, vars(self)[x])
		return vars(self)

	def __str__(self):
		return 'filepath: {}'.format(str(self.filePath))


bang = Base(filePath='/Users/hypebox/PycharmProjects/lancer/test_data/read_test.json')
print bang.read()


class Export(Base):
	def __init__(self, data, filePath, fileName=None, fileType=None):
		Base.__init__(self, data, filePath, fileName, fileType)


class Import(Base):
	def __init__(self, data, filePath, fileName=None, fileType=None):
		Base.__init__(self, data, filePath, fileName, fileType)
