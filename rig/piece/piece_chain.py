# Lancer Modules
from rig.utils import *
from piece_control import *

# Maya Modules
from maya import cmds


class CHAIN(object):
	def __init__(self,
	             objects,
	             controlClass,
	             name='rig_chain',
	             scale=1,
	             index=0,
	             axis=None,
	             side=None,
	             ):
		self.name = name
		self.objects = objects
		self.controlClass = controlClass
		self.scale = scale
		self.index = index
		self.axis = axis
		self.side = side if side else 'Center'
		self.control = None
		self.group = None
		self.parent = None
		self.joint = None
		self.stretchGroup = None
		self.ikHandle = None
		self.ikPoleVector = None

	def create(self):

		controlList = []
		groupList = []
		i = 0
		for obj in self.objects:
			objectLabel = getJointLabel(obj)
			objectSide = objectLabel[0]
			objectType = objectLabel[1]
			objectIndex = getJointIndex(obj)

			ctl = self.controlClass(name=longName(self.name,
			                                      objectType.split(' ')[0].lower(),
			                                      objectIndex if objectIndex else i,
			                                      Component.control,
			                                      ),
			                        child=obj,
			                        scale=self.scale,
			                        side=objectSide,
			                        label=objectType,
			                        index=self.index if self.index else objectIndex,
			                        axis=self.axis,
			                        )
			controlList.append(ctl.transform)
			groupList.append(ctl.group)
			i += 1
		self.control = controlList
		self.group = groupList
		return

	def setUpGroupHierarchy(self):
		groupList = self.group
		for x in groupList:
			i = groupList.index(x)
			if i != 0:
				cmds.parent(x, self.control[i - 1])
		return

	def createParent(self):
		self.parent = createGroup(self.group[0], n=longName(self.name, Component.group))
		return

	def lockGroups(self):
		for grp in self.group:
			lockKeyableAttributes(grp, hide=True)

	def lockCtlScale(self):
		for ctl in self.control:
			lockScale(ctl)
		return

	def limitRotations(self):
		for ctl in self.control:
			cmds.transformLimits(ctl, erx=[1, 1], rx=[-180, 180])
		return


class FKCHAIN(CHAIN):
	def __init__(self,
	             objects,
	             name=Component.fk,
	             scale=1,
	             axis=None,
	             side=None,
	             ):
		CHAIN.__init__(self,
		               objects=objects,
		               name=name,
		               scale=scale,
		               axis=axis,
		               controlClass=FKCONTROL,
		               side=side,
		               )
		self.create()
		self.setUpGroupHierarchy()
		self.resetRotations()
		self.createParent()
		self.createStretch()
		self.limitRotations()
		self.lockGroups()

	# self.lockCtlScale()

	def resetRotations(self):
		if len(self.group) != 1:
			for axis in ['x', 'y', 'z']:
				cmds.setAttr('{}.r{}'.format(self.group[-1], axis), 0)
			return

	def createStretch(self):
		attrName = Component.stretch
		stretchGroup = []
		cmds.addAttr(self.parent, ln=attrName, m=True, at='double', k=True)
		for ctl in self.control:
			i = self.control.index(ctl)
			grp = createGroup(ctl, n=longName(ctl, attrName, Component.group))
			cmds.connectAttr('{}.{}[{}]'.format(self.parent, attrName, i), '{}.tx'.format(grp))
			lockKeyableAttributes(grp, hide=True)
			stretchGroup.append(grp)

		self.stretchGroup = stretchGroup


