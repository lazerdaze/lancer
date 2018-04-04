#########################################################################################################################
#																														#
#																														#
#	LAYOUT																											    #
#																														#
#																														#
#########################################################################################################################


from maya import cmds, mel


class theme:
	margin = 5
	padding = 10
	window = [.267, .267, .267]
	button = [.365, .365, .365]
	layout = [.286, .286, .286]
	vertical = [.286, .286, .286]
	border = 0
	borderColor = [.169, .169, .169]
	field = [.169, .169, .169]
	divider = [.5, .5, .5]
	header = 25
	headerColor = [.365, .365, .365]



#########################################################################################################################
#																														#
#																														#
#	WIDGET CLASS																									    #
#																														#
#																														#
#########################################################################################################################


class widget(object):
	def __init__(self,
	             name=None,
	             label=None,
	             width=0,
	             height=0,
	             margin=theme.margin,
	             padding=theme.padding,
	             visible=True,
	             enable=True,
	             backgroundColor=None,
	             border=theme.border,
	             borderColor=theme.borderColor,
	             parent=None,
	             children=None,
	             annotation=None,
	             ):
		self.name = name
		self.label = label
		self.width = width
		self.height = height
		self.margin = self.defaultSpacing(margin)
		self.padding = self.defaultSpacing(padding)
		self.visible = visible
		self.enable = enable
		self.backgroundColor = backgroundColor
		self.border = self.defaultSpacing(border)
		self.borderColor = borderColor
		self.parent = parent
		self.children = children
		self.annotation = annotation
		self.ui = self.create()

	def create(self):
		return None

	def defaultSpacing(self, value):
		if type(value) is not list:
			value = [value, value, value, value]
		return value

	def end(self):
		cmds.setParent('..')


def end():
	cmds.setParent('..')


#########################################################################################################################
#																														#
#																														#
#	WINDOW																											    #
#																														#
#																														#
#########################################################################################################################


class window(widget):
	def __init__(self,
	             name='window1',
	             label=None,
	             width=100,
	             height=100,
	             backgroundColor=theme.window,
	             ):
		widget.__init__(self, name=name, label=label, width=width, height=height, backgroundColor=backgroundColor)

	def create(self):
		# Delete Existing Window
		if cmds.window(self.name, exists=True):
			cmds.deleteUI(self.name, window=True)

		# Create Window
		cmds.window(
				self.name,
				title=self.label if self.label else self.name,
				width=self.width,
				height=self.height,
				backgroundColor=self.backgroundColor
		)

	def end(self):
		cmds.showWindow(self.name)


#########################################################################################################################
#																														#
#																														#
#	VERTICAL HORIZONTAL LAYOUTS																							#
#																														#
#																														#
#########################################################################################################################


class layout(widget):
	def __init__(self,
	             name='layout1',
	             label=None,
	             labelBackgroundColor=theme.headerColor,
	             labelHeight=theme.header,
	             labelAlign='center',
	             backgroundColor=theme.layout,
	             margin=theme.margin,
	             padding=theme.padding,
	             rowSpace=theme.margin,
	             border=theme.border,
	             borderColor=theme.borderColor,
	             style='header',
	             ):
		self.rowSpace = rowSpace
		self.labelHeight = labelHeight
		self.labelAlign = labelAlign
		self.labelBackgroundColor = labelBackgroundColor
		self.style = style

		widget.__init__(self,
		                name=name,
		                label=label,
		                backgroundColor=backgroundColor,
		                margin=margin,
		                padding=padding,
		                border=border,
		                borderColor=borderColor,
		                )

	def create(self):
		ui0 = cmds.formLayout()
		ui1 = cmds.formLayout(backgroundColor=self.borderColor)
		ui2 = cmds.formLayout(backgroundColor=self.backgroundColor)
		ui3 = self.mainUI()
		cmds.formLayout(ui0,
		                e=True,
		                attachForm=(
			                (ui1, 'left', self.margin[0]),
			                (ui1, 'top', self.margin[1]),
			                (ui1, 'right', self.margin[2]),
			                (ui1, 'bottom', self.margin[3]),
		                ))
		cmds.formLayout(ui1,
		                e=True,
		                attachForm=(
			                (ui2, 'left', self.border[0]),
			                (ui2, 'top', self.border[1]),
			                (ui2, 'right', self.border[2]),
			                (ui2, 'bottom', self.border[3]),
		                ))
		cmds.formLayout(ui2,
		                e=True,
		                attachForm=(
			                (ui3, 'left', self.padding[0]),
			                (ui3, 'top', self.padding[1]),
			                (ui3, 'right', self.padding[2]),
			                (ui3, 'bottom', self.padding[3]),
		                ))

		if self.label:
			header = cmds.text(
					label=self.label,
					align=self.labelAlign,
					height=self.labelHeight,
					backgroundColor=self.labelBackgroundColor,
					parent=ui1,
			)
			cmds.formLayout(ui1,
			                e=True,
			                attachForm=(
				                (header, 'left', self.border[0]),
				                (header, 'top', self.border[1]),
				                (header, 'right', self.border[2])
			                ),
			                attachControl=(ui2, 'top', 0, header),
			                )

		return [ui1, ui2, ui3]

	def mainUI(self):
		return

	def end(self):
		cmds.setParent('..')
		cmds.setParent('..')
		cmds.setParent('..')
		cmds.setParent('..')


