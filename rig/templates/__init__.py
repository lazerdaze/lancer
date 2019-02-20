# Lancer Modules
from library.axml import Axml
from library import xfer

# Python Modules
import os
from xml.etree import ElementTree as etree

TEMPLATE_EXPORT_HANDLER = {
	'definition': None,
	'rig'       : None,
	'hik'       : None,
}
TEMPLATE_IMPORT_HANDLER = {
	'definition': None,
	'rig'       : None,
	'hik'       : None,
}


# TODO: Need to figure out handler operations for future use.
class Templates(Axml):
	def __init__(self, *args, **kwargs):
		Axml.__init__(self, *args, **kwargs)

		self.directory = os.path.dirname(os.path.abspath(__file__))
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
			root = etree.parse(self.filepath).getroot()

			if root.tag == 'template':
				self.root.append(root)

		readFile.close()
		return

	def templateExists(self, name):
		for template in self.findAll(self.root, 'template'):
			attributes = template.attrib

			if 'name' in attributes:
				if name == attributes['name']:
					return True
		return False

	def getTemplate(self, name):
		query = self.findAll(self.root, 'template')

		if not self.templateExists(name):
			raise KeyError('"{}" is not a valid template.'.format(name))
		else:
			for item in query:
				if 'name' in item.attrib and name == item.attrib['name']:
					return item
		raise RuntimeError('Unable to provide a valid template.')

	def getTemplateDefinition(self, name):
		template = self.getTemplate(name)
		query = self.findAll(template, 'definition')

		if not query:
			raise KeyError('Template does not contain definitions.'.format(name))

		return query[0]

	def getTemplateRig(self, name):
		template = self.getTemplate(name)
		query = self.findAll(template, 'rig')

		if not query:
			raise KeyError('Template does not contain rig.'.format(name))

		return query[0]

	def getTemplateHIK(self, name):
		template = self.getTemplate(name)
		query = self.findAll(template, 'hik')

		if not query:
			raise KeyError('Template does not contain hik.'.format(name))

		return query[0]
