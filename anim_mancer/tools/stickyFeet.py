#
#
# stickyFeet.py
#
# Install Instructions:
#
# import stickyFeet
# stickyFeet.ui()
#
#

__author__ = 'Justin Tirado'
__version__ = 1.1

import math
from math import *
import collections
from maya import cmds, mel
from maya.api import OpenMaya

########################################################################################################################
#
#
#	Utility Functions, Classes, Global Variables
#
#
########################################################################################################################

WINDOWNAME = 'sfwinUI'
WINDOWLAYOUT = 'sflayUI'
DEBUGMODE = False


def updateDebug(*args):
    global DEBUGMODE
    DEBUGMODE = True if DEBUGMODE is False else False
    print('Sticky Feet Debug Mode: {}'.format(DEBUGMODE))
    return DEBUGMODE


def getDebug(*args):
    global DEBUGMODE
    return DEBUGMODE


def convertStrToList(var, *args):
    var = str(var).replace('[', '').replace(']', '').replace("u'", '').replace("'", '').replace(" ", '').split(',')
    return var


def updateWindowSize(amount, *args):
    winName = WINDOWNAME

    winHeight = cmds.window(winName, q=True, h=True)
    offset = 22

    if amount > 0:
        offset = offset * -1

    winHeight = (winHeight + amount) + offset

    if winHeight > 0:
        cmds.window(winName, e=True, h=winHeight)

    return


def addAttr(item, attr, value=0):
    attrName = '{}.{}'.format(item, attr)
    if cmds.attributeQuery(attr, node=obj, ex=False):
        cmds.addAttr(item, ln='attr', dv=value)
    else:
        cmds.setAttr(attrName, l=False)
        cmds.deleteAttr(attrName)
        cmds.addAttr(item, ln='attr', dv=value)
    return attrName


class intField():
    def __init__(self, value=0, bc=None, *args):
        self.value = value

        self.layout = cmds.rowLayout(nc=3, ad3=2, rat=[1, 'both', -1])
        self.control = cmds.intField(v=self.value, w=60)
        b1 = cmds.button(l='<', c=lambda *x: self.update('remove'))
        b2 = cmds.button(l='>', c=lambda *x: self.update('add'))
        cmds.setParent('..')

        if bc:
            for x in [b1, b2]:
                cmds.button(x, e=True, bgc=bc)

    def get(self, *args):
        return cmds.intField(self.control, q=True, v=True)

    def update(self, typ='add', *args):
        if typ == 'add':
            value = self.get() + 1
        elif typ == 'remove':
            value = self.get() - 1
        cmds.intField(self.control, e=True, v=value)


class textScrollList():
    def __init__(self, bw=None, h=100, bc=None):
        self.layout = cmds.rowLayout(nc=2, ad2=2, h=h, cw=[1, bw], cat=[2, 'left', 5], ct2=['both', 'both'],
                                     rat=[1, 'top', 0])
        cmds.columnLayout(adj=True)
        b1 = cmds.button(l='Add', c=lambda *x: self.add())
        b2 = cmds.button(l='Remove', c=lambda *x: self.remove())
        b3 = cmds.button(l='Clear', c=lambda *x: self.clear())
        cmds.setParent('..')
        self.control = cmds.textScrollList()
        cmds.setParent('..')

        if bc:
            for b in [b1, b2, b3]:
                cmds.button(b, e=True, bgc=bc)

    def selected(self):
        return cmds.textScrollList(self.control, q=True, si=True)

    def add(self):
        selected = getSelected()
        if selected:
            for obj in selected:
                cmds.textScrollList(self.control, e=True, append=obj)
        return

    def remove(self):
        return cmds.textScrollList(self.control, e=True, ri=self.selected())

    def clear(self):
        return cmds.textScrollList(self.control, e=True, ra=True)

    def get(self):
        return cmds.textScrollList(self.control, q=True, ai=True)


class textField():
    def __init__(self, l='Get', value='', bw=None, bc=None, fc=[0.25, 0.25, 0.25]):
        self.value = value
        self.layout = cmds.rowLayout(nc=2, ad2=2, rat=[2, 'both', 0], cat=[2, 'left', 5])
        self.button = cmds.button(l=l, c=lambda *x: self.update())
        form = cmds.formLayout(bgc=fc)
        self.control = cmds.text(l=self.value, al='left')
        cmds.setParent('..')
        cmds.setParent('..')

        cmds.formLayout(form,
                        e=True,
                        attachForm=((self.control, 'left', 5),
                                    (self.control, 'top', 0),
                                    (self.control, 'right', 5),
                                    (self.control, 'bottom', 0)
                                    ),
                        )

        if bw:
            cmds.button(self.button, e=True, w=bw)

        if bc:
            cmds.button(self.button, e=True, bgc=bc)

    def get(self):
        return cmds.text(self.control, q=True, txt=True)

    def update(self):
        selected = getSelected()
        self.value = selected[0] if selected else ''
        cmds.text(self.control, e=True, l=self.value)


class frameLayout():
    global WINDOWNAME

    def __init__(self, label='Frame', bgc=None):
        self.ui = cmds.frameLayout(l=label,
                                   cll=True,
                                   cl=True,
                                   cc=self.close,
                                   ec=self.open,
                                   )

        if bgc:
            cmds.frameLayout(self.ui, e=True, bgc=bgc)

    def __str__(self):
        return str(cmds.layout(self.ui, q=True, fpn=True))

    def open(self):
        self.collapse(False)
        updateWindowSize(cmds.frameLayout(self.ui, q=True, h=True))
        return

    def close(self, skip=False):
        self.collapse(True)
        updateWindowSize(-(cmds.frameLayout(self.ui, q=True, h=True)))
        return

    def collapse(self, value):
        cmds.frameLayout(self.ui, e=True, cl=value)
        return


class radioLayout():
    def __init__(self, label=None, items=None):
        self.label = label
        self.items = items

    def get(self):
        pass


########################################################################################################################
#
#
#	Foot Plant UI & Functions
#
#
########################################################################################################################


