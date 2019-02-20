# LANCER.RIG.FACEPOSE.CORE
#
#
#
#
#


# Maya Modules
import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om


########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################


ANIMCURVES = ['animCurveUL',
              'animCurveUU',
              'animCurveUA',
              'animCurveUT'
              ]


class types(object):
	blendWeighted = 'blendWeighted'
	animCurve = 'animCurve'
	unitConversion = 'unitConversion'


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################


class query(object):
	def __init__(self, dag):
		self.dag = dag

		self.attributes = self.getAttributes(dag)
		self.animCurves = []
		self.blendWeighted = []
		self.data = self.getData(dag)

	@staticmethod
	def getAttributes(dag):
		attributes = {}
		attrQuery = cmds.listAttr(dag, k=True)

		if attrQuery:
			for attr in attrQuery:
				conn = cmds.listConnections('{}.{}'.format(dag, attr))
				if conn:
					attributes[attr] = conn[0]
		return attributes if attributes else None

	def getData(self, dag):
		data = {}
		for attr in cmds.listAttr(dag, k=True):
			conn = cmds.listConnections('{}.{}'.format(dag, attr))
			if conn:
				if cmds.connectionInfo('{}.{}'.format(dag, attr), isDestination=True):
					conn = conn[0]

					# Unit Conversions
					if cmds.objectType(conn) == types.unitConversion:
						conn = cmds.listConnections('{}.input'.format(conn))[0]


					# Blend Weighted: Input[index] / Outputs
					if cmds.objectType(conn) == types.blendWeighted:
						self.blendWeighted.append(conn)

						inputQuery = {}

						inputs = cmds.listConnections('{}.input'.format(conn))
						if inputs:
							for input in inputs:

								# Unit Conversions
								if cmds.objectType(input) == types.unitConversion:
									input = cmds.listConnections('{}.input'.format(input))[0]

								if cmds.objectType(input).startswith(types.animCurve):
									self.animCurves.append(input)

									if cmds.connectionInfo('{}.{}'.format(dag, attr), isDestination=True):
										parent = cmds.connectionInfo('{}.input'.format(input),
										                             sourceFromDestination=True)

										if parent:
											inputQuery[input] = parent

						data['{}.{}'.format(dag, attr)] = {types.blendWeighted: {conn: inputQuery}}

					# Anim Curves: Input / Outputs
					elif cmds.objectType(conn).startswith(types.animCurve):
						self.animCurves.append(conn)
						parent = cmds.connectionInfo('{}.input'.format(conn), sourceFromDestination=True)
						data['{}.{}'.format(dag, attr)] = {types.animCurve: {conn: parent}}

		return data if data else None


def mirror(parent, child, parentString, childString):
	parentData = query(parent).data

	for attr, attrData in parentData.items():
		childAttr = '{}.{}'.format(child, attr.split('.')[-1])

		for connType, connTypeData in attrData.items():

			# Blend Weighted
			if connType == types.blendWeighted:
				for conn, connData in connTypeData.items():
					blendNode = cmds.duplicate(conn, name='{}_blendWeighted0'.format(child))[0]
					cmds.connectAttr('{}.output'.format(blendNode), childAttr)

					i = 0
					for animCurve, parentAttr in connData.items():
						childCurve = cmds.duplicate(animCurve, name='{}_{}0'.format(child,
						                                                            cmds.objectType(animCurve)))[0]
						cmds.connectAttr('{}.output'.format(childCurve), '{}.input[{}]'.format(blendNode, i))
						cmds.connectAttr(parentAttr.replace(parentString, childString), '{}.input'.format(childCurve))

						i += 1

			# Anim Curves
			elif connType == types.animCurve:
				for animCurve, parentAttr in connTypeData.items():

					childCurve = cmds.duplicate(animCurve, name='{}_{}0'.format(child,
					                                                            cmds.objectType(animCurve)))[0]

					cmds.connectAttr('{}.output'.format(childCurve), childAttr)
					cmds.connectAttr(parentAttr.replace(parentString, childString), '{}.input'.format(childCurve))
	return


