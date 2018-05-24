# LANCER.RIG.UI
#
#
#
#
#

# Lancer Modules
import library.xfer as xfer
import ults
import network
import parts
import skin
import skeleton

reload(skeleton)

# Maya Modules
import maya.cmds as cmds
import maya.mel as mel

# Python Modules
import os

# Global Variables
pad = 5  # UI Padding
mar = 10  # UI Margins
col = 60  # UI Label Columns Width
isDebug = True  # Print Debugging Information

#########################################################################################################################
#																														#
#																														#
#	User Interface																								        #
#																														#
#																														#
#########################################################################################################################


DIRPATH = os.path.dirname(os.path.abspath(__file__))
UIPATH = os.path.join(DIRPATH, 'images')

colorUI = [[.5, 1, .5], [.25, 1, .75], [0, 1, 1], [.25, .75, 1], [.5, .5, 1], [.75, .25, 1], [1, 0, 1],
           [1, .25, .75], [1, .25, .5], [1, .5, .25], [1, 1, .25], [.75, 1, .25]]


def UIImage(n='icon_01.png', *args):
	var = os.path.join(UIPATH, n)
	return var


def button(l='Button', i='circle.png', c=None, bgc=[], *args):
	b = cmds.nodeIconButton(label=l, style='iconAndTextHorizontal', h=40, image1=i, nbg=False)
	if bgc:
		cmds.nodeIconButton(b, e=True, bgc=bgc)
	if c:
		cmds.nodeIconButton(b, e=True, c=c)
	return b


def autoRow(items, label='', *args):
	if label:
		rowUI = cmds.rowLayout(nc=2, ad2=2)
		cmds.text(l=label, al='right', w=10)

	form = cmds.formLayout(nd=100)
	cmds.setParent('..')

	length = float(len(items))
	step = 100 / length

	i = 0
	for x in items:

		if cmds.control(x, q=True, exists=True):

			x = cmds.control(x, e=True, p=form)

		elif cmds.layout(x, q=True, exists=True):
			x = cmds.layout(x, e=True, p=form)

		if i == 0:
			cmds.formLayout(form, edit=True, attachForm=[(x, 'left', 0), (x, 'top', 0), (x, 'bottom', 0), ],
			                attachPosition=[(x, 'right', 1, step), ], )

		else:
			cmds.formLayout(form, edit=True,
			                attachForm=[(x, 'top', 0), (x, 'bottom', 0), ],
			                attachControl=[(x, 'left', 2, items[i - 1]), ],
			                attachPosition=[(x, 'right', 1, step), ]
			                )

		step += 100 / length
		i += 1

	if label:
		cmds.setParent('..')
		return rowUI

	else:
		return form


def divider(label='', mar=10, *args):
	if label:
		ui = cmds.rowLayout(nc=2, ad2=2, )
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


def colorIndexSlider(l='', c='', index=False, *args):
	indexColor = ults.colorIndexList()
	ui = cmds.colorIndexSliderGrp(l=l, min=1, max=32, value=1, cw=[[1, col], [2, col]], rat=(2, 'both', 0))

	if index:
		cmds.colorIndexSliderGrp(ui, e=True, cc=lambda *x: ults.overrideColor(
				color=cmds.colorIndexSliderGrp(ui, q=True, v=True) - 1, index=True))

	else:
		if c:
			cmds.colorIndexSliderGrp(ui, e=True,
			                         cc=lambda *x: c(indexColor[cmds.colorIndexSliderGrp(ui, q=True, v=True) - 1]))

	return ui


def colorSlider(l='', c='', *args):
	ui = cmds.colorSliderGrp(l=l, cw=[[1, col], [2, col]], rat=(2, 'both', 0))

	if c:
		cmds.colorSliderGrp(ui, e=True, cc=lambda *_: c(cmds.colorSliderGrp(ui, q=True, rgb=True)))

	return ui


def colorPalette(l='', color=[], h=100, d=(), r=4, c='', *args):
	global col

	indexColor = ults.colorIndexList()

	if l:
		cmds.rowLayout(nc=2, ad2=2, cw=(1, col), rat=(1, 'both', 0), cat=(1, 'both', 0))
		cmds.text(l=l, align='right')

	cmds.frameLayout(lv=False)

	if not color:
		color = indexColor

	if not d:
		varW = r
		varH = len(color) / r
		d = (varH, varW)

	port = cmds.palettePort(dim=d, h=h, td=True, ced=False)

	for col in range(len(color)):
		cmds.palettePort(port, e=True, rgb=(col, color[col][0], color[col][1], color[col][2]))

	cmds.setParent('..')

	if c:
		cmds.palettePort(port, e=True, cc=lambda *_: c(color=cmds.palettePort(port, q=True, rgb=True)))

	if l:
		cmds.setParent('..')

	return port