ATTRIBUTES = ["translate", "rotate", "scale"]
CHANNELS = ["X", "Y", "Z"]


class UndoChunkContext(object):
    def __enter__(self):
        cmds.undoInfo(openChunk=True)

    def __exit__(self, *exc_info):
        cmds.undoInfo(closeChunk=True)


def getMayaTimeline():
    return mel.eval("$tmpVar=$gPlayBackSlider")


def getFrameRangeFromTimeControl():
    rangeVisible = cmds.timeControl(
        getMayaTimeline(),
        q=True,
        rangeVisible=True
    )

    if not rangeVisible:
        return

    r = cmds.timeControl(
        getMayaTimeline(),
        query=True,
        ra=True
    )
    return [int(r[0]), int(r[-1]) - 1]


def getInvalidAttributes(transform):
    invalidChannels = []
    for attr in ATTRIBUTES:
        # get connection of parent attribute
        node = "{0}.{1}".format(transform, attr)
        if cmds.listConnections(node, destination=False):
            invalidChannels.extend(
                [
                    node + channel
                    for channel in CHANNELS
                    ]
            )
            continue

        # get connection of individual channels
        for channel in CHANNELS:
            node = "{0}.{1}{2}".format(transform, attr, channel)

            # get connections
            animInputs = cmds.listConnections(
                node,
                type="animCurve",
                destination=False
            )
            allInputs = cmds.listConnections(
                node,
                destination=False,
            )

            # check if connections are not of anim curve type
            locked = cmds.getAttr(node, lock=True)
            if (not animInputs and allInputs) or locked:
                invalidChannels.append(node)

    return invalidChannels


def getMatrix(transform, time=None, matrixType="worldMatrix"):
    if not transform:
        return OpenMaya.MMatrix()

    if not time:
        time = cmds.currentTime(query=True)

    rotatePivot = cmds.getAttr("{0}.rotatePivot".format(transform))[0]

    matrix = cmds.getAttr("{0}.{1}".format(transform, matrixType), time=time)
    return OpenMaya.MMatrix(matrix)


def decomposeMatrix(matrix, rotOrder, rotPivot):
    matrixTransform = OpenMaya.MTransformationMatrix(matrix)

    # set pivots
    matrixTransform.setRotatePivot(
        OpenMaya.MPoint(rotPivot),
        OpenMaya.MSpace.kTransform,
        True
    )

    # get rotation pivot translation
    posOffset = matrixTransform.rotatePivotTranslation(
        OpenMaya.MSpace.kTransform
    )

    # get pos values
    pos = matrixTransform.translation(OpenMaya.MSpace.kTransform)
    pos += posOffset
    pos = [pos.x, pos.y, pos.z]

    # get rot values
    euler = matrixTransform.rotation()
    euler.reorderIt(rotOrder)
    rot = [math.degrees(angle) for angle in [euler.x, euler.y, euler.z]]

    # get scale values
    scale = matrixTransform.scale(OpenMaya.MSpace.kTransform)

    return [pos, rot, scale]


def getInTangent(animCurve, time):
    times = cmds.keyframe(animCurve, query=True, timeChange=True) or []
    for t in times:
        if t <= time:
            continue

        tangent = cmds.keyTangent(
            animCurve,
            time=(t, t),
            query=True,
            inTangentType=True
        )

        return tangent[0]

    return "auto"


def getOutTangent(animCurve, time):
    times = cmds.keyframe(animCurve, query=True, timeChange=True) or []
    for t in times:
        if t >= time:
            continue

        tangent = cmds.keyTangent(
            animCurve,
            time=(t, t),
            query=True,
            outTangentType=True
        )

        return tangent[0]

    return "auto"


def applyEulerFilter(transform):
    # get anim curves connected to the rotate attributes
    rotationCurves = []
    for channel in CHANNELS:
        # variables
        node = "{0}.rotate{1}".format(transform, channel)

        # get connected animation curve
        rotationCurves.extend(
            cmds.listConnections(
                node,
                type="animCurve",
                destination=False
            ) or []
        )

    # apply euler filter
    if rotationCurves:
        cmds.filterCurve(*rotationCurves, filter="euler")


def anchorTransform(transform, start, end):
    # wrap in an undo chunk
    with UndoChunkContext():
        # get parent
        rotOrder = cmds.getAttr("{0}.rotateOrder".format(transform))

        # get start matrix
        anchorMatrix = getMatrix(transform, start, "worldMatrix")

        # get invalid attributes
        invalidAttributes = getInvalidAttributes(transform)

        # key frame attributes
        for i in range(start, end + 1):
            # get local matrix
            inverseMatrix = getMatrix(
                transform,
                i,
                "parentInverseMatrix"
            )

            localMatrix = anchorMatrix * inverseMatrix

            # extract transform values from matrix
            rotPivot = cmds.getAttr("{0}.rotatePivot".format(transform))[0]
            transformValues = decomposeMatrix(
                localMatrix,
                rotOrder,
                rotPivot,
            )

            for attr, value in zip(ATTRIBUTES, transformValues):
                for j, channel in enumerate(CHANNELS):
                    # variables
                    node = "{0}.{1}{2}".format(transform, attr, channel)
                    tangents = {
                        "inTangentType": "linear",
                        "outTangentType": "linear"
                    }

                    # skip if its an invalid attribute
                    if node in invalidAttributes:
                        continue

                    # check if input connections are
                    animInputs = cmds.listConnections(
                        node,
                        type="animCurve",
                        destination=False
                    )

                    # adjust tangents
                    if animInputs and i == end:
                        tangents["outTangentType"] = getOutTangent(
                            animInputs[0],
                            end
                        )
                    elif animInputs and i == start:
                        tangents["inTangentType"] = getInTangent(
                            animInputs[0],
                            start
                        )

                    # set key frame
                    cmds.setKeyframe(
                        node,
                        t=i,
                        v=value[j],
                        **tangents
                    )

        # apply euler filter
        applyEulerFilter(transform)


