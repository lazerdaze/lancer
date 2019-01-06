# LANCER.RIG.SKIN
#
#
#
#
#

"""
- Skinning Method: Classic Linear (Dual Quaterion isn't supported in realtime game engines)
- Max Mesh-Influencing Joints: 75
- Max Total Bones: 256
- Max bones influences per vertex: 4 - 8 (will be normalized)
"""

# Lancer Modules
from library import xfer
from rigging import *
from skeleton import *

# Python Modules
import json
import time

# Maya Modules
import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim
from maya import cmds


########################################################################################################################
#
#
#	SKINNING TOOLS
#
#
########################################################################################################################

def getJointRootFromSkin(skin):
	root = None
	influences = getSkinClusterInfluences(skin)
	for inf in influences:
		if cmds.objectType(inf) == 'joint':
			query = skeleton.getJointRoot(inf)
			if query:
				root = query
				break
	return root


class SkinQuery():
	def __init__(self, mesh):
		self.mesh = mesh
		self.meshShape = getMeshShapeNode(mesh)
		self.meshVertices = getMeshVertex(mesh)
		self.skinCluster = getMeshSkinCluster(mesh)
		self.skinInfluences = getSkinClusterInfluences(self.skinCluster)
		self.maxInfluences = cmds.skinCluster(self.skinCluster, q=True, mi=True)
		self.weightedInfluences = len(cmds.skinCluster(self.skinCluster, q=True, wi=True))

	def __str__(self):
		return str(self.__dict__)


def removeSkinCluster(mesh):
	shape = None

	if cmds.objectType(mesh) == 'transform':
		shape = getMeshShapeNode(mesh)
	elif cmds.objectType(mesh) == 'mesh':
		shape = mesh

	if shape:
		cmds.skinCluster(shape, e=True, ub=True)
		cmds.delete(mesh, ch=True)

	else:
		cmds.warning('Unable to remove skin cluster. Skipped.')
	return


def bindSkinToSkeleton(mesh, root):
	joints = skeleton.getAllJointChildren(root)
	joints.append(root)
	cmds.select(joints)
	cmds.select(mesh, add=True)
	skin = cmds.skinCluster(tsb=True, sm=0, omi=False, mi=8)[0]
	cmds.select(d=True)
	return skin


def setAllSkinWeightsToZero(skin):
	mesh = cmds.listConnections('{}.outputGeometry'.format(skin))[0]
	maxAttr = '{}.maintainMaxInfluences'.format(skin)
	normalAttr = '{}.normalizeWeights'.format(skin)

	if cmds.getAttr(maxAttr) == 1:
		cmds.setAttr(maxAttr, 0)

	cmds.setAttr(normalAttr, 0)

	cmds.skinPercent(skin, mesh, prw=100.0, nrm=False)
	cmds.setAttr(normalAttr, 1)
	return


def getMeshShapeNode(mesh):
	shape = cmds.listRelatives(mesh, s=True)
	if shape:
		return shape[0] if cmds.objectType(shape[0]) == 'mesh' else None
	else:
		return None


def getMeshSkinCluster(mesh):
	typ = cmds.objectType(mesh)
	if typ == 'transform':
		shape = getMeshShapeNode(mesh)
		if shape:
			mesh = shape
			typ = cmds.objectType(mesh)
	if typ == 'mesh':
		conn = cmds.listConnections('{}.inMesh'.format(mesh))
		return conn[0] if cmds.objectType(conn[0]) == 'skinCluster' else None
	else:
		return None


def getMeshVertex(mesh):
	for vert in range(cmds.polyEvaluate(mesh, v=1) + 1):
		yield '{}.vtx[{}]'.format(mesh, vert)


def getSkinClusterInfluences(skin):
	for influence in cmds.skinCluster(skin, q=True, inf=True):
		yield influence


def setMeshMaxSkinWeights(skin, max=8):
	return


