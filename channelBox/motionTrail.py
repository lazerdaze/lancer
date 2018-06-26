# LANCER.PIPELINE.MOTIONTRAIL
#
#
#
#
#


# Maya Modules
from maya import cmds, mel

########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################

WINDOWNAME = 'motionTrailWinUI'
WINDOWTITLE = 'Motion Trail'
WINDOWHEIGHT = 10
WINDOWWIDTH = 390

GROUPNAME = 'scene_motionTrail_grp'

PADDING = 5
MARGIN = 10
COLUMN = 60


class component(object):
	objects = 'objects'
	camera = 'camera'
	motion = 'motion'
	motionObject = 'motion_object'
	motionCamera = 'motion_camera'
	ghost = 'ghost'
	modelPanel = 'modelPanel'
	pivot = 'pivot'
	motionTrailPivot = 'motionTrailPivot'


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################


def createMasterGroup():
	if cmds.objExists(GROUPNAME):
		return GROUPNAME
	else:
		return cmds.group(name=GROUPNAME, em=True)


def createPivot(name='pivot0'):
	null = cmds.group(name=name, em=True)
	cmds.addAttr(null, ln='type', dt='string')
	cmds.setAttr('{}.type'.format(null), component.motionTrailPivot, type='string', lock=True)
	return null


def queryPivot(obj):
	if cmds.attributeQuery('type', node=obj, exists=True):
		var = cmds.getAttr('{}.type'.format(obj))
		if var == component.motionTrailPivot:
			return True
	return False


def createMotionTrail(obj, typ):
	camera = None
	motionTrail = None
	pivot = None

	# Query Time Range
	playStart = cmds.playbackOptions(query=True, min=True)
	playEnd = cmds.playbackOptions(query=True, max=True)

	# Master Motion Trail Group
	mtGrp = createMasterGroup()

	# Get Camera
	focus = cmds.getPanel(wf=True)
	if cmds.getPanel(to=focus) == component.modelPanel:
		focusCam = cmds.modelPanel(focus, q=True, cam=True)
		focusCamShape = cmds.listRelatives(focusCam, shapes=True)[0]

		if cmds.objectType(focusCamShape) == component.camera:
			camera = focusCam

	# Create Motion Trail
	if typ == component.motionObject or typ == component.motionCamera:

		# Create Pivot
		if not queryPivot(obj):
			pivot = createPivot('{}_pivot#'.format(obj))
			cmds.parent(pivot, mtGrp)
			cmds.parentConstraint(obj, pivot, mo=False)
		else:
			pivot = obj

		# Motion Camera
		if typ == component.motionCamera:
			if camera:
				motionTrail = cmds.snapshot(pivot,
				                            camera,
				                            n='{}_motionTrail0'.format(pivot),
				                            mt=True,
				                            i=1,
				                            startTime=playStart,
				                            endTime=playEnd,
				                            anchorTransform=True,
				                            )

		# Motion Object
		elif typ == component.motionObject:
			motionTrail = cmds.snapshot(pivot,
			                            n='{}_motionTrail0'.format(pivot),
			                            mt=True,
			                            i=1,
			                            startTime=playStart,
			                            endTime=playEnd,
			                            ch=True,
			                            )

		if motionTrail:
			motionTrailShape = cmds.listRelatives(motionTrail[0], shapes=True)[0]
			motionTrailMainNode = motionTrail[1]

			# Set Handle Attrs
			cmds.setAttr('{}.trailDrawMode'.format(motionTrailShape), 1)
			cmds.setAttr('{}.overrideEnabled'.format(motionTrailShape), 1)
			cmds.setAttr('{}.overrideDisplayType'.format(motionTrailShape), 2)

	# Create Ghost
	elif type == component.ghost:

		if cmds.objectType(cmds.listRelatives(obj, shapes=True)[0]) == 'mesh':
			motionTrail = cmds.snapshot(obj,
			                            n=obj + '_ghost_#',
			                            i=1,
			                            startTime=playStart,
			                            endTime=playEnd,
			                            ch=True,
			                            u='always')

			motionTrailShape = motionTrail[0]
			motionTrailMainNode = motionTrail[1]

			cmds.parent(motionTrailShape, mtGrp)

			# Set Ghost Attrs
			cmds.setAttr('{}.overrideEnabled'.format(motionTrailShape), 1)
			cmds.setAttr('{}.overrideDisplayType'.format(motionTrailShape), 1)

	if motionTrail:
		cmds.parent(motionTrail[0], mtGrp)

	return [pivot, motionTrail]





########################################################################################################################
#
#
#	UI
#
#
########################################################################################################################

def formRadio(items=[], label=[], labelW=60, command=[], *args):
	if label:
		cmds.rowLayout(nc=2, ad2=2)
		cmds.text(l=label, al='right', w=labelW)

	else:
		cmds.columnLayout(adj=True)

	form = cmds.formLayout(nd=100)
	length = float(len(items))
	step = 100 / length

	masterList = []

	i = 0
	for v in items:
		radioLabel = ''
		for a in v.split('_'):
			radioLabel = '{} {}'.format(radioLabel, a.capitalize())

		x = cmds.radioButton(v, l=radioLabel)

		if command:
			cmds.radioButton(x, e=True, cc=command)

		masterList.append(x)

		if i == 0:
			cmds.radioButton(x, e=True, sl=True)
			cmds.formLayout(form, edit=True, attachForm=[(x, 'left', 0), (x, 'top', 0), (x, 'bottom', 0), ],
			                attachPosition=[(x, 'right', 1, step), ], )

		else:
			cmds.formLayout(form, edit=True, attachForm=[(x, 'top', 0), (x, 'bottom', 0), ],
			                attachControl=[(x, 'left', 2, masterList[i - 1]), ],
			                attachPosition=[(x, 'right', 1, step), ])

		step += 100 / length
		i += 1

	cmds.setParent('..')
	cmds.setParent('..')
	return


