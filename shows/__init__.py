import kia
import energizer
import apex
reload(kia)
reload(energizer)
reload(apex)

from maya import cmds


def sub_menu(*args, **kwargs):
	cmds.menuItem(l='Shows', subMenu=True, to=True)
	cmds.menuItem(label='Apex Legends', d=True)
	cmds.menuItem(label='Ingest Tool', command=apex.Ingest_UI)
	cmds.setParent('..', menu=True)
	return
