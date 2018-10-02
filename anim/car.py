from maya import cmds, mel

########################################################################################################################
#
#
#	GLOBALS
#
#
########################################################################################################################


WINDOWNAME = 'CARWINDOWUI'
WINDOWTITLE = 'Car Manager'


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################

def getAllReferences():
    return cmds.ls(references=True)


def getAllTopLevelNodes():
    return cmds.ls(assemblies=True)


def isReferenceLoaded(name):
    return cmds.referenceQuery(name, isLoaded=True)


def loadReference(name):
    cmds.file(loadReference=name)
    return


def unloadReference(name):
    cmds.file(unloadReference=name)
    return


def loadAllReferences(value=True):
    for ref in getAllReferences():
        if not isXmlfReference(ref):
            if value:
                loadReference(ref)
            else:
                unloadReference(ref)
    return


def referenceFilepath(name):
    return cmds.referenceQuery(name, filename=True)


def isXmlfReference(name):
    filename = referenceFilepath(name)
    return True if filename.endswith('.xmlf') else False


def openFile(loaded=False, *args):
    multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"

    # Choose file to open
    filename = cmds.fileDialog2(fileFilter=multipleFilters, dialogStyle=2, fileMode=1)

    # Open file with no reference loaded
    cmds.file(filename[0], open=True, force=True, loadReferenceDepth='all' if loaded else 'none')

    # Ignore XMLF References (Camera)
    if not loaded:
        for ref in getAllReferences():
            if isXmlfReference(ref):
                loadReference(ref)

    return filename


########################################################################################################################
#
#
#	CLASS
#
#
########################################################################################################################

class Item(object):
    def __init__(self,
                 parent=None,
                 name=None,
                 assembly=None,
                 namespace=None,
                 index=0,
                 visibility=True,
                 proxy=True,
                 controls=True,
                 reference=None,
                 state=None,
                 loaded=True,
                 filepath=None,
                 ):
        self.parent = parent
        self.name = name
        self.reference = reference
        self.assembly = assembly
        self.namespace = namespace
        self.index = index
        self.visibility = visibility
        self.proxy = proxy
        self.controls = controls
        self.state = state
        self.loaded = loaded
        self.filepath = filepath


class TreeButton:
    def __init__(self):
        pass