class progressWindow():
	def __init__(self, l='Loading', st='Calculating...', max=100):
		self.value = 0
		self.max = max
		self.ui = cmds.progressWindow(t=l, progress=self.value, st=st, max=max, ii=True)
		self.reachedMax = False

	def update(self, step=1):
		self.value += step
		cmds.progressWindow(self.ui, e=True, progress=self.value)

		if self.value >= self.max:
			self.reachedMax = True
			self.kill()

	def cancel(self):
		if cmds.progressWindow(self.ui, q=True, ic=True):
			self.kill()
			return True
		else:
			return False

	def kill(self):
		cmds.progressWindow(self.ui, endProgress=1)


def selectedDisplayUI(*args):
	ui = cmds.columnLayout(adj=True)
	row = cmds.rowLayout(nc=2)
	cmds.text(l='Selected: ')
	updateSelectedTextUI = cmds.text(l=len(cmds.ls(sl=True)))
	cmds.setParent('..')
	cmds.setParent('..')

	cmds.scriptJob(p=row, protected=True, e=['SelectionChanged', lambda *_: cmds.text(updateSelectedTextUI, e=True,
	                                                                                  l=len(cmds.ls(sl=True)))])
	return ui




def skeletonUI():
	# Header
	ui = cmds.columnLayout(adj=True)

	# Body UI
	cmds.frameLayout(l='Display', mh=mar, mw=mar, bgs=True, cl=True)
	j1 = cmds.button(l='Toggle LRA', enable=False)
	j2 = cmds.button(l='Show', enable=False)
	j3 = cmds.button(l='Hide', enable=False)
	autoRow([j1, j2, j3])
	divider('Joint Scale')
	jdUI = cmds.floatSliderGrp(field=True, pre=2, min=0.01, max=10.00, v=cmds.jointDisplayScale(q=True),
	                           cc=lambda *x: cmds.jointDisplayScale(cmds.floatSliderGrp(jdUI, q=True, v=True)))
	cmds.setParent('..')

	cmds.frameLayout(l='Create', mh=mar, mw=mar, bgs=True, cl=True)
	b1 = cmds.button(l='Create Joint', c=ults.createJoint)
	b2 = cmds.button(l='Orient Chain', c=ults.orientJointChain)
	b3 = cmds.button(l='Select Hierarchy', c=ults.getJointHierarchy)
	autoRow([b1, b2, b3])
	cmds.setParent('..')

	cmds.frameLayout(l='Joint Labels', mh=mar, mw=mar, bgs=True, cl=True)
	a1 = cmds.button(l='Toggle Visibility', c=ults.toggleJointLabel)
	a2 = cmds.button(l='Show', c=lambda *x: mel.eval('displayJointLabels 4;'))
	a3 = cmds.button(l='Hide', c=lambda *x: mel.eval('displayJointLabels 3;'))
	autoRow([a1, a2, a3])

	# Add Label UI
	divider('Add Label')
	cmds.rowLayout(nc=2, adj=1, cat=[1, 'right', -4], rat=[1, 'both', 0])
	om1 = cmds.optionMenuGrp(adj=1, rat=[1, 'both', -2], cat=[1, 'right', 0],
	                         cc=lambda *x: ults.jointLabel().addTypeFromUI(cmds.optionMenuGrp(om1, q=True, sl=True)))
	for l in ults.jointLabel().masterList:
		cmds.menuItem(l=l, dtg=l)
	cmds.button(l='+', w=20, c=lambda *x: ults.jointLabel().addTypeFromUI(cmds.optionMenuGrp(om1, q=True, sl=True)))
	cmds.setParent('..')

	cmds.setParent('..')

	cmds.frameLayout(l='Skinning', mh=mar, mw=mar, bgs=True, cl=True)
	swb1 = cmds.button(l='Paint Weights', c=lambda *x: mel.eval('ArtPaintSkinWeightsToolOptions;'))
	#swb2 = cmds.button(l='Smooth Weights', c=tf_smoothSkinWeight.paint)
	swb3 = cmds.button(l='Mirror Weights', c=lambda *x: [skin.mirrorSkinWeights(mesh=x) for x in cmds.ls(sl=True)])
	autoRow([swb1, swb3])
	cmds.setParent('..')

	# End UI
	cmds.setParent('..')

	return ui


