# AXEL.THUMBNAIL
#
#
#
#
#

# Axel Modules
import ui

# Lancer Modules
from library import xfer

# Python Moduels
import os, shutil

# Maya Modules
MAYALOADED = True
try:
	from maya import cmds, mel, OpenMayaUI
except:
	MAYALOADED = False

########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################


DIRPATH = os.path.dirname(os.path.abspath(__file__))
TESTPATH = os.path.join(DIRPATH, 'test')
TEMPPATH = os.path.join(DIRPATH, 'temp')
TEMPTHUMBPATH = os.path.join(TEMPPATH, 'thumbnail')
TEMPWINDOWNAME = 'thumbnailWindow'

THUMBWIDTH = 256
THUMBHEIGHT = 256


class Componet(object):
	thumbnail = 'thumbnail'
	sequence = 'sequence'


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################

def flushTempDirectory():
	files = []

	if xfer.directoryExist(TEMPPATH):
		files = [os.path.abspath(os.path.join(TEMPPATH, f)) for f in os.listdir(TEMPPATH)]

	if files:
		for f in files:
			try:
				if os.path.isfile(f):
					os.unlink(f)
				elif os.path.isdir(f):
					shutil.rmtree(f)
			except Exception as e:
				print(e)
	return


def snapshot(filepath=TEMPTHUMBPATH, extension='jpg'):
	filename = '{}.{}'.format(filepath, extension)
	cmds.refresh(cv=True, fe="jpg", fn=filename)
	return


def getStartFrame():
	return cmds.playbackOptions(q=True, min=True)


def getEndFrame():
	return cmds.playbackOptions(q=True, max=True)


def getFrameRange(start, end, interval=1):
	return [x for x in range(int(start), int(end) + 1, interval)]


def getFocusCamera():
	focus = cmds.getPanel(wf=True)
	if cmds.modelPanel(focus, q=True, exists=True):
		return cmds.modelPanel(focus, q=True, cam=True)
	else:
		return None


def createTempViewport(camera):
	cmds.window(TEMPWINDOWNAME)
	cmds.paneLayout()
	pbPanel = cmds.modelPanel(cam=camera)
	cmds.modelEditor(pbPanel,
	                 e=True,
	                 allObjects=False,
	                 manipulators=True,
	                 grid=False,
	                 sel=False,
	                 polymeshes=True,
	                 imagePlane=True,
	                 displayAppearance='smoothShaded',
	                 ignorePanZoom=False,
	                 )
	return pbPanel


def createThumbnail(filepath=TEMPTHUMBPATH,
                    extension='jpg',
                    camera=None,
                    w=THUMBWIDTH,
                    h=THUMBHEIGHT,
                    ):
	filename = '{}.{}'.format(filepath, extension)
	camera = camera if camera else getFocusCamera()

	if not camera:
		raise ValueError('Axel Thumbnail: No Camera specified.')
	else:
		# Get Camera Info
		cameraShape = cmds.listRelatives(camera, shapes=True)[0]

		# Set Pan Zoom
		cmds.setAttr(cameraShape + '.panZoomEnabled', 1)
		cmds.panZoom(cameraShape, abs=True, l=0, u=0, z=0.50)

		# Create Window w/ Model Editor
		pbPanel = createTempViewport(camera)

		# Playblast
		cmds.playblast(epn=pbPanel, p=100, wh=(w, h), fr=cmds.currentTime(q=True), fmt='image', cf=filename,
		               c=extension, fo=True, v=False, orn=False, os=True, sqt=False, qlt=100)

		# Remove UI
		cmds.deleteUI(TEMPWINDOWNAME, window=True)

		# Reset Pan Zoom
		cmds.setAttr(cameraShape + '.panZoomEnabled', 0)
		return filename


def createSequence(filepath=TEMPTHUMBPATH,
                   extension='jpg',
                   camera=None,
                   w=THUMBWIDTH,
                   h=THUMBHEIGHT,
                   start=None,
                   end=None,
                   interval=1,
                   ):
	startFrame = start if start else getStartFrame()
	endFrame = end if end else getEndFrame()
	camera = camera if camera else getFocusCamera()

	if not camera:
		raise ValueError('Axel Thumbnail: No Camera specified.')
	else:
		# Get Camera Info
		cameraShape = cmds.listRelatives(camera, shapes=True)[0]

		# Set Pan Zoom
		cmds.setAttr(cameraShape + '.panZoomEnabled', 1)
		cmds.panZoom(cameraShape, abs=True, l=0, u=0, z=0.50)

		# Create Window w/ Model Editor
		pbPanel = createTempViewport(camera)

		# Playblast
		cmds.playblast(editorPanelName=pbPanel,
		               percent=100,
		               wh=(w, h),
		               frame=getFrameRange(startFrame, endFrame, interval),
		               indexFromZero=True,
		               format='image',
		               filename=filepath,
		               compression=extension,
		               forceOverwrite=True,
		               viewer=False,
		               showOrnaments=False,
		               offScreen=True,
		               quality=100,
		               )

		# Remove UI
		cmds.deleteUI(TEMPWINDOWNAME, window=True)

		# Reset Pan Zoom
		cmds.setAttr(cameraShape + '.panZoomEnabled', 0)
		return