class IKCHAIN(CHAIN):
	def __init__(self,
	             objects,
	             name=Component.ik,
	             scale=1,
	             axis=None,
	             side=None,
	             ):
		CHAIN.__init__(self,
		               objects=objects,
		               controlClass=IKCONTROL,
		               name=name,
		               scale=scale,
		               axis=axis,
		               side=side,
		               )

		self.create()
		self.resetRotations()
		self.createParent()
		self.createJointChain()
		self.createIK()
		self.createStretch()
		self.lockGroups()
		self.lockCtlScale()

	def createJointChain(self):
		name = longName(Component.ik, Component.chain, Component.joint)
		self.joint = createJointChain(self.objects, name=name)
		cmds.parent(self.joint[0], self.control[0])
		return

	def resetRotations(self):
		for grp in [self.group[0], self.group[1]]:
			i = self.group.index(grp)
			if i != 0:
				for axis in ['x', 'y', 'z']:
					cmds.setAttr('{}.r{}'.format(grp, axis), 0)
		return

	def createIK(self):
		# IK Handle
		start = self.joint[0]
		mid = self.joint[1]
		end = self.joint[2]
		self.ikHandle = cmds.ikHandle(name=longName(self.name, Component.ikHandle),
		                              sj=start,
		                              ee=end,
		                              sol='ikRPsolver')[0]

		cmds.parent(self.ikHandle, self.control[-1])
		cmds.orientConstraint(self.ikHandle, end, mo=True)
		cmds.setAttr('{}.v'.format(self.ikHandle), 0)

		# Pole Vector
		pvPos = getPoleVectorPosition(start, mid, end)
		cmds.xform(self.group[1], ws=True, t=pvPos)
		poleVector = createPoleVector(joint=mid,
		                              ctl=self.control[1],
		                              ik=self.ikHandle,
		                              name='{}_poleVector'.format(self.name),
		                              )

		swapShape(par=self.control[1],
		          child=createWire(WireType.sphere,
		                           scale=self.scale / 3,
		                           ),
		          )

		lockRotate(self.control[1])

		'''
		rotateNull = cmds.group(name='{}_rotate_null'.format(self.ikHandle), em=True)
		ults.snap(self.control[1], rotateNull, t=True)
		cmds.parent(rotateNull, self.control[-1])
		ults.lockAttributes(rotateNull)

		poleVectorOffset = cmds.group(name='{}_offset'.format(self.control[1]), em=True)
		ults.snap(start, poleVectorOffset, t=True)
		cmds.aimConstraint(self.control[-1], poleVectorOffset, wut='object', wuo=rotateNull)
		cmds.parent(self.group[1], poleVectorOffset)
		'''
		presetWireColor(self.control[1], Component.ik)
		return

	def createStretch(self):
		attrName = Component.stretch
		stretchGroup = []
		cmds.addAttr(self.parent, ln=attrName, m=True, at='double', k=True)
		for joint in self.joint:
			i = self.joint.index(joint)
			grp = cmds.group(joint, em=True, n=longName(joint,
			                                            attrName,
			                                            Component.group
			                                            ))
			snap(joint, grp, t=True, r=True)
			if i == 0:
				cmds.parent(grp, self.parent)
			else:
				cmds.parent(grp, stretchGroup[i - 1])
			origPos = cmds.getAttr('{}.tx'.format(grp))
			cmds.connectAttr('{}.tx'.format(grp), '{}.tx'.format(joint))

			add = cmds.createNode('addDoubleLinear', name='{}_add0'.format(grp))
			cmds.connectAttr('{}.{}[{}]'.format(self.parent, attrName, i), '{}.input1'.format(add), f=True)
			cmds.setAttr('{}.input2'.format(add), origPos)
			cmds.connectAttr('{}.output'.format(add), '{}.tx'.format(grp))
			lockKeyableAttributes(grp, hide=True)
			stretchGroup.append(grp)

		self.stretchGroup = stretchGroup


class DETAILCHAIN(CHAIN):
	def __init__(self,
	             joint,
	             name=Component.detail,
	             scale=1,
	             axis=None,
	             ):

		CHAIN.__init__(self,
		               objects=getBindJoint(joint),
		               controlClass=DETAILCONTROL,
		               name=name,
		               scale=scale,
		               axis=axis,
		               side=getSide(joint),
		               )

		self.joint = joint
		self.create()
		self.parentToJoint()
		self.createConstraints()

	def parentToJoint(self):
		for group in self.group:
			cmds.parent(group, self.joint)
		return

	def createConstraints(self):
		for obj in self.objects:
			i = self.objects.index(obj)
			cmds.parentConstraint(self.control[i], obj, mo=True)
			cmds.scaleConstraint(self.control[i], obj, mo=True)
		return


