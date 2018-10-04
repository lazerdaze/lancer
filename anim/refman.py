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

    def getAssembly(self):
        return self.assembly


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

        cmds.menu(label='Visibility')
        cmds.menuItem(label='Show All', c=lambda *x: self.toggleAssembly(True))
        cmds.menuItem(label='Hide All', c=lambda *x: self.toggleAssembly(False))
        # cmds.menu(label='Extras', enable=False)
        # cmds.menuItem(label='Show All')
        # cmds.menuItem(label='Hide All')

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

        # ScriptJobs
        cmds.scriptJob(p=self.ui, event=['PostSceneRead', self.load])

    def isAssemblyVisibile(self, assembly, *args):
        var = []
        for a in assembly:
            if cmds.objExists(a):
                var.append(cmds.getAttr('{}.v'.format(a)))
        if var:
            if sum(var) >= float(len(var)) / 2.0:
                return True
            else:
                return False
        else:
            return False

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
        self.items[name].namespace = cmds.referenceQuery(name, namespace=True)[1:]
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
            itemData.assembly = [x for x in getAllTopLevelNodes() if x.split(':')[0] == itemData.namespace]
            try:
                itemData.namespace = cmds.referenceQuery(item, namespace=True)[1:]
            except:
                itemData.namespace = None
        return

    def unloadAllReferences(self, *args):
        loadAllReferences(False)
        for item in self.items:
            cmds.treeView(self.ui, e=True, buttonState=(item, 1, 'buttonDown'))
            self.items[item].loaded = False
        return

    def toggleAssembly(self, var, *args):
        for item in self.items:
            cmds.treeView(self.ui, e=True, buttonState=(item, 2, 'buttonUp' if var else 'buttonDown'))
            itemData = self.items[item]
            itemData.visibility = var
            assembly = itemData.assembly

            for a in assembly:
                try:
                    cmds.setAttr('{}.v'.format(a), var)
                except:
                    pass
        return

    def open(self, *args):
        openFile(loaded=self.loadReferencesOnOpen)
        self.load()
        return

    def getUI(self):
        return self.layout

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

                        try:
                            namespace = cmds.referenceQuery(ref, namespace=True)[1:]
                        except:
                            namespace = None

                        assembly = [x for x in getAllTopLevelNodes() if x.split(':')[0] == namespace]

                        loaded = isReferenceLoaded(ref)
                        sets = [x for x in getAllSets() if x.split(':')[0] == namespace]

                        controlSet = '{}:CONTROLS'.format(namespace)
                        controls = cmds.sets(controlSet, q=True) if cmds.objExists(controlSet) else None

                        isVisible = self.isAssemblyVisibile(assembly) if assembly else True

                        # Item Class
                        self.items[ref] = Item(name=ref,
                                               reference=ref,
                                               namespace=namespace,
                                               assembly=assembly,
                                               loaded=loaded,
                                               filepath=referenceFilepath(ref),
                                               controls=controls,
                                               sets=sets,
                                               visibility=isVisible,
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
                        if not isVisible:
                            cmds.treeView(self.ui, e=True, buttonState=(ref, 2, 'buttonDown'))
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
#	UI
#
#
########################################################################################################################


def ui():
    return TreeView().getUI()


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
    ui()
    cmds.showWindow(winName)
    return
