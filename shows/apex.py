import io, os, glob, csv
from os import path
from functools import partial
from zipfile import ZipFile
from maya import cmds, mel

MOCAP_DIR = '/jobs/ads/ea_games_apex_seasonal_J406897/mill_in/data/FROM_ANIMATRIK/Raw Data'
MOCAP_CLEAN_DIR = '/jobs/ads/ea_apex_J406395/mill_in/data/FROM_ANIMATRIK_2019'
PREVIZ_SOURCE = '/jobs/ads/ea_games_apex_seasonal_J406897/mill_in/data/FROM_PROOF'
PREVIZ_DESTINATION = '/jobs/ads/ea_apex_J406395/mill_in/data/FROM_PROOF_2019'
PROOF_CSV = '/jobs/ads/ea_apex_J406395/shared/data/EA Apex 2 Archive Deliveries - Sheet1.csv'
ASSET_CAMERA_PATH = '//jobs//ads//ea_apex_J406395//build//camera//.common//miasma//cameraRig//base//cameraRig_base_v008.mb'
PROOF_PROJECT_DIR = '/jobs/ads/ea_apex_J406395/mill_in/data/FROM_PROOF_2019/Work/Mill_EA_Apex2/'
FACIAL_CUBIC_DIR = '/jobs/ads/ea_apex_J406395/mill_in/data/FROM_CUBIC_MOTION'


def find_all_file(directory, extension='.zip', *args, **kwargs):
	result = []
	for dirpath, dirnames, filenames in os.walk(directory):
		for filename in [f for f in filenames if f.endswith(extension)]:
			result.append(os.path.join(dirpath, filename))
	return result


def unzip_to_destination(source, destination, *args, **kwargs):
	with ZipFile(source, 'r') as zipObj:
		zipObj.extractall(destination)
	return


def get_all_hidden(node=None, *args, **kwargs):
	if node:
		transforms = cmds.listRelatives(node, ad=True)

	else:
		transforms = cmds.ls(type='transform')

	result = []
	for transform in transforms:
		is_visible = cmds.getAttr('{}.v'.format(transform))

		if not is_visible:
			result.append(transform)
	return result


def optimize_scene(*args, **kwargs):
	mel.eval("cleanUpScene 3")
	return


def clean_scene(*args, **kwargs):
	cmds.delete(get_all_hidden('ENV'))
	optimize_scene()
	return