def setSkinWights(skin, weights):
	cmds.setAttr('{}.weights[{}]'.format(skin))
	return


def getInfluenceIDs(skin):
	influenceDict = {}

	selList = OpenMaya.MSelectionList()
	selList.add(skin)
	clusterNode = OpenMaya.MObject()
	selList.getDependNode(0, clusterNode)
	skinFn = OpenMayaAnim.MFnSkinCluster(clusterNode)

	infDags = OpenMaya.MDagPathArray()
	skinFn.influenceObjects(infDags)

	for x in xrange(infDags.length()):
		infPath = infDags[x].fullPathName()
		infId = int(skinFn.indexForInfluenceObject(infDags[x]))
		influenceDict[infPath.split('|')[-1]] = infId

	return influenceDict


def getSkinWeights(skin):  # MAYA API
	influenceDict = {}

	# get the MFnSkinCluster for clusterName
	selList = OpenMaya.MSelectionList()
	selList.add(skin)
	clusterNode = OpenMaya.MObject()
	selList.getDependNode(0, clusterNode)
	skinFn = OpenMayaAnim.MFnSkinCluster(clusterNode)

	# get the MDagPath for all influence
	infDags = OpenMaya.MDagPathArray()
	skinFn.influenceObjects(infDags)

	# create a dictionary whose key is the MPlug indice id and
	# whose value is the influence list id
	infIds = {}
	infs = []
	for x in xrange(infDags.length()):
		infPath = infDags[x].fullPathName()
		infId = int(skinFn.indexForInfluenceObject(infDags[x]))
		infIds[infId] = x
		infs.append(infPath)
		influenceDict[infId] = infPath.split('|')[-1]

	# get the MPlug for the weightList and weights attributes
	wlPlug = skinFn.findPlug('weightList')
	wPlug = skinFn.findPlug('weights')
	wlAttr = wlPlug.attribute()
	wAttr = wPlug.attribute()
	wInfIds = OpenMaya.MIntArray()

	# the weights are stored in dictionary, the key is the vertId,
	# the value is another dictionary whose key is the influence id and
	# value is the weight for that influence
	weights = {}
	for vId in xrange(wlPlug.numElements()):
		vWeights = {}
		# tell the weights attribute which vertex id it represents
		wPlug.selectAncestorLogicalIndex(vId, wlAttr)

		# get the indice of all non-zero weights for this vert
		wPlug.getExistingArrayAttributeIndices(wInfIds)

		# create a copy of the current wPlug
		infPlug = OpenMaya.MPlug(wPlug)
		for infId in wInfIds:
			# tell the infPlug it represents the current influence id
			infPlug.selectAncestorLogicalIndex(infId, wAttr)

			# add this influence and its weight to this verts weights
			try:
				# vWeights[infIds[infId]] = infPlug.asDouble()
				vWeights[influenceDict[infId]] = {infIds[infId]: infPlug.asDouble()}

			except KeyError:
				# assumes a removed influence
				pass

		weights[vId] = vWeights

	return weights


def mirrorSkinWeights(mesh=None, skin=None, *args):
	skin = getMeshSkinCluster(mesh) if not skin else skin
	if skin:
		cmds.copySkinWeights(ss=skin,
		                     ds=skin,
		                     mirrorMode='YZ',
		                     surfaceAssociation='closestPoint',
		                     influenceAssociation='oneToOne',
		                     )
	return


def pruneSkinWeights(max=8, *args):
	return


#########################################################################################################################
#																														#
#																														#
#	External																											#
#																														#
#																														#
#########################################################################################################################

skinClusterAttributes = ['skinningMethod',
                         'normalizeWeights',
                         'dropoffRate',
                         'maintainMaxInfluences',
                         'maxInfluences',
                         'bindMethod',
                         'useComponents',
                         'normalizeWeights',
                         'weightDistribution',
                         'heatmapFalloff',
                         ]