def editFormRow(form, items, *args):
	length = float(len(items))
	step = 100 / length

	i = 0
	for x in items:

		if i == 0:
			cmds.formLayout(form, edit=True, attachForm=[(x, 'left', 0), (x, 'top', 0), (x, 'bottom', 0), ],
			                attachPosition=[(x, 'right', 1, step), ], )

		else:
			cmds.formLayout(form, edit=True, attachForm=[(x, 'top', 0), (x, 'bottom', 0), ],
			                attachControl=[(x, 'left', 2, items[i - 1]), ],
			                attachPosition=[(x, 'right', 1, step), ])

		step += 100 / length
		i += 1
	return


def selectTextScroll(obj, *args):
	if cmds.objExists(obj):
		cmds.select(obj)
	return


class ui:
	def __init__(self):
		cmds.columnLayout(adj=True)
		cmds.frameLayout(lv=False)

		self.typeUI = cmds.radioCollection()
		formRadio(items=[component.motionObject, component.motionCamera])

		buttonForm = cmds.formLayout(nd=100)
		b1 = cmds.button(l='Create', c=self.create, bgc=[.5, 1, .5])
		b2 = cmds.button(l='Delete', bgc=[1, .25, .5], c=self.deleteAll)
		cmds.setParent('..')
		editFormRow(form=buttonForm, items=[b1, b2])

		mtForm = cmds.formLayout(nd=100)
		mt1 = cmds.columnLayout(adj=True)
		cmds.text(l='Objects')
		self.objectUI = cmds.textScrollList(h=50, w=100, sc=lambda *_: selectTextScroll(
				cmds.textScrollList(self.objectUI, q=True, si=True)[0]))
		cmds.setParent('..')

		mt2 = cmds.columnLayout(adj=True)
		cmds.text(l='Motion Trails')
		self.motionTrailUI = cmds.textScrollList(h=50, w=100, sc=lambda *_: selectTextScroll(
				cmds.textScrollList(self.motionTrailUI, q=True, si=True)[0]))
		cmds.setParent('..')
		cmds.setParent('..')
		editFormRow(form=mtForm, items=[mt1, mt2])

		cmds.button(l='Update', c=self.update)

		cmds.setParent('..')
		cmds.setParent('..')

		self.startup()

	def startup(self):
		if cmds.objExists(GROUPNAME):
			children = cmds.listRelatives(GROUPNAME, children=True)
			if children:
				for child in children:
					shape = cmds.listRelatives(child, shapes=True)
					if shape:
						shapeType = cmds.objectType(shape[0])
						if shapeType == 'motionTrailShape':
							cmds.textScrollList(self.motionTrailUI, e=True, append=str(shape[0]))
					else:
						cmds.textScrollList(self.objectUI, e=True, append=str(child))
		return

	def getType(self):
		return cmds.radioCollection(self.typeUI, q=True, sl=True)

	def create(self, *args):
		selected = cmds.ls(sl=True)

		if selected:
			for obj in selected:
				trail = createMotionTrail(obj, typ=self.getType())
				pivot = trail[0]
				motionTrail = trail[1]
				if pivot:
					cmds.textScrollList(self.objectUI, e=True, append=str(pivot))
				if motionTrail:
					cmds.textScrollList(self.motionTrailUI, e=True, append=str(motionTrail[0]))
		cmds.select(d=True)
		return

	def update(self, *args):
		# Update locators
		for item in cmds.textScrollList(self.objectUI, q=True, ai=True):
			try:
				pc = cmds.listRelatives(item, type='parentConstraint')[0]
				target = cmds.parentConstraint(pc, q=True, tl=True)[0]
				cmds.parentConstraint(target, pc, e=True, mo=True, )

			except:
				print 'Unable to update "{}". Skipped.'.format(item)

		# Update Motion Paths
		for item in cmds.textScrollList(self.motionTrailUI, q=True, ai=True):
			try:
				cmds.snapshot(cmds.listConnections(item, type='motionTrail')[0], e=True,
				              st=cmds.playbackOptions(q=True, min=True), et=cmds.playbackOptions(q=True, max=True))
			except:
				print 'Unable to update "{}". Skipped.'.format(item)
		return

	def deleteAll(self, *args):
		allObjects = cmds.textScrollList(self.objectUI, q=True, ai=True)
		allTrails = cmds.textScrollList(self.motionTrailUI, q=True, ai=True)

		if allObjects:
			for obj in allObjects:
				if cmds.objExists(obj):
					cmds.delete(obj)

		if allTrails:
			for obj in allTrails:
				if cmds.objExists(obj):
					cmds.delete(obj)

		if cmds.objExists(GROUPNAME):
			cmds.delete(GROUPNAME)

		cmds.textScrollList(self.objectUI, e=True, ra=True)
		cmds.textScrollList(self.motionTrailUI, e=True, ra=True)
		return


########################################################################################################################
#
#
#	WINDOW
#
#
########################################################################################################################


def window():
	if cmds.window(WINDOWNAME, q=True, ex=True):
		cmds.deleteUI(WINDOWNAME)

	winPref = cmds.windowPref(WINDOWNAME, exists=True)
	if winPref:
		cmds.windowPref(WINDOWNAME, e=True, h=WINDOWHEIGHT, w=WINDOWWIDTH)

	cmds.window(WINDOWNAME,
	            t=WINDOWTITLE,
	            rtf=True,
	            h=WINDOWHEIGHT,
	            w=WINDOWWIDTH,
	            )

	ui()
	cmds.showWindow(WINDOWNAME)
	return
