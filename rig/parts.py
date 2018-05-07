# LANCER.RIG.PARTS
#
#
#
#
#

# Lancer Modules
import ults
import control
import network
import skeleton

reload(ults)
reload(control)
reload(network)
reload(skeleton)

# Maya Modules
from maya import cmds, mel

#########################################################################################################################
#																														#
#																														#
#	MODULES / COMPONENTS 																								#
#																														#
#																														#
#########################################################################################################################


characterName = 'character'


class CONTROL:
	def __init__(self,
	             name='control',
	             typ='circle',
	             scale=1,
	             axis=None,
	             translate=False,
	             rotate=False,
	             child=None,
	             parent=None,
	             index=0,
	             side=None,
	             label=None,

	             ):
		self.name = name
		self.typ = typ
		self.scale = scale
		self.axis = axis
		self.translate = translate
		self.rotate = rotate
		self.child = child
		self.parent = parent
		self.index = index
		self.side = side
		self.label = label

		self.transform = None
		self.shape = None
		self.group = None

		self.create()

	def create(self):
		ctl = control.create(name=self.name, shape=self.typ)
		self.transform = ctl[0]
		self.shape = ctl[1]
		self.setAttributes(self.transform)
		self.createGroup()
		return

	def setAttributes(self, selected):
		for attr in ['character', 'skeletonNetwork', 'rigNetwork']:
			cmds.addAttr(selected, ln=attr, at='message')

		cmds.addAttr(selected, ln='index', at='long', dv=self.index)

		return

	def createGroup(self):
		self.group = cmds.group(self.transform, name='{}_grp'.format(self.transform))
		self.setAttributes(self.group)

		for attr in ['t', 'r', 's']:
			for axis in ['x', 'y', 'z']:
				cmds.setAttr('{}.{}{}'.format(self.group, attr, axis), keyable=False, channelBox=False)
		return

	def setLabel(self):
		if self.side and self.label:
			skeleton.setJointLabel(self.transform, side=self.side, typ=self.label)


class BASE(object):
	def __init__(self, name='character', selected=None, scale=1, typ='root', side='center', index=0, *args):
		'''
		Base Class to create rig components: Bind Joints, FK, IK, & FKIK Switching.

		:param selected:    Objects to be rigged.
		:param name:        Name of rig network
		:param typ:         Component type
		:param scale:       Scale of rig controls
		:param args:        Extra argument for MayaUI
		'''
		self.name = name
		self.selected = selected
		self.scale = scale
		self.typ = typ
		self.side = side
		self.index = index

		self.bindJoint = None
		self.control = None
		self.fkJoint = None
		self.fkControl = None
		self.ikJoint = None
		self.ikControl = None
		self.ikHandle = None
		self.ikPoleVector = None
		self.fkPoleVector = None
		self.group = None
		self.fkikNetwork = None
		self.network = None
		self.set = None
		self.attrControl = None
		self.rootQuery = network.queryNetwork()

		self.createNetwork()

	def createName(self, suffix, index=0):
		return '{}_{}_{}{}'.format(self.typ, self.side[0].upper(), suffix, index)

	def createBindJoints(self):
		self.bindJoint = ults.createBindChain(self.selected)

	def createFK(self, objects):
		objects = ults.listCheck(objects)

		fk = createFKChain(objects, scale=self.scale)
		self.fkJoint = fk.joint
		self.fkControl = fk.control

		for x in self.fkControl:
			self.control.append(x[0])
			ults.presetWireColor(x[0], typ=ults.componentType.fk)

	def createIK(self, objects):
		objects = ults.listCheck(objects)

		ik = createIKChain(objects, scale=self.scale, typ=self.typ)

		self.ikJoint = ik.joint
		self.ikControl = ik.control
		self.ikHandle = ik.ikHandle
		self.ikPoleVector = ik.poleVector

		for x in self.ikControl:
			self.control.append(x[0])
			ults.presetWireColor(x[0], typ=ults.componentType.ik)

	def createFKIK(self, objects):
		self.createFK(objects)
		self.createIK(objects)
		self.createFKPoleVector()
		self.createFKIKNetwork(objects, self.fkJoint, self.ikJoint)

		self.createAttrControl(objects[-1])

	def createFKPoleVector(self):
		fkPoleVector = cmds.group(n=self.createName('_FKPoleVector_null'), em=True)
		snap(self.ikControl[1][0], fkPoleVector, t=True, r=True)
		cmds.parent(fkPoleVector, self.fkJoint[1])
		self.fkPoleVector = fkPoleVector

	def createAttrControl(self, selected):
		if self.typ == ults.componentType.arm:
			axis = [1, -1, 0]
		elif self.typ == ults.componentType.leg:
			axis = [0, 2, 0]
		else:
			axis = [0, 0, 0]

		self.attrControl = control.create(n=self.createName('attr_ctl'), typ='lollipop', axis=axis,
		                                  parent=False, scale=self.scale)

		for attr in cmds.listAttr(self.attrControl[0], k=True):
			cmds.setAttr('{}.{}'.format(self.attrControl[0], attr), lock=True, k=False, cb=False)

		cmds.addAttr(self.attrControl[0], ln='FKIK', dv=0, min=0, max=1, k=True)
		cmds.connectAttr('{}.FKIK'.format(self.attrControl[0]), '{}.FKIK'.format(self.fkikNetwork))

		snap(selected, self.attrControl[1], t=True)
		cmds.parent(self.attrControl[1], selected)

		connectToNetwork(self.attrControl[0], self.fkikNetwork, 'attributeControl')

		overrideColor(self.attrControl[0], color=[.355, 0.0, .468])

	def createFKIKNetwork(self, obj=None, fk=None, ik=None):
		fkikNet = network(n=self.createName('fkik_network'), typ=ults.componentType.fkik)
		self.setNetworkDefaults(fkikNet)
		connectToNetwork(fkikNet, self.network, 'fkikNetwork')

		if fk and ik:
			fkik = createFKIK(obj=obj, fk=fk, ik=ik, ctl=fkikNet)
			for f in self.fkControl:
				i = self.fkControl.index(f)
				cmds.connectAttr('{}.outputX'.format(fkik[1][i]), '{}.v'.format(f[0]))

			for i in self.ikControl:
				cmds.connectAttr('{}.FKIK'.format(fkikNet), '{}.v'.format(i[0]))

		if self.bindJoint:
			multiConnectToNetwork(self.bindJoint, fkikNet, 'bindJoint')

		if self.fkControl:
			fkControl = [x[0] for x in self.fkControl]
			multiConnectToNetwork(self.fkJoint, fkikNet, 'fkJoint')
			multiConnectToNetwork(fkControl, fkikNet, 'fkControl')

		if self.ikHandle:
			connectToNetwork(self.ikHandle, fkikNet, 'ikHandle')
		# connectToNetwork(self.ikPoleVector, fkikNet, 'ikPoleVector')

		if self.fkPoleVector:
			connectToNetwork(self.fkPoleVector, fkikNet, 'fkPoleVector')

		if self.ikControl:
			ikControl = [x[0] for x in self.ikControl]
			multiConnectToNetwork(self.ikJoint, fkikNet, 'ikJoint')
			multiConnectToNetwork(ikControl, fkikNet, 'ikControl')

		self.fkikNetwork = fkikNet

	def createNetwork(self):
		self.network = network(n=self.createName('network'), typ=self.typ)
		self.setNetworkDefaults(self.network)

	def setNetworkDefaults(self, network):
		cmds.setAttr('{}.index'.format(network), self.index)
		cmds.setAttr('{}.side'.format(network), self.side, type='string', lock=True)

	def createSet(self):
		self.set = createSet(self.control, n=self.createName('control_set'))
		connectToNetwork(self.set, self.network, ults.componentType.set)