def footPlantUI(label='Foot Plant', padding=10, lc=[.067, .298, .165], bgc=[.114, .494, .271], bc=[.25, 1, .45]):
    ui = frameLayout(label=label, bgc=lc)
    form = cmds.formLayout(bgc=bgc)
    col = cmds.columnLayout(adj=True, rs=padding)
    cmds.text(align='left',
              l="- Select foot control, then PLANT. \n"
                "- Use the Time slider to select frame range.\n"
                "- Works in both local and global space.")

    cmds.separator()

    r1 = cmds.rowLayout(nc=2)
    cmds.text(l='Start:\t')
    iui1 = intField(getTimeRange()[0], bc=bc)
    cmds.setParent('..')
    r2 = cmds.rowLayout(nc=2)
    cmds.text(l='End:\t')
    iui2 = intField(getTimeRange()[0], bc=bc)
    cmds.setParent('..')
    row([r1, r2])

    cmds.button(l='PLANT',
                bgc=bc,
                c=lambda *x: anchorTransform(cmds.ls(sl=True)[0],
                                             iui1.get() if not getFrameRangeFromTimeControl() else
                                             getFrameRangeFromTimeControl()[0],
                                             iui2.get() if not getFrameRangeFromTimeControl() else
                                             getFrameRangeFromTimeControl()[1]))

    cmds.setParent('..')  # column end
    cmds.setParent('..')  # form end
    cmds.setParent('..')  # frame end

    cmds.formLayout(form,
                    e=True,
                    attachForm=((col, 'left', padding),
                                (col, 'top', padding),
                                (col, 'right', padding),
                                (col, 'bottom', padding)
                                )
                    )

    return ui


########################################################################################################################
#
#
#	Bake UI & Functions
#
#
########################################################################################################################


def bakeToWorld(selected=None, globalObject=None, smart=False, *args):
    locList = []
    pcList = []

    start = int(getTimeRange()[0])
    end = int(getTimeRange()[1])
    timeRange = getFrameRangeFromTimeControl()

    if timeRange:
        start = timeRange[0]
        end = timeRange[1]

    # Get Objects
    if not selected:
        cmds.warning('No objects selected.')
    else:
        if globalObject:
            if not cmds.objExists(globalObject):
                cmds.warning('Global Object does not exist in scene.')
            else:

                for obj in selected:
                    loc = createLocatorOnObject(obj)
                    locList.append(loc)

                # Bake Locators
                bakeAnimation(locList, start, end, smart)

                # Delete Keys
                for obj in selected:
                    i = selected.index(obj)
                    deleteKeys(obj)

                    # Parent
                    pc = constraint(locList[i], obj)

                    for x in pc:
                        pcList.append(x)

                # Break From Global
                deleteKeys(globalObject)
                zeroOut(globalObject)

                # Bake Objects
                bakeAnimation(selected, start, end, smart)

                # CleanUp
                cmds.delete(locList, pcList)


def constraint(par, child, *args):
    conList = []
    try:
        conList.append(cmds.pointConstraint(par, child, *args)[0])
    except:
        pass
    try:
        conList.append(cmds.orientConstraint(par, child, *args)[0])
    except:
        pass
    return conList


def getSelected(*args):
    selected = cmds.ls(sl=True)
    return selected if selected else None


def createLocatorOnObject(selected, *args):
    loc = cmds.spaceLocator(n='{}_locator1'.format(selected))[0]
    cmds.parentConstraint(selected, loc)
    return loc


def getTimeRange(*args):
    start = cmds.playbackOptions(q=True, minTime=True)
    end = cmds.playbackOptions(q=True, maxTime=True)
    return [start, end]


def zeroOut(selected, *args):
    for attr in ['t', 'r']:
        for axis in ['x', 'y', 'z']:
            try:
                cmds.setAttr('{}.{}{}'.format(selected, attr, axis), 0)
            except:
                pass


def deleteKeys(selected, *args):
    for attr in ['t', 'r']:
        for axis in ['x', 'y', 'z']:
            for typ in ['TU', 'TL', 'TA']:
                con = cmds.listConnections('{}.{}{}'.format(selected, attr, axis),
                                           s=True,
                                           type='animCurve{}'.format(typ)
                                           )
                if con:
                    try:
                        cmds.delete(con)
                    except:
                        'Delete {}. Skipped'.format(con)


def bakeAnimation(selected, start, end, smart=False, *args):
    if smart:
        cmds.bakeResults(
            selected,
            simulation=True,
            t=(start, end),
            sampleBy=1,
            smart=True,
            disableImplicitControl=True,
            preserveOutsideKeys=True,
            sparseAnimCurveBake=False,
            removeBakedAttributeFromLayer=False,
            removeBakedAnimFromLayer=False,
            bakeOnOverrideLayer=False,
            minimizeRotation=True,
            controlPoints=False,
            shape=False,
        )
    else:
        cmds.bakeResults(
            selected,
            simulation=True,
            t=(start, end),
            sampleBy=1,
            disableImplicitControl=True,
            preserveOutsideKeys=True,
            sparseAnimCurveBake=False,
            removeBakedAttributeFromLayer=False,
            removeBakedAnimFromLayer=False,
            bakeOnOverrideLayer=False,
            minimizeRotation=True,
            controlPoints=False,
            shape=False,
        )


def bakeToolUI(label='Bake To World', padding=10, lc=[.408, .114, .133], bgc=[.455, .125, .149], bc=[1, .28, .25]):
    ui = frameLayout(label=label, bgc=lc)
    form = cmds.formLayout(bgc=bgc)
    col = cmds.columnLayout(adj=True, rs=padding)

    cmds.text(align='left',
              l='- First get Global Object, then select all objects to bake. (IK, COG)')

    cmds.separator()

    tui1 = textField(l='Global Object', bw=80, bc=bc, fc=lc)

    cui1 = cmds.checkBox(l='Smart Bake')
    cmds.button(l='BAKE', bgc=[1, .5, .490],
                c=lambda *x: bakeToWorld(getSelected(), globalObject=cmds.textFieldButtonGrp(tui1, q=True, tx=True),
                                         smart=bool(cmds.checkBox(cui1, q=True, v=True))))
    cmds.setParent('..')  # column end
    cmds.setParent('..')  # form end
    cmds.setParent('..')  # frame end

    cmds.formLayout(form,
                    e=True,
                    attachForm=((col, 'left', padding),
                                (col, 'top', padding),
                                (col, 'right', padding),
                                (col, 'bottom', padding)
                                )
                    )
    return ui


