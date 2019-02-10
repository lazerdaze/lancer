# Lancer Modules
from library.axml import Axml
from library import xfer

# Python Modules
import os
from xml.etree import ElementTree as etree


class Templates(Axml):
	def __init__(self, directory=None, *args, **kwargs):
		Axml.__init__(self, *args, **kwargs)

		self.directory = os.path.dirname(os.path.abspath(__file__)) if not directory else directory
		self.root = 'root'

		for file in xfer.getAllFilesInPath(self.directory):
			if file.endswith('.xml'):
				self.read(file)

	def read(self, filepath=None):
		if not filepath:
			if not self.filepath:
				raise RuntimeError('No filepath specified.')
			else:
				pass
		else:
			self.filepath = filepath

		with open(self.filepath, 'r') as readFile:
			self.root.append(etree.parse(self.filepath).getroot())
		readFile.close()
		return

	def templateExists(self, template):
		if self.findAll(self.root, template):
			return True
		return False

	def getTemplate(self, template):
		query = self.findAll(self.root, template)
		if not query:
			raise KeyError('"{}" is not a valid template.'.format(template))
		else:
			for item in query:
				if item == template:
					return item
		return query