class Import:
	def __init__(self, filepath, debug=False, *args):
		self.filepath = filepath
		self.debug = debug
		self.transform = None
		self.mesh = None
		self.skin = None
		self.skinData = None
		self.skeletonRoot = None
		self.skeletonJoints = None
		self.data = xfer.Import(self.filepath, isDebug=False).getData()

		self.organizeData()

	def debugInfo(self):
		return json.dumps(self.data, indent=1)

	def __str__(self):
		value = ''
		for x in vars(self).iterkeys():
			if str(x) != 'data':
				value += '{}: {}\n'.format(x, vars(self)[x])
		return value

	def canProcess(self):
		canProcessList = []

		for obj in [self.transform, self.mesh, self.skeletonRoot]:
			exists = cmds.objExists(obj)
			canProcessList.append(exists)

			if not exists:
				print '''Skin Import: "{}" doesn't exist in scene.'''.format(obj)

		return False if False in canProcessList else True

	def organizeData(self):
		for transform in self.data:
			self.transform = transform
			self.mesh = self.data[transform]['mesh']
			self.skin = self.data[transform]['skinCluster'].keys()[0]
			self.skinData = self.data[transform]['skinCluster']

			self.skeletonRoot = self.data[transform]['skeletonRoot']
			self.skeletonJoints = skeleton.getAllJointChildren(self.skeletonRoot)

			if self.skeletonJoints:
				if self.skeletonRoot not in self.skeletonJoints:
					self.skeletonJoints.append(self.skeletonRoot)
		return

	def cleanMesh(self):
		if self.mesh:
			try:
				removeSkinCluster(self.mesh)
			except:
				print 'Skin Import: Remove Skin Cluster on "{}". Skipped.'.format(self.mesh)
		return

	def bindMeshToSkeleton(self):
		self.cleanMesh()
		self.skin = bindSkinToSkeleton(self.mesh, self.skeletonRoot)
		setAllSkinWeightsToZero(self.skin)
		return

	def processWeights(self):
		if not self.canProcess():
			print self.debugInfo()
			cmds.error('Skin Import Failed: View Script Editor For details.')
			return
		else:
			self.bindMeshToSkeleton()
			maxAttr = '{}.maintainMaxInfluences'.format(self.skin)

			if cmds.getAttr(maxAttr) == 1:
				cmds.setAttr(maxAttr, 0)

			for skin, skinValues in self.skinData.items():

				# Set New Weights
				oldInfIDs = getInfluenceIDs(self.skin)

				for vertID, vertIDValue in skinValues['weights'].items():
					for inf, infValue in vertIDValue.items():
						for infID, infIDValue in infValue.items():
							cmds.setAttr('{}.weightList[{}].weights[{}]'.format(self.skin,
							                                                    vertID,
							                                                    oldInfIDs[inf]),
							             infIDValue
							             )

				# Set Skin Attributes
				for attribute, attrValue in skinValues.items():
					if attribute not in ['weights', 'influences']:
						cmds.setAttr('{}.{}'.format(self.skin, attribute), attrValue)
			return


def importSkinWeights(debug=False, *args):
	filepath = xfer.mayaFileBrowse(label='Import Skin Weights', fileMode=1, okCaption='Import',
	                               fileFilter="*.json")

	if filepath:
		importer = Import(filepath=filepath, debug=debug)

		if debug:
			t1 = time.time()
			print 'Skin Import: Debug Mode {}\n\n'.format('-' * 100)
			print importer, '\n\n'
			print importer.debugInfo(), '\n\n'
			print 'Skin Import Debug Mode: Completed in {} seconds. {}'.format(time.time() - t1, '-' * 100)
			return
		else:
			try:
				t1 = time.time()
				importer.processWeights()
				print 'Skin imported successfully in {} seconds.'.format(time.time() - t1)
				return
			except:
				cmds.error('Skin Import Failed: View Script Editor for details.')
				return
	else:
		print 'Skin Import: Canceled.',
		return