########################################################################################################################
#
#
#	Path Tool UI & Functions
#
#
########################################################################################################################


class cyclePath():
    def __init__(self, curve=None, globalObject=None, name='cyclePath', isDebug=False, *args):
        global DEBUGMODE
        self.curve = curve if curve else None
        self.globalObject = globalObject if globalObject else None
        self.name = name
        self.isDebug = DEBUGMODE if DEBUGMODE else isDebug
        self.nodeList = []
        self.bakeList = []
        self.translateZ = None
        self.start = getTimeRange()[0]
        self.end = getTimeRange()[1]
        self.selected = getSelected()
        self.network = None
        self.null = None
        self.animCurves = {}

        self.getDebugInfo()

    def getDebugInfo(self):
        if self.isDebug:
            print ''
            for x in sorted(vars(self)):
                print '{}: {}'.format(x, vars(self)[x])
            print ''
        return

    def attach(self):
        if not self.curve:
            cmds.warning('No curve selected.')
        else:
            if not self.globalObject:
                cmds.warning('No Global Object selected.')
            else:
                self.createNetwork()
                self.setupGlobalObject()
                self.createPathNetwork(self.curve, self.null[0])
                if self.selected:
                    if self.translateZ:
                        self.createTimewarpNetwork(self.selected, self.curve, self.globalObject)
                    else:
                        print(
                            'No "TranslateZ" animation curves found on "{}". Timewarp skipped'.format(
                                self.globalObject))
                else:
                    print('Timewarp skipped. Nothing selected.')
                self.connectNodesToNetwork()

                cmds.select(self.curve)
        return

    def createNull(self):
        child = cmds.group(n='{}_offset_null#'.format(self.name), em=True)
        parent = cmds.group(child, n='{}_world_null#'.format(self.name))
        cmds.parentConstraint(child, self.globalObject)
        self.null = [child, parent]
        for x in self.null:
            self.nodeList.append(x)
        return

    def connectNullToGlobalObject(self):
        for attr in ['t', 'r']:
            for axis in ['x', 'y', 'z']:
                try:
                    cmds.connectAttr('{}.{}{}'.format(self.null[0], attr, axis),
                                     '{}.{}{}'.format(self.globalObject, attr, axis))
                except:
                    print('Connect to Global Object attribute {}{}. Skipped.'.format(attr, axis))

    def createNetwork(self):
        self.network = cmds.createNode('network', n='{}_network1'.format(self.name))
        return

    def saveExistingAnim(self, selected, network):

        for attr in ['t', 'r']:
            for axis in ['x', 'y', 'z']:
                attrName = '{}.{}{}'.format(selected, attr, axis)
                isKeyable = cmds.getAttr(attrName, k=True)

                if isKeyable:
                    conn = cmds.listConnections(attrName)
                    if conn:
                        for c in conn:
                            if 'animCurve' in cmds.objectType(c) or 'unitConversion' in cmds.objectType(c):
                                if attr == 't' and axis == 'z':
                                    self.translateZ = c

                                cmds.disconnectAttr('{}.output'.format(c),
                                                    '{}.{}{}'.format(selected, attr, axis))
                                cmds.addAttr(network, ln='savedAnim_{}{}'.format(attr, axis))
                                cmds.connectAttr('{}.output'.format(c),
                                                 '{}.savedAnim_{}{}'.format(network, attr, axis), f=True)

    def checkSelected(self):
        if self.selected:
            for x in [self.curve, self.globalObject]:
                if x in self.selected:
                    self.selected.remove(x)
        return

    def setupGlobalObject(self):
        self.checkSelected()
        self.bakeList.append(self.globalObject)
        self.saveExistingAnim(self.globalObject, self.network)

        if self.translateZ:
            self.start = cmds.findKeyframe(self.translateZ, which='first')
            self.end = cmds.findKeyframe(self.translateZ, which='last')

        self.createNull()
        # self.connectNullToGlobalObject()
        return

    def calculateValueCorrection(self):
        endValue = cmds.keyframe(self.translateZ, q=True, t=(self.end, self.end), vc=True)[0]
        return (self.end - self.start) / endValue

    def setOnMotionPath(self, selected, curve, uValue=0):
        # Create Nodes
        mp = cmds.createNode('motionPath', n='{}_mp1'.format(self.name))

        mpAttr = {
            'follow': 1,
            'fractionMode': 1,
            'worldUpType': 3,
            'frontAxis': 2,
            'upAxis': 1,
        }
        for attr in mpAttr:
            cmds.setAttr('{}.{}'.format(mp, attr), mpAttr[attr])

        add = []
        for x in range(3):
            a = cmds.createNode('addDoubleLinear', n='{}_add{}'.format(self.name, x))
            add.append(a)
            self.nodeList.append(a)

        # Make Connections
        cmds.connectAttr('{}.worldSpace[0]'.format(curve), '{}.geometryPath'.format(mp), f=True)
        cmds.connectAttr('{}.rotateOrder'.format(mp), '{}.rotateOrder'.format(selected), f=True)

        i = 0
        for axis in ['x', 'y', 'z']:
            cmds.connectAttr('{}.{}Coordinate'.format(mp, axis), '{}.input2'.format(add[i]), f=True)
            cmds.connectAttr('{}.output'.format(add[i]), '{}.t{}'.format(selected, axis), f=True)
            cmds.connectAttr('{}.r{}'.format(mp, axis), '{}.r{}'.format(selected, axis), f=True)
            cmds.connectAttr('{}.transMinusRotatePivot{}'.format(selected, axis.upper()), '{}.input1'.format(add[i]))
            i += 1

        cmds.setAttr('{0}.uValue'.format(mp), uValue)

        return mp

    def createPathNetwork(self, curve, globalObject, *args):
        cmds.cycleCheck(e=False)
        mp = self.setOnMotionPath(globalObject, curve)
        cmds.addAttr(curve, ln='curveLength', dv=0, k=True)
        for attr in ['uValue', 'frontTwist', 'upTwist', 'sideTwist']:
            try:
                cmds.addAttr(curve, ln=attr, dv=0, k=True)
            except:
                print '{}.{} already exists. Skipped.'.format(curve, attr)
            cmds.connectAttr('{}.{}'.format(curve, attr), '{}.{}'.format(mp, attr), f=True)

        cmds.addAttr(curve, ln='uValueOffset', dv=0, k=True)
        cmds.addAttr(curve, ln='bank', at='bool', k=True)
        cmds.addAttr(curve, ln='bankScale', dv=1, k=True)
        cmds.addAttr(curve, ln='bankLimit', dv=90, k=True)

        for attr in ['bank', 'bankScale', 'bankLimit']:
            cmds.connectAttr('{}.{}'.format(curve, attr), '{}.{}'.format(mp, attr))

        ci = cmds.createNode('curveInfo', name='{}_curveInfo1'.format(self.name))
        curveShape = cmds.listRelatives(curve, shapes=True)
        cmds.connectAttr('{}.worldSpace'.format(curveShape[0]), '{}.inputCurve'.format(ci))

        plus = cmds.createNode('plusMinusAverage', name='{}_sum1'.format(self.name))
        cmds.connectAttr('{}.uValue'.format(curve), '{}.input1D[0]'.format(plus))
        cmds.connectAttr('{}.uValueOffset'.format(curve), '{}.input1D[1]'.format(plus))

        setR = cmds.createNode('setRange', name='{}_range1'.format(self.name))
        cmds.setAttr('{}.maxX'.format(setR), 1)
        cmds.connectAttr('{}.output1D'.format(plus), '{}.valueX'.format(setR))
        cmds.connectAttr('{}.arcLength'.format(ci), '{}.curveLength'.format(curve))
        cmds.connectAttr('{}.curveLength'.format(curve), '{}.oldMaxX'.format(setR))
        cmds.connectAttr('{}.outValueX'.format(setR), '{}.uValue'.format(mp), f=True)
        cmds.setAttr('{}.curveLength'.format(curve), l=True)

        if self.translateZ:
            cmds.connectAttr('{}.output'.format(self.translateZ), '{}.uValue'.format(curve))

        for x in [mp, ci, plus, setR]:
            self.nodeList.append(x)
        return

    def createTimewarpNetwork(self, selected, network, *args):
        cmds.addAttr(network, ln='timeWarpOffset', dv=0, k=True)

        mul = cmds.createNode('multiplyDivide', name='{}_mul1'.format(self.name))
        cmds.connectAttr('{}.uValue'.format(network), '{}.input1X'.format(mul))
        cmds.setAttr('{}.input2X'.format(mul), self.calculateValueCorrection())

        add = cmds.createNode('addDoubleLinear', name='{}_add1'.format(self.name))
        cmds.setAttr('{}.input1'.format(add), self.start)
        cmds.connectAttr('{}.outputX'.format(mul), '{}.input2'.format(add))

        add2 = cmds.createNode('addDoubleLinear', name='{}_add2'.format(self.name))
        cmds.connectAttr('{}.output'.format(add), '{}.input1'.format(add2))
        cmds.connectAttr('{}.timeWarpOffset'.format(network), '{}.input2'.format(add2))

        for obj in selected:
            animCurves = getAnimCurvesFromObject(obj)
            shapes = cmds.listRelatives(obj, shapes=True)
            if shapes:
                for shape in shapes:
                    shapeCurves = getAnimCurvesFromObject(shape)
                    if shapeCurves:
                        for sc in shapeCurves:
                            animCurves.append(sc)
                        self.bakeList.append(shape)
            for anim in animCurves:
                cmds.connectAttr('{}.output'.format(add2), '{}.input'.format(anim))
            self.bakeList.append(obj)

        for x in [mul, add, add2]:
            self.nodeList.append(x)
        return

    def connectNodesToNetwork(self, *args):
        network = self.network
        attrDict = {
            'type': 'cyclePathNetwork',
            'globalObject': self.globalObject,
            'bakeObjects': self.bakeList,
        }
        cmds.addAttr(network, ln='curve', at='message')
        try:
            cmds.addAttr(self.curve, ln='parent', at='message')
        except:
            print '{}.parent already exists. Skipped.'.format(self.curve)

        cmds.connectAttr('{}.curve'.format(network), '{}.parent'.format(self.curve), f=True)
        cmds.connectAttr('{}.parent'.format(self.curve), '{}.curve'.format(network), f=True)

        for attr in attrDict:
            cmds.addAttr(network, ln=attr, dt='string')
            cmds.setAttr('{}.{}'.format(network, attr), attrDict[attr], type='string', lock=True)

        cmds.addAttr(network, ln='nodes', dt='string')
        for node in self.nodeList:
            cmds.addAttr(node, ln='parent', at='message')
            cmds.connectAttr('{}.nodes'.format(network), '{}.parent'.format(node), f=True)

        return

    def getConnected(self, obj, attr, *args):
        name = '{}.{}'.format(obj, attr)
        if cmds.attributeQuery(attr, node=obj, ex=True):

            if cmds.connectionInfo(name, id=True):
                query = cmds.listConnections(cmds.connectionInfo(name, ged=True))[0]
                return query
            else:
                query = cmds.listConnections(name)
                if query:
                    query = query[0]
                    return query

                else:
                    return None
        else:
            return None

    def queryNetwork(self, network):
        # Get global
        if cmds.attributeQuery('globalObject', node=network, ex=True):
            self.globalObject = cmds.getAttr('{}.globalObject'.format(network))

        # Get bake objects
        if cmds.attributeQuery('bakeObjects', node=network, ex=True):
            self.bakeList = convertStrToList(cmds.getAttr('{}.bakeObjects'.format(network)))

        # Get nodes
        if cmds.attributeQuery('nodes', node=network, ex=True):
            self.nodeList = cmds.listConnections('{}.nodes'.format(network))

        # Get saved anim curves
        attrDict = {}
        for attr in cmds.listAttr(network):
            if 'saved' in attr:
                conn = cmds.listConnections('{}.{}'.format(network, attr))
                if conn:
                    attrDict[attr.split('_')[-1]] = conn[0]

        self.animCurves = attrDict

    def detach(self):
        attrs = ['curveLength',
                 'uValue',
                 'frontTwist',
                 'upTwist',
                 'sideTwist',
                 'uValueOffset',
                 'bank',
                 'bankScale',
                 'bankLimit',
                 'timeWarpOffset',
                 'parent']

        if not self.selected:
            cmds.warning('First select a curve. Then DETACH.')
        else:
            for obj in self.selected:
                shape = cmds.listRelatives(obj, shapes=True)
                if shape:
                    if cmds.objectType(shape[0]) == 'nurbsCurve':
                        network = self.getConnected(obj, 'parent')
                        if network:
                            self.queryNetwork(network)

                            if self.animCurves:
                                for anim in self.animCurves:
                                    cmds.connectAttr('{}.output'.format(self.animCurves[anim]),
                                                     '{}.{}'.format(self.globalObject, anim), f=True)
                            try:
                                cmds.delete(network)
                            except:
                                print'Network {} does not exist. Delete skipped.'.format(network)

                            if self.nodeList:
                                for n in self.nodeList:
                                    if cmds.objExists(n):
                                        cmds.delete(n)

                        for attr in attrs:
                            if cmds.attributeQuery(attr, node=obj, ex=True):
                                attrName = '{}.{}'.format(obj, attr)
                                cmds.setAttr(attrName, lock=False)
                                try:
                                    cmds.deleteAttr(attrName)
                                except:
                                    print 'Curve does not have attribute {}. Delete Atrribute Skipped.'.format(attr)