def rigUI():
	ui = cmds.columnLayout(adj=True, enable=False)

	# Root

	cmds.frameLayout(mh=10, mw=10, bgs=True, cll=False, cl=True, lv=False)
	nameField = cmds.textFieldGrp(l='Rig Name: ', tx='character', adj=2, cw2=[60, 60], nbg=False)
	button(l='1. Root', i=UIImage('icon_01_100.png'), c=lambda *x: parts.ROOT(
			name=cmds.textFieldGrp(nameField, q=True, tx=True) if cmds.textFieldGrp(nameField, q=True,
			                                                                        tx=True) else 'character'))
	cmds.setParent('..')

	# Cog

	cmds.frameLayout(l='2. COG Setup', bgs=True, mh=10, mw=10, cll=False, cl=True, lv=False)
	button(l='2. Center of Gravity', i=UIImage('icon_02_100.png'), c=parts.COG)
	cmds.setParent('..')

	# Spine

	cmds.frameLayout(l='3. Spine Setup', bgs=True, mh=10, mw=10, cll=False, cl=True, lv=False)
	button(l='3. Spine', i=UIImage('icon_06_100.png'), c=parts.SPINE)
	cmds.setParent('..')

	# Neck / Head

	cmds.frameLayout(l='4. Neck / Head Setup', bgs=True, mh=10, mw=10, cll=False, cl=True, lv=False)
	button(l='4. Neck / Head', i=UIImage('icon_03_100.png'), c=parts.HEAD)
	cmds.setParent('..')

	# Arms

	cmds.frameLayout(l='5. Arms / Hands', bgs=True, mh=10, mw=10, cll=False, cl=True, lv=False)
	button(l='5. Arm', i=UIImage('icon_05_100.png'), c=parts.ARM)
	cmds.setParent('..')

	# Legs

	cmds.frameLayout(l='6. Legs / Feet', bgs=True, mh=10, mw=10, cll=False, cl=True, lv=False)
	#button(l='6. Hip', i=UIImage('icon_04_100.png'), c=parts.HIP)
	#button(l='7. Leg', i=UIImage('icon_04_100.png'), c=parts.LEG)
	cmds.setParent('..')

	cmds.setParent('..')

	return ui


def autoUI(*args):
	global procressControl

	# Head UI
	ui = cmds.columnLayout(adj=True, enable=False)

	# Body UI
	cmds.frameLayout(l='Joint Labels', mh=mar, mw=mar, bgs=True, cl=True)
	a1 = cmds.button(l='Toggle Visibility', c=ults.toggleJointLabel)
	a2 = cmds.button(l='Show', c=lambda *x: mel.eval('displayJointLabels 4;'))
	a3 = cmds.button(l='Hide', c=lambda *x: mel.eval('displayJointLabels 3;'))
	autoRow([a1, a2, a3])

	# Add Label UI
	divider('Add Label')
	cmds.rowLayout(nc=2, adj=1, cat=[1, 'right', -4], rat=[1, 'both', 0])
	om1 = cmds.optionMenuGrp(adj=1, rat=[1, 'both', -2], cat=[1, 'right', 0],
	                         cc=lambda *x: ults.jointLabel().addTypeFromUI(cmds.optionMenuGrp(om1, q=True, sl=True)))
	for l in ults.jointLabel().masterList:
		cmds.menuItem(l=l, dtg=l)
	cmds.button(l='+', w=20, c=lambda *x: ults.jointLabel().addTypeFromUI(cmds.optionMenuGrp(om1, q=True, sl=True)))
	cmds.setParent('..')

	cmds.button(l='Create Rig', c=parts.autoRig)

	cmds.setParent('..')

	# End UI
	cmds.setParent('..')

	return ui


