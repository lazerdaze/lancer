# LANCER.CHANNELBOX.UI
#
#
#
#
#

# Lancer
import note
import tweenKey
import motionTrail
import ghost

reload(note)
reload(tweenKey)
reload(motionTrail)
reload(ghost)

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
    #AEenableTextureMaxRes "hardwareRenderingGlobals";
    #attrFieldSliderGrp -e -en true attrFieldSliderGrp3;
	#AEReloadAllTextures;
	#generateAllUvTilePreviews;
	#setAttr "hardwareRenderingGlobals.textureMaxResolution" 4096;

    print 'Lancer: ScriptJob "Open New Scene" Successful'
    return


########################################################################################################################
#
#
#	PREFERENCES / MENU
#
#
########################################################################################################################


def savePrefs():
    cmds.savePrefs(g=True)
    return


def defaultPreferences():
    # Anim Layers
    cmds.timeControl(mayaUI.timeControl, e=True,
                     animLayerFilterOptions='selected')
    mel.eval('outlinerEditor -edit -animLayerFilterOptions selected graphEditor1OutlineEd;')

    # Buffer Curves
    mel.eval('animCurveEditor -edit -showBufferCurves true graphEditor1GraphEd;')
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
    defaultPreferences()
    cmds.paneLayout(mayaUI.channelPane, e=True, cn='horizontal3')

    # Main Layout
    if cmds.layout(name, exists=True):
        cmds.deleteUI(name)

    cmds.formLayout(name, p=mayaUI.channelPane)

    cmds.separator(st='none', h=PADDING)

    # Menu
    menuUI = menu()

    # Main Layout
    tab = cmds.tabLayout()

    keyUI = cmds.scrollLayout(cr=True)
    tweenKey.ui()
    cmds.setParent('..')

    motionTrailUI = motionTrail.ui()

    ghostUI = ghost.ui()
    noteUI = note.ui()

    # motionTrail.ui()
    # note.ui()

    # End UI
    cmds.setParent('..')  # end tab
    cmds.setParent('..')  # end form

    cmds.tabLayout(tab,
                   edit=True,
                   tabLabel=((keyUI, 'Tween'),
                             (motionTrailUI, 'Motion Trail'),
                             (noteUI, 'Notes'),
                             (ghostUI, 'Ghost'),
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

    # ScriptJobs
    cmds.scriptJob(p=name, event=['SceneOpened', openNewScene])

    return