class bakeCyclePath():
    def __init__(self, smart=False, bakeWorld=False, type='cyclePathNetwork', isDebug=True, *args):
        self.type = type
        self.curve = self.getCurve()
        self.network = self.getNetwork()
        self.globalObject = self.getGlobalObject()

        if not self.curve:
            cmds.warning('First select a curve. Then BAKE.')
        else:
            if not self.network:
                cmds.error('Curve does not have a path network.')
            else:
                cmds.cycleCheck(e=True)
                bakeObjects = convertStrToList(cmds.getAttr('{}.bakeObjects'.format(self.network)))
                self.bake(bakeObjects, smart=smart)
                self.cleanup()

    def cleanup(self):
        attrs = ['curveLength',
                 'uValue',
                 'frontTwist',
                 'upTwist',
                 'sideTwist',
                 'uValueOffset',
                 'bank',
                 'bankScale',
                 'bankLimit',
                 'timeWarpOffset',
                 'parent']

        network = self.getConnected(self.curve, 'parent')

        if cmds.attributeQuery('nodes', node=network, ex=True):
            nodeList = cmds.listConnections('{}.nodes'.format(network))
            for node in nodeList:
                try:
                    cmds.delete(node)
                except:
                    print 'Node {} does not exist. Delete Skipped.'.format(node)

        try:
            cmds.delete(network)
        except:
            print 'Network {} does not exist. Delete skipped.'.format(network)

        for attr in attrs:
            if cmds.attributeQuery(attr, node=self.curve, ex=True):
                attrName = '{}.{}'.format(self.curve, attr)
                cmds.setAttr(attrName, lock=False)

                conn = cmds.listConnections(attrName)
                if conn:
                    for c in conn:
                        try:
                            cmds.delete(c)
                        except:
                            print'Delete connection {}. Skipped.'.format(c)

                try:
                    cmds.deleteAttr(attrName)
                except:
                    print 'Curve does not have attribute {}. Delete Atrribute Skipped.'.format(attr)

    def getCurve(self):
        curve = cmds.ls(sl=True)
        curve = curve[0] if curve else None
        return curve

    def getNetwork(self):
        return self.getConnected(self.curve, 'parent') if self.curve else None

    def getGlobalObject(self):
        return cmds.getAttr('{}.globalObject'.format(self.network)) if self.network else None

    def getConnected(self, obj, attr, *args):
        name = '{}.{}'.format(obj, attr)
        if cmds.attributeQuery(attr, node=obj, ex=True):

            if cmds.connectionInfo(name, id=True):
                query = cmds.listConnections(cmds.connectionInfo(name, ged=True))[0]
                return query
            else:
                query = cmds.listConnections(name)
                if query:
                    query = query[0]
                    return query

                else:
                    return None
        else:
            return None

    def bake(self, selected, smart=False, *args):
        # Animation Layer Workaround
        cmds.select(d=True)
        layer = cmds.animLayer('timewarp_bakeLayer1')
        cmds.setAttr('{}.rotationAccumulationMode'.format(layer), 0)
        cmds.setAttr('{}.scaleAccumulationMode'.format(layer), 1)
        cmds.select(selected)
        cmds.animLayer(layer, e=True, addSelectedObjects=True)

        # Bake
        timeRange = getTimeRange()
        if smart:
            cmds.bakeResults(
                selected,
                simulation=True,
                t=(timeRange[0], timeRange[1]),
                sampleBy=1,
                smart=True,
                disableImplicitControl=True,
                preserveOutsideKeys=False,
                sparseAnimCurveBake=False,
                removeBakedAttributeFromLayer=False,
                removeBakedAnimFromLayer=False,
                bakeOnOverrideLayer=False,
                minimizeRotation=True,
                controlPoints=False,
                shape=False,
            )
        else:
            cmds.bakeResults(
                selected,
                simulation=True,
                t=(timeRange[0], timeRange[1]),
                sampleBy=1,
                disableImplicitControl=True,
                preserveOutsideKeys=False,
                sparseAnimCurveBake=False,
                removeBakedAttributeFromLayer=False,
                removeBakedAnimFromLayer=False,
                bakeOnOverrideLayer=False,
                minimizeRotation=True,
                controlPoints=False,
                shape=False,
            )
        # Clean Up
        cmds.delete(layer, 'BaseAnimation')


