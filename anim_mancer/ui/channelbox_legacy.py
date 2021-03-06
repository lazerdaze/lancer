# LANCER.CHANNELBOX.UI
#
#
#
#
#

# Lancer
import anim_mancer.tools.note
import anim_mancer.tools.tweenKey
import anim_mancer.tools.motionTrail
import anim_mancer.tools.ghost
import anim_mancer.tools.refman as refman
import anim_mancer.tools.keys

reload(anim_mancer.tools.note)
reload(anim_mancer.tools.tweenKey)
reload(anim_mancer.tools.motionTrail)
reload(anim_mancer.tools.ghost)
reload(refman)
reload(anim_mancer.tools.keys)

# Python Modules
from functools import partial
# from PySide2 import QtCore, QtGui, QtWidgets
# from shiboken2 import wrapInstance

# Maya Modules
from maya import cmds, mel

########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################

NAME = 'animToolsChannelBoxUI'
PADDING = 5
MARGIN = 10
COLUMN = 60


class mayaUI(object):
	mayaVersion = int(cmds.about(v=True))

	if mayaVersion == 2018:
		channelPane = 'ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout'
		timeControl = 'TimeSlider|MainTimeSliderLayout|formLayout8|frameLayout2|timeControl1'

	else:
		channelPane = 'MayaWindow|MainChannelsLayersLayout|ChannelsLayersPaneLayout'
		timeControl = 'MayaWindow|toolBar6|MainTimeSliderLayout|formLayout9|frameLayout2|timeControl1'


########################################################################################################################
#
#
#	SCRIPT JOBS
#
#
########################################################################################################################


def getCameras():
	exclude = ['frontShape', 'perspShape', 'sideShape', 'topShape']
	cameras = cmds.ls(type='camera')
	renderCameras = [cam for cam in cameras if cam not in exclude]
	return renderCameras if renderCameras else None


def set_timeline(start=1001.0, end=1200.0, fps=None):
	if fps == 24:
		fps = 'film'
	elif fps == 30:
		fps = 'ntsc'


	cmds.currentTime(1001.0)
	return cmds.playbackOptions(ast=start, aet=end, min=start, max=end, v='all', fps=True)


def tearOffPanel():
	renderCams = getCameras()

	if renderCams:
		window = cmds.window(t=renderCams[0], w=800, h=600)
		cmds.paneLayout()
		mpUI = cmds.modelPanel()
		cmds.modelPanel(mpUI, e=True, cam=renderCams[0])
		cmds.showWindow(window)

		# Off
		cmds.modelEditor(mpUI,
						 e=True,
						 allObjects=False,
						 grid=False,
						 manipulators=False,
						 selectionHiliteDisplay=False,
						 polymeshes=True,
						 imagePlane=True,
						 headsUpDisplay=False,
						 displayAppearance='smoothShaded',
						 )
		return


def openNewScene():
	tearOffPanel()
	mel.eval('generateAllUvTilePreviews;')


	mel.eval('''
	evaluationManager -mode parallel;
	optionVar -iv gpuOverride  true;
	setAttr "hardwareRenderingGlobals.vertexAnimationCache" 2;
	setAttr "hardwareRenderingGlobals.enableTextureMaxRes" 1;
	'''
			 )
	# AEenableTextureMaxRes "hardwareRenderingGlobals";
	# attrFieldSliderGrp -e -en true attrFieldSliderGrp3;
	# AEReloadAllTextures;
	# generateAllUvTilePreviews;
	# setAttr "hardwareRenderingGlobals.textureMaxResolution" 4096;

	print 'Lancer: ScriptJob "Open New Scene" Successful'
	return


########################################################################################################################
#
#
#	PREFERENCES CLASS
#
#
########################################################################################################################

class Component(object):
	# Evaluation Modes
	dg = 'dg'
	serial = 'serial'
	parallel = 'parallel'
	gpuOverride = 'gpuOverride'

	# Tangents
	auto = 'auto'
	stepped = 'stepped'
	linear = 'linear'
	spline = 'spline'

	# Playback
	everyFrame = 'everyFrame'
	maxFrame = 'maxFrame'

	# Framerate
	time24 = '24'
	time30 = '30'
	time60 = '60'