class vertical(layout):
	def __init__(self,
	             name='vertical1',
	             label=None,
	             backgroundColor=theme.vertical,
	             margin=theme.margin,
	             padding=theme.padding,
	             border=theme.border,
	             borderColor=theme.borderColor,
	             ):
		layout.__init__(self,
		                name=name,
		                label=label,
		                backgroundColor=backgroundColor,
		                margin=margin,
		                padding=padding,
		                border=border,
		                borderColor=borderColor,
		                )

	def mainUI(self):
		return cmds.columnLayout(
				adjustableColumn=True,
				rowSpacing=self.rowSpace,
		)


class horizontal(layout):
	def __init__(self,
	             name='horizontal1',
	             label=None,
	             backgroundColor=theme.vertical,
	             margin=theme.margin,
	             padding=theme.padding,
	             ):
		layout.__init__(self,
		                name=name,
		                label=label,
		                backgroundColor=backgroundColor,
		                margin=margin,
		                padding=padding
		                )

	def mainUI(self):
		return cmds.columnLayout(
				adjustableColumn=True,
				rowSpacing=self.rowSpace,
		)


#########################################################################################################################
#																														#
#																														#
#	BUTTONS																											    #
#																														#
#																														#
#########################################################################################################################


class button(widget):
	def __init__(self,
	             label='button1',
	             backgroundColor=theme.button,
	             ):
		widget.__init__(self,
		                label=label,
		                backgroundColor=backgroundColor,
		                )

	def create(self):
		return cmds.button(
				label=self.label,
				backgroundColor=self.backgroundColor,
		)


#########################################################################################################################
#																														#
#																														#
#	DECORATIONS																											#
#																														#
#																														#
#########################################################################################################################

'''
def divider(label=None, mar=10):
	if label:
		ui = cmds.rowLayout(nc=2, ad2=2)
		cmds.text(l=label + '  ', al='left')
		cmds.columnLayout(bgc=[.5, .5, .5], h=1)
		cmds.setParent('..')
		cmds.setParent('..')
	else:
		ui = cmds.columnLayout(h=mar, adj=True)
		cmds.columnLayout(bgc=[.5, .5, .5], h=1)
		cmds.setParent('..')
		cmds.setParent('..')
	return ui
'''


class divider(widget):
	def __init__(self, label=None, height=1, margin=0, align='center', color=theme.borderColor):
		self.align = align
		self.color = color

		widget.__init__(self, label=label, height=height, margin=margin)

	def create(self):
		ui0 = cmds.formLayout()
		ui1 = cmds.formLayout()

		if self.label:
			ui2 = cmds.rowLayout(nc=3, ad3=3)
			cmds.columnLayout(height=self.height, width=40, backgroundColor=self.color)
			cmds.setParent('..')
			cmds.text(label=self.label, align='center')
			self.line()
			cmds.setParent('..')

			cmds.formLayout(ui1,
			                e=True,
			                attachForm=(
				                (ui2, 'left', 0),
				                (ui2, 'top', 0),
				                (ui2, 'right', 0),
				                (ui2, 'bottom', 0),
			                ))

		cmds.formLayout(ui0,
		                e=True,
		                attachForm=(
			                (ui1, 'left', self.margin[0]),
			                (ui1, 'top', self.margin[1]),
			                (ui1, 'right', self.margin[2]),
			                (ui1, 'bottom', self.margin[3]),
		                ))

		cmds.setParent('..')
		cmds.setParent('..')

	def line(self):
		ui = cmds.columnLayout(height=self.height, backgroundColor=self.color)
		cmds.setParent('..')
		return ui