def load_array_from_csv(filepath, *args, **kwargs):
	result = []

	with open(filepath, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|')

		for row in reader:
			row = [row[0], row[1], [x.strip() for x in row[2].split('|')]]
			result.append(row)
	return result


def load_miasma_asset_camera(*args, **kwargs):
	import miasma
	mia = miasma.connect()

	shopping_list = []

	# Camera Rig
	shopping_list.extend(mia.search(asset_type="animation_rig", tags="ea_apex_j406395, build, camera"))

	for asset in shopping_list:
		asset.version().mio.load()
	return


def set_project_to_path(filepath, *args, **kwargs):
	if not path.isdir(filepath):
		raise RuntimeError('''Directory "{}" doesn't exist.'''.format(filepath))

	return cmds.workspace(filepath, o=True)


def getAllReferences():
	return cmds.ls(references=True)


def isReferenceLoaded(name):
	return cmds.referenceQuery(name, isLoaded=True)


def loadReference(name):
	cmds.file(loadReference=name, loadReferenceDepth="asPrefs")
	return


def unloadReference(name):
	cmds.file(unloadReference=name)
	return


def loadAllReferences(value=True):
	for ref in getAllReferences():
		if value:
			loadReference(ref)
		else:
			unloadReference(ref)
	return


def get_all_anim_nodes(*args, **kwargs):
	return cmds.ls(type='animCurve')


def referenceFilepath(name):
	return cmds.referenceQuery(name, filename=True)


def isXmlfReference(name):
	filename = referenceFilepath(name)
	return True if filename.endswith('.xmlf') else False


def timecode_to_frames(timecode, framerate=24):
	return sum(f * int(t) for f, t in zip((3600 * framerate, 60 * framerate, framerate, 1), timecode.split(':')))


def frames_to_timecode(frames, framerate=30):
	return '{0:02d}:{1:02d}:{2:02d}:{3:02d}'.format(frames / (3600 * framerate),
													frames / (60 * framerate) % 60,
													frames / framerate % 60,
													frames % framerate)


def offset_anim_nodes(nodes, offset, *args, **kwargs):
	if not isinstance(nodes, (list, dict, tuple)):
		nodes = [nodes]

	for node in nodes:
		cmds.keyframe(node, edit=True, relative=True, timeChange=offset)
	return


class RigPath(object):
	crypto_facial = '/jobs/ads/ea_apex_J406395/build/chrCrypto/m_rig/scenes/forCubicMotion/chrCrypto_build_rig_v002.ma'
	crypto = 'ECCR'

	wattson_facial = '/jobs/ads/ea_apex_J406395/build/chrWattson/m_rig/scenes/forCubicMotion/build_chrWattson_rig_v018.ma'
	wattson = 'WTSR'

	bangalore_facial = '/jobs/ads/ea_apex_J406395/build/chrBangalore/m_rig/scenes/forCubicMotion/build_chrBangalore_rig_v015.ma'
	bangalore = 'ECIR'

	gibraltar_facial = '/jobs/ads/ea_apex_J406395/build/chrGibraltar/m_rig/scenes/forCubicMotion/build_chrGibraltar_rig_v032.ma'
	gibraltar = 'EAGR'

	mirage_facial = '/jobs/ads/ea_apex_J406395/build/chrMirage/m_rig/scenes/forCubicMotion/build_chrMirage_rig_v039.ma'
	mirage = 'ECMR'


def import_facial(filepath, *args, **kwargs):
	# Query Current Scene
	# old_references = cmds.ls(type='reference')
	old_animation = cmds.ls(type='animCurve')

	# Import
	cmds.file(filepath, i=True, force=True, prompt=False)

	# Get Imported Objects
	# new_references = set(cmds.ls(type='reference')) - set(old_references)
	new_animation = set(cmds.ls(type='animCurve')) - set(old_animation)

	# Fix References
	# if new_references:
	# 	for ref in new_references:
	# 		refFilepath = cmds.referenceQuery(ref, f=True)
	# 		refFilename = os.path.basename(refFilepath)
	# 		cmds.file(refpath, loadReference=ref, options='v=0;')
	return list(new_animation)


def get_anim_start(nodes, *args, **kwargs):
	return min(cmds.keyframe(nodes, index=(0, 0), query=True))


def attach_anim_to_rig(nodes, rig, *args, **kwargs):
	if not isinstance(nodes, (list, dict, tuple)):
		nodes = [nodes]

	namespace = getattr(RigPath, rig.lower())

	for node in nodes:
		items = node.split('_SLDR_')

		name = cmds.rename(node, '{}_{}'.format(rig.lower(), node))

		slider = '{}:{}_SLDR'.format(namespace, items[0])
		attribute = ''.join([x for x in items[-1] if not x.isdigit()])

		try:
			cmds.connectAttr('{}.output'.format(name), '{}.{}'.format(slider, attribute))
		except RuntimeError:
			print 'Unable to attach: "{}". Skipped.'.format(node)
	return


def clean_facial_anim_in_scene(rig=None, *args, **kwargs):
	curves = ['C_eye_SLDR_translateX',
			  'C_eye_SLDR_translateY',
			  'C_jaw_SLDR_translateX',
			  'C_jaw_SLDR_translateY',
			  'C_mouth_SLDR_translateX',
			  'C_mouth_SLDR_translateY',
			  'C_scalp_SLDR_translateX',
			  'C_tongue_SLDR_translateX',
			  'C_tongue_SLDR_translateY',
			  'L_brow_depressor_SLDR_translateX',
			  'L_brow_inner_raiser_SLDR_translateX',
			  'L_brow_lateral_SLDR_translateX',
			  'L_brow_outer_raiser_SLDR_translateX',
			  'L_cheek_puff_suck_SLDR_translateX',
			  'L_cheek_raiser_SLDR_translateX',
			  'L_corner_depressor_SLDR_translateX',
			  'L_corner_dimpler_SLDR_translateX',
			  'L_corner_puller_SLDR_translateX',
			  'L_ear_puller_SLDR_translateX',
			  'L_eye_lid_SLDR_translateX',
			  'L_eye_SLDR_translateX',
			  'L_eye_SLDR_translateY',
			  'L_lip_funneler_SLDR_translateX',
			  'L_lip_lower_SLDR_translateX',
			  'L_lip_pucker_SLDR_translateX',
			  'L_lip_upper_SLDR_translateX',
			  'L_nose_SLDR_translateX',
			  'L_nose_SLDR_translateY',
			  'L_platsyma_flex_SLDR_translateX',
			  'L_sterno_flex_SLDR_translateX',
			  'R_brow_depressor_SLDR_translateX',
			  'R_brow_inner_raiser_SLDR_translateX',
			  'R_brow_lateral_SLDR_translateX',
			  'R_brow_outer_raiser_SLDR_translateX',
			  'R_cheek_puff_suck_SLDR_translateX',
			  'R_cheek_raiser_SLDR_translateX',
			  'R_corner_depressor_SLDR_translateX',
			  'R_corner_dimpler_SLDR_translateX',
			  'R_corner_puller_SLDR_translateX',
			  'R_ear_puller_SLDR_translateX',
			  'R_eye_lid_SLDR_translateX',
			  'R_eye_SLDR_translateX',
			  'R_eye_SLDR_translateY',
			  'R_lip_funneler_SLDR_translateX',
			  'R_lip_lower_SLDR_translateX',
			  'R_lip_pucker_SLDR_translateX',
			  'R_lip_upper_SLDR_translateX',
			  'R_nose_SLDR_translateX',
			  'R_nose_SLDR_translateY',
			  'R_platsyma_flex_SLDR_translateX',
			  'R_sterno_flex_SLDR_translateX',
			  'C_jaw_SLDR_back_forward',
			  'C_jaw_SLDR_chin_depress_lower_l',
			  'C_jaw_SLDR_chin_depress_lower_r',
			  'C_jaw_SLDR_chin_depress_upper_l',
			  'C_jaw_SLDR_chin_depress_upper_r',
			  'C_jaw_SLDR_chin_raise_lower_l',
			  'C_jaw_SLDR_chin_raise_lower_r',
			  'C_jaw_SLDR_chin_raise_upper_l',
			  'C_jaw_SLDR_chin_raise_upper_r',
			  'C_jaw_SLDR_clench_l',
			  'C_jaw_SLDR_clench_r',
			  'C_mouth_SLDR_lips_together',
			  'C_mouth_SLDR_puff_l',
			  'C_mouth_SLDR_puff_r',
			  'C_mouth_SLDR_sticky_lips',
			  'C_mouth_SLDR_tighten_lower',
			  'C_mouth_SLDR_tighten_upper',
			  'C_mouth_SLDR_together_lower',
			  'C_mouth_SLDR_together_upper',
			  'C_tongue_SLDR_bias',
			  'C_tongue_SLDR_curl',
			  'C_tongue_SLDR_drop_lift',
			  'C_tongue_SLDR_push_in_out',
			  'C_tongue_SLDR_twist',
			  'L_corner_depressor_SLDR_stretcher',
			  'L_corner_puller_SLDR_sharpen',
			  'L_eye_lid_SLDR_compress',
			  'L_eye_lid_SLDR_reach_lower',
			  'L_eye_lid_SLDR_reach_upper',
			  'L_eye_lid_SLDR_squint',
			  'L_eye_SLDR_constrict_dilate',
			  'L_lip_funneler_SLDR_lower',
			  'L_lip_funneler_SLDR_upper',
			  'L_lip_lower_SLDR_pinch',
			  'L_lip_lower_SLDR_press',
			  'L_lip_pucker_SLDR_lower',
			  'L_lip_pucker_SLDR_narrow',
			  'L_lip_pucker_SLDR_upper',
			  'L_lip_upper_SLDR_deepen',
			  'L_lip_upper_SLDR_pinch',
			  'L_lip_upper_SLDR_press',
			  'R_corner_depressor_SLDR_stretcher',
			  'R_corner_puller_SLDR_sharpen',
			  'R_eye_lid_SLDR_compress',
			  'R_eye_lid_SLDR_reach_lower',
			  'R_eye_lid_SLDR_reach_upper',
			  'R_eye_lid_SLDR_squint',
			  'R_eye_SLDR_constrict_dilate',
			  'R_lip_funneler_SLDR_lower',
			  'R_lip_funneler_SLDR_upper',
			  'R_lip_lower_SLDR_pinch',
			  'R_lip_lower_SLDR_press',
			  'R_lip_pucker_SLDR_lower',
			  'R_lip_pucker_SLDR_narrow',
			  'R_lip_pucker_SLDR_upper',
			  'R_lip_upper_SLDR_deepen',
			  'R_lip_upper_SLDR_pinch',
			  'R_lip_upper_SLDR_press'
			  ]

	for curve in curves:
		for anim in get_all_anim_nodes():
			if anim.startswith(curve):
				cmds.delete(anim)

			if rig:
				name = '{}_{}'.format(rig.lower(), curve)

				if anim.startswith(name):
					if cmds.objExists(anim):
						cmds.delete(anim)

		if cmds.objExists(curve):
			cmds.delete(curve)
		if rig:
			name = '{}_{}'.format(rig.lower(), curve)
			if cmds.objExists(name):
				cmds.delete(name)

			if curve.startswith(name):
				if cmds.objExists(curve):
					cmds.delete(curve)
	return


class Ingest_UI(object):
	def __init__(self, *args, **kwargs):
		self.winName = 'apex_ingest_ui'
		self.csv_data = [x[1].split('\\')[-1] for x in load_array_from_csv(PROOF_CSV)]

		self.all_zips = find_all_file(PREVIZ_SOURCE, '.zip')
		self.all_raw_fbx = {}
		self.all_clean_fbx = {}
		self.current_mocap_filepath = None
		self.can_offset_mocap = 'auto'
		self.mocap_type = 'raw'
		self.all_facial_maya = {}
		self.current_mocap_rig = ''

		# Get Mocap
		for item in find_all_file(MOCAP_DIR, '.fbx'):
			self.all_raw_fbx[path.basename(item).lower()] = item

		for item in find_all_file(MOCAP_CLEAN_DIR, '.fbx'):
			self.all_clean_fbx[path.basename(item).lower()] = item

		for item in find_all_file(FACIAL_CUBIC_DIR, '.ma'):
			char = path.basename(path.dirname(item))
			name = '{} : {}'.format(char, path.basename(item).lower())
			self.all_facial_maya[name] = item

		self.show()
		self.update_mocap_option_callback('raw')

	def show(self):
		margin = 10

		if cmds.window(self.winName, q=True, ex=True):
			cmds.deleteUI(self.winName)

		cmds.window(self.winName, title='Apex Ingest Tool')

		cmds.columnLayout(adj=True, columnAttach=('both', 10))
		cmds.separator(h=10, st='none')
		cmds.frameLayout(label='Find Maya File', bgs=True, mw=margin, mh=margin)
		# Maya Files
		maya_option = cmds.optionMenu(label='Maya File')
		for item in sorted(self.csv_data):
			cmds.menuItem(label=item)
		zip_check = cmds.checkBox(label='Un-Zip', value=False)
		skip_check = cmds.checkBox(label='Skip Missing References', value=False, enable=False, vis=False)
		cmds.button(label='Open',
					command=lambda *x: self.open_maya_file(cmds.optionMenu(maya_option, q=True, value=True),
														   cmds.checkBox(zip_check, q=True, value=True),
														   cmds.checkBox(skip_check, q=True, value=True)
														   )
					)
		cmds.setParent('..')
		cmds.separator(h=10, st='none')
		cmds.frameLayout(label='Clean Scene', bgs=True, mw=margin, mh=margin)
		optimize_check = cmds.checkBox(label='Optimize', value=True)
		hidden_check = cmds.checkBox(label='Delete Hidden (Env)', value=True)
		cmds.button(label='Clean', command=lambda *x: self.clean_file(cmds.checkBox(optimize_check, q=True, value=True),
																	  cmds.checkBox(hidden_check, q=True, value=True),
																	  ))
		cmds.setParent('..')
		cmds.separator(h=10, st='none')
		cmds.frameLayout(label='Camera', bgs=True, mw=margin, mh=margin)
		parent_check = cmds.checkBox(label='Parent to Existing', value=False, enable=False)
		cmds.button(label='Import Miasma Camera',
					command=lambda *x: self.import_camera(cmds.checkBox(parent_check, q=True, value=True), ))
		cmds.setParent('..')
		cmds.separator(h=10, st='none')

		# MOCAP UI
		cmds.frameLayout(label='Import MOCAP', bgs=True, mw=margin, mh=margin)
		mocap_collection = cmds.radioCollection()
		cmds.rowLayout(nc=3, adj=3)
		mocap_rb1 = cmds.radioButton(label='Raw', select=True, onc=partial(self.update_mocap_option_callback, 'raw'))
		mocap_rb2 = cmds.radioButton(label='Clean', select=False,
									 onc=partial(self.update_mocap_option_callback, 'clean'))
		mocap_rb3 = cmds.radioButton(label='Facial', select=False,
									 onc=partial(self.update_mocap_option_callback, 'facial'))
		cmds.setParent('..')
		self.mocap_option = cmds.optionMenu(label='File', cc=self.update_current_mocap)
		for item in sorted([path.basename(x) for x in self.all_raw_fbx]):
			cmds.menuItem(label=item)

		self.mocap_rig_option = cmds.optionMenu(label='Rig', cc=self.update_current_rig, enable=False)
		for item in sorted(['Mirage', 'Wattson', 'Bangalore', 'Crypto', 'Gibraltar', '']):
			cmds.menuItem(label=item)

		self.offset_mocap_collection = cmds.radioCollection()
		cmds.rowLayout(nc=3, adj=3)
		mocap_off_rb1 = cmds.radioButton(label='No Offset', select=False,
										 onCommand=partial(self.mocap_offset_callback, 'no'))
		mocap_off_rb2 = cmds.radioButton(label='Auto Offset', select=True,
										 onCommand=partial(self.mocap_offset_callback, 'auto'))
		mocap_off_rb3 = cmds.radioButton(label='Timecode Offset', select=False,
										 onCommand=partial(self.mocap_offset_callback, 'time'))
		cmds.setParent('..')

		# cmds.checkBox(label='Offset', value=False, changeCommand=self.mocap_offset_callback)
		self.mocap_time = cmds.timeFieldGrp(label='Timecode', adj=2, cw=[1, 60], enable=False)
		self.mocap_start = cmds.timeFieldGrp(label='Start Frame', adj=2, cw=[1, 60], value1=1001.0, enable=False)

		cmds.button(label='Import', command=self.import_file)

		cmds.setParent('..')
		cmds.separator(h=10, st='none')

		cmds.setParent('..')
		cmds.showWindow(self.winName)
		return

	def update_current_rig(self, *args):
		self.current_mocap_rig = args[0]
		return

	def clear_mocap_option(self, *args):
		menuItems = cmds.optionMenu(self.mocap_option, q=True, itemListLong=True)
		if menuItems:
			cmds.deleteUI(menuItems)
		return

	def mocap_offset_callback(self, kind, *args):
		self.can_offset_mocap = kind

		if kind == 'time':
			cmds.timeFieldGrp(self.mocap_time, e=True, enable=True)
			cmds.timeFieldGrp(self.mocap_start, e=True, enable=True)
		else:
			cmds.timeFieldGrp(self.mocap_time, e=True, enable=False)
			cmds.timeFieldGrp(self.mocap_start, e=True, enable=False)
		return

	def update_current_mocap(self, *args):
		query = args[0]

		if query in self.all_raw_fbx:
			self.current_mocap_filepath = self.all_raw_fbx[query]
		elif query in self.all_clean_fbx:
			self.current_mocap_filepath = self.all_clean_fbx[query]
		elif query in self.all_facial_maya:
			self.current_mocap_filepath = self.all_facial_maya[query]
		else:
			self.current_mocap_filepath = None

		print self.current_mocap_filepath,
		return

	def update_mocap_option_callback(self, value, *args):
		self.clear_mocap_option()
		if value == 'raw':
			for item in sorted([x for x in self.all_raw_fbx.keys()]):
				cmds.menuItem(label=item, parent=self.mocap_option)
			self.current_mocap_filepath = self.all_raw_fbx[cmds.optionMenu(self.mocap_option, q=True, value=True)]
		elif value == 'clean':
			for item in sorted([x for x in self.all_clean_fbx.keys()]):
				cmds.menuItem(label=item, parent=self.mocap_option)
			self.current_mocap_filepath = self.all_clean_fbx[cmds.optionMenu(self.mocap_option, q=True, value=True)]
		elif value == 'facial':
			cmds.optionMenu(self.mocap_rig_option, e=True, enable=True)
			for item in sorted([x for x in self.all_facial_maya.keys()]):
				cmds.menuItem(label=item, parent=self.mocap_option)
			self.current_mocap_filepath = self.all_facial_maya[cmds.optionMenu(self.mocap_option, q=True, value=True)]
		self.mocap_type = value
		return

	def import_file(self, is_debug=False, *args, **kwargs):
		old_anim = get_all_anim_nodes()
		filepath = self.current_mocap_filepath

		# Edge Case
		if not os.path.isfile(filepath):
			raise RuntimeError("Couldn't find file: {}".format(filepath))

		# Clean Facial Data
		if self.mocap_type == 'facial':
			if not self.current_mocap_rig:
				raise RuntimeError('No Rig Specified.')

			clean_facial_anim_in_scene(rig=self.current_mocap_rig)

		# Import File
		cmds.file(filepath, i=True, force=True, prompt=False)

		# Offset Anim Nodes
		new_anim = list(set(get_all_anim_nodes()) - set(old_anim))

		if self.can_offset_mocap != 'no':
			offset_diff = 0

			# Auto Offset
			if self.can_offset_mocap == 'auto':
				if new_anim:
					timecode = get_anim_start(new_anim)
					offset_diff = 1001.0 - timecode

			# Manuel Offset
			elif self.can_offset_mocap == 'time':
				timecode = cmds.timeFieldGrp(self.mocap_time, q=True, value1=True)
				start = cmds.timeFieldGrp(self.mocap_start, q=True, value1=True)
				offset_diff = start - timecode
				# new_anim = [x for x in get_all_anim_nodes() if x not in old_anim]

				if is_debug:
					print timecode, start, offset_diff

			# Shift Keys
			if new_anim:
				offset_anim_nodes(new_anim, offset_diff)

			if is_debug:
				print old_anim
				print new_anim

		# Attach To Rig
		if self.mocap_type == 'facial' and self.current_mocap_rig:
			attach_anim_to_rig(new_anim, self.current_mocap_rig)

		return

	def clean_file(self, is_optimize=False, is_hidden=False, *args, **kwargs):
		if is_hidden:
			if cmds.objExists('ENV'):
				cmds.delete(get_all_hidden('ENV'))

		if is_optimize:
			optimize_scene()
		print 'Scene Cleaned.',
		return

	def import_camera(self, is_parent=False):
		load_miasma_asset_camera()

		if is_parent:
			pass

		return

	def open_maya_file(self, file_name, is_zip=False, is_skip=False, *args, **kwargs):
		# Find zip
		if is_zip:
			zip_file = None

			for item in self.all_zips:
				if file_name in path.basename(item):
					zip_file = item
					break

			if not zip_file:
				raise RuntimeError("Couldn't find zip file.")

			# Unzip
			unzip_to_destination(zip_file, PREVIZ_DESTINATION)

		# Todo: Mutiple Maya Files (Same Names)
		# Find Maya File
		all_maya_files = find_all_file(PREVIZ_DESTINATION, '.ma')
		maya_path = None

		for maya_file in all_maya_files:
			if file_name in path.basename(maya_file):
				maya_path = maya_file
				break

		if not maya_path:
			raise RuntimeError("Couldn't find maya file.")

		# Set Project Path
		set_project_to_path(PROOF_PROJECT_DIR)

		# Open
		cmds.file(maya_path, open=True, force=True, loadReferenceDepth='none')

		# Re-Load References
		loadAllReferences()
		return


def bake_animation(nodes, startFrame, endFrame, *args, **kwargs):
	cmds.bakeResults(
		nodes,
		simulation=True,
		t=(startFrame, endFrame),
		sampleBy=1,
		disableImplicitControl=True,
		preserveOutsideKeys=True,
		sparseAnimCurveBake=False,
		removeBakedAttributeFromLayer=False,
		removeBakedAnimFromLayer=False,
		bakeOnOverrideLayer=False,
		minimizeRotation=True,
		controlPoints=False,
		shape=False,
	)
	return


def create_locator(*args, **kwargs):
	return cmds.spaceLocator()[0]


def delete_keys(dag_nodes, *args, **kwargs):
	if not isinstance(dag_nodes, (dict, tuple, list)):
		dag_nodes = [dag_nodes]

	for dag in dag_nodes:
		for attr in ['t', 'r']:
			for axis in ['x', 'y', 'z']:
				for typ in ['TU', 'TL', 'TA']:
					con = cmds.listConnections('{}.{}{}'.format(dag, attr, axis),
											   s=True,
											   type='animCurve{}'.format(typ),
											   scn=True
											   )
					if con:
						try:
							cmds.delete(con)
						except RuntimeError:
							print 'Delete skipped: {}'.format(con)
	return


def getTimeRange(*args):
	start = cmds.playbackOptions(q=True, minTime=True)
	end = cmds.playbackOptions(q=True, maxTime=True)
	return [start, end]


# Todo: Faster way to bake
def local_world_bake_attribute(dag_nodes, attribute, value):
	if not isinstance(dag_nodes, (list, dict, tuple)):
		dag_nodes = [dag_nodes]

	# Create Locator
	locators = []

	for dag in dag_nodes:
		locator = create_locator()
		cmds.parentConstraint(dag, locator, mo=False)
		locators.append(locator)

	# Bake Locator
	start = int(getTimeRange()[0])
	end = int(getTimeRange()[1])

	bake_animation(locators, start, end)

	# Delete Keys On Object
	delete_keys(dag_nodes)

	# Switch Attr
	connList = []

	for dag in dag_nodes:
		index = dag_nodes.index(dag)
		cmds.setAttr('{}.{}'.format(dag, attribute), value)

		# New Constraint
		conn2 = cmds.parentConstraint(locators[index], dag, mo=False)[0]
		connList.append(conn2)

	# Bake Item
	bake_animation(dag_nodes, start, end)

	# Cleanup
	cmds.delete(locators, connList)
	return True


if __name__ == '__main__':
	Ingest_UI()
