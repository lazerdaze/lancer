# Python Modules
import os
from os import path
import sys
import platform

# Maya Modules
from maya import cmds, mel


class System(object):
	operating_system = platform.system()
	maya_version = str(cmds.about(v=True))
	maya_2016 = '2016'
	maya_2017 = '2017'
	maya_2018 = '2018'
	maya_2019 = '2019'
	maya_2020 = '2020'


class Path(object):
	directory = path.dirname(path.abspath(__file__))
	package = path.dirname(directory)
	resource = path.join(package, 'ui', 'resource')
	theme = path.join(resource, 'theme.css')
	user_script = cmds.internalVar(userScriptDir=True)
	user_app = cmds.internalVar(userAppDir=True)
	user_pref = cmds.internalVar(userPrefDir=True)
	user_temp = cmds.internalVar(userTmpDir=True)
	maya_plugin = mel.eval('getenv "MAYA_PLUG_IN_PATH"')


class Env(object):
	# Virtual
	is_virtual = hasattr(sys, 'real_prefix')
	
	# The Mill
	is_mill = False
	
	for x in sys.path:
		if 'mill' in x:
			is_mill = True
			break


class ConfigPath(object):
	name = 'animMancer'
	directory = path.join(name, Path.user_pref)


class IconPath(object):
	directory = Path.resource
	gear = path.join(directory, 'icon_gear.png')
	logo = path.join(directory, 'icon_logo.png')
	snap = path.join(directory, 'icons_snap.png')
	locator = path.join(directory, 'icons_locate.png')
	time = path.join(directory, 'icons_time.png')
	grid = path.join(directory, 'icons_grid.png')
	motion_trail = path.join(directory, 'icons_motion.png')
	motion_path = path.join(directory, 'icons_path.png')
	ghost = path.join(directory, 'icons_ghost.png')
	bake = path.join(directory, 'icons_bake.png')
	key = path.join(directory, 'icons_key.png')
	fk = path.join(directory, 'icons_fk.png')
	ik = path.join(directory, 'icons_ik.png')
	set = path.join(directory, 'icons_set.png')


class UI(object):
	package = 'Anim-Mancer'
	title = 'Anim-Mancer'
	name = 'anim_mancer_ui'
	window = '{}_window'.format(name)
	
	# Maya Channelbox
	channelbox_editor = 'ChannelBoxLayerEditor'
	channelbox_main = 'ChannelBoxLayerEditor|MainChannelsLayersLayout'
	channelbox_button = 'ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelButtonForm'
	channelbox_pane = 'ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout'
	channelbox_menu = 'ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|ChannelBoxForm|menuBarLayout1'
	channelbox_control = 'mainChannelBox'
	channelbox_layer = 'ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm'
	channelbox_layer_tab = 'ChannelBoxLayerEditor|MainChannelsLayersLayout|ChannelsLayersPaneLayout|LayerEditorForm|DisplayLayerUITabLayout'
	
	# Maya Graph Editor
	graph_editor = 'graphEditor1'
	graph_editor_outliner = 'graphEditor1OutlineEd'
	graph_editor_menu = 'graphEditor1'
	graph_editor_curve = 'graphEditor1GraphEd'
	graph_editor_curve_canvas = 'graphEditor1GraphEdImpl'
	
	# Maya Timeline Editor
	timeline_editor = ''
	
	# Maya Time Editor
	time_editor = ''
