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
import library.xfer as xfer
import ults
reload(xfer)
reload(ults)


# Maya Modules
import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim
import maya.cmds as cmds


########################################################################################################################
#
#
#	SKINNING TOOLS
#
#
########################################################################################################################


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


class Export():
	def __init__(self, filepath, mesh, *args):
		self.filepath = filepath
		self.mesh = mesh
		self.skin = getMeshSkinCluster(mesh)

		if self.mesh and self.skin:
			self.data = {self.mesh: {self.skin: self.getData()}}
			xfer.Export(self.filepath, data=self.data, isDebug=False)

		else:
			cmds.error('Export Failed. Mesh: {}. Skin: {}.'.format(self.mesh, self.skin))

	def getData(self):
		data = {}

		for attr in skinClusterAttributes:
			data[attr] = cmds.getAttr('{}.{}'.format(self.skin, attr))

		data['influences'] = [x for x in getSkinClusterInfluences(self.skin)]
		data['weights'] = getSkinWeights(self.skin)

		return data


class Import():
	def __init__(self, filepath, mesh, skin, *args):
		self.filepath = filepath
		self.mesh = mesh
		self.skin = skin

		self.importFile = xfer.Import(self.filepath, isDebug=False)
		self.data = self.importFile.data

		if self.data:
			self.setData()

	def setData(self):
		for mesh, meshValues in self.data.items():
			meshShape = getMeshShapeNode(mesh)

			for skin, skinValues in meshValues.items():
				if cmds.objExists(skin):

					# unlock influences used by skincluster
					for inf in getSkinClusterInfluences(skin):
						cmds.setAttr('{}.liw'.format(inf), 0)

					# normalize needs turned off for the prune to work
					skinNorm = cmds.getAttr('{}.normalizeWeights'.format(self.skin))
					if skinNorm != 0:
						cmds.setAttr('{}.normalizeWeights'.format(self.skin), 0)
					cmds.skinPercent(self.skin, meshShape, nrm=False, prw=100)

					# restore normalize setting
					if skinNorm != 0:
						cmds.setAttr('{}.normalizeWeights'.format(self.skin), skinNorm)

					# remove unused influences
					if inf not in skinValues['influences']:
						cmds.skinCluster(skin, e=True, ri=inf)

					# Set Skin Attributes

					for attribute, attrValue in skinValues.items():
						if attribute not in ['weights', 'influences']:
							print attribute
							cmds.setAttr('{}.{}'.format(skin, attribute), attrValue)

					# Set New Weights
					oldInfIDs = getInfluenceIDs(self.skin)

					for vertID, vertIDValue in skinValues['weights'].items():
						for inf, infValue in vertIDValue.items():
							for infID, infIDValue in infValue.items():
								cmds.setAttr('{}.weightList[{}].weights[{}]'.format(skin,
								                                                    vertID,
								                                                    oldInfIDs[inf]),
								             infIDValue)
							# cmds.skinPercent(skin, '{}.vtx[{}]'.format(mesh, vertID), tv=[inf, infIDValue])
		return


def importSkinWeights(*args):
	selected = ults.getSelected()

	if selected:
		selected = selected[0]
		skinCluster = getMeshSkinCluster(selected)

		if selected and skinCluster:
			filepath = xfer.mayaFileBrowse(label='Import Skin Weights', fileMode=1, okCaption='Import',
			                               fileFilter="*.json")

			if filepath:
				Import(filepath=filepath, mesh=selected, skin=skinCluster)
			else:
				return
		else:
			cmds.error('Import Failed. Mesh: {}. Skin: {}.'.format(selected, skinCluster))

	else:
		cmds.warning('Nothing Selected.')
		return


def exportSkinWeights(*args):
	selected = ults.getSelected()

	if selected:
		selected = selected[0]
		filepath = xfer.mayaFileBrowse(label='Export Skin Weights', fileMode=0, okCaption='Export', fileFilter="*.json")

		if filepath:
			Export(filepath=filepath, mesh=selected)
		else:
			return


#########################################################################################################################
#																														#
#																														#
#	Menu																											#
#																														#
#																														#
#########################################################################################################################

def menu():
	cmds.menuItem(l='Import Skin Weights', c=importSkinWeights)
	cmds.menuItem(l='Export Skin Weights', c=exportSkinWeights)
	return
