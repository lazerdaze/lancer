import io, os, glob, csv
from os import path
from zipfile import ZipFile
from maya import cmds, mel

MOCAP_DIR = '/jobs/ads/ea_games_apex_seasonal_J406897/mill_in/data/FROM_ANIMATRIK/Raw Data'
PREVIZ_SOURCE = '/jobs/ads/ea_games_apex_seasonal_J406897/mill_in/data/FROM_PROOF'
PREVIZ_DESTINATION = '/jobs/ads/ea_apex_J406395/mill_in/data/FROM_PROOF_2019'
PROOF_CSV = '/jobs/ads/ea_apex_J406395/shared/data/EA Apex 2 Archive Deliveries - Sheet1.csv'
ASSET_CAMERA_PATH = '//jobs//ads//ea_apex_J406395//build//camera//.common//miasma//cameraRig//base//cameraRig_base_v008.mb'
PROOF_PROJECT_DIR = '/jobs/ads/ea_apex_J406395/mill_in/data/FROM_PROOF_2019/Work/Mill_EA_Apex2'


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


class Ingest_UI(object):
	def __init__(self, *args, **kwargs):
		self.winName = 'apex_ingest_ui'
		self.csv_data = [x[1].split('\\')[-1] for x in load_array_from_csv(PROOF_CSV)]
		self.all_zips = find_all_file(PREVIZ_SOURCE, '.zip')
		self.all_fbx = find_all_file(MOCAP_DIR, '.fbx')
		self.show()

	def show(self):
		margin=10

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
		skip_check = cmds.checkBox(label='Skip Missing References', value=False)
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

		cmds.frameLayout(label='Import MOCAP', bgs=True, mw=margin, mh=margin)
		mocap_option = cmds.optionMenu(label='FBX File')
		for item in sorted([path.basename(x) for x in self.all_fbx]):
			cmds.menuItem(label=item)
		cmds.button(label='Import', command=lambda *x: self.import_fbx(cmds.optionMenu(mocap_option, q=True, value=True)
																	  ))
		cmds.setParent('..')

		cmds.setParent('..')
		cmds.showWindow(self.winName)
		return

	# Fixme: Overwrites existing nodes in file. Causes issue with Mill Retargeter
	def import_fbx(self, filepath, *args, **kwargs):
		import_path = None

		for item in self.all_fbx:
			if item.endswith(filepath):
				import_path = item
				break

		if not import_path:
			raise RuntimeError("Couldn't find FBX.")

		cmds.file(import_path, i=True)
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

	# Todo: Set Project Dir?
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

		# Open
		cmds.file(maya_path, open=True, force=True, prompt=is_skip)
		return


