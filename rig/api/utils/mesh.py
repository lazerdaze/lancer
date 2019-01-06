# Maya Modules
from maya import cmds


def getVertPosition(obj, *args):
	verts = cmds.ls('{0}.vtx[:]'.format(obj), fl=True)

	for v in verts:
		print
		cmds.xform(v, q=True, ws=True, t=True)
