from maya import cmds


def testCallback(*args, **kwargs):
    print args


def show():
    cmds.menuItem(label='Test', command=testCallback)
    return
