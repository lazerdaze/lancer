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
		                 name=Component.Global,
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
				if hasattr(ctrl, 'transform'):
					value = getattr(ctrl, 'transform')
					if value:
						result.append(value)

				if hasattr(ctrl, 'offset'):
					value = ctrl.offset.transform

					if value:
						result.append(value)

			elif ctrl is not None:
				if ctrl not in result:
					result.append(self.interface)
		return result

	def create(self):
		self.createRootControl()

		if self.cogItem:
			self.createCOGControl()

		if self.hipItem:
			self.createHipControl()

		self.set = self.createSet(self.allControls)
		# self.finalize()
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
		self.interface = INTERFACE_CONTROL(name=self.name,
		                                   prefix=self.prefix,
		                                   item=item,
		                                   wire=WireType.gearMover,
		                                   axis=[0, 0, 0],
		                                   scale=scale,
		                                   offset=WireType.circleRotate
		                                   )

		self.interface.offset.rigInterface = self.interface
		self.world = self.interface.offset.transform

		# createRootOffset
		attrName = 'repoVisibility'

		self.repoControl = Control(prefix=self.prefix,
		                           name=self.name,
		                           item=item,
		                           wireType=WireType.sphere,
		                           axis=[0, 0, 0],
		                           scale=scale * .25,
		                           color=WireColor.purple,
		                           kind=camelCase('repo', Component.control, capitalize=False),
		                           )

		addAttribute(node=self.interface, attribute=attrName, kind=MayaAttrType.bool, channelBox=True, keyable=False)
		cmds.connectAttr('{}.{}'.format(self.interface, attrName), '{}.v'.format(self.repoControl.shape))

		self.repoControl.parent = self.interface.offset.transform
		self.repoControl.rigInterface = self.interface

		createMonoRelationship(source=self.interface,
		                       sourceAttr='repo',
		                       destination=self.repoControl.transform,
		                       destinationAttr='rigParent',
		                       )

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
		                                    wire=WireType.gear,
		                                    axis=[0, 2, 0],
		                                    scale=scale * .3,
		                                    offset=WireType.circleRotate,
		                                    )

		self.local = self.cogControl.offset.transform

		# Hierarchy
		self.cogControl.offset.rigInterface = self.cogControl

		self.cogControl.parent = self.interface.offset.transform
		self.cogControl.snapTo(item, True, False)
		self.cogControl.rigParent = self.interface
		self.cogControl.rigRoot = self.interface

		# Constrain
		cmds.parentConstraint(self.cogControl.offset.transform, item, mo=True)
		cmds.scaleConstraint(self.cogControl.offset.transform, item, mo=True)

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
		self.hipControl.parent = self.cogControl.offset.transform
		self.hipControl.snapTo(item)
		self.hipControl.rigParent = self.interface
		self.hipControl.rigRoot = self.interface

		# Constrain
		cmds.parentConstraint(self.hipControl.offset.transform, item, mo=True)
		return

	def finalize(self, items=None, parent=None):
		BASERIG.finalize(self, items, parent)

		self.connectToRig(self.repoControl, self.interface, 'repoControl')
		self.connectToRig(self.cogControl, self.interface, 'cogControl')
		self.connectToRig(self.hipControl, self.interface, 'hipControl')
		return