def createTimeWarpNode(name='timeWarp1', *args):
    node = cmds.createNode('animCurveTT', name=name)
    timeRange = getTimeRange()

    for x in timeRange:
        cmds.setKeyframe(node, t=x, v=x)
        cmds.keyTangent(node, t=(x, x), itt='spline', ott='spline')
        cmds.setAttr('{}.preInfinity'.format(node), 1)
        cmds.setAttr('{}.postInfinity'.format(node), 1)

    return node


def connectTimeWarpToObject(selected, timewarp=None, *args):
    if not timewarp:
        timewarp = createTimeWarpNode()
    animCurves = getAnimCurvesFromObject(selected)
    for anim in animCurves:
        cmds.connectAttr('{}.output'.format(timewarp), '{}.input'.format(anim))
    return


def getAnimCurvesFromObject(selected, *args):
    attrs = cmds.listAttr(selected, k=True)
    print attrs
    animCurveList = []
    if attrs:
        for at in attrs:
            if cmds.attributeQuery(at, node=selected, exists=True):
                conn = cmds.listConnections('{}.{}'.format(selected, at))
                if conn:
                    for c in conn:
                        if 'animCurve' in cmds.objectType(c):
                            animCurveList.append(c)

    return animCurveList


def getConnectedObj(obj, attr, *args):
    name = '{}.{}'.format(obj, attr)

    if cmds.connectionInfo(name, id=True):
        query = cmds.listConnections(cmds.connectionInfo(name, ged=True))[0]
        return query
    else:
        query = cmds.listConnections(name)
        if query:
            query = query[0]
            return query

        else:
            return None