class RIBBONCHAIN(CHAIN):
	def __init__(self,
	             objects,
	             name=Component.ribbon,
	             scale=1,
	             axis=None,
	             side=None,
	             ):
		CHAIN.__init__(self,
		               objects=objects,
		               controlClass=DETAILCONTROL,
		               name=name,
		               scale=scale,
		               axis=axis,
		               side=side,
		               )
		self.create()
		self.createFlexiPlane()

	def createFlexiPlane(self):
		startObject = self.objects[0]
		endObject = self.objects[-1]
		amount = len(self.objects)
		distance = getDistance(startObject, endObject)
		flex = createFlexiPlane(name=self.name, amount=amount, width=distance, side=self.side)

		cmds.delete(cmds.parentConstraint(startObject, endObject, flex.parent))

		for grp in self.group:
			i = self.group.index(grp)
			cmds.parent(grp, flex.follicle[i])

		self.ribbonLocators = flex.control
		self.ribbonLocatorsGroup = flex.group
		self.parent = flex.parent
		return


class RIBBONLIMB:
	def __init__(self,
	             start,
	             mid,
	             end,
	             upperObjects,
	             midObject,
	             lowerObjects,
	             name=Component.ribbon,
	             scale=1,
	             axis=None,
	             side=Position.left,
	             ):
		self.start = start
		self.startParent = self.getStartParent()
		self.mid = mid
		self.end = end
		self.objects = [start, mid, end]

		self.upperObjects = upperObjects
		self.lowerObjects = lowerObjects
		self.midObject = midObject
		self.name = name
		self.scale = scale
		self.axis = axis
		self.side = side
		self.color = [0, .7, .7]

		self.mainControl = []
		self.mainGroup = []

		self.upperControl = []
		self.upperGroup = []
		self.midControl = []
		self.midGroup = []
		self.lowerControl = []
		self.lowerGroup = []

		self.detailControl = []
		self.detailGroup = []

		self.upperFlexiPlane = None
		self.lowerFlexiPlane = None

		self.createMainControls()
		self.createIntermediateControls()
		self.createDetailControls()
		self.createRibbon()
		self.createHierarchy()
		self.createTwist()
		self.cleanUp()

	def getStartParent(self):
		parent = cmds.listRelatives(self.start, parent=True)
		return parent[0] if parent else None

	def createMainControls(self):
		for obj in self.objects:
			i = self.objects.index(obj)
			ctl = CONTROL(name=longName(self.name,
			                            'main',
			                            i,
			                            Component.control,
			                            ),
			              typ=WireType.octagon,
			              scale=self.scale,
			              axis=self.axis,
			              child=obj,
			              color=self.color,
			              )

			cmds.parent(ctl.group, obj)
			self.mainControl.append(ctl.transform)
			self.mainGroup.append(ctl.group)

		snap(self.mid, self.mainGroup[-1], r=True)

		cmds.delete(cmds.orientConstraint(self.mainGroup[0], self.mainGroup[2], self.mainGroup[1]))
		return

	def createIntermediateControls(self):
		for i in range(2):
			ctl = CONTROL(name=longName(self.name,
			                            'intermediate',
			                            i,
			                            Component.control,
			                            ),
			              typ=WireType.hexigon,
			              scale=self.scale,
			              axis=self.axis,
			              color=self.color,
			              )

			cmds.parent(ctl.group, self.objects[i])

			if i == 0:
				j = 1
				startIndex = 0
				endIndex = 1
			else:
				j = 2
				startIndex = 2
				endIndex = 3

			cmds.delete(cmds.parentConstraint(self.mainControl[startIndex], self.mainControl[endIndex], ctl.group))
			cmds.pointConstraint(self.mainControl[startIndex], self.mainControl[endIndex], ctl.group, mo=True)
			self.mainControl.insert(i + j, ctl.transform)
			self.mainGroup.insert(i + j, ctl.group)
		return

	def createDetailControls(self):
		upperIndex = len(self.upperObjects) - 1
		midIndex = upperIndex + 1
		objects = self.upperObjects + listCheck(self.midObject) + self.lowerObjects
		i = 0
		for obj in objects:
			i = objects.index(obj)
			ctl = DETAILCONTROL(name=longName(self.name,
			                                  'detail',
			                                  i,
			                                  Component.control,
			                                  ),
			                    scale=self.scale,
			                    axis=self.axis,
			                    child=obj,
			                    )

			cmds.parentConstraint(ctl.transform, obj, mo=True)
			cmds.scaleConstraint(ctl.transform, obj, mo=True)

			if i < midIndex:
				self.upperControl.append(ctl.transform)
				self.upperGroup.append(ctl.group)

			elif i == midIndex:
				self.midControl.append(ctl.transform)
				self.midGroup.append(ctl.group)

			else:
				self.lowerControl.append(ctl.transform)
				self.lowerGroup.append(ctl.group)

			self.detailControl.append(ctl.transform)
			self.detailGroup.append(ctl.group)
			i += 1

		return

	def createFlexiPlane(self, start, end, amount, name):
		distance = getDistance(start, end)
		flex = createFlexiPlane(name=name,
		                        amount=amount,
		                        width=distance,
		                        side=self.side,
		                        )

		cmds.delete(cmds.parentConstraint(start, end, flex.parent))
		return flex

	def createRibbon(self):
		self.upperFlexiPlane = self.createFlexiPlane(start=self.start,
		                                             end=self.mid,
		                                             amount=len(self.upperObjects + listCheck(self.midObject)),
		                                             name=longName(self.name,
		                                                           'upper',
		                                                           ),
		                                             )
		self.lowerFlexiPlane = self.createFlexiPlane(start=self.mid,
		                                             end=self.end,
		                                             amount=len(self.upperObjects + listCheck(self.midObject)),
		                                             name=longName(self.name,
		                                                           'lower',
		                                                           ),
		                                             )
		return

	def createHierarchy(self):

		cmds.pointConstraint(self.mainControl[0], self.upperFlexiPlane.control[0])
		cmds.pointConstraint(self.mainControl[2], self.upperFlexiPlane.control[2])

		cmds.pointConstraint(self.mainControl[2], self.lowerFlexiPlane.control[0])
		cmds.pointConstraint(self.mainControl[4], self.lowerFlexiPlane.control[2])

		cmds.connectAttr('{}.t'.format(self.mainControl[1]), '{}.t'.format(self.upperFlexiPlane.control[1]))
		cmds.connectAttr('{}.t'.format(self.mainControl[3]), '{}.t'.format(self.lowerFlexiPlane.control[1]))

		i = 0
		for grp in self.upperGroup:
			cmds.parent(grp, self.upperFlexiPlane.follicle[i])
			i += 1

		i = 1
		for grp in self.lowerGroup:
			cmds.parent(grp, self.lowerFlexiPlane.follicle[i])
			i += 1

		cmds.parent(self.midGroup[0], self.upperFlexiPlane.follicle[-1])
		cmds.orientConstraint(self.mainControl[2], self.midGroup[0], mo=True)
		cmds.orientConstraint(self.mainControl[-1], self.detailGroup[-1], mo=True)

		# if self.startParent:
		#	cmds.parent(self.upperFlexiPlane.masterGroup, self.startParent)
		#	cmds.parent(self.lowerFlexiPlane.masterGroup, self.startParent)

		return

	def createTwist(self):
		cmds.connectAttr('{}.rx'.format(self.mainControl[0]), '{}.startTwistAmount'.format(self.upperFlexiPlane.parent))
		cmds.connectAttr('{}.rx'.format(self.mainControl[2]), '{}.endTwistAmount'.format(self.upperFlexiPlane.parent))

		cmds.connectAttr('{}.rx'.format(self.mainControl[2]), '{}.startTwistAmount'.format(self.lowerFlexiPlane.parent))
		cmds.connectAttr('{}.rx'.format(self.mainControl[-1]), '{}.endTwistAmount'.format(self.lowerFlexiPlane.parent))

		cmds.connectAttr('{}.rx'.format(self.start), '{}.endTwistAdd'.format(self.upperFlexiPlane.parent))
		cmds.connectAttr('{}.rx'.format(self.start), '{}.startTwistAdd'.format(self.lowerFlexiPlane.parent))

		add = cmds.createNode('addDoubleLinear', name='{}_lower_ribbon_add0'.format(self.name))
		cmds.connectAttr('{}.rx'.format(self.start), '{}.input1'.format(add))
		cmds.connectAttr('{}.rx'.format(self.end), '{}.input2'.format(add))
		cmds.connectAttr('{}.output'.format(add), '{}.endTwistAdd'.format(self.lowerFlexiPlane.parent))
		return

	def cleanUp(self):

		for obj in self.mainControl:
			lockScale(obj)

		return