class PreferencesMenu(object):
	def __init__(self):
		self.evaluation = cmds.evaluationManager(q=True, mode=True)[0]
		self.tearOffScriptJob = None
		self.timelineScriptJob = None

		self.ui = cmds.menuBarLayout()

		cmds.menu(l='Scene')
		cmds.menuItem(d=True, dl='On New Scene')
		cmds.menuItem(l='Tear Off Copy', cb=True, c=self.tearOffCallback)
		cmds.menuItem(l='Set Timeline (1001-1200)', cb=True, c=self.timelineCallback)
		# cmds.menuItem(l='Playback: Every Frame', cb=True)

		cmds.menu(l='Evaluation')
		cmds.radioMenuItemCollection()
		cmds.menuItem(l='DG', rb=False, c=lambda *_: self.evalCallback(Component.dg), enable=False)
		cmds.menuItem(l='Serial', rb=False, c=lambda *_: self.evalCallback(Component.serial), enable=False)
		cmds.menuItem(l='Parallel', rb=True, c=lambda *_: self.evalCallback(Component.parallel))
		cmds.menuItem(d=True)
		cmds.menuItem(l='Print Debug Info', c=self.debugEvaluation)

		cmds.menu(l='Keys')
		cmds.menuItem(l='Delete Redundant', c=anim_mancer.tools.keys.deleteRedundant)
		cmds.menuItem(l='Delete All Static Channels', c=anim_mancer.tools.keys.deleteStaticAllChannels)

		cmds.menu(l='Tangents')
		prefsRadioMenu(pref='default tangent', )
		cmds.menuItem(l='', divider=True)
		cmds.menuItem(l='Weighted tangents', checkBox=(cmds.keyTangent(q=True, g=True, wt=True)),
					  c=lambda x: cmds.keyTangent(e=True, g=True, wt=x))

		cmds.menu(l='Time')
		prefsRadioMenu(pref='playback speed', )
		cmds.menuItem(d=True)
		cmds.menuItem(l='Snapping', cb=mel.eval('timeControl -q -snap $gPlayBackSlider;'), c=self.timeSnapCallback)

		gridMenu()

		cmds.menu(l='UI', hm=True)
		cmds.menuItem(l='Close', c=removeUI)
		cmds.setParent('..')

		# ScriptJobs
		cmds.scriptJob(p=self.ui, event=['SceneOpened', self.setDefaults])

		# Defaults
		self.setDefaults()
		# self.createTearOffScriptJob()
		self.createTimelineScriptJob()
		set_timeline()
		savePrefs()

	def debugEvaluation(self, *args):
		print cmds.evaluationManager(q=True, mode=True)[0],
		return

	def setDefaults(self):
		# Anim Layers
		cmds.timeControl(mayaUI.timeControl, e=True,
						 animLayerFilterOptions='selected')
		mel.eval('outlinerEditor -edit -animLayerFilterOptions selected graphEditor1OutlineEd;')

		# Buffer Curves
		mel.eval('animCurveEditor -edit -showBufferCurves true graphEditor1GraphEd;')

		# Auto Frame
		mel.eval('animCurveEditor -edit -autoFit true graphEditor1GraphEd;optionVar -intValue graphEditorAutoFit true;')

		# Evaluation
		cmds.evaluationManager(mode=Component.parallel)

		mel.eval('generateAllUvTilePreviews;')

		return

	def timeSnapCallback(self, *args):
		mel.eval('timeControl -e -snap {} $gPlayBackSlider;'.format(str(args[0]).lower()))
		return

	def tearOffCallback(self, *args):
		if args[0]:
			self.createTearOffScriptJob()
		else:
			self.killTearOffScriptJob()
		return

	def timelineCallback(self, *args):
		if args[0]:
			self.createTimelineScriptJob()
		else:
			self.killTimelineScriptJob()
		return

	def createTimelineScriptJob(self):
		self.timelineScriptJob = cmds.scriptJob(p=self.ui, event=['NewSceneOpened', set_timeline])
		return

	def killTimelineScriptJob(self):
		if self.timelineScriptJob:
			cmds.scriptJob(kill=self.timelineScriptJob, force=True)
		self.timelineScriptJob = None
		return

	def createTearOffScriptJob(self):
		self.tearOffScriptJob = cmds.scriptJob(p=self.ui, event=['SceneOpened', tearOffPanel])
		return

	def killTearOffScriptJob(self):
		if self.tearOffScriptJob:
			cmds.scriptJob(kill=self.tearOffScriptJob, force=True)
		self.tearOffScriptJob = None
		return

	def evalScriptJob(self):
		return

	def evalCallback(self, *args):
		value = args[0]
		if value == Component.dg:
			value = 'off'
		cmds.evaluationManager(mode=value)
		self.evaluation = value
		print 'Evaluation Mode: Set to {}.'.format(cmds.evaluationManager(q=True, mode=True)[0])
		savePrefs()
		return

	def getUI(self):
		return self.ui


########################################################################################################################
#
#
#	PREFERENCES / MENU
#
#
########################################################################################################################

# Todo: Grid: Auto Adjust Clipping Planes on All Cameras in scenes
# Todo: Grid Script Jobs On UI start and new scene start
def gridMenu(*args, **kwargs):
	ui = cmds.menu(l='Grid')
	cmds.menuItem(label='Visible', checkBox=True, command=toggle_grid)
	cmds.menuItem(d=True)
	cmds.radioMenuItemCollection()
	cmds.menuItem(label='Centimeters', radioButton=True, command=partial(edit_grid, 'centimeters'))
	cmds.menuItem(label='Meters', radioButton=False, command=partial(edit_grid, 'meters'))
	cmds.menuItem(label='Inches', radioButton=False, command=partial(edit_grid, 'inches'))
	cmds.menuItem(label='Feet', radioButton=False, command=partial(edit_grid, 'feet'))
	return ui


def toggle_grid(value, *args, **kwargs):
	return cmds.grid(toggle=value)


