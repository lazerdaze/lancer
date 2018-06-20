# LANCER. JT CHANNELBOX
#
#
#
#
#

# Lancer
import note

reload(note)

# Python Modules
from functools import partial

# Maya Modules
import maya.cmds as cmds
import maya.mel as mel


class mayaUI(object):
	mayaVersion = int(cmds.about(v=True))

	if mayaVersion == 2018:
		channelPane = 'ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout'
		timeControl = 'TimeSlider|MainTimeSliderLayout|formLayout8|frameLayout2|timeControl1'

	else:
		channelPane = 'MayaWindow|MainChannelsLayersLayout|ChannelsLayersPaneLayout'
		timeControl = 'MayaWindow|toolBar6|MainTimeSliderLayout|formLayout9|frameLayout2|timeControl1'


class show():

	def __init__(self, *args):

		# Global Var

		self.pad = 5
		self.mar = 10
		self.col = 60

		self.colorDict = {
			'green'   : [.5, 1, .5], 'greenCyan': [.25, 1, .75], 'cyan': [0, 1, 1],
			'blueCyan': [.25, .75, 1], 'blue': [.5, .5, 1], 'blueMagenta': [.75, .25, 1],
			'magenta' : [1, 0, 1], 'redMagenta': [1, .25, .75], 'red': [1, .25, .5],
			'orange'  : [1, .5, .25], 'yellow': [1, 1, .25], 'greenYellow': [.75, 1, .25],
		}

		self.channelPane = mayaUI.channelPane
		cmds.paneLayout(self.channelPane, e=True, cn='horizontal3')

		# Functions

		self.defaultSettings()
		self.ui()

	def defaultSettings(self, *args):

		# Anim Layers

		cmds.timeControl(mayaUI.timeControl, e=True,
		                 animLayerFilterOptions='selected')
		mel.eval('outlinerEditor -edit -animLayerFilterOptions selected graphEditor1OutlineEd;')

		# Buffer Curves

		mel.eval('animCurveEditor -edit -showBufferCurves true graphEditor1GraphEd;')

	def savedLayout(self, *args):
		# Saved Layout

		mel.eval('setNamedPanelLayout "JTLayout";')

		var = ''

		for cam in cmds.ls(type='camera'):
			par = cmds.listRelatives(cam, parent=True)[0]

			if par not in ['front', 'persp', 'side', 'top']:
				if not var:
					var = par

		if var:
			mel.eval('lookThroughModelPanel %s modelPanel1;' % var)

	def removeUI(self, *args):
		cmds.deleteUI('animToolsChannelBoxUI')
		cmds.paneLayout(self.channelPane, e=True, cn='horizontal2')

	def prefFunction(self, pref, obj, *args):

		if pref == 'evaluation':
			cmds.evaluationManager(mode=obj)
			print 'Evaluation Mode: %s' % cmds.evaluationManager(q=True, mode=True)[0]

		elif pref == 'default tangent':
			cmds.keyTangent(g=True, itt=obj)
			cmds.keyTangent(g=True, ott=obj)
			print 'Default Tangents: %s, %s' % (
				cmds.keyTangent(q=True, g=True, itt=True)[0], cmds.keyTangent(q=True, g=True, ott=True)[0])

		elif pref == 'frames per second':
			# Keep Keys at Current Frames
			# cmds.currentUnit(time='', ua=True)

			cmds.currentUnit(t=obj)
			print 'Frames Per Second: %s' % cmds.currentUnit(q=True, t=True,
			                                                 ua=cmds.menuItem(self.keepFrames, q=True, checkBox=True))

		elif pref == 'playback speed':
			cmds.playbackOptions(ps=obj)
			print 'Playback Speed: %s' % cmds.playbackOptions(q=True, ps=True)

		elif pref == 'up axis':
			cmds.upAxis(ax=obj)
			print 'Up Axis: %s' % cmds.upAxis(q=True, ax=True)

		elif pref == 'working units':
			cmds.currentUnit(l=obj)
			print 'Working Units: %s' % cmds.currentUnit(q=True, l=True)

	def prefsRadioMenu(self, pref, *args):

		if pref:

			# Get pref type

			if pref == 'evaluation':
				list = ['off', 'serial', 'parallel']
				current = cmds.evaluationManager(q=True, mode=True)[0]

			elif pref == 'default tangent':
				list = ['auto', 'clamped', 'linear', 'spline']
				current = cmds.keyTangent(q=True, g=True, itt=True)[0]

			elif pref == 'frames per second':
				list = ['film', 'ntsc', 'ntscf']
				current = cmds.currentUnit(q=True, t=True)

			elif pref == 'playback speed':
				list = [0.0, 1.0]
				current = cmds.playbackOptions(q=True, ps=True)

			elif pref == 'up axis':
				list = ['y', 'z']
				current = cmds.upAxis(q=True, ax=True)

			elif pref == 'working units':
				list = ['mm', 'cm', 'm']
				current = cmds.currentUnit(q=True, l=True)

			# Build Menu

			# Divider

			cmds.menuItem(l=pref.capitalize(), divider=True)
			cmds.radioMenuItemCollection()

			# Radio Buttons

			for obj in list:

				if obj == current:
					currentVar = True

				else:
					currentVar = False

				item = cmds.menuItem(label=str(obj).capitalize(), radioButton=currentVar,
				                     c=partial(self.prefFunction, pref, obj))

	def editFormRow(self, form, items, *args):

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

	def formRow(self, items=[], exclude=[], special=[], specialColor=[1, 0, 0], roundOff=1, command=[], *args):

		form = cmds.formLayout(nd=100)

		length = float(len(items))
		step = 100 / length

		masterList = []

		i = 0
		for v in items:

			if type(v) == float or type(v) == int:
				label = int(v * roundOff)

			elif type(v) == str:
				label = v.capitalize()

			if v in exclude:
				x = cmds.text(l=label, enable=False)

			else:
				x = cmds.button(l=label, c=partial(command, v), )

			if special:
				if v in special:
					cmds.button(x, e=True, bgc=specialColor)

			masterList.append(x)

			if i == 0:
				cmds.formLayout(form, edit=True, attachForm=[(x, 'left', 0), (x, 'top', 0), (x, 'bottom', 0), ],
				                attachPosition=[(x, 'right', 1, step), ], )

			else:
				cmds.formLayout(form, edit=True, attachForm=[(x, 'top', 0), (x, 'bottom', 0), ],
				                attachControl=[(x, 'left', 2, masterList[i - 1]), ],
				                attachPosition=[(x, 'right', 1, step), ])

			step += 100 / length
			i += 1

		cmds.setParent('..')

	def frame(self, label='', cl=False, bgc=None, annotation='', *args):

		if label:
			labelQ = True

		else:
			labelQ = False

		if not bgc:
			cmds.frameLayout(l=label, bgs=True, mh=self.mar, mw=self.mar, cll=True, cl=cl, lv=labelQ,
			                 annotation=annotation)

		else:
			inc = .2
			cmds.frameLayout(l=label, bgs=False, cll=True, cl=cl, mh=self.pad - 3, mw=self.pad - 3, lv=labelQ, bgc=bgc,
			                 annotation=annotation)
			cmds.columnLayout(adj=True, cat=['both', self.pad + 1], rs=8,
			                  bgc=(bgc[0] - inc, bgc[1] - inc, bgc[2] - inc))
			cmds.separator(style='none', h=self.pad - 1, )

	def end(self, separator=True, frame=False, *args):

		if frame:
			cmds.separator(style='none', h=self.pad - 1, )

			frame = cmds.setParent('..')
			col = cmds.layout(frame, q=True, ca=True)
			color = cmds.layout(col, q=True, bgc=True)

			inc = .2

		cmds.setParent('..')

		if separator:
			cmds.separator(st='none', h=self.mar)

	def column(self, label='', *args):

		if label:

			ui = cmds.columnLayout(label, adj=True)

		else:
			ui = cmds.columnLayout(adj=True)

		return ui

	def formRadio(self, items=[], label=[], labelW=60, command=[], *args):

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
			x = cmds.radioButton(v + '_animChRadioButton', l=v.capitalize())

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

	def divider(self, label='', *args):
		mar = self.mar

		if label:
			cmds.separator(st='none', ebg=False)
			cmds.rowLayout(nc=2, ad2=2, )

			cmds.text(l=label + '  ', al='left')
			cmds.columnLayout(bgc=[.5, .5, .5], h=1)
			cmds.setParent('..')

			cmds.setParent('..')

		else:
			cmds.columnLayout(h=mar, adj=True)
			cmds.columnLayout(bgc=[.5, .5, .5], h=1)
			cmds.setParent('..')
			cmds.setParent('..')

	# KEYS ===================================================================================================

	def getTimeRange(self, *args):

		playbackSlider = mel.eval('$tmpVar=$gPlayBackSlider')
		timeVar = str(cmds.timeControl(playbackSlider, q=True, range=True))
		timeRange = timeVar.split(':')
		nums = []

		for x in timeRange:
			my_int = int(x.replace('"', ''))
			nums.append(my_int)

		return nums

	def getKeyable(self, obj, *args):

		var = []

		# Query Main Channel Box Attrs

		cbb = cmds.channelBox('mainChannelBox', q=True, sma=True)

		if cbb:
			var = cbb

		else:
			var = cmds.listAttr(obj, k=True)

		# print var
		return var

	def matchFunction(self, type, *args):

		selected = cmds.ls(sl=True)
		currentTime = cmds.currentTime(query=True)

		translate = ['translateX', 'translateY', 'translateZ']
		rotate = ['rotateX', 'rotateY', 'rotateZ']

		translateCheck = cmds.checkBox(self.translateCheck, q=True, v=True)
		rotateCheck = cmds.checkBox(self.rotateCheck, q=True, v=True)

		for obj in selected:

			if translateCheck == True and rotateCheck == False:
				attributes = translate

			elif rotateCheck == True and translateCheck == False:
				attributes = rotate

			elif rotateCheck == True and translateCheck == True:
				attributes = translate + rotate

			else:
				attributes = cmds.listAttr(obj, k=True)

			for attr in attributes:

				querry = obj + '.' + attr

				if type == 'previous':
					time = cmds.findKeyframe(querry, which='previous')

				elif type == 'next':
					time = cmds.findKeyframe(querry, which='next')

				try:
					value = cmds.getAttr(querry, time=time)
					cmds.setAttr(querry, value)

				except:
					pass

	def updateTweenUI(self, value, *args):

		cmds.floatField(self.tweenFloat, e=True, v=value)
		cmds.floatSlider(self.tweenSlide, e=True, v=value)

		cmds.intField(self.tweenInt, e=True, v=int(value * 100))

	def tweenKeyFunction(self, percent, *args):

		selected = cmds.ls(sl=True)
		currentTime = cmds.currentTime(query=True)

		if selected:

			for obj in selected:

				# attributes = cmds.listAttr(obj, k=True)
				attributes = self.getKeyable(obj)

				for attr in attributes:

					query = obj + '.' + attr
					currentValue = cmds.getAttr(query, time=currentTime)

					nextTime = cmds.findKeyframe(query, which='next')
					nextValue = cmds.getAttr(query, time=nextTime)

					previousTime = cmds.findKeyframe(query, which='previous')
					previousValue = cmds.getAttr(query, time=previousTime)

					newValue = (nextValue - previousValue) * percent + previousValue

					try:
						cmds.setAttr(query, newValue)

					except:
						pass

		self.updateTweenUI(percent)

	# Keys ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	def keysUI(self, *args):

		cmds.columnLayout('Keys', adj=True)

		# Match Key
		'''
		self.frame('Match Attribute')

		matchKeyForm = cmds.formLayout()
		self.translateCheck = cmds.checkBox(l=' Translate', v=True)
		self.rotateCheck = cmds.checkBox(l=' Rotate', v=True)
		cmds.setParent('..')

		self.editFormRow(form=matchKeyForm, items=[self.translateCheck, self.rotateCheck])

		self.formRow(items=['previous', 'next'], command=self.matchFunction)

		self.end()
		'''
		# Tween Key

		self.frame('Tween Key')

		self.tweenFloat = cmds.floatField(minValue=0.0, maxValue=1.0, value=.5, precision=2, cc=self.tweenKeyFunction,
		                                  vis=False)
		self.tweenInt = cmds.intField(minValue=0, maxValue=100, value=50, ed=False)

		self.tweenSlide = cmds.floatSlider(minValue=0.0, maxValue=1.0, value=.5, dc=self.tweenKeyFunction)

		self.formRow(items=[0.0, .0833, .1666, .2499, .3332, .4165, .5, .5833, .6666, .7499, .8332, .9165, 1.0],
		             special=[0.0, .2499, .5, .7499, 1.0], roundOff=100, command=self.tweenKeyFunction)

		self.end()

		'''

		# Overshoot Key

		cmds.frameLayout(l='Overshoot Key', li=5, bgs=True, mh=5, mw=5, cll=True)
		self.formRow(items = [-.5, -.25, -.125, -.0625, -.03125, 0.0, 1.0, 1.03125, 1.0625, 1.125, 1.25, 1.5], special=[0.0,1.0], roundOff= 100, command= self.tweenKeyFunction)
		cmds.setParent('..')
		cmds.separator(st='none', nbg=True, h=5)



		# Offset Key UI

		cmds.frameLayout(l='Offset Key', li=5, bgs=True, mh=5, mw=5, cll=True)

		self.domino = cmds.checkBox(l=' Domino', v=1)

		self.autoModeUI = cmds.columnLayout(adj=True)
		self.formRow([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], exclude= [0], command= self.offsetFunction)
		cmds.setParent('..')

		cmds.setParent('..') #frameEnd
		cmds.separator(st='none', nbg=True, h=5)



		# Scale Key

		cmds.frameLayout(l='Scale Key', li=5, bgs=True, mh=5, mw=5, cll=True)

		self.formRow([-.5, -.4, -.3, -.2, -.1, '%' , .1, .2, .3, .4, .5], exclude = ['%'], roundOff = 100, command= self.scaleKeyFunction)

		cmds.button(l='Flip Keys', c= partial(self.scaleKeyFunction, 0, True))
		cmds.setParent('..')

		cmds.separator(st='none', nbg=True, h=5)

		'''

		cmds.setParent('..')  # tabEnd

	# MOTIONTRAIL

	def motionTrail(self, *args):

		# Get Vars

		getType = cmds.radioCollection(self.mtType, q=True, sl=True)

		selected = cmds.ls(sl=True)
		objList = []
		camList = []

		playStart = cmds.playbackOptions(query=True, min=True)
		playEnd = cmds.playbackOptions(query=True, max=True)

		if selected:

			# Master Motion Trail Group

			mtGrp = 'bboy_motionTrail_grp'

			if not cmds.objExists(mtGrp):
				cmds.group(n=mtGrp, em=True)

			# Create Lists

			for obj in selected:

				objShape = cmds.listRelatives(obj, s=True)[0]

				if cmds.objectType(objShape) == 'camera':
					camList.append(obj)

				else:
					objList.append(obj)

			if not camList:
				focus = cmds.getPanel(wf=True)

				if cmds.getPanel(to=focus) == 'modelPanel':
					focusCam = cmds.modelPanel(focus, q=True, cam=True)
					focusCamShape = cmds.listRelatives(focusCam, shapes=True)[0]

					if cmds.objectType(focusCamShape) == 'camera':
						camList.append(focusCam)
			# print camList
			# print objList

			if camList:
				for obj in objList:

					if 'motion' in getType:
						print 'motion'

						allItems = cmds.textScrollList(self.mt1TextScroll, q=True, ai=True)

						if allItems and obj in allItems:

							loc = obj

						else:
							if 'mt_pivot' not in obj:
								loc = cmds.spaceLocator(n=obj + '_mt_pivot_#')[0]
								cmds.parent(loc, mtGrp)
								cmds.parentConstraint(obj, loc, mo=False)
								cmds.setAttr(loc + '.v', 0)

								cmds.textScrollList(self.mt1TextScroll, e=True, append=str(loc))

						if 'camera' in getType:
							# print 'camera'
							mt = cmds.snapshot(loc, camList[0], n=loc + '_motionTrail_#', mt=True, i=1,
							                   startTime=playStart, endTime=playEnd, anchorTransform=True)


						elif 'object' in getType:
							# print 'object'
							mt = cmds.snapshot(loc, n=loc + '_motionTrail_#', mt=True, i=1, startTime=playStart,
							                   endTime=playEnd, ch=True)

						mtShape = cmds.listRelatives(mt[0], shapes=True)[0]
						mtMainNode = mt[1]

						# Set Handle Attrs

						cmds.setAttr(mtShape + '.trailDrawMode', 1)
						cmds.setAttr(mtShape + '.overrideEnabled', 1)
						cmds.setAttr(mtShape + '.overrideDisplayType', 2)

						cmds.textScrollList(self.mt2TextScroll, e=True, append=str(mtShape))


					elif 'ghost' in getType:

						if cmds.objectType(cmds.listRelatives(obj, shapes=True)[0]) == 'mesh':
							mt = cmds.snapshot(obj, n=obj + '_ghost_#', i=1, startTime=playStart, endTime=playEnd,
							                   ch=True, u='always')
							mtShape = mt[0]
							mtMainNode = mt[1]

							cmds.parent(mtShape, mtGrp)

							# Set Ghost Attrs

							cmds.setAttr(mt[0] + '.overrideEnabled', 1)
							cmds.setAttr(mt[0] + '.overrideDisplayType', 1)

							# Update UI

							cmds.textScrollList(self.mt1TextScroll, e=True, append=str(obj))
							cmds.textScrollList(self.mt2TextScroll, e=True, append=str(mtShape))

			# Clean Up

			cmds.select(d=True)

	def updateMotionTrail(self, var, *args):

		if var == 'update':

			# Update locators

			try:
				for item in cmds.textScrollList(self.mt1TextScroll, q=True, ai=True):
					pc = cmds.listRelatives(item, type='parentConstraint')[0]
					target = cmds.parentConstraint(pc, q=True, tl=True)[0]
					cmds.parentConstraint(target, pc, e=True, mo=True, )

			except:
				pass

			# Update Motion Paths

			try:
				for item in cmds.textScrollList(self.mt2TextScroll, q=True, ai=True):
					cmds.snapshot(cmds.listConnections(item, type='motionTrail')[0], e=True,
					              st=cmds.playbackOptions(q=True, min=True), et=cmds.playbackOptions(q=True, max=True))

			except:
				pass


		elif var == 'delete':

			masterGrp = 'bboy_motionTrail_grp'
			deleteList = []

			if cmds.objExists(masterGrp):

				for obj in cmds.listRelatives(masterGrp, ad=True):
					print obj
					x = cmds.listConnections(obj, type='motionTrail')

					if x:
						for y in x:
							print '         ' + y

							if y not in deleteList:
								deleteList.append(y)

							z = cmds.listConnections(y, type='motionTrailShape')[0]

							if z not in deleteList:
								deleteList.append(z)

				for obj in deleteList:
					try:
						cmds.delete(obj)
					except:
						pass

			try:
				cmds.delete('bboy_motionTrail_grp')


			except:
				pass

			cmds.textScrollList(self.mt1TextScroll, e=True, ra=True)
			cmds.textScrollList(self.mt2TextScroll, e=True, ra=True)

		elif var == 'deleteMotionTrail':
			try:
				selected = cmds.textScrollList(self.mt2TextScroll, q=True, si=True)

				cmds.delete(cmds.listRelatives(selected, p=True))
				cmds.textScrollList(self.mt2TextScroll, e=True, ri=selected)

			except:
				pass

	def motionTrailUI(self, *args):

		self.column('Motion Trail')

		self.frame()

		self.mtType = cmds.radioCollection()
		self.formRadio(items=['motion object', 'motion camera', 'ghost'])

		cmds.button(l='Create', c=self.motionTrail, bgc=self.colorDict['green'])

		mtForm = cmds.formLayout(nd=100)

		mt1 = cmds.columnLayout(adj=True, )
		cmds.text(l='Objects')
		self.mt1TextScroll = cmds.textScrollList(h=125, w=100, sc=lambda *_: self.selectTextScroll(
				cmds.textScrollList(self.mt1TextScroll, q=True, si=True)))
		cmds.button(l='Update All', c=partial(self.updateMotionTrail, 'update'))
		cmds.setParent('..')

		mt2 = cmds.columnLayout(adj=True)
		cmds.text(l='Motion Trails')
		self.mt2TextScroll = cmds.textScrollList(h=125, w=100, sc=lambda *_: self.selectTextScroll(
				cmds.textScrollList(self.mt2TextScroll, q=True, si=True)))
		cmds.button(l='Delete', c=partial(self.updateMotionTrail, 'deleteMotionTrail'))
		cmds.setParent('..')

		cmds.setParent('..')

		self.editFormRow(form=mtForm, items=[mt1, mt2])

		self.divider()

		cmds.button(l='Delete All', c=partial(self.updateMotionTrail, 'delete'), bgc=self.colorDict['red'])

		self.end()
		self.end(False)  # tabEnd

	def noteUI(self, *args):
		padding = 5

		form = cmds.formLayout('Notes')
		col = note.widget().control
		cmds.setParent('..')

		cmds.formLayout(form,
		                e=True,
		                attachForm=[
			                [col, 'top', padding],
			                [col, 'left', padding],
			                [col, 'bottom', padding],
			                [col, 'right', padding],
		                ],
		                )
		return

	def ui(self):

		# Main Layout ===================================================================================================

		if cmds.layout('animToolsChannelBoxUI', exists=True):
			cmds.deleteUI('animToolsChannelBoxUI')

		cmds.formLayout('animToolsChannelBoxUI', p=self.channelPane)

		scrollUI = cmds.scrollLayout(cr=True)

		cmds.separator(st='none', h=5)

		# Menu ===================================================================================================

		cmds.menuBarLayout()

		cmds.menu(l='UI', hm=True)
		cmds.menuItem(l='Close', c=self.removeUI)

		cmds.menu(l='Playblast')
		cmds.menuItem(l='Playblast - Temp',
		              c=lambda *_: cmds.playblast(format='image', sequenceTime=0, clearCache=1, viewer=1,
		                                          showOrnaments=1, offScreen=True, fp=4, percent=100, compression='jpg',
		                                          quality=100))
		cmds.menuItem(divider=True)
		# cmds.menuItem(l='Playblast - Allison UI', c=allison.playblastWrapper)

		'''
		cmds.menu(l='Camera')
		cmds.menuItem(l='Set Saved Layout', c=self.savedLayout)
		cmds.menuItem(d=True)
		cmds.menuItem(l='Toggle Display', c=bboy.toggleViewport)
		'''

		cmds.menu(l='Anim')
		self.prefsRadioMenu(pref='evaluation', )
		self.prefsRadioMenu(pref='default tangent', )
		cmds.menuItem(l='', divider=True)
		cmds.menuItem(l='Weighted tangents', checkBox=(cmds.keyTangent(q=True, g=True, wt=True)),
		              c=lambda x: cmds.keyTangent(e=True, g=True, wt=x))

		cmds.menu(l='Time')
		self.prefsRadioMenu(pref='playback speed', )
		self.prefsRadioMenu(pref='frames per second', )
		cmds.menuItem(l='', divider=True)
		self.keepFrames = cmds.menuItem(l='Keep keys at current frames', checkBox=False)

		cmds.menu(l='World')
		self.prefsRadioMenu(pref='up axis', )
		# self.prefsRadioMenu(pref='working units',)

		cmds.setParent('..')  # endMenu

		# Main Layout ===================================================================================================

		tab = cmds.tabLayout()

		self.keysUI()
		self.motionTrailUI()
		self.noteUI()

		# End UI ===================================================================================================

		cmds.setParent('..')  # end tab
		cmds.setParent('..')  # end scroll
		cmds.setParent('..')  # end form

		cmds.formLayout('animToolsChannelBoxUI', e=True,
		                attachForm=[(scrollUI, 'left', 0), (scrollUI, 'top', 0), (scrollUI, 'bottom', 0),
		                            (scrollUI, 'right', 0), ],
		                )
