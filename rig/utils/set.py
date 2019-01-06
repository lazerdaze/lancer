# Maya Modules
from maya import cmds

def createSet(objs, n='set1', *args):
	rootQuery = queryNetwork()
	rootSet = rootQuery.set

	cmds.select(d=True)
	objs = listCheck(objs)
	set = cmds.sets(objs, name=n)

	if cmds.objExists(str(rootSet)):
		cmds.sets(set, add=rootSet)

	return set