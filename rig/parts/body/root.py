# Lancer Modules
from rig.utils import *
from rig.parts.baseRig import BASERIG

# Maya Modules
from maya import cmds


class ROOT(BASERIG):
	def __init__(self,
				 root=None,
				 cog=None,
				 hip=None,
				 ):

		'''
		Central Rigging Part used in all rigging hierarchies.
		Rig is not complete without a ROOT.

		:param root:
		:param cog:
		:param hip:
		'''

		items = []

		for x in [root, cog, hip]:
			if x is not None:
				items.append(x)

		BASERIG.__init__(self,
						 prefix=Part.root,
						 side=Position.center,
						 kind=Part.root,
						 items=items,
						 )

		# Items
		self.rootItem = root
		self.cogItem = cog
		self.hipItem = hip

		# Controls
		self.repoControl = None
		self.cogControl = None
		self.hipControl = None

		# Init
		self.create()

	@property
	def allControls(self):
		result = []

		for ctrl in [self.interface, self.repoControl, self.cogControl, self.hipControl]:
			if isinstance(ctrl, object):
				for attr in ['transform', 'offsetTransform']:
					if hasattr(ctrl, attr):
						value = getattr(ctrl, attr)
						if value:
							result.append(value)
			elif ctrl is not None:
				result.append(self.interface)
		return result

	def create(self):
		self.createRootControl()

		if self.cogItem:
			self.createCOGControl()

		if self.hipItem:
			self.createHipControl()

		self.set = self.createSet(self.allControls)
		self.finalize()
		return

	def createRootControl(self, item=None):
		# Edge Case
		if not item:
			item = self.rootItem

		# Scale
		scale = 1.0

		if self.items:
			scale = self.scaleByHeight(self.items) * .35

		# Controls
		self.interface = INTERFACE_CONTROL(name=Component.Global,
										   prefix=self.prefix,
										   item=item,
										   wireType=WireType.gearMover,
										   axis=[0, 0, 0],
										   scale=scale,
										   color=WireColor.purple,
										   kind=Component.rig,
										   offset=WireType.circleRotate
										   )

		self.world = self.interface.offset.transform

		# createRootOffset
		attrName = 'repoVisibility'

		self.repoControl = RIGCONTROL(name=Component.Global,
									  prefix=self.prefix,
									  item=item,
									  wireType=WireType.sphere,
									  axis=[0, 0, 0],
									  scale=scale * .25,
									  color=WireColor.purple,
									  kind='repo',
									  )

		addAttribute(node=self.interface, attribute=attrName, kind=MayaAttrType.bool, channelBox=True, keyable=False)
		cmds.connectAttr('{}.{}'.format(self.interface, attrName), '{}.v'.format(self.repoControl.shape))

		# Hierarchy
		self.repoControl.parent = self.interface.offset.transform

		# Constrain
		if item:
			cmds.parentConstraint(self.repoControl, item, mo=True)
			cmds.scaleConstraint(self.repoControl, item, mo=True)

		# Global
		globalNode = self.interface.nullConnection
		attrName = 'globalScale'

		cmds.addAttr(self.interface, ln=attrName, dv=1)
		cmds.setAttr('{}.{}'.format(self.interface, attrName), k=False, channelBox=True)

		for axis in ['x', 'y', 'z']:
			cmds.connectAttr('{}.{}'.format(self.interface, attrName), '{}.s{}'.format(globalNode, axis))
		return

	def createCOGControl(self, item=None):
		# Edge Case
		if not item:
			if self.cogItem:
				item = self.cogItem
			else:
				raise ValueError('No item provided.')

		# Scale
		scale = 1.0

		if item:
			scale = distanceFromOrigin(item)

		self.cogControl = INTERFACE_CONTROL(name=Component.rig,
											prefix=Part.cog,
											item=item,
											wireType=WireType.gear,
											axis=[0, 2, 0],
											scale=scale * .3,
											color=WireColor.purple,
											offset=WireType.circleRotate,
											)

		self.local = self.cogControl.offset.transform

		# Hierarchy
		self.cogControl.parent = self.interface.offset.tranform
		self.cogControl.snapTo(item, True, False)

		# Constrain
		cmds.parentConstraint(self.cogControl.offset.tranform, item, mo=True)
		cmds.scaleConstraint(self.cogControl.offset.tranform, item, mo=True)

		return

	def createHipControl(self, item=None):
		# Edge Case
		if not item:
			if self.hipItem:
				item = self.hipItem
			else:
				raise ValueError('No item provided.')

		# Scale
		scale = 1.0

		if item:
			scale = distanceFromOrigin(item)

		self.hipControl = RIGCONTROL(name=Component.rig,
									 prefix=Part.hip,
									 item=item,
									 side=Position.center,
									 wireType=WireType.circleRotate,
									 scale=scale * .2,
									 color=WireColor.yellow,
									 offset=True,
									 axis=[1, 1, 0]
									 )
		# Hierarchy
		self.hipControl.parent = self.cogControl.offsetTransform
		self.hipControl.snapTo(item)

		# Constrain
		cmds.parentConstraint(self.hipControl.offset.transform, item, mo=True)
		return

	def finalize(self, items=None, parent=None):
		BASERIG.finalize(self, items, parent)

		self.connectToRig(self.repoControl, self.interface, 'repoControl')
		self.connectToRig(self.cogControl, self.interface, 'cogControl')
		self.connectToRig(self.hipControl, self.interface, 'hipControl')
		return