class ROOT(BASE):

	def __init__(self, selected=None, name='character', scale=1, *args):
		super(ROOT, self).__init__(selected=selected, name=name, scale=scale, typ=ults.componentType.character)

		self.createControls()
		self.updateNetwork()

	def determineControlScale(self):
		self.parent = False

		if self.selected:
			self.parent = True

			children = cmds.listRelatives(self.selected[0], ad=True)

			posList = []

			if children:
				for child in children:
					if cmds.objectType(child, isType='joint'):
						pos = cmds.xform(child, q=True, ws=True, rp=True)
						posList.append(pos[1])
			if posList:
				self.scale = int(max(posList) / 2)

	def createControls(self):
		self.determineControlScale()

		# Controls

		ctl = control(self.selected, n='root_ctl', typ='root', r=False, scale=self.scale + 2, parent=False)
		offset = control(self.selected, n='root_offset_ctl', typ='center', r=False, scale=self.scale - 2,
		                 parent=self.parent)
		presetWireColor([ctl[0], offset[0]], typ=ults.componentType.center)
		cmds.parent(offset[1], ctl[0])

		# Global Scale

		cmds.addAttr(ctl[0], ln='globalScale', dv=1)
		cmds.setAttr('{}.globalScale'.format(ctl[0]), k=False, channelBox=True)

		for axis in ['x', 'y', 'z']:
			cmds.connectAttr('{}.globalScale'.format(ctl[0]), '{}.s{}'.format(ctl[0], axis))

			if self.selected:
				cmds.connectAttr('{}.globalScale'.format(ctl[0]), '{}.s{}'.format(self.selected[0], axis))

			cmds.setAttr('{}.s{}'.format(ctl[0], axis), k=False, channelBox=False, lock=True)
			cmds.setAttr('{}.s{}'.format(offset[0], axis), k=False, channelBox=False, lock=True)

		cmds.connectAttr('{}.globalScale'.format(ctl[0]), '{}.globalScale'.format(self.network))

		# Master Group
		self.group = createGroup(ctl[1], n='{}_RIG'.format(self.name))

		# Return
		self.fkControl = [ctl, offset]
		for x in self.fkControl:
			self.control.append(x[0])

	def updateNetwork(self):
		cmds.setAttr('{}.characterName'.format(self.network), self.name, type='string')
		self.createSet()
		multiConnectToNetwork(self.control, self.network, 'control')


class COG(BASE):

	def __init__(self, selected=None, name='cog', scale=1, *args):
		super(COG, self).__init__(selected=selected, name=name, scale=scale, typ=ults.componentType.cog)

		if self.selected:
			self.createControls()
			self.updateNetwork()

	def determineControlScale(self):
		self.scale = cmds.xform(self.selected[0], q=True, ws=True, rp=True)[1] / 4 + 1

	def createControls(self):
		self.determineControlScale()
		self.createBindJoints()

		ctl = control(self.bindJoint, n='cog_ctl', typ='center', r=False, parent=False, scale=self.scale, nest=True)
		presetWireColor(ctl, typ=ults.componentType.center)

		self.fkControl = ctl
		self.control.append(ctl[0])

	def updateNetwork(self):
		self.createSet()

		if self.rootQuery.network:
			connectToNetwork(self.network, self.rootQuery.network, ults.componentType.cog)
			rootCtl = getConnectedObj(self.rootQuery.network, 'control[0]')
			cmds.parent(self.fkControl[1], rootCtl)

		multiConnectToNetwork(self.control, self.network, 'control')
		multiConnectToNetwork(self.bindJoint, self.network, 'bindJoint')


class HIP(BASE):

	def __init__(self, selected=None, name='hip', scale=1, *args):
		super(HIP, self).__init__(selected=selected, name=name, scale=scale, typ=ults.componentType.hip)

		if self.selected:
			self.createControls()
			self.updateNetwork()

	def determineControlScale(self):
		self.scale = cmds.xform(self.selected[0], q=True, ws=True, rp=True)[1] / 4

	def createControls(self):
		self.determineControlScale()
		self.createBindJoints()

		ctl = control(self.bindJoint, n='hip_ctl', typ='circle', r=False, parent=False, scale=self.scale, nest=True)
		presetWireColor(ctl, typ=ults.componentType.center)

		self.fkControl = ctl
		self.control.append(ctl[0])

	def updateNetwork(self):
		self.createSet()

		if self.rootQuery.network:
			connectToNetwork(self.network, self.rootQuery.network, ults.componentType.hip)

		if self.rootQuery.cog:
			cog = getConnectedObj(self.rootQuery.cog, 'control[0]')

			if cog:
				cmds.parent(self.fkControl[1], cog)

		multiConnectToNetwork(self.control, self.network, 'control')
		multiConnectToNetwork(self.bindJoint, self.network, 'bindJoint')