def mirrorFacePose(node,
                   transforms,
                   parentAttrString='_L_',
                   childAttrString='_R_',
                   parentDagString='_L_',
                   childDagString='_R_'):

	if type(transforms) is str:
		transforms = [transforms]

	for transform in transforms:
		child = transform.replace(parentDagString, childDagString)

		if cmds.objExists(child):
			data = query(transform).data

			for attr, attrData in data.items():
				childAttr = '{}.{}'.format(child, attr.split('.')[-1])

				for connType, connTypeData in attrData.items():

					# Blend Weighted
					if connType == types.blendWeighted:
						for conn, connData in connTypeData.items():
							blendNode = cmds.duplicate(conn, name='{}_blendWeighted0'.format(child))[0]
							cmds.connectAttr('{}.output'.format(blendNode), childAttr)

							i = 0
							for animCurve, parentAttr in connData.items():
								childCurve = cmds.duplicate(animCurve,
								                            name='{}_{}0'.format(child, cmds.objectType(animCurve)))[0]

								cmds.connectAttr('{}.output'.format(childCurve), '{}.input[{}]'.format(blendNode, i))

								# Mirror Attr
								mirrorAttr = parentAttr.replace(parentAttrString, childAttrString).split('.')[-1]

								if not cmds.attributeQuery(mirrorAttr, node=node, ex=True):
									attrQuery = parentAttr.split('.')[-1]
									minV = cmds.attributeQuery(attrQuery, node=node, min=True)[0]
									maxV = cmds.attributeQuery(attrQuery, node=node, max=True)[0]
									defV = cmds.attributeQuery(attrQuery, node=node, listDefault=True)[0]
									cmds.addAttr(node, ln=mirrorAttr, min=minV, max=maxV, dv=defV, k=True)

								cmds.connectAttr('{}.{}'.format(node, mirrorAttr), '{}.input'.format(childCurve))
								i += 1

					# Anim Curves
					elif connType == types.animCurve:
						for animCurve, parentAttr in connTypeData.items():
							childCurve = cmds.duplicate(animCurve, name='{}_{}0'.format(child,
							                                                            cmds.objectType(animCurve)))[0]

							cmds.connectAttr('{}.output'.format(childCurve), childAttr)

							# Mirror Attr
							mirrorAttr = parentAttr.replace(parentAttrString, childAttrString).split('.')[-1]

							if not cmds.attributeQuery(mirrorAttr, node=node, ex=True):
								attrQuery = parentAttr.split('.')[-1]
								minV = cmds.attributeQuery(attrQuery, node=node, min=True)
								maxV = cmds.attributeQuery(attrQuery, node=node, max=True)
								defV = cmds.attributeQuery(attrQuery, node=node, listDefault=True)
								cmds.addAttr(node, ln=mirrorAttr, min=minV, max=maxV, dv=defV, k=True)

							cmds.connectAttr('{}.{}'.format(node, mirrorAttr), '{}.input'.format(childCurve))

		else:
			print 'Mirror Face Pose: "{}" does not exist. Skipped.'.format(child)
			return

	return


def pruneNetwork():
	return


def deleteUnusedDriverCurves():
	for driverCurve in cmds.ls(type=("animCurveUL", "animCurveUU", "animCurveUA", "animCurveUT")):
		try:

			# 0 Value
			canDelete = []
			for value in cmds.keyframe(driverCurve, valueChange=1, q=1):
				if abs(value) == 0.0:
					canDelete.append(True)
				else:
					canDelete.append(False)

			if canDelete:
				if False not in canDelete:
					cmds.delete(driverCurve)
		except:
			cmds.delete(driverCurve)
	return


def deleteUnusedBlendNodes():
	# rewire blend nodes that aren't blending anything
	for blendNode in cmds.ls(type='blendWeighted'):
		if len(cmds.listConnections(blendNode, destination=0)) == 1:
			curveOutput = None
			drivenInput = None

			# leap over the unitConversion if it exists and find the driving curve
			curveOutput = cmds.listConnections(blendNode, destination=0, plugs=1, skipConversionNodes=1)[0]
			# leap over the downstream unitConversion if it exists
			conns = cmds.listConnections(blendNode, source=0, plugs=1, skipConversionNodes=1)
			for conn in conns:
				if cmds.nodeType(conn.split('.')[0]) == 'hyperLayout': conns.pop(conns.index(conn))
			if len(conns) == 1:
				drivenInput = conns[0]
			else:
				cmds.warning('BlendWeighted had more than two outputs? Node: ' + blendNode)

			# connect the values, delete the blendWeighted
			cmds.connectAttr(curveOutput, drivenInput, force=1)
			cmds.delete(blendNode)
			print 'Removed', blendNode, 'and wired', curveOutput, 'to', drivenInput


def getHistory():
	pass
	'''
	# search down the dag for all future nodes
	futureNodes = [node for node in cmds.listHistory(c, future=1, ac=1)]
	# reverse the list order so that you get farthest first
	futureNodes.reverse()
	drivenAttr = None

	# walk the list until you find either a unitConversion, blendWeighted, or nothing
	for node in futureNodes:
		if cmds.nodeType(node) == 'unitConversion':
			try:
				drivenAttr = cmds.listConnections(node + '.output', p=1)[0]
				break
			except:
				cmds.warning('blendWeighted node with no output: ' + node)
				break
		elif cmds.nodeType(node) == 'blendWeighted':
			try:
				drivenAttr = cmds.listConnections(node + '.output', p=1)[0]
				break
			except:
				cmds.warning('blendWeighted node with no output: ' + node)
				break
	if not drivenAttr:
		drivenAttr = cmds.listConnections(c + '.output', p=1)[0]
	if drivenAttr:
		dk.drivenAttr = drivenAttr
	else:
		cmds.warning('No driven attr found for ' + c)
	'''