class bankRig():
    def __init__(self, selected=None, name='bankRig'):
        self.name = name
        self.selected = selected
        self.joints = []
        self.curve = None
        self.ik = None
        self.group = None

        if self.selected and len(self.selected) >= 1:
            self.joints = self.createJointChain(self.selected)
            self.curve = self.createCurve(self.joints)
            self.ik = self.createSpline(start=self.joints[0], end=self.joints[-1], curve=self.curve)
            self.group = cmds.group(self.joints[0], self.curve, self.ik, n='{}_group#'.format(self.name))[0]

    def getDistance(self, start, end):
        if type(start) is list:
            startPos = start
        else:
            startPos = cmds.xform(start, q=True, ws=True, rp=True)

        if type(end) is list:
            endPos = end
        else:
            endPos = cmds.xform(end, q=True, ws=True, rp=True)
        distance = sqrt(
            pow((startPos[0] - endPos[0]), 2) + pow((startPos[1] - endPos[1]), 2) + pow((startPos[2] - endPos[2]), 2))
        return distance

    def createJointChain(self, selected, name='joint#'):
        jointList = []
        i = 0
        distance = 0
        cmds.select(d=True)
        for obj in selected:
            if i != 0:
                distance += self.getDistance(selected[i - 1], selected[i])
            jnt = cmds.joint(n='{}_{}'.format(self.name, name))
            cmds.xform(jnt, ws=True, t=[0, 0, distance])
            jointList.append(jnt)
            i += 1
        cmds.select(d=True)
        return jointList

    def createCurve(self, selected, name='curve#', d=1):
        # 1 == Linear / 3 == Curve
        pointList = []
        for obj in selected:
            if type(obj) == str or type(obj) == unicode:
                var = cmds.xform(obj, q=True, ws=True, rp=True)
            elif type(obj) == list:
                var = obj
            pointList.append(var)
        curve = cmds.curve(n='{}_{}'.format(self.name, name), d=d, p=pointList)
        shape = cmds.listRelatives(curve, shapes=True)
        cmds.rename(shape, '{}Shape'.format(curve))
        cmds.xform(curve, cpc=True)
        cmds.rebuildCurve(curve, rt=0, s=len(selected) * (len(selected) * 2), ch=False)
        return curve

    def createSpline(self, start, end, curve):
        return cmds.ikHandle(sj=start, ee=end, sol='ikSplineSolver', ccv=False, c=curve)[0]


def pathToolUI(label='Animation Cycle Path Tool',
               padding=10,
               lc=[.055, .2, .376],
               bgc=[.063, .227, .431],
               bc=[0, .5, 1],
               ):
    ui = frameLayout(label=label, bgc=lc)
    form = cmds.formLayout(bgc=bgc)
    col = cmds.columnLayout(adj=True, rs=padding)
    cmds.text(align='left',
              l='- First get Curve. Then get Global Object.\n'
                '- Select all animated objects and ATTACH for timewarp. (Optional)\n'
                '- Creates new attributes on Curve. Select Curve to BAKE.\n'
                '- Does not work with Animation Curves.')

    cmds.separator()
    tui1 = textField(l='Curve', bw=80, bc=bc, fc=lc)
    tui2 = textField(l='Global Object', bw=80, bc=bc, fc=lc)
    #cmds.separator()
    #frameLayout(label='Advance Quadruped Bank Controls', bgc=bgc)
    #cmds.separator(st='none')
    #bcui1 = textScrollList(bw=80, bc=bc)
    #cmds.button(l='Test', c=lambda *x:bankRig(bcui1.get()))
    #cmds.setParent('..')

    cmds.separator()

    cui1 = cmds.checkBox(l='Smart Bake')
    cui2 = cmds.checkBox(l='Bake Time Warp Only', vis=False)

    bui1 = cmds.button(l='ATTACH',
                       bgc=[0, .5, 1],
                       c=lambda *x: cyclePath(globalObject=tui2.value,
                                              curve=tui1.value
                                              ).attach()
                       )

    bui2 = cmds.button(l='BAKE',
                       bgc=[.25, 1, 1],
                       c=lambda *x: bakeCyclePath(smart=bool(cmds.checkBox(cui1,
                                                                           q=True,
                                                                           v=True)),
                                                  bakeWorld=bool(False)))

    s1 = cmds.separator(st='none', ebg=False)
    bui3 = cmds.button(l='DETACH',
                       bgc=[0, .5, 1],
                       c=lambda *x: cyclePath().detach())

    row([bui1, bui3, s1, bui2])

    cmds.setParent('..')  # column end
    cmds.setParent('..')  # form end
    cmds.setParent('..')  # frame end

    cmds.formLayout(form,
                    e=True,
                    attachForm=((col, 'left', padding),
                                (col, 'top', padding),
                                (col, 'right', padding),
                                (col, 'bottom', padding)
                                )
                    )

    return ui