class SPINE(BASE):
	def __init__(self, selected=None, name='spine', scale=1, *args):
		super(SPINE, self).__init__(selected=selected, name=name, scale=scale, typ=ults.componentType.spine)

		if self.selected:
			self.createControls()
			self.updateNetwork()

	def determineControlScale(self):
		bound = estimateBoundsByJoint(self.selected[0])
		if bound:
			self.scale = bound.maxX[0]

	def createControls(self):
		self.determineControlScale()
		self.createBindJoints()
		self.createFK(self.bindJoint)

		i = 0
		for jnt in self.fkJoint:
			cmds.parentConstraint(jnt, self.bindJoint[i], mo=True)
			i += 1

	def updateNetwork(self):
		self.createSet()
		self.createFKIKNetwork()

		if self.rootQuery.network:
			connectToNetwork(self.network, self.rootQuery.network, ults.componentType.spine)

		if self.rootQuery.cog:
			cog = getConnectedObj(self.rootQuery.cog, 'control[0]')
			cogBind = getConnectedObj(self.rootQuery.cog, 'bindJoint[0]')

			if cog:
				cmds.parent(self.fkControl[0][1], cog)
				cmds.parent(self.bindJoint[0], cogBind)


class HEAD(BASE):
	def __init__(self, selected=None, name='head', scale=1, *args):
		super(HEAD, self).__init__(selected=selected, name=name, scale=scale, typ=ults.componentType.head)

		if self.selected:
			self.createControls()
			self.createFKIKNetwork()
			self.createFKIK()
			self.updateNetwork()

	def createControls(self):
		self.createBindJoints()
		self.createFK(self.bindJoint)
		cmds.parentConstraint(self.fkControl[0][0], self.bindJoint[0])
		self.createIK(self.bindJoint)

	def createIK(self, objects):
		cmds.select(d=True)

		distance = cmds.xform(objects[-1], q=True, ws=True, rp=True)[1] / 2

		ikJnt = cmds.joint(n='{}_ik_jnt'.format(removeJointStr(objects[-1])))
		cmds.setAttr('{}.v'.format(ikJnt), 0)
		ikCtl = control(n='{}_ik_ctl'.format(removeJointStr(objects[-1])), axis=[1, 0, 0], t=False, r=False)

		snap(objects[-1], ikJnt, t=True, r=True)
		snap(objects[-1], ikCtl[-1], t=True, r=False)
		cmds.xform(ikCtl[-1], ws=True, t=[0, 0, distance], r=True)

		cmds.parent(ikJnt, self.fkControl[0][0])
		makeAimVector(ikCtl[0], ikJnt)

		presetWireColor(ikCtl[0], typ=ults.componentType.ik)

		self.ikJoint = [ikJnt]
		self.ikControl = [ikCtl]

	def createFKIK(self):
		fkik = createFKIK(self.bindJoint[-1], self.fkJoint[-1], self.ikJoint[-1], ctl=self.fkikNetwork)
		cmds.connectAttr('{}.outputX'.format(fkik[1][0]), '{}.v'.format(self.fkControl[-1][1]))
		cmds.connectAttr('{}.{}'.format(self.fkikNetwork, fkik[2]), '{}.v'.format(self.ikControl[0][1]))

	def updateNetwork(self):
		self.createSet()

		if self.rootQuery.network:
			connectToNetwork(self.network, self.rootQuery.network, ults.componentType.head)

			rootCtl = getConnectedObj(self.rootQuery.network, 'control[0]')

			if rootCtl:
				cmds.parent(self.ikControl[0][1], rootCtl)

			if self.rootQuery.cog:
				cog = getConnectedObj(self.rootQuery.cog, 'control[0]')
				if cog:
					createLocalWorld(self.fkControl[-1][0], local=self.bindJoint[0], world=cog)

			if self.rootQuery.spine:
				spineFKIK = getConnectedObj(self.rootQuery.spine, 'fkikNetwork')
				spineJnt = cmds.listConnections('{}.bindJoint'.format(spineFKIK))

				if spineJnt:
					cmds.parent(self.fkControl[0][-1], self.bindJoint[0], spineJnt[-1])


class COLLAR(BASE):
	def __init__(self, selected=None, name='collar', scale=1, index=0, *args):
		super(COLLAR, self).__init__(selected=selected, name=name, scale=scale, index=index,
		                             typ=ults.componentType.collar)

		if self.selected:
			self.bindJoint = [self.selected[0]]
			self.createControls()
			self.createFKIKNetwork(self.bindJoint[0], self.fkJoint[0], self.ikJoint[0])
			self.updateNetwork()

	def createControls(self):
		self.createFK(self.bindJoint[0])
		self.createIK(self.selected)
		self.createFKPoleVector()

	def createIK(self, selected):
		ikJnt = createJointChain(selected, typ='ik_aux', world=False)
		ikCtl = control(selected[1], n='{}_ik_ctl'.format(removeJointStr(selected[0])), axis=[1, 0, 0],
		                parent=False)
		ikHandle = cmds.ikHandle(n='collar_{}_ikHandle'.format(self.side[0].upper()), sj=ikJnt[0], ee=ikJnt[1],
		                         sol='ikSCsolver')[0]
		cmds.setAttr('{}.v'.format(ikHandle), 0)
		cmds.parent(ikHandle, ikCtl[0])

		presetWireColor(ikCtl[0], ults.componentType.ik)

		self.control.append(ikCtl[0])

		self.ikJoint = ikJnt
		self.ikControl = [ikCtl]
		self.ikHandle = ikHandle

	def createFKPoleVector(self):
		fkPoleVector = cmds.group(n='{}_fkPoleVector_null'.format(self.fkJoint[0]), em=True)
		snap(self.ikJoint[1], fkPoleVector, t=True, r=True)
		cmds.parent(fkPoleVector, self.fkJoint[0])

		self.fkPoleVector = fkPoleVector

	def updateNetwork(self):
		if self.rootQuery.network:
			if self.rootQuery.cog:
				cog = cmds.listConnections('{}.control[0]'.format(self.rootQuery.cog))
				if cog:
					cmds.parent(self.ikControl[0][1], cog)

			if self.rootQuery.spine:
				spineFKIK = getConnectedObj(self.rootQuery.spine, 'fkikNetwork')
				spineJnt = cmds.listConnections('{}.bindJoint'.format(spineFKIK))
				if spineFKIK:
					cmds.parent(self.fkControl[0][1], self.ikJoint[0], spineJnt[-1])