def edit_grid(unit=None, *args, **kwargs):
	# Default
	size = 12.0
	spacing = 5.0
	divisions = 5.0

	if unit == 'centimeters':
		size = 12.0
		spacing = 5.0
		divisions = 5.0

	elif unit == 'meters':
		size = 30.4800 * 5.0
		spacing = 30.4800
		divisions = 1.0

	elif unit == 'inches':
		size = 2.54 * 12.0
		spacing = 2.54
		divisions = 1.0

	elif unit == 'feet':
		size = 30.48 * 5.0
		spacing = 30.48
		divisions = 1.0

	cmds.grid(size=size, spacing=spacing, divisions=divisions)
	return


def savePrefs():
	cmds.savePrefs(g=True)
	print ''
	return


def savedLayout(*args):
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
	return


def prefFunction(pref, obj, *args):
	if pref == 'evaluation':
		cmds.evaluationManager(mode=obj)
		print 'Evaluation Mode: %s' % cmds.evaluationManager(q=True, mode=True)[0]
		savePrefs()

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
														 ua=cmds.menuItem(keepFrames, q=True, checkBox=True))

	elif pref == 'playback speed':
		cmds.playbackOptions(ps=obj)
		print 'Playback Speed: %s' % cmds.playbackOptions(q=True, ps=True)

	elif pref == 'up axis':
		cmds.upAxis(ax=obj)
		print 'Up Axis: %s' % cmds.upAxis(q=True, ax=True)

	elif pref == 'working units':
		cmds.currentUnit(l=obj)
		print 'Working Units: %s' % cmds.currentUnit(q=True, l=True)

	return


def prefsRadioMenu(pref, *args):
	if pref:
		# Get pref type
		if pref == 'evaluation':
			list = ['off', 'serial', 'parallel']
			current = cmds.evaluationManager(q=True, mode=True)[0]

		elif pref == 'default tangent':
			list = ['auto', 'step', 'linear', 'spline']
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
								 c=partial(prefFunction, pref, obj))
	return


def playblastTemp():
	cmds.playblast(
		format='image',
		sequenceTime=0,
		clearCache=1,
		viewer=1,
		showOrnaments=1,
		offScreen=True,
		fp=4, percent=100,
		compression='jpg',
		quality=100,
	)
	return


def menu():
	ui = cmds.menuBarLayout()
	cmds.menu(l='UI', hm=True)
	cmds.menuItem(l='Close', c=removeUI)

	cmds.menu(l='Evaluation')
	prefsRadioMenu(pref='evaluation')

	# cmds.menu(l='Playblast')
	# cmds.menuItem(l='Temp Settings', c=playblastTemp)

	cmds.menu(l='Tangents')
	prefsRadioMenu(pref='default tangent', )
	cmds.menuItem(l='', divider=True)
	cmds.menuItem(l='Weighted tangents', checkBox=(cmds.keyTangent(q=True, g=True, wt=True)),
				  c=lambda x: cmds.keyTangent(e=True, g=True, wt=x))

	cmds.menu(l='Time')
	prefsRadioMenu(pref='playback speed', )
	prefsRadioMenu(pref='frames per second', )
	# cmds.menuItem(l='', divider=True)
	# keepFrames = cmds.menuItem(l='Keep keys at current frames', checkBox=False)

	# cmds.menu(l='World')
	# prefsRadioMenu(pref='up axis', )
	cmds.setParent('..')
	return ui


########################################################################################################################
#
#
#	UI
#
#
########################################################################################################################


def removeUI(*args):
	cmds.deleteUI(NAME)
	cmds.paneLayout(mayaUI.channelPane, e=True, cn='horizontal2')
	return


def show(name=NAME, *args):
	cmds.paneLayout(mayaUI.channelPane, e=True, cn='horizontal3')

	# Main Layout
	if cmds.layout(name, exists=True):
		cmds.deleteUI(name)

	cmds.formLayout(name, p=mayaUI.channelPane)

	cmds.separator(st='none', h=PADDING)

	# Menu
	menuUI = PreferencesMenu().getUI()

	# Main Layout
	tab = cmds.tabLayout()

	keyUI = cmds.scrollLayout(cr=True)
	anim_mancer.tools.tweenKey.UI()
	cmds.setParent('..')

	motionTrailUI = anim_mancer.tools.motionTrail.ui()

	ghostUI = anim_mancer.tools.ghost.ui()
	noteUI = anim_mancer.tools.note.ui()
	refUI = refman.ui()

	# End UI
	cmds.setParent('..')  # end tab
	cmds.setParent('..')  # end form

	cmds.tabLayout(tab,
				   edit=True,
				   tabLabel=((keyUI, 'Tween'),
							 (motionTrailUI, 'Motion Trail'),
							 (noteUI, 'Notes'),
							 (ghostUI, 'Ghost'),
							 (refUI, 'Reference')
							 ))

	cmds.formLayout('animToolsChannelBoxUI', e=True,
					attachForm=[(tab, 'left', 0),
								(tab, 'bottom', 0),
								(tab, 'right', 0),
								(menuUI, 'left', 0),
								(menuUI, 'top', 0),
								(menuUI, 'right', 0),
								],
					attachControl=[[tab, 'top', 0, menuUI]]
					)

	return