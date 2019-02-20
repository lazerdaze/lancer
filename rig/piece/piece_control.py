# Lancer Modules
from rig.utils import *


class CONTROL(Control):
	def __init__(self,
	             name=Component.rig,
	             parent=None,
	             prefix=None,
	             item=None,
	             wireType=WireType.circleRotate,
	             axis=None,
	             scale=1.0,
	             index=None,
	             side=None,
	             sector=None,
	             color=WireColor.blue,
	             offset=False,
	             kind=None,
	             ):
		Control.__init__(self,
		                 name=name,
		                 parent=parent,
		                 prefix=prefix,
		                 item=item,
		                 wire=wireType,
		                 axis=axis,
		                 scale=scale,
		                 index=index,
		                 side=side,
		                 sector=sector,
		                 color=color,
		                 offset=offset,
		                 kind=camelCase(kind, Component.control, capitalize=False),
		                 )

		self.setDefaults()

	def setDefaults(self):
		for item in [self.transform, self.offsetTransform]:
			if item:
				for attr in [Component.parent,
				             Component.rig,
				             ]:
					if not attributeExist(item, attr):
						addAttribute(node=item, attribute=attr, kind=MayaAttrType.message)

				for attr in [Component.children]:
					if not attributeExist(item, attr):
						addAttribute(node=item, attribute=attr, kind=MayaAttrType.string, lock=True)
		return


class FKCONTROL(CONTROL):
	def __init__(self,
	             name=Component.rig,
	             parent=None,
	             prefix=None,
	             item=None,
	             wireType=WireType.circleRotate,
	             axis=None,
	             scale=1.0,
	             index=None,
	             side=None,
	             sector=None,
	             color=None,
	             ):

		if color is None:
			if side == Position.left:
				color = WireColor.blue
			elif side == Position.right:
				color = WireColor.red
			elif side == Position.center:
				color = WireColor.yellow
			else:
				color = WireColor.blue

		CONTROL.__init__(self,
		                 name=name,
		                 parent=parent,
		                 prefix=prefix,
		                 item=item,
		                 wireType=wireType,
		                 axis=axis,
		                 scale=scale,
		                 index=index,
		                 side=side,
		                 sector=sector,
		                 offset=True,
		                 kind=Component.fk,
		                 color=color,
		                 )


class IKCONTROL(CONTROL):
	def __init__(self,
	             name=Component.rig,
	             parent=None,
	             prefix=None,
	             item=None,
	             wireType=WireType.sphere,
	             axis=None,
	             scale=1.0,
	             index=None,
	             side=None,
	             sector=None,
	             color=None,
	             ):

		if color is None:
			if side == Position.left:
				color = WireColor.cyan
			elif side == Position.right:
				color = WireColor.magenta
			elif side == Position.center:
				color = WireColor.green
			else:
				color = WireColor.red

		CONTROL.__init__(self,
		                 name=name,
		                 parent=parent,
		                 prefix=prefix,
		                 item=item,
		                 wireType=wireType,
		                 axis=axis,
		                 scale=scale,
		                 index=index,
		                 side=side,
		                 sector=sector,
		                 color=color,
		                 offset=True,
		                 kind=Component.ik,
		                 )


class MASTERCONTROL(CONTROL):
	def __init__(self,
	             name=Component.rig,
	             parent=None,
	             prefix=None,
	             item=None,
	             wireType=WireType.master,
	             axis=None,
	             scale=1.0,
	             index=None,
	             side=None,
	             sector=None,
	             ):
		CONTROL.__init__(self,
		                 name=name,
		                 parent=parent,
		                 prefix=prefix,
		                 item=item,
		                 wireType=wireType,
		                 axis=axis,
		                 scale=scale,
		                 index=index,
		                 side=side,
		                 sector=sector,
		                 color=WireColor.purple,
		                 kind=Component.master,
		                 )

	def setDefaults(self):
		CONTROL.setDefaults(self)

		item = self.transform
		lockKeyableAttributes(item, hide=True)

		for attr in [Component.joint,
		             Component.bind,
		             Component.leaf,
		             ]:

			if not attributeExist(item, attr):
				addAttribute(node=item, attribute=attr, kind=MayaAttrType.string, lock=True)

		for attr in [Component.fkControl,
		             Component.ikControl,
		             Component.ikJoint,
		             Component.bindControl,
		             Component.leafControl,
		             ]:

			if not attributeExist(item, attr):
				addAttribute(node=item, attribute=attr, kind=MayaAttrType.string, array=True)

		for attr in [Component.bindTwist,
		             Component.fkStretch,
		             Component.ikStretch,
		             Component.bindStretch,
		             Component.bindSns,
		             ]:

			if not attributeExist(item, attr):
				addAttribute(node=item, attribute=attr, kind=MayaAttrType.float, array=True,
				             keyable=False)

		for attr in [Component.fkik,
		             Component.fkLocalWorld,
		             Component.ikLocalWorld,
		             Component.twistAuto,
		             Component.twist,
		             Component.stretchAuto,
		             Component.stretch,
		             Component.snsAuto,
		             Component.sns,
		             ]:

			if not attributeExist(item, attr):
				minValue = None
				maxValue = None
				defaultValue = None

				if 'local' in attr.lower():
					minValue = 0
					maxValue = 1
					defaultValue = 0

				elif 'auto' in attr.lower():
					minValue = 0
					maxValue = 1
					defaultValue = 1

				elif Component.fkik == attr:
					minValue = 0
					maxValue = 1
					defaultValue = 0

				addAttribute(node=item, attribute=attr, kind=MayaAttrType.float, minValue=minValue, maxValue=maxValue,
				             value=defaultValue, channelBox=False, keyable=True)

		for attr in [Component.mirror,
		             Component.fkPoleVector,
		             Component.ikPoleVector,
		             Component.ikHandle,
		             Component.set,
		             ]:

			if not attributeExist(item, attr):
				addAttribute(node=item, attribute=attr, kind=MayaAttrType.message)

		for attr in [Component.jointDisplay, Component.controlDisplay, Component.detailControlDisplay]:
			if not attributeExist(item, attr):
				addAttribute(node=item, attribute=attr, kind=MayaAttrType.bool, channelBox=True, keyable=False)
		return


class BINDCONTROL(CONTROL):
	def __init__(self,
	             name=Component.rig,
	             parent=None,
	             prefix=None,
	             item=None,
	             wireType=WireType.doubleLollipop,
	             axis=None,
	             scale=1.0,
	             index=None,
	             side=None,
	             sector=None,
	             ):
		CONTROL.__init__(self,
		                 name=name,
		                 parent=parent,
		                 prefix=prefix,
		                 item=item,
		                 wireType=wireType,
		                 axis=axis,
		                 scale=scale * 1.5,
		                 index=index,
		                 side=side,
		                 sector=sector,
		                 color=[.5, 1, 1],
		                 kind=Component.bind,
		                 )


class LEAFCONTROL(CONTROL):
	def __init__(self,
	             name=Component.rig,
	             parent=None,
	             prefix=None,
	             item=None,
	             wireType=WireType.diamond,
	             axis=None,
	             scale=1.0,
	             index=None,
	             side=None,
	             sector=None,
	             ):
		CONTROL.__init__(self,
		                 name=name,
		                 parent=parent,
		                 prefix=prefix,
		                 item=item,
		                 wireType=wireType,
		                 axis=axis,
		                 scale=scale,
		                 index=index,
		                 side=side,
		                 sector=sector,
		                 color=[.5, 1, 1],
		                 kind=Component.leaf,
		                 )