class ARM(BASE):
	def __init__(self, selected=None, name='arm', scale=1, index=0, *args):
		super(ARM, self).__init__(selected=selected, name=name, scale=scale, index=index, typ=ults.componentType.arm)

		if self.selected:
			self.createControls()
			self.updateNetwork()

	def createControls(self):
		self.createBindJoints()

		if len(self.bindJoint) == 4:
			self.createFKIK([self.bindJoint[1], self.bindJoint[2], self.bindJoint[3]])
			self.createCollar(self.bindJoint[0], self.bindJoint[1])

		elif len(self.bindJoint) == 3:
			self.createFKIK(self.bindJoint)

		self.createHand()

	def createCollar(self, start, end):
		collar = COLLAR([start, end])
		presetWireColor(collar.fkControl[0], ults.componentType.fk)
		presetWireColor(collar.ikControl[0], ults.componentType.ik)

		connectToNetwork(collar.network, self.network, 'collar')
		cmds.parent(self.fkControl[0][1], self.ikControl[0][1], collar.bindJoint[0])

		self.control = self.control + collar.control

		if self.rootQuery.cog:
			cog = cmds.listConnections('{}.control'.format(self.rootQuery.cog))[0]
			if cog:
				createLocalWorld(self.fkControl[0][0], local=collar.bindJoint[0], world=cog)

		cmds.addAttr(self.attrControl[0], ln='collarFKIK', dv=0, min=0, max=1, k=True)
		cmds.connectAttr('{}.collarFKIK'.format(self.attrControl[0]), '{}.FKIK'.format(collar.fkikNetwork))

	def createHand(self):
		hand = HAND(self.selected[-1])
		connectToNetwork(hand.network, self.network, 'hand')

		self.control = self.control + hand.control

		cmds.parent(hand.group, [x[0] for x in hand.bindJoint], self.bindJoint[-1])

	def updateNetwork(self):
		self.createSet()

		if self.rootQuery.network:
			connectToNetwork(self.network, self.rootQuery.network, ults.componentType.arm)
			rootCtl = cmds.listConnections('{}.control'.format(self.rootQuery.network))

			if rootCtl:
				cmds.parent(self.ikControl[1][1], self.ikControl[2][1], rootCtl[0])

			if self.rootQuery.spine:
				spineFKIK = getConnectedObj(self.rootQuery.spine, 'fkikNetwork')
				spineJnt = cmds.listConnections('{}.bindJoint'.format(spineFKIK))

				if spineJnt:
					cmds.parent(self.bindJoint[0], spineJnt[-1])


class LEG(BASE):
	def __init__(self, selected=None, name='leg', scale=1, *args):
		super(LEG, self).__init__(selected=selected, name=name, scale=scale, typ=ults.componentType.leg)

		if self.selected:
			self.createControls()
			self.updateNetwork()

	def createControls(self):
		self.createBindJoints()

		if len(self.bindJoint) == 4:
			self.createFK(self.bindJoint)
			self.createIKLeg([self.bindJoint[0], self.bindJoint[1], self.bindJoint[2]])
			self.createFKIKNetwork(self.bindJoint, self.fkJoint, self.ikJoint)
			self.createAttrControl(self.bindJoint[2])

		elif len(self.bindJoint) == 3:
			self.createFKIK(self.bindJoint)

	def createIKLeg(self, objects):
		self.createIK(objects)

		ballJnt = createJointChain(self.bindJoint[-1], typ=ults.componentType.ik, world=True)[0]
		cmds.parent(ballJnt, self.ikJoint[-1])
		self.ikJoint.append(ballJnt)

		self.createFoot()

	def createFoot(self):
		foot = createIKFootPivot(n=self.createName('ik_footPivot'), ik=self.ikHandle,
		                         start=self.selected[2], end=self.ikJoint[-1], ctl=self.ikControl[-1][0])

	def updateNetwork(self):
		cmds.setAttr('{}.FKIK'.format(self.attrControl[0]), 1)

		if self.rootQuery.network:
			connectToNetwork(self.network, self.rootQuery.network, ults.componentType.leg)
			rootCtl = cmds.listConnections('{}.control'.format(self.rootQuery.network))

			if rootCtl:
				cmds.parent(self.ikControl[1][1], self.ikControl[2][1], rootCtl[0])

			cogCtl = None
			if self.rootQuery.cog:
				cogCtl = cmds.listConnections('{}.control'.format(self.rootQuery.cog))

			if self.rootQuery.hip:
				hipCtl = cmds.listConnections('{}.control'.format(self.rootQuery.hip))
				hipBind = getConnectedObj(self.rootQuery.hip, 'bindJoint[0]')

				if hipBind:
					cmds.parent(self.bindJoint[0], hipBind)

				if hipCtl:
					cmds.parent(self.ikControl[0][1], self.fkControl[0][1], hipCtl[0])

					if cogCtl:
						createLocalWorld(self.fkControl[0][0], local=hipCtl[0], world=cogCtl[0])