class TWISTCHAIN:
	def __init__(self,
	             start,
	             mid,
	             end,
	             name=Component.aux,
	             scale=1,
	             axis=None,
	             ):
		self.start = start
		self.mid = mid
		self.end = end

		self.name = name
		self.scale = scale
		self.side = getSide(start)
		self.axis = axis

		self.upperObject = getBindJoint(start)
		self.lowerObject = getBindJoint(mid)
		self.midObject = self.lowerObject[0]

		self.upperChain = DETAILCHAIN(joint=self.start,
		                              scale=self.scale,
		                              axis=self.axis,
		                              name=longName(self.name,
		                                            'upper',
		                                            Component.detail,
		                                            )
		                              )
		self.lowerChain = DETAILCHAIN(joint=self.mid,
		                              scale=self.scale,
		                              axis=self.axis,
		                              name=longName(self.name,
		                                            'lower',
		                                            Component.detail
		                                            )
		                              )

		self.objects = self.upperObject + self.lowerObject
		self.control = self.upperChain.control + self.lowerChain.control
		self.group = self.upperChain.group + self.lowerChain.group
		self.stretch = []
		self.distance = []

		self.upperTwist = None
		self.lowerTwist = None

		self.createIKTwist()
		self.createStretch(objects=self.upperChain.control, start=self.start, end=self.mid, typ='upper',
		                   ctl=self.upperTwist.parent)
		self.createStretch(objects=self.lowerChain.control, start=self.mid, end=self.end, typ='lower',
		                   ctl=self.lowerTwist.parent)

		self.createSnS()

	def createIKTwist(self):
		self.upperTwist = createIKTwist(start=self.start,
		                                end=self.mid,
		                                name=longName(self.name, 'upper_twist'),
		                                )

		self.lowerTwist = createIKTwist(start=self.end,
		                                end=self.mid,
		                                name=longName(self.name, 'lower_twist'),
		                                )

		self.createTwistConnections(self.upperChain.group, self.upperTwist.joint[0], self.upperTwist.parent,
		                            typ='upper')
		self.createTwistConnections(self.lowerChain.group, self.lowerTwist.joint[0], self.lowerTwist.parent,
		                            typ='lower')
		cmds.parent(self.lowerTwist.ikHandle, self.end)
		cmds.parent(self.lowerTwist.parent, self.mid)
		return

	def createTwistConnections(self, objects, twist, ctl, typ):
		attrName = 'twist'
		cmds.addAttr(ctl, ln=attrName, m=True, at='double', k=True)

		max = 1.0
		step = max / float(len(objects))
		var = max if typ == 'upper' else 0.0
		for obj in objects:
			i = objects.index(obj)
			mult = cmds.createNode('multDoubleLinear', name='{}_twist_mult0'.format(obj))
			cmds.connectAttr('{}.{}[{}]'.format(ctl, attrName, i), '{}.input1'.format(mult))
			cmds.connectAttr('{}.rx'.format(twist), '{}.input2'.format(mult))
			cmds.connectAttr('{}.output'.format(mult), '{}.rx'.format(obj))
			cmds.setAttr('{}.{}[{}]'.format(ctl, attrName, i), var)
			var += -step if typ == 'upper' else step
		return

	def createStretch(self, objects, start, end, ctl, typ):
		attrName = Component.stretch
		cmds.addAttr(ctl, ln=attrName, m=True, at='double', k=True)
		distance = createDistanceNode(start=start, end=end,
		                              n=longName(self.name, '{}_distance0'.format(typ)))

		max = 1.0
		if typ == 'upper':
			step = max / float(len(objects))
		else:
			step = max / float(len(objects) - 1)
		var = 0

		for obj in objects:
			i = objects.index(obj)
			cmds.setAttr('{}.{}[{}]'.format(ctl, attrName, i), var)
			grp = createGroup(obj, n=longName(obj, attrName, Component.group))
			self.stretch.append(grp)
			if i != 0:
				sub = cmds.createNode('plusMinusAverage', name='{}_subtract0'.format(grp))
				mult = cmds.createNode('multDoubleLinear', name='{}_mult0'.format(grp))
				cmds.connectAttr('{}.distance'.format(distance[0]), '{}.input3D[0].input3Dx'.format(sub))
				cmds.setAttr('{}.input3D[1].input3Dx'.format(sub), distance[1])
				cmds.setAttr('{}.operation'.format(sub), 2)
				cmds.connectAttr('{}.output3Dx'.format(sub), '{}.input1'.format(mult))
				cmds.connectAttr('{}.output'.format(mult), '{}.tx'.format(grp))
				cmds.connectAttr('{}.{}[{}]'.format(ctl, attrName, i), '{}.input2'.format(mult))
			var += step
		self.distance.append(distance[0])
		return

	def createSnS(self):
		globalGrp = self.upperTwist.parent
		cmds.addAttr(globalGrp, ln='sns', min=0, max=1, dv=0, k=True)
		cmds.addAttr(globalGrp, ln='snsAdd', k=True)

		maxDistance = getDistance(self.start, self.mid) + getDistance(self.mid, self.end)
		# distance = ults.createDistanceNode(self.start, self.end)
		distanceAdd = cmds.createNode('addDoubleLinear', name='{}_add0'.format(self.name))
		cmds.connectAttr('{}.distance'.format(self.distance[0]), '{}.input1'.format(distanceAdd))
		cmds.connectAttr('{}.distance'.format(self.distance[1]), '{}.input2'.format(distanceAdd))

		divideA = cmds.createNode('multiplyDivide', name='{}_divide0'.format(self.name))
		cmds.setAttr('{}.operation'.format(divideA), 2)
		cmds.setAttr('{}.input2X'.format(divideA), maxDistance)
		divideB = cmds.createNode('multiplyDivide', name='{}_divide0'.format(self.name))
		cmds.setAttr('{}.operation'.format(divideB), 2)
		cmds.setAttr('{}.input1X'.format(divideB), 1)

		cmds.connectAttr('{}.output'.format(distanceAdd), '{}.input1X'.format(divideA))
		cmds.connectAttr('{}.outputX'.format(divideA), '{}.input2X'.format(divideB))

		setRange = cmds.createNode('setRange', name='{}_sns_setRange0'.format(self.name))
		cmds.setAttr('{}.minX'.format(setRange), 1)
		cmds.setAttr('{}.oldMaxX'.format(setRange), 1)
		cmds.connectAttr('{}.sns'.format(globalGrp), '{}.valueX'.format(setRange))
		cmds.connectAttr('{}.outputX'.format(divideB), '{}.maxX'.format(setRange))

		add = cmds.createNode('addDoubleLinear', name='{}_add0'.format(self.name))
		cmds.connectAttr('{}.outValueX'.format(setRange), '{}.input1'.format(add))
		cmds.connectAttr('{}.snsAdd'.format(globalGrp), '{}.input2'.format(add))

		amount = len(self.objects)
		var = 0
		step = 1.0 / float(len(self.objects) - 1)
		stepRangePos = []

		for x in range(amount):
			if x == 0:
				stepRangePos.append(.1)
			else:
				stepRangePos.append(var)
			var += step

		for grp in self.stretch:
			for axis in ['y', 'z']:
				cmds.connectAttr('{}.output'.format(add), '{}.s{}'.format(grp, axis))
		return
