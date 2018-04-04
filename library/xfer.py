#
#
#
# xfer.py
#
#
#


import os
import sys
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


def pathFile(path):
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


class ComponentType:
	py = 'py'
	text = 'txt'
	json = 'json'
	xml = 'xml'

	def __init__(self):
		pass


isDebug = True

class Base:
	def __init__(self, data=None, filePath=None, fileName=None, fileType=None, isDebug=isDebug):
		self.data = data
		self.filePath = filePath
		self.fileName = fileName
		self.fileType = fileType
		self.isDebug = isDebug

		self.makeFileName()
		self.makeFilePath()

		if self.isDebug:
			self.getDebugInfo()

	def makeFileName(self):
		if self.fileName and self.fileType:
			self.fileName = '{}.{}'.format(self.fileName, self.fileType)

	def makeFilePath(self):
		path = ''
		for x in [self.filePath, self.fileName]:
			if x:
				path = pathJoin(path, x)

		self.filePath = path if path else None

	def getDebugInfo(self):
		for x in vars(self):
			print '{}: {}'.format(x, vars(self)[x])
		return vars(self)

	def __str__(self):
		return 'Filepath: {}'.format(str(self.filePath))


class Export(Base):
	def __init__(self, data, filePath, fileName=None, fileType=None):
		Base.__init__(self, data, filePath, fileName, fileType)


Base()


class Import(Base):
	def __init__(self, data, filePath, fileName=None, fileType=None):
		Base.__init__(self, data, filePath, fileName, fileType)