class HAND(BASE):
	def __init__(self, selected=None, name='hand', scale=1, index=0, *args):
		super(HAND, self).__init__(selected=selected, name=name, scale=scale, index=0, typ=ults.componentType.hand)

		self.handDict = {
			ults.componentType.thumb : [],
			ults.componentType.index : [],
			ults.componentType.middle: [],
			ults.componentType.ring  : [],
			ults.componentType.pinky : [],
		}

		if self.selected:
			self.createControls()

	def createControls(self):
		self.bindJoint = []

		cmds.addAttr(self.network, ln='finger', dt='string', m=True)

		jointChain = self.getJointOrder()
		if jointChain:
			masterGrp = cmds.group(n=self.createName('rig_fk_ctl_grp'), em=True)
			snap(self.selected[0], masterGrp, t=True, r=True)

			i = 0
			for chain in jointChain:
				fingerRig = FINGER(jointChain[chain], index=i)
				connectToNetwork(fingerRig.network, self.network, 'finger')

				self.control = self.control + fingerRig.control
				self.bindJoint.append(fingerRig.bindJoint)
				cmds.parent(fingerRig.fkControl[0][1], masterGrp)
				i += 1

			self.group = masterGrp

	def getJointOrder(self):
		return self.getJointOrderByName() if not self.getJointOrderByLabel() else self.getJointOrderByLabel()

	def getJointOrderByName(self):
		chain = handJointHierarchy(self.selected)

		handDict = self.handDict

		for x in self.handDict:
			for jnt in chain:
				for j in jnt:
					if x in j:
						handDict[x] = jnt
						break

		return handDict

	def getJointOrderByLabel(self):
		chain = handJointHierarchy(self.selected)
		handDict = self.handDict

		newChain = []
		for c in chain:
			for x in c:
				newChain.append(x)

		newChain = jointLabel(newChain).get(self.typ, self.side)

		i = 0
		for x in self.handDict:
			handDict[x] = newChain[i]
			i += 1

		return handDict


class FINGER(BASE):
	def __init__(self, selected=None, name='finger', scale=1, index=0, *args):
		super(FINGER, self).__init__(selected=selected, name=name, scale=scale, index=index,
		                             typ=ults.componentType.finger)

		if self.selected:
			self.createControls()
			self.updateNetwork()

	def createControls(self):
		self.determineControlScale(self.selected[-1])
		self.createBindJoints()
		self.createFK(self.bindJoint)

		i = 0
		for jnt in self.fkJoint:
			cmds.parentConstraint(jnt, self.bindJoint[i], mo=True)
			i += 1

	def determineControlScale(self, selected):
		bound = estimateBoundsByJoint(selected)
		if bound:
			self.scale = getDistance(bound.maxZ, bound.minZ) / 2

	def updateNetwork(self):
		self.createFKIKNetwork()


class NOODLE(BASE):
	def __init__(self, selected=None, name='limb', typ=ults.componentType.noodle, scale=1, *args):
		super(NOODLE, self).__init__(selected=selected, name=name, scale=scale, typ=typ)

		if self.selected:

			if len(self.selected) % 2 == 0:
				cmds.warning('Need Odd Number of Joints.')

			else:
				self.midNum = (len(self.selected) / 2) + 1
				self.mainControl = None

				self.createControls()
				self.createConnections()
				self.updateNetwork()

	def createControls(self):
		self.bindJoint = self.createBindJoints(self.selected)
		self.createBindControls()
		self.createMainControls()

		upperList = [self.mainControl[0][0], self.mainControl[1][0], self.mainControl[2][0]]
		lowerList = [self.mainControl[2][0], self.mainControl[3][0], self.mainControl[4][0]]

		self.upperBound = self.createCurveBound(upperList, name='upperBound_curve1', amount=self.midNum)
		self.lowerBound = self.createCurveBound(lowerList, name='lowerBound_curve1', amount=self.midNum)

	# self.smoothBound = self.createCurveBound([x[0] for x in self.mainControl], name='smoothBound_curve1',
	#                                         amount=len(self.bindJoint))

	def createBindControls(self):
		for jnt in self.bindJoint:
			ctl = control(jnt, n='{}_ctl'.format(removeJointStr(jnt)), typ='circle', axis=[1, 0, 0], nest=True,
			              parent=False)
			self.control.append(ctl)

	def createMainControls(self):
		start = self.bindJoint[0]
		mid = self.bindJoint[len(self.bindJoint) / 2]
		end = self.bindJoint[-1]

		# Main Controls

		mainCtlList = []
		i = 0
		for jnt in [start, mid, end]:
			ctl = control(jnt, n=self.createName('main_{}_ctl'.format(i)),
			              typ='square',
			              axis=[1, 0, 0], parent=False)
			mainCtlList.append(ctl)
			i += 1

		# Main Curve
		self.mainBound = self.makeCurve(selected=[x[0] for x in mainCtlList],
		                                name=self.createName('main_curve1'), amount=len(self.bindJoint))

		# Int Controls

		intCtlList = []
		i = 0
		for obj in ['upper', 'lower']:
			ctl = control(n=self.createName('{}Bound_{}_ctl'.format(obj, i)),
			              typ='square',
			              axis=[1, 0, 0])
			cmds.delete(cmds.pointConstraint(mainCtlList[i][1], mainCtlList[i + 1][1], ctl[1]))
			snap(mainCtlList[i][1], ctl[1], r=True, t=False)
			intCtlList.append(ctl)
			i += 1

		mainCtlList.insert(1, intCtlList[0])
		mainCtlList.insert(3, intCtlList[1])

		self.mainControl = mainCtlList

	def createCurveBound(self, selected, name, amount, parent=True, start=True, end=True, d=2):
		return self.makeCurve(selected,
		                      name=self.createName(name),
		                      amount=amount,
		                      parent=parent,
		                      start=start,
		                      end=end,
		                      d=d)

	def createBindJoints(self, selected):
		bindJoints = createJointChain(selected, typ=self.typ, world=True)

		i = 0
		for jnt in bindJoints:
			cmds.parentConstraint(jnt, selected[i], mo=True)
			cmds.scaleConstraint(jnt, selected[i], mo=True)
			i += 1

		return bindJoints

	class makeCurve(object):
		def __init__(self, selected, name, amount, upObject=None, parent=True, start=True, end=True, d=1):
			curve = makeNurbsCurve(selected, n=name, d=d)
			clusters = clusterCurve(curve, n='{}_cluster'.format(curve))
			null = locOnCurve(curve=curve, intLoc=amount, n='{}_null'.format(curve), upObject=upObject, start=start,
			                  end=end)
			grp = cmds.group(null, n='{}_null_grp'.format(name))

			if parent:
				i = 0
				for c in clusters:
					cmds.parent(c, selected[i])
					i += 1

			self.curve = curve
			self.cluster = clusters
			self.null = null
			self.group = grp

	def createConnections(self):

		cmds.addAttr(self.network, ln='smooth', at='double', dv=0, min=0, max=1)

		for i in [self.midNum / 2, self.midNum]:
			cmds.parent(self.mainControl[i][1], self.mainBound.null[i])

		del (self.upperBound.null)[-1]

		i = 0
		for null in self.upperBound.null + self.lowerBound.null:
			cmds.parent(self.control[i][1], null)
			i += 1

	def updateNetwork(self):
		pass