########################################################################################################################
#
#
#	Menu UI & Functions
#
#
########################################################################################################################

def mayaMotionTrail(selected, *args):
    timeRange = getTimeRange()
    mt = cmds.snapshot(selected,
                       n='{}_motionTrail1'.format(selected),
                       mt=True,
                       i=1,
                       startTime=timeRange[0],
                       endTime=timeRange[1],
                       ch=True,
                       )

    mtShape = cmds.listRelatives(mt[0], shapes=True)[0]

    cmds.setAttr('{}.trailDrawMode'.format(mtShape), 1)
    cmds.setAttr('{}.keyframeSize'.format(mtShape), 0.1)
    return mt


def motionTrailToCurve(selected, *args):
    curve = None
    if cmds.objectType(selected, isType='motionTrailShape'):
        pts = cmds.getAttr('{}.pts'.format(selected))
        ptList = [[p[0], p[1], p[2]] for p in pts]
        curve = cmds.curve(d=3, p=ptList)
    return curve


def curveMotionTrail(selected, *args):
    mt = mayaMotionTrail(selected)[0]
    mtShape = cmds.listRelatives(mt, shapes=True)[0]
    curve = motionTrailToCurve(mtShape)
    cmds.delete(mt)
    return curve


def reverseCurveDirection(*args):
    selected = getSelected()
    if selected:
        for obj in selected:
            shape = cmds.listRelatives(obj, shapes=True)
            if shape:
                shape = shape[0]
                if cmds.objectType(shape, isType='nurbsCurve'):
                    cmds.reverseCurve(obj, ch=False, rpo=True)
    return


def menuUI(*args):
    ui = cmds.menuBarLayout(bgc=[0, 0, 0])
    cmds.menu(l='Curve Tools')
    cmds.menuItem(l='CV Curve Tool', c=lambda *x: mel.eval('CVCurveToolOptions;'))
    cmds.menuItem(l='EP Curve Tool', c=lambda *x: mel.eval('EPCurveToolOptions;'))
    cmds.menuItem(d=True)
    cmds.menuItem(l='Rebuild Curve', c=lambda *x: mel.eval('RebuildCurveOptions;'))
    cmds.menuItem(l='Reverse Curve Direction', c=reverseCurveDirection)
    cmds.menuItem(d=True)
    cmds.menuItem(l='Wire Color', c=lambda *x: mel.eval('objectColorPalette ();'))
    cmds.menu(l='Motion Trail Tools')
    cmds.menuItem(l='Create Maya Motion Trail', c=lambda *x: mayaMotionTrail(getSelected()[0]))
    cmds.menuItem(l='Create Curve Motion Trail', c=lambda *x: curveMotionTrail(getSelected()[0]))
    cmds.menuItem(d=True)
    cmds.menuItem(l='Convert Motion Trail To Curve', c=lambda *x: motionTrailToCurve(getSelected()[0]))
    # cmds.menu(l='Debug')
    # cmds.menuItem(l='Debug Mode', cb=False, c=updateDebug)
    cmds.setParent('..')
    return ui


########################################################################################################################
#
#
#	UI Functions
#
#
########################################################################################################################

def row(items, label='', *args):
    if label:
        rowUI = cmds.rowLayout(nc=2, ad2=2)
        cmds.text(l=label, al='right')

    form = cmds.formLayout(nd=100)
    cmds.setParent('..')

    length = float(len(items))
    step = 100 / length

    i = 0
    for x in items:

        if cmds.control(x, q=True, exists=True):

            x = cmds.control(x, e=True, p=form)

        elif cmds.layout(x, q=True, exists=True):
            x = cmds.layout(x, e=True, p=form)

        if i == 0:
            cmds.formLayout(form, edit=True, attachForm=[(x, 'left', 0), (x, 'top', 0), (x, 'bottom', 0), ],
                            attachPosition=[(x, 'right', 1, step), ], )

        else:
            cmds.formLayout(form, edit=True,
                            attachForm=[(x, 'top', 0), (x, 'bottom', 0), ],
                            attachControl=[(x, 'left', 2, items[i - 1]), ],
                            attachPosition=[(x, 'right', 1, step), ]
                            )

        step += 100 / length
        i += 1

    if label:
        cmds.setParent('..')
        return rowUI

    else:
        return form


def ui(padding=5):
    global WINDOWNAME, WINDOWLAYOUT
    winName = WINDOWNAME
    layName = WINDOWLAYOUT
    winH = 10
    winW = 390

    if cmds.window(winName, q=True, ex=True):
        cmds.deleteUI(winName)

    winPref = cmds.windowPref(winName, exists=True)
    if winPref:
        cmds.windowPref(winName, e=True, h=winH, w=winW)

    cmds.window(winName,
                t='JT Sticky Feet v.{}'.format(__version__),
                s=False,
                rtf=True,
                h=winH,
                w=winW,
                bgc=[.1, .1, .1]
                )

    form = cmds.formLayout()
    menu = menuUI()
    col = cmds.columnLayout(layName, adj=True, rs=padding)
    pathToolUI()
    bakeToolUI()
    footPlantUI()
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.formLayout(form,
                    e=True,
                    attachForm=[[menu, 'left', 0],
                                [menu, 'top', 0],
                                [menu, 'right', 0],
                                [col, 'left', padding],
                                [col, 'bottom', padding],
                                [col, 'right', padding],
                                ],
                    attachControl=[col, 'top', padding, menu],
                    )

    cmds.showWindow(winName)