########################################################################################################################
#
#
#	EXPORT
#
#
########################################################################################################################

class Export:
	def __init__(self, filepath=None, mesh=None, debug=False, *args):
		self.filepath = filepath
		self.mesh = mesh
		self.debug = debug
		self.transform = None
		self.skeletonRoot = None
		self.skin = getMeshSkinCluster(mesh)
		self.data = None

		self.organizeMeshData()
		self.calculateData()

	def setFilepath(self, path):
		self.filepath = path
		return

	def setMesh(self, mesh):
		self.mesh = mesh
		self.organizeMeshData()
		self.calculateData()
		return

	def organizeMeshData(self):
		if self.mesh:
			self.skin = getMeshSkinCluster(self.mesh)

			if self.skin:
				self.skeletonRoot = getJointRootFromSkin(self.skin)

			objType = cmds.objectType(self.mesh)
			if objType == 'mesh':
				self.transform = cmds.listRelatives(self.mesh, parent=True)[0]
			elif objType == 'transform':
				self.transform = self.mesh
				self.mesh = getMeshShapeNode(self.mesh)
		return

	def calculateData(self):
		self.data = {
			self.transform: {
				'skeletonRoot': self.skeletonRoot,
				'mesh'        : self.mesh,
				'skinCluster' : {self.skin: self.getSkinData()}
			}
		} if self.mesh and self.skin else None
		return

	def getSkinData(self):
		data = {}

		for attr in skinClusterAttributes:
			data[attr] = cmds.getAttr('{}.{}'.format(self.skin, attr))

		data['influences'] = [x for x in getSkinClusterInfluences(self.skin)]
		data['weights'] = getSkinWeights(self.skin)
		return data

	def saveToFile(self):
		if not self.data:
			self.calculateData()

		if not self.filepath:
			cmds.error('Skin Export Failed: No filepath specified.')
			return

		if self.filepath and self.data:
			xfer.Export(self.filepath, data=self.data, isDebug=False)
			return
		else:
			print self.debugInfo()
			cmds.error('Skin Export Failed: View Script Editor for details.')
			return

	def debugInfo(self):
		return json.dumps(self.data, indent=1)

	def __str__(self):
		value = ''
		for x in vars(self).iterkeys():
			if str(x) != 'data':
				value += '{}: {}\n'.format(x, vars(self)[x])
		return value


def exportSkinWeights(debug=False, *args):
	selected = rigging.getSelected()

	if selected:
		if len(selected) > 1:
			cmds.warning('Skin Export Failed: Select only a single mesh.')
			return
		else:
			mesh = selected[0]

			if not getMeshShapeNode(mesh):
				cmds.warning('Skin Export Failed: Select a mesh.')
				return

			elif not getMeshSkinCluster(mesh):
				cmds.warning('''Skin Export Failed: Mesh doesn't have a skin cluster.''')
				return

			else:
				exporter = Export(mesh=mesh, debug=debug)

				if debug:
					t1 = time.time()
					print 'Skin Export: Debug Mode {}\n\n'.format('-' * 100)
					print exporter, '\n\n'
					print exporter.debugInfo(), '\n\n'
					print 'Skin Export Debug Mode: Completed in {} seconds. {}'.format(time.time() - t1, '-' * 100)
					return
				else:
					filepath = xfer.mayaFileBrowse(label='Export Skin Weights', fileMode=0, okCaption='Export',
					                               fileFilter="*.json")

					if filepath:
						exporter.setFilepath(filepath)
						exporter.saveToFile()
					else:
						print 'Skin Export: Canceled.',
					return
	else:
		cmds.warning('Skin Export Failed: No mesh was selected.')
		return


########################################################################################################################
#
#
#	MENU
#
#
########################################################################################################################

def menu():
	cmds.menuItem(l='Import Skin Weights', c=importSkinWeights)
	cmds.menuItem(l='Export Skin Weights', c=exportSkinWeights)
	return