class createFKChain():
	def __init__(self, objs, scale=1, *args):

		self.control = None
		self.joint = None

		jointList = []
		controlList = []

		objs = createJointChain(objs, typ='fk', world=True)

		for obj in objs:
			ctl = control(obj, n='{}_ctl'.format(removeJointStr(obj)), axis=[1, 0, 0], parent=False, nest=True,
			              scale=scale)
			controlList.append(ctl)

		i = 0
		for x in controlList:
			if i != 0:
				cmds.parent(x[-1], controlList[i - 1][0])
			i += 1

		self.joint = objs
		self.control = controlList


class createIKChain():
	def __init__(self, objs, typ=ults.componentType.limb, scale=1, jnt=True, stretch=True, *args):

		if typ == ults.componentType.arm:
			axis = [1, 0, 0]
		elif typ == ults.componentType.leg:
			axis = [0, 0, 0]
		else:
			axis = [1, 0, 0]

		side = getPositionSide(objs)
		prefix = '{}_{}'.format(typ, side[0].upper())

		jointList = []
		controlList = []

		if jnt:
			objs = createJointChain(objs, typ='ik', world=False)

		start = objs[0]
		mid = objs[1]
		end = objs[2]

		# Controls

		for obj in [start, mid, end]:
			ctl = control(obj, n='{}_ctl'.format(removeJointStr(obj)), axis=axis, r=False, parent=False, scale=scale)
			controlList.append(ctl)

		# Hip Constraint

		# cmds.pointConstraint(controlList[0][0], start, mo=True)
		cmds.parent(start, controlList[0][0])

		# Create IK

		if typ == ults.componentType.leg:
			cmds.setAttr('{}.ty'.format(controlList[-1][-1]), 0)

		handle = \
			cmds.ikHandle(name='{}_{}_ikHandle_0'.format(typ, side[0].upper()), sj=start, ee=end, sol='ikRPsolver')[0]
		cmds.parent(handle, controlList[-1][0])
		cmds.orientConstraint(handle, end, mo=True)
		cmds.setAttr('{}.v'.format(handle), 0)

		distance = getDistance(start, end)

		pvPos = getPoleVectorPosition(start, mid, end)
		cmds.xform(controlList[1][1], ws=True, t=pvPos)

		# PoleVector

		pv = makePoleVector(handle, controlList[1][0], mid)

		# Create Stretch
		'''
		sCtl = controlList[-1][0]

		addEmptyAttr(sCtl, n='stretch')
		cmds.addAttr(sCtl, ln='addStretch', dv=0, k=True)
		cmds.addAttr(sCtl, ln='autoStretch', dv=0, min=0, max=1, k=True)
		cmds.addAttr(sCtl, ln='pin', dv=0, min=-10, max=10, k=True)
		cmds.addAttr(sCtl, ln='slide', dv=0, min=-10, max=10, k=True)

		stretchLoc = cmds.spaceLocator(n='{}_stretch_loc'.format(sCtl))[0]
		cmds.setAttr('{}.v'.format(stretchLoc), 0)
		snap(end, stretchLoc, r=True, t=True)
		cmds.parent(stretchLoc, sCtl)
		distanceA = getDistance(objs[0], objs[1])
		distanceB = getDistance(objs[1], objs[2])

		# Auto / Add Stretch
		disA = createDistanceNode(controlList[0][0], stretchLoc, n='{}_distance_0'.format(prefix))[0]

		amd = cmds.createNode('multiplyDivide', n='{}_autoStretch_ik_md_0'.format(prefix))
		cmds.setAttr('{}.operation'.format(amd), 2)
		cmds.setAttr('{}.input2X'.format(amd), distanceA + distanceB)
		cmds.connectAttr('{}.distance'.format(disA), '{}.input1X'.format(amd))

		aco = cmds.createNode('condition', n='{}_autoStretch_ik_cn_0'.format(prefix))
		cmds.setAttr('{}.operation'.format(aco), 2)
		cmds.connectAttr('{}.distance'.format(disA), '{}.firstTerm'.format(aco))
		cmds.connectAttr('{}.input2X'.format(amd), '{}.secondTerm'.format(aco))
		cmds.connectAttr('{}.outputX'.format(amd), '{}.colorIfTrueR'.format(aco))

		asr = cmds.createNode('setRange', n='{}_autoStretch_ik_sr_0'.format(prefix))
		cmds.setAttr('{}.minX'.format(asr), 1)
		cmds.setAttr('{}.oldMaxX'.format(asr), 1)
		cmds.connectAttr('{}.autoStretch'.format(sCtl), '{}.valueX'.format(asr))
		cmds.connectAttr('{}.outColorR'.format(aco), '{}.maxX'.format(asr))

		apm = cmds.createNode('plusMinusAverage', n='{}_autoStretch_ik_pm_0'.format(prefix))
		cmds.connectAttr('{}.addStretch'.format(sCtl), '{}.input3D[0].input3Dx'.format(apm))
		cmds.connectAttr('{}.addStretch'.format(sCtl), '{}.input3D[0].input3Dy'.format(apm))
		cmds.connectAttr('{}.outValueX'.format(asr), '{}.input3D[1].input3Dx'.format(apm))
		cmds.connectAttr('{}.outValueX'.format(asr), '{}.input3D[1].input3Dy'.format(apm))

		# Sliding Stretch

		slm = cmds.createNode('multiplyDivide', n='{}_slide_ik_md_0'.format(prefix))
		cmds.setAttr('{}.input2X'.format(slm), -1)
		cmds.connectAttr('{}.slide'.format(sCtl), '{}.input1X'.format(slm))

		slc = cmds.createNode('condition', n='{}_slide_ik_cn_0'.format(prefix))
		cmds.setAttr('{}.operation'.format(slc), 2)
		cmds.connectAttr('{}.slide'.format(sCtl), '{}.firstTerm'.format(slc))
		cmds.connectAttr('{}.slide'.format(sCtl), '{}.colorIfTrueG'.format(slc))
		cmds.connectAttr('{}.slide'.format(sCtl), '{}.colorIfFalseG'.format(slc))
		cmds.connectAttr('{}.outputX'.format(slm), '{}.colorIfTrueR'.format(slc))
		cmds.connectAttr('{}.outputX'.format(slm), '{}.colorIfFalseR'.format(slc))

		cmds.connectAttr('{}.outColorR'.format(slc), '{}.input3D[2].input3Dx'.format(apm))
		cmds.connectAttr('{}.outColorG'.format(slc), '{}.input3D[2].input3Dy'.format(apm))

		# Pinning / Locking

		disB = createDistanceNode(controlList[0][0], controlList[1][0], n='{}_distance_0'.format(prefix))[0]
		disC = createDistanceNode(controlList[1][0], stretchLoc, n='{}_distance_0'.format(prefix))[0]

		pmd = cmds.createNode('multiplyDivide', n='{}_pin_ik_md_0'.format(prefix))
		cmds.setAttr('{}.input2X'.format(pmd), distanceA)
		cmds.setAttr('{}.input2Y'.format(pmd), distanceB)
		cmds.connectAttr('{}.distance'.format(disB), '{}.input1X'.format(pmd))
		cmds.connectAttr('{}.distance'.format(disC), '{}.input1Y'.format(pmd))

		pbc = cmds.createNode('blendColors', n='{}_pin_ik_bc_0'.format(prefix))
		cmds.connectAttr('{}.pin'.format(sCtl), '{}.blender'.format(pbc))
		cmds.connectAttr('{}.outputX'.format(pmd), '{}.color1R'.format(pbc))
		cmds.connectAttr('{}.outputY'.format(pmd), '{}.color1G'.format(pbc))

		cmds.connectAttr('{}.output3Dx'.format(apm), '{}.color2R'.format(pbc))
		cmds.connectAttr('{}.output3Dy'.format(apm), '{}.color2G'.format(pbc))

		# Scale

		cmds.connectAttr('{}.outputR'.format(pbc), '{}.sx'.format(objs[0]))
		cmds.connectAttr('{}.outputG'.format(pbc), '{}.sx'.format(objs[1]))
		'''
		# Return
		self.joint = objs
		self.ikHandle = handle
		self.poleVector = pv
		self.control = controlList