class TreeView:
    def __init__(self):
        self.loadReferencesOnOpen = False
        self.items = {}

        self.layout = cmds.formLayout()
        self.menu = cmds.menuBarLayout()
        cmds.menu(label='File')
        cmds.menuItem(label='Load References On Open', checkBox=False, c=self.setloadReferencesOnOpen)
        cmds.menuItem(divider=True)
        cmds.menuItem(label='Open', c=self.open)

        cmds.menu(label='References')
        cmds.menuItem(label='Load All', c=self.loadAllReferences)
        cmds.menuItem(label='Unload All', c=self.unloadAllReferences)

        cmds.menu(label='Extras')
        cmds.menuItem(label='Show All')
        cmds.menuItem(label='Hide All')

        cmds.menu(label='UI')
        cmds.menuItem(label='Refresh')

        # cmds.menu(label='Items')
        # cmds.menuItem(label='Add')
        # cmds.menuItem(label='Remove')
        # cmds.menuItem(label='Refresh')
        # cmds.menu(label='Help', helpMenu=True)
        # cmds.menuItem(label='About...')
        cmds.setParent('..')

        self.ui = cmds.treeView(parent=self.layout,
                                numberOfButtons=2,
                                abr=False,
                                adr=False,
                                ams=False,
                                idc=self.doubleClickCallback,
                                dc2=self.doubleClickCallback,
                                pc=[[1, self.loadReferenceCallback], [2, self.setVisibleCallback]]
                                )
        cmds.setParent('..')

        cmds.formLayout(self.layout, e=True, attachForm=(self.menu, 'top', 0))
        cmds.formLayout(self.layout, e=True, attachForm=(self.menu, 'left', 0))
        cmds.formLayout(self.layout, e=True, attachForm=(self.menu, 'right', 0))
        cmds.formLayout(self.layout, e=True, attachControl=(self.ui, 'top', 0, self.menu))
        cmds.formLayout(self.layout, e=True, attachForm=(self.ui, 'bottom', 0))
        cmds.formLayout(self.layout, e=True, attachForm=(self.ui, 'left', 0))
        cmds.formLayout(self.layout, e=True, attachForm=(self.ui, 'right', 0))

        # cmds.treeView(self.ui, e=True, addItem=("layer 1", ""))
        # cmds.treeView(self.ui, e=True, addItem=("layer 2", ""))
        # cmds.treeView(self.ui, e=True, addItem=("layer 3", ""))
        # cmds.treeView(self.ui, e=True, addItem=("layer 4", ""))
        # cmds.treeView(self.ui, e=True, addItem=("layer 5", ""))
        # cmds.treeView(self.ui, e=True, addItem=("layer 6", ""))
        # cmds.treeView(self.ui, edit=True,
        #               pressCommand=[(1, pressTreeCallBack),
        #                             (2, pressTreeCallBack),
        #                             (3, pressTreeCallBack)])
        cmds.treeView(self.ui, edit=True, selectCommand=self.selectTreeCallBack)
        self.load()

    def loadReferenceCallback(self, *args):
        name = args[0]
        value = bool(int(args[1]))
        if not value:
            loadReference(name)
        else:
            unloadReference(name)
        self.items[name].loaded = False if value else True
        return

    def setVisibleCallback(self, *args):
        name = args[0]
        value = bool(int(args[1]))
        nodes = self.items[name].assembly

        if nodes:
            for node in nodes:
                cmds.setAttr('{}.v'.format(node), False if value else True)
        self.items[name].visibility = False if value else True
        return

    def doubleClickCallback(self, *args):
        return

    def setloadReferencesOnOpen(self, *args):
        self.loadReferencesOnOpen = args[0]
        return

    def loadAllReferences(self, *args):
        loadAllReferences(True)

        for item in self.items:
            cmds.treeView(self.ui, e=True, buttonState=(item, 1, "buttonUp"))
            itemData = self.items[item]
            itemData.loaded = True
            itemData.assembly = [x for x in getAllTopLevelNodes() if x.startswith(itemData.namespace)]
        return

    def unloadAllReferences(self, *args):
        loadAllReferences(False)
        for item in self.items:
            cmds.treeView(self.ui, e=True, buttonState=(item, 1, "buttonDown"))
            self.items[item].loaded = False
        return

    def open(self, *args):
        openFile(loaded=self.loadReferencesOnOpen)
        self.load()
        return

    def getUI(self):
        return self.ui

    def popupMenu(self):
        return

    def createNode(self):
        return

    def clear(self):
        self.items = {}
        cmds.treeView(self.ui, e=True, removeAll=True)
        return

    def load(self):
        self.clear()

        references = getAllReferences()
        if references:
            for ref in references:
                if ref not in self.items:
                    if not isXmlfReference(ref):
                        namespace = ref[:-2]
                        assembly = [x for x in getAllTopLevelNodes() if x.startswith(namespace)]
                        loaded = isReferenceLoaded(ref)

                        # Item Class
                        self.items[ref] = Item(name=ref,
                                               reference=ref,
                                               namespace=namespace,
                                               assembly=assembly,
                                               loaded=loaded,
                                               filepath=referenceFilepath(ref),
                                               )

                        # Buttons
                        cmds.treeView(self.ui, e=True, addItem=(ref, ''))
                        cmds.treeView(self.ui, e=True,
                                      buttonTextIcon=[[ref, 1, 'R'], [ref, 2, 'V']],
                                      buttonStyle=[[ref, 1, "2StateButton"], [ref, 2, "2StateButton"]])

                        if not loaded:
                            cmds.treeView(self.ui, e=True, buttonState=(ref, 1, "buttonDown"))

        return

    def buttonCallback(self, *args):
        print args
        return

    def addItem(self):
        return

    def removeItem(self):
        return

    def scriptJob(self):
        return

    def selectTreeCallBack(self, *args):
        # print 'selection :- str= ' + args[0] + ' onoff= ' + str(args[1])
        item = self.items[args[0]]
        if item.assembly:

            if args[1]:
                cmds.select(item.assembly)
            else:
                cmds.select(item.assembly, d=True)

        return True

    def pressTreeCallBack(*args):
        print 'press :- str= ' + args[0] + ' onoff= ' + str(args[1])


########################################################################################################################
#
#
#	WINDOW
#
#
########################################################################################################################


def show(winName=WINDOWNAME, title=WINDOWTITLE):
    if cmds.window(winName, exists=True):
        cmds.deleteUI(winName, wnd=True)

    cmds.window(winName, t=title)
    TreeView()
    cmds.showWindow(winName)
    return
