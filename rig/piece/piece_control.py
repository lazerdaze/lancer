# Lancer Modules
from rig.utils import *

# Maya Modules
from maya import cmds


class CONTROL(object):
	def __init__(self,
	             name=Component.control,
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
	             color=None,
	             ):
		"""
		Base Control class to be used in all parts classes.
		Created as a joint with nurbs shape node and default attributes.

		:param name:        Name of the control.
		:param typ:         Preset wire type.
		:param scale:       Scale of control. Default is 1.
		:param axis:        Forward axis of the control.
		:param translate:   Snap the position of the control to the child.
		:param rotate:      Snap the rotation of the control to the child.
		:param child:       Object that is parented to the control.
		:param parent:      Object that the control is parented to.
		:param index:       Used to determined rig priority.
		:param side:        Side of the controls origin.
		:param label:       Label of the control to determine rig type.
		:param color:       Color of control.
		"""

		self.name = name
		self.typ = typ
		self.scale = scale
		self.axis = axis if axis else [1, 0, 0]
		self.translate = translate
		self.rotate = rotate
		self.child = child
		self.parent = parent
		self.index = index
		self.side = side
		self.label = label
		self.color = color

		self.transform = None
		self.shape = None
		self.group = None

		self.create()

	def create(self):
		ctl = createControl(name=self.name,
		                    shape=self.typ,
		                    axis=self.axis,
		                    scale=self.scale,
		                    )
		self.transform = ctl[0]
		self.shape = ctl[1]
		self.setAttributes(self.transform)
		self.setLabel()
		self.setColor()
		self.createGroup()
		return

	def setAttributes(self, selected):
		for attr in [Component.character,
		             Component.skeletonNetwork,
		             Component.rigNetwork,
		             Component.rigNetworkRoot,
		             ]:
			cmds.addAttr(selected, ln=attr, at='message')

		cmds.addAttr(selected, ln=Component.index, at='long', dv=self.index)
		return

	def setColor(self):
		if type(self.color) is str:
			presetWireColor(self.transform, self.color)
		if type(self.color) is list:
			overrideColor(listCheck(self.transform), color=self.color)
		return

	def createGroup(self):
		self.group = cmds.group(name=longName(self.transform, Component.group), em=True)
		cmds.parent(self.transform, self.group)
		if self.child:
			snap(self.child, self.group, t=True, r=True)
		self.setAttributes(self.group)
		return

	def setLabel(self):
		if self.label:
			if ' ' in self.label:
				newStr = ''
				var = self.label.split(' ')

				for x in var:
					i = var.index(x)
					if i == 0:
						space = ''
					else:
						space = ' '
					newStr += '{}{}'.format(space, str(x).capitalize())

				self.label = newStr
			else:
				self.label = self.label.capitalize()

		if self.side and self.label:
			setJointLabel(self.transform, side=self.side.capitalize(), typ=self.label)
		elif self.side and not self.label:
			setJointLabel(self.transform, side=self.side.capitalize(), typ='None')
		elif self.label and not self.side:
			setJointLabel(self.transform, side='Center', typ=self.label)
		return


class FKCONTROL(CONTROL):
	def __init__(self,
	             name='fk_control',
	             scale=1,
	             child=None,
	             parent=None,
	             index=0,
	             side=None,
	             label=None,
	             axis=None,
	             ):
		CONTROL.__init__(self,
		                 name=name,
		                 typ=WireType.circleRotate,
		                 scale=scale,
		                 child=child,
		                 parent=parent,
		                 index=index,
		                 side=side,
		                 label=label,
		                 color=Component.fk,
		                 axis=axis,
		                 )


class IKCONTROL(CONTROL):
	def __init__(self,
	             name='ik_control',
	             scale=1,
	             child=None,
	             parent=None,
	             index=0,
	             side=None,
	             label=None,
	             axis=None,
	             ):
		CONTROL.__init__(self,
		                 name=name,
		                 typ=WireType.sphere,
		                 scale=scale,
		                 child=child,
		                 parent=parent,
		                 index=index,
		                 side=side,
		                 label=label,
		                 color=Component.ik,
		                 axis=axis,
		                 )


class ATTRCONTROL(CONTROL):
	def __init__(self,
	             name='attr_control',
	             scale=1,
	             child=None,
	             parent=None,
	             index=0,
	             side=None,
	             label=None,
	             axis=None,
	             ):
		CONTROL.__init__(self,
		                 name=name,
		                 typ=WireType.lollipop,
		                 scale=scale,
		                 child=child,
		                 parent=parent,
		                 index=index,
		                 side=side,
		                 label=label,
		                 color=Component.attr,
		                 axis=axis,
		                 )


class DETAILCONTROL(CONTROL):
	def __init__(self,
	             name='detail_control',
	             scale=1,
	             child=None,
	             parent=None,
	             index=0,
	             side=None,
	             label=None,
	             axis=None,
	             ):
		CONTROL.__init__(self,
		                 name=name,
		                 typ=WireType.doubleLollipop,
		                 scale=scale * 1.5,
		                 child=child,
		                 parent=parent,
		                 index=index,
		                 side=side,
		                 label=label,
		                 color=[.5, 1, 1],
		                 axis=axis,
		                 )


class GRANDCHILDCONTROL(CONTROL):
	def __init__(self,
	             name='grandChild_control',
	             scale=1,
	             child=None,
	             parent=None,
	             index=0,
	             side=None,
	             label=None,
	             axis=None,
	             ):
		CONTROL.__init__(self,
		                 name=name,
		                 typ=WireType.diamond,
		                 scale=scale * 2,
		                 child=child,
		                 parent=parent,
		                 index=index,
		                 side=side,
		                 label=label,
		                 color=[.5, 1, 1],
		                 axis=axis,
		                 )