class createIKFootPivot():
	def __init__(self, n='ik_footPivot', ik=None, start=None, end=None, ctl=None, *args):

		side = getPositionSide(start)

		# Query IK

		if not ik:
			ik = queryIK(start).ikHandle

		# Create Nulls

		grpList = []

		for grp in ['inner', 'outter', 'heel', 'toe', 'ball']:
			g = cmds.group(n='{}_{}_null'.format(n, grp), em=True)
			grpList.append(g)

		i = 0
		for g in grpList:
			if i != 0:
				cmds.parent(g, grpList[i - 1])
			i += 1

		masterGrp = cmds.group(grpList[0], n='{}_grp'.format(n))

		# Toe Raise

		toeRaise = cmds.group(n='{}_toeRaise_null'.format(n), em=True)
		cmds.parent(toeRaise, grpList[3])
		grpList.append(toeRaise)

		# Pivot Locations

		snap(start, masterGrp, t=True, r=False)
		loc = cmds.spaceLocator()
		snap(end, loc, t=True, r=False)
		cmds.delete(
				cmds.aimConstraint(loc, masterGrp, aimVector=[0, 0, 1], upVector=[0, 1, 0], worldUpType='vector',
				                   worldUpVector=[0, 1, 0], skip=['x', 'z']))
		cmds.delete(loc)

		bounds = estimateBoundsByJoint(start)

		if bounds.verts:
			if side == ults.componentType.right:
				grpList[0], grpList[1] = grpList[1], grpList[0]

			i = 0
			for b in [bounds.minX, bounds.maxX, bounds.minZ, bounds.maxZ]:
				cmds.xform(grpList[i], ws=True, rp=[b[0], 0, b[2]])
				i += 1

		for grp in [grpList[4], grpList[5]]:
			snap(end, grp, t=True, r=False)
			freezeTransform(grp)

		# Ball Control

		ballCtl = control(end, n='{}_ball_ctl'.format(n), axis=[1, 0, 0], parent=False)
		cmds.parent(ballCtl[1], grpList[4])

		# Toe Control

		toeCtl = control(grpList[3], n='{}_toe_ctl'.format(n), axis=[1, 0, 0], parent=False)
		cmds.parent(toeCtl[1], grpList[5])
		snap(end, toeCtl[1], t=False, r=True)

		toePos = cmds.xform(grpList[5], q=True, ws=True, rp=True)
		cmds.xform(toeCtl[0], ws=True, rp=toePos)
		cmds.xform(toeCtl[1], ws=True, rp=toePos)
		cmds.orientConstraint(toeCtl[0], end, mo=True)

		# Main Control

		if not ctl:
			ctl = network(n='{}_Network_0'.format(n), typ='foot')
			cmds.setAttr('{}.side'.format(ctl), side, type='string', l=True)

			i = 0
			for null in ['inner', 'outter', 'heel', 'toe', 'ball', 'toeRaise']:
				connectToNetwork(grpList[i], ctl, '{}_pivot'.format(null))
				i += 1

		else:
			cmds.parent(masterGrp, ctl)

		addEmptyAttr(ctl, n='footPivot')

		attrDict = {
			'roll'     : 0,
			'heelAngle': 45,
			'ballAngle': 45,
			'toeAngle' : 70,
			'toeRaise' : 0,
			'bank'     : 0,
		}

		for attr in attrDict:
			cmds.addAttr(ctl, ln=attr, at='double', dv=attrDict[attr], k=True)

		# Control Visibility

		cmds.addAttr(ctl, ln='footControls', at='bool', k=True)
		cmds.setAttr('{}.footControls'.format(ctl), e=True, channelBox=True)

		for x in [ballCtl[1], toeCtl[1]]:
			cmds.connectAttr('{}.footControls'.format(ctl), '{}.v'.format(x))

		# Heel

		mul = cmds.createNode('multDoubleLinear')
		cmds.setAttr('{}.input2'.format(mul), -1)

		cmds.connectAttr('{}.heelAngle'.format(ctl), '{}.input1'.format(mul))

		range = cmds.createNode('setRange')
		cmds.setAttr('{}.oldMinX'.format(range), -10)

		cmds.connectAttr('{}.output'.format(mul), '{}.minX'.format(range))
		cmds.connectAttr('{}.roll'.format(ctl), '{}.valueX'.format(range))

		cmds.connectAttr('{}.outValueX'.format(range), '{}.rx'.format(grpList[2]))

		# Toe Pivot Connections

		range = cmds.createNode('setRange')
		cmds.setAttr('{}.oldMinX'.format(range), 10)
		cmds.setAttr('{}.oldMaxX'.format(range), 20)

		cmds.connectAttr('{}.toeAngle'.format(ctl), '{}.maxX'.format(range))
		cmds.connectAttr('{}.roll'.format(ctl), '{}.valueX'.format(range))

		cmds.connectAttr('{}.outValueX'.format(range), '{}.rx'.format(grpList[3]))
		cmds.connectAttr('{}.toeRaise'.format(ctl), '{}.rx'.format(toeRaise))

		# Ball Pivot Connections

		range = cmds.createNode('setRange')
		cmds.setAttr('{}.oldMaxX'.format(range), 10)
		cmds.setAttr('{}.oldMinY'.format(range), 10)
		cmds.setAttr('{}.oldMaxY'.format(range), 20)

		cmds.connectAttr('{}.ballAngle'.format(ctl), '{}.maxX'.format(range))
		cmds.connectAttr('{}.ballAngle'.format(ctl), '{}.minY'.format(range))
		cmds.connectAttr('{}.roll'.format(ctl), '{}.valueX'.format(range))
		cmds.connectAttr('{}.roll'.format(ctl), '{}.valueY'.format(range))

		con = cmds.createNode('condition')
		cmds.setAttr('{}.secondTerm'.format(con), 10)
		cmds.setAttr('{}.operation'.format(con), 2)

		cmds.connectAttr('{}.roll'.format(ctl), '{}.firstTerm'.format(con))
		cmds.connectAttr('{}.outValueX'.format(range), '{}.colorIfFalseR'.format(con))
		cmds.connectAttr('{}.outValueY'.format(range), '{}.colorIfTrueR'.format(con))
		cmds.connectAttr('{}.outColorR'.format(con), '{}.rx'.format(grpList[4]))

		# Inner / Outter

		con = cmds.createNode('condition')
		cmds.setAttr('{}.operation'.format(con), 2)

		cmds.connectAttr('{}.bank'.format(ctl), '{}.firstTerm'.format(con))
		cmds.connectAttr('{}.bank'.format(ctl), '{}.colorIfTrueR'.format(con))
		cmds.connectAttr('{}.bank'.format(ctl), '{}.colorIfFalseG'.format(con))

		cmds.connectAttr('{}.outColorR'.format(con), '{}.rz'.format(grpList[0]))
		cmds.connectAttr('{}.outColorG'.format(con), '{}.rz'.format(grpList[1]))

		# IK

		if ik:
			cmds.parent(ik, ballCtl[0])

		# Return

		# self.network = net
		self.pivot = grpList
		self.group = masterGrp
		self.control = [ballCtl, toeCtl]
		self.attr = attrDict


