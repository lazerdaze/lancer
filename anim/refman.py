from maya import cmds, mel

########################################################################################################################
#
#
#	GLOBALS
#
#
########################################################################################################################


WINDOWNAME = 'REFMANWINDOWUI'
WINDOWTITLE = 'Reference Manager'


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


def getAllSets():
    return cmds.ls(set=True)


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
    multipleFilters = 'Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)'

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
                 proxy=False,
                 controls=True,
                 reference=None,
                 state=None,
                 loaded=True,
                 filepath=None,
                 sets=None,
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
        self.sets = sets

    def __str__(self):
        value = ''
        for x in vars(self).iterkeys():
            value += '{}: {}\n'.format(x, vars(self)[x])
        return value


class TreeView:
    def __init__(self, margin=5, padding=5):
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

        cmds.menu(label='Extras', enable=False)
        cmds.menuItem(label='Show All')
        cmds.menuItem(label='Hide All')

        cmds.menu(label='UI')
        cmds.menuItem(label='Refresh', c=self.load)

        cmds.menu(label='Help', helpMenu=True)
        cmds.menuItem(label='Print Debug Info', c=self.debugInfo)

        cmds.setParent('..')

        self.ui = cmds.treeView(parent=self.layout,
                                numberOfButtons=3,
                                abr=False,
                                adr=False,
                                ams=False,
                                idc=self.doubleClickCallback,
                                dc2=self.doubleClickCallback,
                                pc=[[1, self.loadReferenceCallback],
                                    [2, self.setVisibleCallback],
                                    [3, self.selectControlsCallback],
                                    ]
                                )
        cmds.setParent('..')

        cmds.formLayout(self.layout, e=True, attachForm=(self.menu, 'top', padding))
        cmds.formLayout(self.layout, e=True, attachForm=(self.menu, 'left', padding))
        cmds.formLayout(self.layout, e=True, attachForm=(self.menu, 'right', padding))
        cmds.formLayout(self.layout, e=True, attachControl=(self.ui, 'top', margin, self.menu))
        cmds.formLayout(self.layout, e=True, attachForm=(self.ui, 'bottom', padding))
        cmds.formLayout(self.layout, e=True, attachForm=(self.ui, 'left', padding))
        cmds.formLayout(self.layout, e=True, attachForm=(self.ui, 'right', padding))

        cmds.treeView(self.ui, edit=True, selectCommand=self.selectTreeCallBack)
        self.load()

    def debugInfo(self, *args):
        for item in self.items:
            print item
            print self.items[item]
            print ''
        return

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

    def selectControlsCallback(self, *args):
        name = args[0]
        nodes = self.items[name].controls
        cmds.select(nodes)
        return

    def doubleClickCallback(self, *args):
        return

    def setloadReferencesOnOpen(self, *args):
        self.loadReferencesOnOpen = args[0]
        return

    def loadAllReferences(self, *args):
        loadAllReferences(True)

        for item in self.items:
            cmds.treeView(self.ui, e=True, buttonState=(item, 1, 'buttonUp'))
            itemData = self.items[item]
            itemData.loaded = True
            itemData.assembly = [x for x in getAllTopLevelNodes() if x.startswith(itemData.namespace)]
        return

    def unloadAllReferences(self, *args):
        loadAllReferences(False)
        for item in self.items:
            cmds.treeView(self.ui, e=True, buttonState=(item, 1, 'buttonDown'))
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

    def load(self, *args):
        self.clear()

        references = getAllReferences()
        if references:
            for ref in references:
                if ref not in self.items:
                    if not isXmlfReference(ref):
                        namespace = ref[:-2]
                        assembly = [x for x in getAllTopLevelNodes() if x.startswith(namespace)]
                        loaded = isReferenceLoaded(ref)
                        sets = [x for x in getAllSets() if x.startswith(namespace)]

                        controlSet = '{}:CONTROLS'.format(namespace)
                        controls = cmds.sets(controlSet, q=True) if cmds.objExists(controlSet) else None

                        # Item Class
                        self.items[ref] = Item(name=ref,
                                               reference=ref,
                                               namespace=namespace,
                                               assembly=assembly,
                                               loaded=loaded,
                                               filepath=referenceFilepath(ref),
                                               controls=controls,
                                               sets=sets,
                                               )

                        # Buttons
                        cmds.treeView(self.ui, e=True, addItem=(ref, ''))
                        cmds.treeView(self.ui, e=True,
                                      buttonTextIcon=[[ref, 1, 'R'],
                                                      [ref, 2, 'V'],
                                                      [ref, 3, 'C']
                                                      ],
                                      buttonStyle=[[ref, 1, '2StateButton'],
                                                   [ref, 2, '2StateButton'],
                                                   [ref, 3, 'pushButton']
                                                   ]
                                      )

                        if not loaded:
                            cmds.treeView(self.ui, e=True, buttonState=(ref, 1, 'buttonDown'))

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


def show(winName=WINDOWNAME, title=WINDOWTITLE, *args):
    if cmds.window(winName, exists=True):
        cmds.deleteUI(winName, wnd=True)

    cmds.window(winName, t=title)
    TreeView()
    cmds.showWindow(winName)
    return
