'''
AXIE
Animation XML Import Export
Justin Tirado

Notes:
- Add Alphabetical Sorting
- Add Drag Drop / Moving files
- Add Search
- Add Rename File Function
- Add Overwrite File
- Add Select Objects from file
- Add Objects To Item
- Add Offset Animation

Future Stuff:
- Add Meta node Functionality
'''
# PYTHON
import os
import datetime

# MAYA
import maya.cmds as cmds
import maya.mel as mel

# EIXML
from anim.axel.core import eixml

reload(eixml)
xml = eixml.eixml()


class AXIE():

	def __init__(self):

		# Default Directories
		self.scriptDir = os.path.dirname(os.path.abspath(__file__))
		self.prefsFile = os.path.join(self.scriptDir, 'axie_prefs.py')
		self.prefsDir = os.path.join(self.scriptDir, 'axie_files')

		# Global Variables
		self.prefSettings = {}
		self.currentDir = ''
		self.currentGroup = ''
		self.isDebug = False

		# XML Attributes
		self.rootAttr = ['fileName', 'filePath', 'fileType', 'dateModified', 'objects', 'namespaces', 'animLayers',
		                 'frameStartTime', 'frameEndTime', 'frameTotalTime', 'thumbnail']
		self.objectAttr = ['name', 'namespace']
		self.attribAttr = ['name', 'type', 'value']
		self.animCurveAttr = ['name', 'type', 'preInfinity', 'postInfinity', 'weighted']
		self.keyAttr = ['time', 'value', 'inTangent', 'outTangent', 'inAngle', 'outAngle', 'inWeight', 'outWeight',
		                'ix', 'iy', 'ox', 'oy', 'tangentUnity', 'tangentWeight']

		# Images
		self.image1 = 'fileOpen.png'  # File
		self.image2 = 'out_character.png'  # Pose
		self.image3 = 'animPrefsWndIcon.png'  # Animation
		self.image4 = 'refresh.png'  # Refresh
		self.image5 = 'file.svg'  # Placeholder
		self.image6 = 'selectByObject.png'  # Select Objects

		# Functions
		self.startup()

	# File Functions +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	def startup(self, isDebug=True, *args):

		if not os.path.isfile(self.prefsFile):

			confirm = cmds.confirmDialog(t='Setup AXIE', message='Please select a directory to save files.',
			                             button=['Default', 'Browse', 'Cancel'], defaultButton='Default',
			                             cancelButton='Cancel', dismissString='Cancel')

			if confirm == 'Default':
				directory = self.prefsDir

			elif confirm == 'Browse':
				browseDir = self.browseDir()

				if browseDir:
					directory = browseDir
				else:
					directory = self.prefsDir

			if confirm != 'Cancel':
				self.createDir(directory)
				self.writeFile(self.prefsFile, {'directory': directory})
				self.UI()
				self.updateUI(self.prefsFile)

			else:
				print 'AXIE Setup Cancelled.',

		else:
			self.UI()
			self.updateUI(self.prefsFile)

	def createDir(self, filepath, *args):

		if not os.path.exists(filepath):
			os.makedirs(filepath)

	def writeFile(self, filepath, data, *args):

		exportFile = open(filepath, 'w')
		exportFile.write(str(data))
		exportFile.close()

	def readFile(self, filepath, *args):

		importFile = open(filepath, 'r')
		data = eval(importFile.read())
		importFile.close()

		return data

	def updateUI(self, filepath, *args):

		self.currentDir = self.readFile(filepath)['directory']
		self.createDir(self.currentDir)
		self.updateTree()
		cmds.text(self.pathDisplay, e=True, l=self.currentDir)

		print 'AXIE: Update UI'
		print self.currentDir

	def fileGetDirFunction(self, *args):
		filepath = self.browseDir()

		if filepath:
			self.currentDir = filepath
			self.savePrefs()
			self.updateTree()

	def savePrefs(self, *args):

		data = {}
		data['directory'] = self.currentDir
		self.writeFile(self.prefsFile, data)

	def browseDir(self, l='Browse Directories', isDebug=False, *args):
		filepath = cmds.fileDialog2(cap=l, fm=3, okc='Set', ff='directory', ds=2)

		if filepath:
			filepath = str(filepath[0])

		if isDebug:
			print filepath
		return filepath

	def getParentDir(self, filepath, *args):
		removeVar = os.path.basename(filepath)
		parent = os.path.abspath(os.path.join(filepath, os.pardir))

		return parent

	def updateTree(self, *args):
		cmds.treeView(self.tree, e=True, ra=True)

		rootDir = self.currentDir

		for root, dirs, files in os.walk(rootDir):

			if root == rootDir:
				parentName = ''
			else:
				parentName = self.getParentDir(root)

			self.addTreeItem(root, parentName)

			for f in files:
				if '.xml' in f:
					xmlroot = xml.parse(os.path.join(root, f)).attrib
					if 'fileType' in xmlroot:
						self.addTreeItem(os.path.join(root, f), root, typ=xmlroot['fileType'])

	# UI Functions +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	def divider(self, label='', *args):

		if label:

			cmds.rowLayout(nc=2, ad2=2, )
			cmds.text(l=label + '  ', al='left')
			cmds.columnLayout(bgc=[.5, .5, .5], h=1)
			cmds.setParent('..')
			cmds.setParent('..')

		else:

			cmds.columnLayout(h=10, adj=True)
			cmds.columnLayout(bgc=[.5, .5, .5], h=1)
			cmds.setParent('..')
			cmds.setParent('..')

			# Menubar UI Functions +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	def enableDebugMode(self, var, *args):

		self.isDebug = var

	def menuUI(self, *args):

		cmds.menuBarLayout()

		cmds.menu(l='File')
		cmds.menuItem(l='Open Directory', c=self.fileGetDirFunction)

		cmds.menu(l='Create')
		cmds.menuItem(l='Group', i=self.image1, c=self.createGroupDir)
		cmds.menuItem(d=True)

		cmds.menuItem(l='Pose', i=self.image2, c=lambda *_: self.createItemFile(typ='pose'))
		cmds.menuItem(l='Animation', i=self.image3, c=lambda *_: self.createItemFile(typ='anim'))

		cmds.menu(l='Debug')
		cmds.menuItem(l='Enable', cb=False, c=self.enableDebugMode)

		cmds.setParent('..')

	# File Browse UI Functions +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	def textPrompt(self, title='Name', message='Enter Name: ', *args):

		prompt = cmds.promptDialog(title=title, message=message, button=['OK', 'Cancel'], defaultButton='OK',
		                           cancelButton='Cancel', dismissString='Cancel')

		if prompt == 'OK':
			inputName = cmds.promptDialog(query=True, text=True)
			return inputName

		else:
			return None

	def getTreeSelect(self, *args):
		select = cmds.treeView(self.tree, q=True, si=True)

		if select:
			return select[0]
		else:
			return ''

	def getTreeGroup(self, item, *args):

		parent = cmds.treeView(self.tree, q=True, ip=item)

		if parent:
			return parent
		else:
			return ''

	def getTreeChildren(self, item, *args):
		children = cmds.treeView(self.tree, q=True, ch=item)

		if children:
			return children
		else:
			return ''

	def getTreeChildrenFiles(self, filepath, *args):
		ca = []
		for file in os.listdir(filepath):
			if self.isxml(file):
				ca.append(os.path.join(filepath, file))

		return ca

	def isxml(self, item, *args):

		if item.endswith('.xml'):
			return True
		else:
			return False

	def isTreeItem(self, item, *args):

		if cmds.treeView(self.tree, q=True, iex=item):
			return True
		else:
			return False

	def getAnimLayerTree(self, *args):

		root = 'BaseAnimation'
		animLayers = cmds.ls(type='animLayer')

		if animLayers:

			animList = {}

			for x in animLayers:
				animList[x] = cmds.animLayer(x, q=True, parent=True)

			hasParent = set()
			allIitems = {}

			for child, parent in animList.iteritems():
				if parent not in allIitems:
					allIitems[parent] = {}

				if child not in allIitems:
					allIitems[child] = {}

				allIitems[parent][child] = allIitems[child]
				hasParent.add(child)

			result = {}

			for key, value in allIitems.items():
				if key not in hasParent:
					result[key] = value

			return result['']

		return None

	def prettyTree(self, d, indent=0, *args):

		for key, value in d.iteritems():

			print '\t' * indent + str(key)

			if isinstance(value, dict):
				prettyTree(value, indent + 1)

			else:
				print '\t' * (indent + 1) + str(value)

	def isObjectInLayer(self, obj, animLayer, *args):

		objAnimLayers = cmds.animLayer([obj], q=True, affectedLayers=True) or []
		if animLayer in objAnimLayers:
			return True
		else:
			return False

			# Export File ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	def xmlAnimLayer(self, parent, layerName, *args):

		animLayer_node = xml.createElement(parent, 'animLayer')

		xml.addAttr(animLayer_node, 'name', layerName)
		xml.addAttr(animLayer_node, 'parent', cmds.animLayer(layerName, q=True, p=True))
		xml.addAttr(animLayer_node, 'layerMute', int(cmds.animLayer(layerName, q=True, m=True)))
		xml.addAttr(animLayer_node, 'layerSolo', int(cmds.animLayer(layerName, q=True, m=True)))
		xml.addAttr(animLayer_node, 'layerLock', int(cmds.animLayer(layerName, q=True, m=True)))
		xml.addAttr(animLayer_node, 'layerOverride', int(cmds.animLayer(layerName, q=True, o=True)))
		xml.addAttr(animLayer_node, 'layerPassthrough', int(cmds.animLayer(layerName, q=True, pth=True)))
		xml.addAttr(animLayer_node, 'layerWeight', float(cmds.animLayer(layerName, q=True, w=True)))

		return animLayer_node

	def xmlAnimCurve(self, parent, animCurve, attr, *args):

		anim_node = xml.createElement(parent, 'animCurve')

		xml.addAttr(anim_node, 'name', animCurve)
		xml.addAttr(anim_node, 'type', cmds.nodeType(animCurve))
		xml.addAttr(anim_node, 'preInfinity', cmds.setInfinity(attr, at=animCurve, q=True, pri=True)[0])
		xml.addAttr(anim_node, 'postInfinity', cmds.setInfinity(attr, at=animCurve, q=True, poi=True)[0])
		xml.addAttr(anim_node, 'weighted', int(cmds.keyTangent(animCurve, q=True, wt=True)[0]))

		return anim_node

	def xmlKey(self, parent, key, animCurve, *args):

		key_node = xml.createElement(parent, 'key')

		xml.addAttr(key_node, 'time', key)
		xml.addAttr(key_node, 'value', cmds.keyframe(animCurve, q=True, t=(key, key), vc=True)[0])
		xml.addAttr(key_node, 'inTangent', cmds.keyTangent(animCurve, q=True, t=(key, key), itt=True)[0])
		xml.addAttr(key_node, 'outTangent', cmds.keyTangent(animCurve, q=True, t=(key, key), ott=True)[0])
		xml.addAttr(key_node, 'inAngle', cmds.keyTangent(animCurve, q=True, t=(key, key), ia=True)[0])
		xml.addAttr(key_node, 'outAngle', cmds.keyTangent(animCurve, q=True, t=(key, key), oa=True)[0])
		xml.addAttr(key_node, 'inWeight', cmds.keyTangent(animCurve, q=True, t=(key, key), iw=True)[0])
		xml.addAttr(key_node, 'outWeight', cmds.keyTangent(animCurve, q=True, t=(key, key), ow=True)[0])
		xml.addAttr(key_node, 'ix', cmds.keyTangent(animCurve, q=True, t=(key, key), ix=True)[0])
		xml.addAttr(key_node, 'iy', cmds.keyTangent(animCurve, q=True, t=(key, key), iy=True)[0])
		xml.addAttr(key_node, 'ox', cmds.keyTangent(animCurve, q=True, t=(key, key), ox=True)[0])
		xml.addAttr(key_node, 'oy', cmds.keyTangent(animCurve, q=True, t=(key, key), oy=True)[0])
		xml.addAttr(key_node, 'tangentUnity', int(cmds.keyTangent(animCurve, q=True, t=(key, key), l=True)[0]))
		xml.addAttr(key_node, 'tangentWeight', int(cmds.keyTangent(animCurve, q=True, t=(key, key), wl=True)[0]))

		return key_node

	def recurseAnimLayers(self, obj, attr, animLayers, xmlParent):

		for parent, child in animLayers.iteritems():

			layerName = parent

			if self.isObjectInLayer(attr, layerName):

				animLayer_node = self.xmlAnimLayer(xmlParent, layerName)

				# Get Layer Weight Anim Curve

				if cmds.connectionInfo('{0}.weight'.format(layerName), id=True):
					xml.addAttr(animLayer_node, 'layerWeight', 'animCurve')

					animCurve = cmds.connectionInfo('{0}.weight'.format(layerName), sfd=True).split('.')[0]

					weight_node = xml.createElement(animLayer_node, 'weightAnimCurve')

					xml.addAttr(weight_node, 'name', animCurve)
					xml.addAttr(weight_node, 'type', cmds.nodeType(animCurve))
					xml.addAttr(weight_node, 'preInfinity',
					            cmds.setInfinity('{0}.weight'.format(layerName), at=animCurve, q=True, pri=True)[0])
					xml.addAttr(weight_node, 'postInfinity',
					            cmds.setInfinity('{0}.weight'.format(layerName), at=animCurve, q=True, poi=True)[0])
					xml.addAttr(weight_node, 'weighted', int(cmds.keyTangent(animCurve, q=True, wt=True)[0]))

					# Get Weight Keys

					for key in cmds.keyframe(animCurve, q=True):
						key_node = self.xmlKey(weight_node, key, animCurve)

				# Get Base Animation Curves

				if layerName == cmds.animLayer(q=True, root=True):

					connections = cmds.listConnections(attr, type='animBlendNodeBase', s=True, d=False)
					blendNode = None

					while connections:
						blendNode = connections[0]
						connections = cmds.listConnections(blendNode, type='animBlendNodeBase', s=True, d=False)

					input = '{0}.inputA'.format(blendNode)

				# Get Other Layer Animation Curves

				else:

					input = mel.eval('animLayer -q -layeredPlug {0} {1}'.format(attr, layerName))

				# Get AnimCurve Values

				if input:

					animCurve = cmds.connectionInfo(input, sfd=True).split('.')[0]
					anim_node = self.xmlAnimCurve(animLayer_node, animCurve, input)

					# Get Keys

					for key in cmds.keyframe(animCurve, q=True):
						key_node = self.xmlKey(anim_node, key, animCurve)

			# Continue Recursion

			if isinstance(child, dict):
				self.recurseAnimLayers(obj, attr, child, xmlParent)

	def createItemFile(self, objectList=[], typ='pose', *args):

		if not objectList:
			objectList = cmds.ls(sl=True)

		if objectList:

			prompt = self.textPrompt(title='Create {0}'.format(typ.capitalize()))

			if prompt:

				# Create file path

				treeSelect = self.getTreeSelect()

				if treeSelect:
					parentDir = self.getTreeGroup(treeSelect)
				else:
					parentDir = self.currentDir

				filepath = os.path.join(parentDir, prompt)

				if self.isTreeItem(filepath):
					cmds.warning('AXIE: File already exists in current directory.')
					return
				else:

					# XML File ==================================================================================

					totalObjectList = []
					totalNamespaceList = []
					totalAnimLayerList = []
					totalKeyTime = []

					# ROOT

					root_node = xml.createRoot('root')

					xml.addAttr(root_node, 'fileName', os.path.basename(filepath))
					xml.addAttr(root_node, 'filePath', '{0}.xml'.format(filepath))
					xml.addAttr(root_node, 'fileType', typ)
					xml.addAttr(root_node, 'dateModified', datetime.datetime.now().strftime('%Y/%m/%d %I:%M%p'))

					# ThumbNail

					if not self.isDebug:
						xml.addAttr(root_node, 'thumbnail', self.exportThumb(filepath))

					# Query Animation Layers
					'''
					animLayerList = cmds.treeView('AnimLayerTabanimLayerEditor', q=True, children=True)
					animLayerSelect = cmds.treeView('AnimLayerTabanimLayerEditor', q=True, selectItem=True)

					animExport = animLayerList #<<<<<<<<< All Animation Layers | Need to add if layer is selected
					'''
					animLayers = self.getAnimLayerTree()

					# Get Object Data ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

					for obj in objectList:

						# Get Name space

						if ':' in obj:
							name = str(obj.split(':')[-1])
							namespace = str(obj.split(':')[0])

						else:
							name = obj
							namespace = ''

						if namespace not in totalNamespaceList:
							totalNamespaceList.append(str(namespace))

						totalObjectList.append(str(name))

						# OBJECT

						object_node = xml.createElement(root_node, 'object')
						xml.addAttr(object_node, 'name', name)
						xml.addAttr(object_node, 'namespace', namespace)

						# ATTRIBUTES

						for attr in cmds.listAttr(obj, k=True):

							attrName = '{0}.{1}'.format(obj, attr)
							attrType = cmds.getAttr(attrName, type=True)
							attrValue = cmds.getAttr(attrName)

							attr_node = xml.createElement(object_node, 'attribute')
							xml.addAttr(attr_node, 'name', attr)
							xml.addAttr(attr_node, 'type', attrType)

							# If file type is pose +++++++++++++++++++++++++++++++++++++++++++++++++

							if typ == 'pose' or not cmds.connectionInfo(attrName, id=True):

								if attrType == 'bool' or attrType == 'enum':
									staticVar = int(cmds.getAttr(attrName))
								else:
									staticVar = float(cmds.getAttr(attrName))

								xml.addAttr(attr_node, 'value', staticVar)



							# If file type is animation ++++++++++++++++++++++++++++++++++++++++++++

							elif typ == 'anim':

								# Save Animation Values

								connection = cmds.connectionInfo(attrName, sfd=True).split('.')[0]
								connectionType = cmds.nodeType(connection)

								# Regular Anim Curves

								if connectionType.startswith('animCurve'):

									# Skip Set Driven Keys

									if cmds.connectionInfo('{0}.input'.format(connection), id=True):

										object_node.remove(attr_node)

									else:

										animLayer_node = xml.createElement(attr_node, 'animLayer')
										xml.addAttr(animLayer_node, 'name', 'BaseAnimation')
										xml.addAttr(animLayer_node, 'parent', '')

										# AnimCurve

										animCurve = cmds.connectionInfo(attrName, sfd=True).split('.')[0]
										anim_node = self.xmlAnimCurve(animLayer_node, animCurve, attrName)

										# Get Keys

										for key in cmds.keyframe(animCurve, q=True):
											key_node = self.xmlKey(anim_node, key, animCurve)

											# Anim Layers +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

								elif connectionType.startswith('animBlendNodeAdditive'):

									self.recurseAnimLayers(obj, attrName, animLayers, attr_node)

					# Update Root Info

					xml.addAttr(root_node, 'objects', totalObjectList)
					xml.addAttr(root_node, 'namespaces', totalNamespaceList)

					if typ == 'anim':
						# Anim Layer Tree

						xml.addAttr(root_node, 'animLayers', animLayers)

						'''
						xml.addAttr(root_node, 'animLayers', totalAnimLayerList)

						xml.addAttr(root_node, 'frameStartTime', int(min(totalKeyTime)))
						xml.addAttr(root_node, 'frameEndTime', int(max(totalKeyTime)))
						xml.addAttr(root_node, 'frameTotalTime', int(max(totalKeyTime) - min(totalKeyTime)))
						'''

					# Write To File ================================================================================

					xml.build(root_node, filepath, isDebug=self.isDebug)

					# Update UI ====================================================================================

					cmds.treeView(self.tree, e=True, ra=True)
					self.updateTree()

					print "AXIE: File '{0}.xml' was created successfully.".format(filepath),
					return

		else:
			cmds.warning('AXIE: Nothing Selected')
			return

	def doesObjectExist(self, obj, namespace='', *args):

		if not namespace:
			if ':' in obj:
				namespace = obj.split(':')[0]
				obj = obj.split(':')[-1]

		objNamespace = '{0}:{1}'.format(namespace, obj)
		namespaceWild = '*:{0}*'.format(obj)

		if cmds.objExists(objNamespace):
			return objNamespace

		elif cmds.objExists(namespaceWild):
			return namespaceWild

		elif cmds.objExists(obj):
			return obj

		else:
			return None

	def doesAttrExist(self, obj, attr, *args):

		if cmds.attributeQuery(attr, node=obj, ex=True):
			return True
		else:
			return False

	def importItemFile(self, filepath, *args):

		# Parse XML file

		root = xml.parse(filepath, isDebug=self.isDebug)

		# Get FileType

		fileType = root.attrib['fileType']

		# Apply Data

		for obj in root:
			objVar = self.doesObjectExist(obj.attrib['name'], obj.attrib['namespace'])

			if objVar:
				for attr in obj:

					# Attributes

					attribute = attr.attrib['name']
					defaultAttr = '{0}.{1}'.format(objVar, attribute)

					# If filetype is pose +++++++++++++++++++++++++++++++++++++++++++++++++

					if fileType == 'pose':

						if 'value' in attr.attrib:
							cmds.setAttr('{0}.{1}'.format(objVar, attr.attrib['name']), float(attr.attrib['value']))

					# If filetype is anim +++++++++++++++++++++++++++++++++++++++++++++++++

					elif fileType == 'anim':

						# Get Anim Layers

						animLayerList = cmds.treeView('AnimLayerTabanimLayerEditor', q=True, children=True)
						animLayerSelect = xml.convertStrToList(root.attrib['animLayers'])

						for layer in animLayerSelect:
							if animLayerList == None or layer not in animLayerList:
								if layer != 'BaseAnimation':
									# Create Anim Layer
									cmds.animLayer(layer)

									# Get Anim Curve

						for animCurve in attr:

							animLayerName = animCurve.attrib['animLayer']
							curveName = animCurve.attrib['name']
							curveWeight = animCurve.attrib['weighted']
							postI = animCurve.attrib['postInfinity']
							preI = animCurve.attrib['preInfinity']

							# cmds.animLayer(animLayerName, e= True, at= defaultAttr)

							if animLayerName in animLayerSelect:

								# Get Keys

								for key in animCurve:

									time = float(key.attrib['time'])
									value = float(key.attrib['value'])

									inAngle = float(key.attrib['inAngle'])
									outAngle = float(key.attrib['outAngle'])

									inTangent = str(key.attrib['inTangent'])
									outTangent = str(key.attrib['outTangent'])

									inWeight = float(key.attrib['inWeight'])
									outWeight = float(key.attrib['outWeight'])

									ix = float(key.attrib['ix'])
									iy = float(key.attrib['iy'])

									ox = float(key.attrib['ox'])
									oy = float(key.attrib['oy'])

									tangentUnity = 1 if key.attrib['tangentUnity'] == 'True' else 0
									tangentWeight = 1 if key.attrib['tangentWeight'] == 'True' else 0

									# Set Key

									try:
										# cmds.setKeyframe(objVar, at=attribute, t=time, animLayer=animLayerName, v=value, nr=True) # Animation Layer Version

										cmds.setKeyframe(objVar, at=attribute, t=time, v=value, nr=True)
										cmds.keyTangent(objVar, at=attribute, t=(time, time), ix=ix, iy=iy, ox=ox,
										                oy=oy, l=tangentUnity, wl=tangentWeight, itt=inTangent,
										                ott=outTangent)
									except:
										pass
								cmds.setInfinity(objVar, at=attribute, pri=preI, poi=postI)
			else:
				print 'AXIE: Object "{0}" not in scene. Skipped.'.format(obj.attrib['name'])

	def createGroupDir(self, *args):

		prompt = self.textPrompt(title='Create Group')

		if prompt:

			select = self.getTreeSelect()

			if select:
				parentDir = self.getTreeGroup(select)
			else:
				parentDir = self.currentDir

			filepath = os.path.join(parentDir, prompt)

			if self.isTreeItem(filepath):
				cmds.warning('AXIE: Group already exists in current directory.')
				return
			else:
				self.createDir(filepath)
				cmds.treeView(self.tree, e=True, ra=True)
				self.updateTree()

				print "AXIE: Directory '{0}' was created successfully.".format(filepath),

	def addTreeItem(self, n, parent='', typ='group', niceName=True, *args):

		cmds.treeView(self.tree, e=True, addItem=(n, parent))

		if typ == 'group':
			cmds.treeView(self.tree, e=True, i=(n, 1, self.image1), fn=(n, 'boldLabelFont'), ff=(n, 1))

		elif typ == 'pose':
			cmds.treeView(self.tree, e=True, i=(n, 1, self.image2))

		elif typ == 'anim':
			cmds.treeView(self.tree, e=True, i=(n, 1, self.image3))

		if niceName:
			cmds.treeView(self.tree, e=True, ibc=(n, 1, 1), dl=(n, self.niceName(n)))
		else:
			cmds.treeView(self.tree, e=True, ibc=(n, 1, 1))

	def niceName(self, var, *args):

		newvar = os.path.basename(var).split('.xml')[0].replace('_', ' ')
		return newvar

	def exportThumb(self, filepath, ext='jpg', w=200, h=200, *args):

		imagefilepath = '{0}_thumbnail.{1}'.format(filepath, ext)

		focus = cmds.getPanel(wf=True)

		if cmds.modelPanel(focus, q=True, exists=True):
			# Get Camera Info

			focusCam = cmds.modelPanel(focus, q=True, cam=True)
			focusCamShape = cmds.listRelatives(focusCam, shapes=True)[0]

			# Set Pan Zoom

			cmds.setAttr(focusCamShape + '.panZoomEnabled', 1)
			cmds.panZoom(focusCamShape, abs=True, l=0, u=0, z=0.50)

			# Create Window w/ Model Editor

			cmds.window('pbWin')
			cmds.paneLayout()
			pbPanel = cmds.modelPanel(cam=focusCam)

			cmds.modelEditor(pbPanel,
			                 e=True,
			                 allObjects=False,
			                 manipulators=True,
			                 grid=False,
			                 sel=False,
			                 polymeshes=True,
			                 imagePlane=True,
			                 displayAppearance='smoothShaded',
			                 ignorePanZoom=False,
			                 )

			# Playblast

			cmds.playblast(epn=pbPanel, p=100, wh=(w, h), fr=cmds.currentTime(q=True), fmt='image', cf=imagefilepath,
			               c=ext, fo=True, v=False, orn=False, os=True, sqt=False, qlt=100)

			# Remove UI

			cmds.deleteUI('pbWin', window=True)

			# Reset Pan Zoom

			cmds.setAttr(focusCamShape + '.panZoomEnabled', 0)
			return imagefilepath

	def updateButtonUI(self, item, *args):
		group = ''

		if not self.isxml(item):
			group = item

		else:
			group = self.getTreeGroup(item)

		if group:
			if group != self.currentGroup:

				gridCa = cmds.gridLayout(self.buttonGrid, q=True, ca=True)
				tempLayout = cmds.columnLayout(m=False)
				cmds.setParent('..')

				if gridCa:
					for ca in gridCa:
						cmds.control(ca, e=True, p=tempLayout)

				cmds.evalDeferred(lambda *_: cmds.deleteUI(tempLayout, layout=True))

				ca = self.getTreeChildrenFiles(group)
				for x in ca:
					xmlroot = xml.parse(x).attrib
					self.button(l=x, i=self.hasThumbnail(xmlroot))

				self.currentGroup = group

	def hasThumbnail(self, dict, *args):

		if 'thumbnail' in dict:
			thumbImage = dict['thumbnail']

		else:
			thumbImage = self.image5

		return thumbImage

	def objectExistsList(self, list, *args):

		var = []
		for obj in list:
			if not cmds.objExists(obj):
				if not cmds.objExists('*:{0}*'.format(obj)):
					var.append(obj)

		return var

	def selectItemFunction(self, item, *args):

		if item:
			# Update Button Grid

			self.updateButtonUI(item)

			if self.isxml(item):

				cmds.scrollField(self.objectWarningDisplay, e=True, vis=False)

				# Update InfoDisplay Pane

				xmlroot = xml.parse(item).attrib

				# Get Display Data

				infoStr1 = ''
				infoStr2 = ''
				skip = ['thumbnail', 'filePath', 'objects', 'animLayers']

				for attr in self.rootAttr:

					if attr not in skip:
						if attr in xmlroot:

							infoStr1 += '{0}:\n'.format(attr.capitalize())

							if xmlroot[attr].startswith('['):

								attrList = xml.convertStrToList(xmlroot[attr])
								for y in attrList:

									infoStr2 += '{0}\n'.format(y)

									if attrList.index(y) > 0:
										infoStr1 += '\n'
							else:
								infoStr2 += '{0}\n'.format(xmlroot[attr])

				cmds.text(self.infoDisplayUI1, e=True, l=infoStr1)
				cmds.text(self.infoDisplayUI2, e=True, l=infoStr2)

				# Get Missing Objects

				if 'objects' in xmlroot:
					objInFile = xml.convertStrToList(xmlroot['objects'])

					objNotInScene = self.objectExistsList(xml.convertStrToList(xmlroot['objects']))

					if objNotInScene:
						infoStr3 = 'Objects {0} of {1} not in scene:\n\n'.format(len(objNotInScene), len(objInFile))

						for x in objNotInScene:
							infoStr3 += '{0}\n'.format(x)

						cmds.scrollField(self.objectWarningDisplay, e=True, tx=infoStr3, vis=True)

					else:
						cmds.scrollField(self.objectWarningDisplay, e=True, tx='', vis=False)

				cmds.iconTextButton(self.infoDisplayImage, e=True, i=self.hasThumbnail(xmlroot))

				cmds.image(self.infoDisplayTypeImage, e=True,
				           i=self.image2 if xmlroot['fileType'] == 'pose' else self.image3)
				cmds.text(self.infoDisplayType, e=True, l=xmlroot['fileType'].upper())

				cmds.button(self.importFileButton, e=True, c=lambda *_: self.importItemFile(item))

	def fileBrowseUI(self, *args):

		form = cmds.formLayout()

		topButtons = cmds.columnLayout(adj=True)

		cmds.rowLayout(nc=4)
		cmds.iconTextButton(i=self.image1, st='iconOnly', sic=True, ann='Create Group')
		cmds.iconTextButton(i=self.image2, st='iconOnly', sic=True, ann='Create Pose')
		cmds.iconTextButton(i=self.image3, st='iconOnly', sic=True, ann='Create Animation')
		cmds.iconTextButton(i=self.image4, st='iconOnly', sic=True, ann='Refresh', c=self.updateTree)
		cmds.setParent('..')

		cmds.setParent('..')

		self.tree = cmds.treeView(nb=1, adr=False, ams=False, arp=False, enk=True,
		                          scc=lambda *_: self.selectItemFunction(self.getTreeSelect()))  # <<<<<< GLOBAL TREE UI

		cmds.setParent('..')

		cmds.formLayout(form, edit=True,
		                attachForm=[(topButtons, 'top', 0), (topButtons, 'left', 0), (topButtons, 'right', 0),
		                            (self.tree, 'left', 0), (self.tree, 'bottom', 0), (self.tree, 'right', 0)],
		                attachControl=[(self.tree, 'top', 0, topButtons)])

	# Icon Button UI Functions +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	def scaleUI(self, size, *args):

		cmds.gridLayout(self.buttonGrid, e=True, cwh=(size, size))

	def updateThumbnail(self, filepath, control, *args):

		thumbVar = self.exportThumb(filepath.split('.')[0])
		xml.editRoot(filepath, 'thumbnail', thumbVar)

		cmds.iconTextButton(control, e=True, i=self.image5)
		cmds.iconTextButton(self.infoDisplayImage, e=True, i=self.image5)

		cmds.iconTextButton(control, e=True, i=thumbVar)
		cmds.iconTextButton(self.infoDisplayImage, e=True, i=thumbVar)

	def button(self, l, i='', *args):

		cmds.frameLayout(mw=1, mh=1, lv=False, p=self.buttonGrid, )

		control = cmds.iconTextButton(l='{0}'.format(self.niceName(l)), st='iconAndTextVertical', sic=True, fla=False,
		                              ann=l, bgc=[1, .5, 0], c=lambda *_: self.selectItemFunction(l))
		if i:
			cmds.iconTextButton(control, e=True, i=i)
		else:
			cmds.iconTextButton(control, e=True, i='file.svg')

		cmds.setParent('..')

		cmds.popupMenu(p=control, b=3)
		cmds.menuItem(l='Update Thumbnail', i=self.image5,
		              c=lambda *_: self.updateThumbnail(l, cmds.control(control, q=True, fpn=True)))
		cmds.menuItem(d=True)
		cmds.menuItem(l='Update Pose', i=self.image2, enable=False)
		cmds.menuItem(d=True)
		cmds.menuItem(l='Select Objects from File', i=self.image6, enable=False)

		return control

	def buttonUI(self, *args):

		form = cmds.formLayout()
		scaleUI = cmds.intSlider(min=50, max=200, v=100, h=25)
		UI = cmds.scrollLayout(cr=True)

		form2 = cmds.formLayout()
		self.buttonGrid = cmds.gridLayout(nc=1, cr=True, aec=False, cwh=(100, 100))
		cmds.setParent('..')
		cmds.setParent('..')

		cmds.setParent('..')
		cmds.setParent('..')

		cmds.intSlider(scaleUI, e=True, dc=lambda *_: self.scaleUI(size=cmds.intSlider(scaleUI, q=True, v=True)))

		cmds.formLayout(form, e=True,
		                attachForm=[(scaleUI, 'top', 0), (scaleUI, 'left', 0), (scaleUI, 'right', 0), (UI, 'left', 0),
		                            (UI, 'bottom', 0), (UI, 'right', 0)], attachControl=[(UI, 'top', 0, scaleUI)])
		cmds.formLayout(form2, e=True, attachForm=[(self.buttonGrid, 'top', 0), (self.buttonGrid, 'left', 0),
		                                           (self.buttonGrid, 'right', 0), (self.buttonGrid, 'bottom', 0)])

	# Info / Import UI +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	def infoUI(self, *args):

		cmds.columnLayout(adj=True)
		cmds.frameLayout(mw=10, mh=10, lv=False)

		self.infoDisplayImage = cmds.iconTextButton(sic=True, st='iconAndTextVertical', w=200, h=200, )

		cmds.rowLayout(nc=2, adj=2)
		self.infoDisplayTypeImage = cmds.image(i='info.png')
		self.infoDisplayType = cmds.text(l='Info.', al='left', fn='boldLabelFont')
		cmds.setParent('..')

		self.divider()

		cmds.rowLayout(nc=2, ad2=2, rat=[(1, 'top', 0), (2, 'top', 0)])
		self.infoDisplayUI1 = cmds.text(l='', al='right', fn='boldLabelFont')
		self.infoDisplayUI2 = cmds.text(l='', al='left', )
		cmds.setParent('..')

		self.objectWarningDisplay = cmds.scrollField(editable=False, wordWrap=False, font='tinyBoldLabelFont', h=100,
		                                             text='', vis=False)

		self.importFileButton = cmds.button(l='Import')

		cmds.setParent()
		cmds.setParent()

	# Build UI Window ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	def UI(self):
		winName = 'axie_windowUI'

		if cmds.window(winName, exists=True):
			cmds.deleteUI(winName, window=True)
			cmds.windowPref(winName, ra=True)

		cmds.window(winName, title='AXIE - Animation XML Import | Exporter', rtf=True, mxb=False)

		# MenuBar UI ==============
		self.menuUI()

		# Start UI ================
		form = cmds.formLayout(w=1000, h=750)

		pathDisplay = cmds.text(al='left', h=20)

		pane = cmds.paneLayout(cn='vertical3', ps=[(1, 40, 0), (2, 70, 0), (3, 10, 0), ], st=1)
		self.fileBrowseUI()
		self.buttonUI()
		self.infoUI()
		cmds.setParent('..')

		# End UI ==================
		cmds.setParent('..')  # formEnd

		cmds.formLayout(form, edit=True,
		                attachForm=[(pane, 'top', 0), (pane, 'left', 0), (pane, 'right', 0), (pathDisplay, 'bottom', 0),
		                            (pathDisplay, 'left', 0), (pathDisplay, 'right', 0)],
		                attachControl=[(pane, 'bottom', 0, pathDisplay)])
		self.pathDisplay = pathDisplay
		cmds.showWindow(winName)


AXIE()