#########################################################################################################################
#																														#
#																														#
#	Auto Rig    																								        #
#																														#
#																														#
#########################################################################################################################

class autoRig():
	def __init__(self, characterName='character', *args):

		selected = cmds.ls(sl=True)

		if not selected:
			selected = self.queryScene()

		if selected:
			joints = cmds.listRelatives(selected[0], ad=True, type='joint')
			joints.append(selected[0])

			jointQuery = jointLabel(joints, isDebug=False)

			# BiPed
			root = jointQuery.get(ults.componentType.root)
			cog = jointQuery.get(ults.componentType.cog)
			hip = jointQuery.get(ults.componentType.hip)
			spine = jointQuery.get(ults.componentType.spine)
			head = jointQuery.get(ults.componentType.head)
			armLeft = jointQuery.get(ults.componentType.arm, ults.componentType.left)
			armRight = jointQuery.get(ults.componentType.arm, ults.componentType.right)
			legLeft = jointQuery.get(ults.componentType.leg, ults.componentType.left)
			legRight = jointQuery.get(ults.componentType.leg, ults.componentType.right)

			pUI = progressWindow(st='Creating Control Modules...', max=9)

			ROOT(root)
			pUI.update()

			COG(cog)
			pUI.update()

			HIP(hip)
			pUI.update()

			SPINE(spine)
			pUI.update()

			HEAD(head)
			pUI.update()

			ARM(armLeft)
			pUI.update()

			ARM(armRight)
			pUI.update()

			LEG(legLeft)
			pUI.update()

			LEG(legRight)
			pUI.update()

	def queryScene(self):
		joints = cmds.ls(type='joint')
		return jointLabel(joints).get(ults.componentType.root)


#########################################################################################################################
#																														#
#																														#
#	Menu    																								        #
#																														#
#																														#
#########################################################################################################################


def menu():
	cmds.menuItem(l='Root', c=ROOT)
	cmds.menuItem(l='COG', c=COG)
	cmds.menuItem(d=True)
	cmds.menuItem(l='Spine', c=SPINE)
	cmds.menuItem(l='Neck', )
	cmds.menuItem(l='Head', c=HEAD)
	cmds.menuItem(d=True)
	cmds.menuItem(l='Collar')
	cmds.menuItem(l='Arm', c=ARM)
	cmds.menuItem(l='Hand')
	cmds.menuItem(d=True)
	cmds.menuItem(l='Hip')
	cmds.menuItem(l='Leg', c=LEG)
	cmds.menuItem(l='Foot')
	cmds.menuItem(d=True)
	cmds.menuItem(l='Tail')
	return
