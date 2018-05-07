import maya.cmds as cmds

uiName = 'lancerMarkingMenu'


def postMenuCommand(uiFunction, attrName='type'):
	def wrapper(*args):
		selected = cmds.ls(sl=True)
		if cmds.popupMenu(uiName, exists=True):
			cmds.popupMenu(uiName, e=True, deleteAllItems=True)
			cmds.setParent(uiName, menu=True)
			if selected:
				selected = selected[0]
				if cmds.attributeQuery(attrName, node=selected, exists=True):
					uiFunction()
			else:
				cmds.menuItem(l='None', enable=False)
		return

	return wrapper


@postMenuCommand
def ui(*args):
	cmds.menuItem(l='FK | IK Switch')
	cmds.menuItem(l='Mirror Pose')


def show(uiFunction=ui, *args):
	if cmds.popupMenu(uiName, exists=True):
		cmds.deleteUI(uiName)
	cmds.popupMenu(uiName, alt=True, sh=True, button=3, mm=True, p='viewPanes', pmc=uiFunction)
	return


