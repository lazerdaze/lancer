# AXEL XML
#
#
#
#
#
'''
Export Import XML - AXML

Build Based on Dictonaries

#Write
doc = xml.setup()
root = xml.element('test')
test2 = xml.element('test2', parent=root)
test3 = xml.element('test3', parent=root, attrs={'one':1, 'two':2})
xml.build(doc=doc, filepath='', isDebug=True)

# Read
doc = xml.readFile('/home/jtirado/maya/scripts/lacie_userData/sphereTest_6_pose.xml')
for obj in xml.getElement('object'):
        print xml.getAttr(obj, 'name')

File Structure

<root metadata='...'>
	<object>
		<name></name>
		<namespace></namespace>
		<type></type>
		<attribute>
			<name></name>
			<type></type>
			<layer>
				<name></name>
				<curve>
					<name></name>
					<type></name>
					<preInfinity></preInfinity>
					<postInfinity></postInfinity>
					<key>
						<time></time>
						<value></value>
						<tangent></tangent>
					</key>
				</curve>
			</layer>
		<attribute>
	</object>
</root>

'''

# Python Modules
import ast
from xml.dom import minidom
from xml.etree import ElementTree as etree


class Axml(object):
	def __init__(self, filepath=None):

		self.filepath = filepath
		self._root = None
		self._exceptions = []
		self._handlers = {}

	def __str__(self):
		return str(self.prettyXML(self._root)) if self._root else ''

	@property
	def root(self):
		return self._root

	@root.setter
	def root(self, root):
		self._root = self.createRoot(root)
		return

	@property
	def exceptions(self):
		return self._exceptions

	@exceptions.setter
	def exceptions(self, exceptions):

		if isinstance(exceptions, (list, tuple, dict)):
			self._exceptions = exceptions

		elif isinstance(exceptions, (str, unicode, object)):
			if exceptions not in self._exceptions:
				self._exceptions.append(exceptions)
		else:
			raise TypeError('Exception must be str or array type.')
		return

	@property
	def handlers(self):
		return self._handlers

	@handlers.setter
	def handlers(self, handlers):
		if isinstance(handlers, dict):
			self._handlers = handlers
		else:
			raise TypeError('Handlers must be type dict: "{tag name: function}"')
		return

	def handleRecursiveElement(self, root):
		if root.tag in self._exceptions:
			return

		if root.tag in self._handlers:
			handler = self._handlers[root.tag]
			handler(root)

		for element in root.getchildren():
			self.handleRecursiveElement(element)
		return

	def toString(self, element):
		return etree.tostring(element)

	def write(self, filepath=None, root=None):
		if not filepath:
			if not self.filepath:
				raise RuntimeError('No filepath specified.')
			else:
				pass
		else:
			self.filepath = filepath

		if not root:
			if self._root is None:
				raise RuntimeError('No Root Element provided specified.')
			else:
				pass
		else:
			self._root = root

		with open(self.filepath, 'w') as writeFile:
			writeFile.write(self.prettyXML(self._root))
		writeFile.close()
		return

	def read(self, filepath=None):
		if not filepath:
			if not self.filepath:
				raise RuntimeError('No filepath specified.')
			else:
				pass
		else:
			self.filepath = filepath

		with open(self.filepath, 'r') as readFile:
			self._root = etree.parse(self.filepath).getroot()
		readFile.close()
		return self._root

	def convertStrToList(self, string):
		value = str(string).replace('[', '').replace(']', '').replace("u'", '').replace("'", '').replace('"', '').split(
				',')
		return [x.strip() for x in value]

	def convertStrToTuple(self, string):
		value = str(string).replace('(', '').replace(')', '').replace("u'", '').replace("'", '').replace('"', '').split(
				',')
		return [x.strip() for x in value]

	def convertStrToDict(self, string):
		return ast.literal_eval(string)

	def createRoot(self, name):
		return etree.Element(name)

	def createElement(self, parent, name, text=None):
		element = etree.SubElement(parent, name)
		if text:
			element.text = text
		return element

	def addAttr(self, element, name, value):
		element.set(str(name), str(value))
		return

	def setAttr(self, element, attribute, value):
		attribute = str(attribute)
		value = str(value)

		if attribute in element.attrib:
			element.set(str(attribute), str(value))
		else:
			raise AttributeError('Element does not have attribute: "{}".'.format(attribute))
		return

	def getAttr(self, element, attribute):
		if attribute not in element.attrib:
			return None
		else:
			value = element.attrib[attribute]

			try:
				result = float(value)
				return result
			except ValueError:
				pass

			try:
				result = int(value)
				return result
			except ValueError:
				pass

			if '[' in value and ']' in value or ',' in value:
				try:
					result = self.convertStrToList(value)
					return result
				except RuntimeError:
					pass

			if '(' in value and ')' in value:
				try:
					result = self.convertStrToTuple(value)
					return result
				except RuntimeError:
					pass

			if '{' in value and '}' in value:
				try:
					result = self.convertStrToList(value)
					return result
				except RuntimeError:
					pass

			return str(value)

	def prettyXML(self, root):
		return minidom.parseString(etree.tostring(root)).toprettyxml()

	def findAll(self, element, tag):
		return element.findall(tag)

	def getAllDescendents(self, element):
		return list(element.iter())

	def getChildren(self, element):
		return element.getchildren()