def colorUI(cl=True, cll=True, *args):
	ui = cmds.columnLayout(adj=True)

	cmds.frameLayout(l='Color', mh=mar, mw=mar, bgs=True, cl=cl, cll=cll)
	cmds.button(l='Disable Color', c=lambda *x: ults.overrideColor(reset=True))
	divider('Index')
	colorPalette(c=ults.overrideColor)
	cmds.setParent('..')
	cmds.setParent('..')

	return ui


class getAllInScene():

	def __init__(self):
		self.ui()

	def get(self, dupe=False, *args):
		uiquery = cmds.optionMenu(self.getAllInSceneOptionUI, q=True, v=True)

		objectList = []

		if dupe == True:

			objects = [f for f in cmds.ls() if '|' in f]
			objects.sort(key=lambda obj: obj.count('|'), reverse=True)

			for obj in objects:
				objectList.append(obj)


		else:

			objects = cmds.ls(type=uiquery)

			for obj in objects:
				if cmds.objectType(obj) == uiquery:
					objectList.append(obj)

		cmds.textScrollList(self.getAllInSceneListUI, e=True, ra=True)
		cmds.textScrollList(self.getAllInSceneListUI, e=True, append=objectList)

	def selectTextScrollObject(self, control, *args):
		uiquery = cmds.textScrollList(control, q=True, si=True)

		try:
			cmds.select(uiquery)
		except:
			pass

	def ui(self, cl=True, h=100, *args):
		cmds.columnLayout(adj=True)
		cmds.frameLayout(l='List Objects in Scene', cl=cl, mh=mar, mw=mar, bgs=True, cll=False,
		                 ann='Find all nodes in the scene by type.')

		cmds.rowLayout(nc=2, ad2=1, rat=[1, 'both', -2], cat=[1, 'left', -2])
		self.getAllInSceneOptionUI = cmds.optionMenu(cc=self.get)
		nodeList = ['transform', 'locator', 'mesh', 'joint', 'network', 'nurbsSurface', 'nurbsCurve']
		for opt in sorted(nodeList):
			cmds.menuItem(l=opt, p=self.getAllInSceneOptionUI)
		b1 = cmds.button(l='Find Duplicates', c=lambda *x: self.get(dupe=True))
		cmds.setParent('..')

		self.getAllInSceneListUI = cmds.textScrollList(h=h,
		                                               sc=lambda *x: self.selectTextScrollObject(
				                                               self.getAllInSceneListUI))
		cmds.setParent('..')
		cmds.setParent('..')

		self.get()


def miscUI(cl=True, cll=True, *args):
	ui = cmds.columnLayout(adj=True)
	cmds.frameLayout(l='Misc.', mh=mar, mw=mar, bgs=True, cl=cl, cll=cll)
	cmds.button(l='Create Locator')
	cmds.button(l='Snap')
	cmds.setParent('..')
	cmds.setParent('..')
	return ui


def toolUI(*args):
	ui = cmds.columnLayout(adj=True)
	getAllInScene()
	colorUI()
	miscUI()
	cmds.setParent('..')
	return ui


# Main Window UI

def menuUI():
	ui = cmds.menuBarLayout()

	cmds.menu(l='Skeleton')
	skeleton.menu()
	cmds.menu(l='Skin')
	skin.menu()
	cmds.setParent('..')

	return ui


def show(*args):
	uiName = 'LANCERRIGTOOLS'
	if cmds.window(uiName, exists=True):
		cmds.deleteUI(uiName, window=True)

	win = cmds.window(uiName, title='LANCER RIG TOOLS')
	menuUI()
	# Start Header

	form = cmds.formLayout()
	sUI = selectedDisplayUI()

	# Start Body

	tab = cmds.tabLayout()
	tab0 = toolUI()
	tab1 = skeletonUI()
	tab2 = rigUI()
	tab3 = autoUI()

	# End Body

	cmds.formLayout(form, e=True,
	                attachForm=((sUI, 'top', 0), (sUI, 'left', 0), (sUI, 'right', 0),))

	cmds.formLayout(form, e=True,
	                attachForm=((tab, 'bottom', 0), (tab, 'left', 0), (tab, 'right', 0),),
	                attachControl=(tab, 'top', 0, sUI), )

	cmds.tabLayout(tab, e=True, tabLabel=((tab0, 'Tools'), (tab1, 'Joints'), (tab2, 'Modules'), (tab3, 'Auto Rig')))

	cmds.setParent('..')

	cmds.setParent('..')
	cmds.setParent('..')  # end form
	cmds.showWindow(uiName)
