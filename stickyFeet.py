# Sticky Feet
# Justin Tirado
# v 1.0
#
#
#

'''
# Install Instructions:
import stickyFeet
stickyFeet.ui()

'''

import os
import math
from maya import cmds, mel, OpenMayaUI
from maya.api import OpenMaya


class UndoChunkContext(object):
    """
    The undo context is used to combine a chain of commands into one undo.
    Can be used in combination with the "with" statement.

    with UndoChunkContext():
        # code
    """

    def __enter__(self):
        cmds.undoInfo(openChunk=True)

    def __exit__(self, *exc_info):
        cmds.undoInfo(closeChunk=True)


def getMayaTimeline():
    """
    Get the object name of Maya's timeline.

    :return: Object name of Maya's timeline
    :rtype: str
    """
    return mel.eval("$tmpVar=$gPlayBackSlider")


def getFrameRangeFromTimeControl():
    """
    Get frame range from time control.

    :return: Frame range
    :rtype: list/None
    """
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


def findIcon(icon):
    """
    Loop over all icon paths registered in the XBMLANGPATH environment
    variable ( appending the tools icon path to that list ). If the
    icon exist a full path will be returned.

    :param str icon: icon name including extention
    :return: icon path
    :rtype: str or None
    """
    paths = []

    # get maya icon paths
    if os.environ.get("XBMLANGPATH"):
        paths = os.environ.get("XBMLANGPATH").split(os.pathsep)

    # append tool icon path
    paths.insert(
        0,
        os.path.join(
            os.path.split(__file__)[0],
            "icons"
        )
    )

    # loop all potential paths
    for path in paths:
        filepath = os.path.join(path, icon)
        if os.path.exists(filepath):
            return filepath


ATTRIBUTES = ["translate", "rotate", "scale"]
CHANNELS = ["X", "Y", "Z"]


def getInvalidAttributes(transform):
    """
    Loop over the transform attributes of the transform and see if the
    attributes are locked or connected to anything other than a animation
    curve. If this is the case the attribute is invalid.

    :param str transform: Path to transform
    :return: List of invalid attributes.
    :rtype: list
    """
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
    """
    Get the matrix of the desired matrix type from the transform in a specific
    moment in time. If the transform doesn't exist an empty matrix will be
    returned. If not time is specified, the current time will be used.

    :param str transform: Path to transform
    :param float/int time: Time value
    :param str matrixType: Matrix type to query
    :return: Matrix
    :rtype: OpenMaya.MMatrix
    """
    if not transform:
        return OpenMaya.MMatrix()

    if not time:
        time = cmds.currentTime(query=True)

    rotatePivot = cmds.getAttr("{0}.rotatePivot".format(transform))[0]

    matrix = cmds.getAttr("{0}.{1}".format(transform, matrixType), time=time)
    return OpenMaya.MMatrix(matrix)


def decomposeMatrix(matrix, rotOrder, rotPivot):
    """
    Decompose a matrix into translation, rotation and scale values. A
    rotation order has to be provided to make sure the euler values are
    correct.

    :param OpenMaya.MMatrix matrix:
    :param int rotOrder: Rotation order
    :param list rotPivot: Rotation pivot
    :return: Translate, rotate and scale values
    :rtype: list
    """
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
    """
    Query the in tangent type of the key frame closest but higher than the
    parsed time.

    :param str animCurve: Animation curve to query
    :param int time:
    :return: In tangent type
    :rtype: str
    """
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
    """
    Query the out tangent type of the key frame closest but lower than the
    parsed time.

    :param str animCurve: Animation curve to query
    :param int time:
    :return: Out tangent type
    :rtype: str
    """
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
    """
    Apply an euler filter to fix euler issues on curves connected to the
    transforms rotation attributes.

    :param str transform: Path to transform
    """
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
    """
    Anchor a transform for the parsed time range, ideal to fix sliding feet.
    Function will take into account the in and out tangents in case the
    transform is already animated.

    :param str transform: Path to transform
    :param int start: Start time value
    :param int end: End time value
    """
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
                con = cmds.listConnections(selected, s=True, type='animCurve{}'.format(typ))
                if con:
                    cmds.delete(con)


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


class intField():
    def __init__(self, value=0, *args):
        self.value = value

        self.layout = cmds.rowLayout(nc=3, ad3=2)
        self.control = cmds.intField(v=self.value, w=60)
        cmds.button(l='<', c=lambda *x: self.update('remove'))
        cmds.button(l='>', c=lambda *x: self.update('add'))
        cmds.setParent('..')

    def get(self, *args):
        return cmds.intField(self.control, q=True, v=True)

    def update(self, typ='add', *args):
        if typ == 'add':
            value = self.get() + 1
        elif typ == 'remove':
            value = self.get() - 1
        cmds.intField(self.control, e=True, v=value)


def convertStrToList(var, *args):
    var = str(var).replace('[', '').replace(']', '').replace("u'", '').replace("'", '').replace(" ", '').split(',')
    return var


class cyclePath():
    def __init__(self, curve=None, globalObject=None, name='cyclePath', *args):
        self.curve = curve
        self.globalObject = globalObject
        self.name = name
        self.nodeList = []
        self.bakeList = []
        self.translateZ = None
        self.start = getTimeRange()[0]
        self.end = getTimeRange()[1]
        self.selected = getSelected()

        if not curve:
            cmds.warning('No curve selected.')
        else:
            if not globalObject:
                cmds.warning('No Global Object selected.')
            else:
                self.setupGlobalObject()
                self.createPathNetwork(curve, globalObject)
                if self.selected:
                    if self.translateZ:
                        self.createTimewarpNetwork(self.selected, curve, globalObject)
                    else:
                        cmds.warning(
                            'Timewarp skipped. No "TranslateZ" animation curves on "{}".'.format(self.globalObject))

                else:
                    cmds.warning('Timewarp skipped. Nothing selected.')
                self.connectNodesToNetwork()

    def setupGlobalObject(self):
        self.checkSelected()
        self.bakeList.append(self.globalObject)
        animCurves = getAnimCurvesFromObject(self.globalObject)
        tz = None
        for anim in animCurves:
            if 'translateZ' in anim:
                tz = anim
            else:
                if 'translate' or 'rotate' in anim:
                    cmds.delete(anim)

        if tz:
            cmds.disconnectAttr('{}.output'.format(tz), '{}.translateZ'.format(self.globalObject))
            self.translateZ = tz
            self.start = cmds.findKeyframe(self.translateZ, which='first')
            self.end = cmds.findKeyframe(self.translateZ, which='last')

    def calculateValueCorrection(self):
        endValue = cmds.keyframe(self.translateZ, q=True, t=(self.end, self.end), vc=True)[0]
        return (self.end - self.start) / endValue

    def createPathNetwork(self, curve, globalObject, *args):
        cmds.cycleCheck(e=False)
        mp = setOnMotionPath(globalObject, curve)
        cmds.addAttr(curve, ln='curveLength', dv=0, k=True)
        for attr in ['uValue', 'frontTwist', 'upTwist', 'sideTwist']:
            try:
                cmds.addAttr(curve, ln=attr, dv=0, k=True)
            except:
                pass
            cmds.connectAttr('{}.{}'.format(curve, attr), '{}.{}'.format(mp, attr), f=True)

        cmds.addAttr(curve, ln='uValueOffset', dv=0, k=True)
        cmds.addAttr(curve, ln='bank', at='bool', k=True)
        cmds.addAttr(curve, ln='bankScale', dv=1, k=True)
        cmds.addAttr(curve, ln='bankLimit', dv=90, k=True)

        for attr in ['bank', 'bankScale', 'bankLimit']:
            cmds.connectAttr('{}.{}'.format(curve, attr), '{}.{}'.format(mp, attr))

        ci = cmds.createNode('curveInfo')
        curveShape = cmds.listRelatives(curve, shapes=True)
        cmds.connectAttr('{}.worldSpace'.format(curveShape[0]), '{}.inputCurve'.format(ci))

        plus = cmds.createNode('plusMinusAverage')
        cmds.connectAttr('{}.uValue'.format(curve), '{}.input1D[0]'.format(plus))
        cmds.connectAttr('{}.uValueOffset'.format(curve), '{}.input1D[1]'.format(plus))

        setR = cmds.createNode('setRange')
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

    def checkSelected(self):
        if self.selected:
            for x in [self.curve, self.globalObject]:
                if x in self.selected:
                    self.selected.remove(x)

    def createTimewarpNetwork(self, selected, network, *args):
        cmds.addAttr(network, ln='timeWarpOffset', dv=0, k=True)

        mul = cmds.createNode('multiplyDivide')
        cmds.connectAttr('{}.uValue'.format(network), '{}.input1X'.format(mul))
        cmds.setAttr('{}.input2X'.format(mul), self.calculateValueCorrection())

        add = cmds.createNode('addDoubleLinear')
        cmds.setAttr('{}.input1'.format(add), self.start)
        cmds.connectAttr('{}.outputX'.format(mul), '{}.input2'.format(add))

        add2 = cmds.createNode('addDoubleLinear')
        cmds.connectAttr('{}.output'.format(add), '{}.input1'.format(add2))
        cmds.connectAttr('{}.timeWarpOffset'.format(network), '{}.input2'.format(add2))

        for obj in selected:
            animCurves = getAnimCurvesFromObject(obj)
            for anim in animCurves:
                cmds.connectAttr('{}.output'.format(add2), '{}.input'.format(anim))
            self.bakeList.append(obj)

        for x in [mul, add, add2]:
            self.nodeList.append(x)
        return

    def connectNodesToNetwork(self, *args):
        network = cmds.createNode('network', n='{}_cyclePathNetwork1'.format(self.curve))
        attrDict = {
            'type': 'cyclePathNetwork',
            'globalObject': self.globalObject,
            'bakeObjects': self.bakeList,
        }
        cmds.addAttr(network, ln='curve', at='message')
        try:
            cmds.addAttr(self.curve, ln='parent', at='message')
        except:
            pass

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


class bakeCyclePath():
    def __init__(self, smart=False, bakeWorld=False, type='cyclePathNetwork', isDebug=True, *args):
        self.type = type
        self.curve = self.getCurve()
        self.network = self.getNetwork()
        self.globalObject = self.getGlobalObject()

        if not self.curve:
            cmds.warning('No curve selected.')
        else:
            if not self.network:
                cmds.error('Curve does not have a path network.')
            else:
                cmds.cycleCheck(e=True)
                bakeObjects = convertStrToList(cmds.getAttr('{}.bakeObjects'.format(self.network)))
                self.bake(bakeObjects, smart=smart)
                if bakeWorld:
                    if not self.globalObject:
                        cmds.warning('No Global Object in path network.')
                    else:
                        bakeObjects.remove(self.globalObject)
                        if bakeObjects:
                            bakeToWorld(selected=bakeObjects, globalObject=self.globalObject, smart=smart)

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
    animCurveList = []
    for at in attrs:
        # anim = getConnectedObj(selected, at)
        anim = cmds.listConnections('{}.{}'.format(selected, at))
        if anim:
            if 'animCurve' in cmds.objectType(anim[0]):
                animCurveList.append(anim[0])

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


def setOnMotionPath(selected, curve, name='motionPath', uValue=0, *args):
    # Create Nodes
    mp = cmds.createNode('motionPath', n='{}_mp'.format(name))

    mpAttr = {'follow': 1,
              'fractionMode': 1,
              'worldUpType': 3,
              'frontAxis': 2,
              'upAxis': 1,
              }
    for attr in mpAttr:
        cmds.setAttr('{}.{}'.format(mp, attr), mpAttr[attr])

    add = []
    for x in range(3):
        a = cmds.createNode('addDoubleLinear', n='{}_add{}'.format(name, x))
        add.append(a)

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


def pathToolUI():
    cmds.frameLayout(l='Animation Cycle Path Tool', bgs=True, mw=10, mh=10, bgc=[0, 0, 0])
    cmds.text(
        l='First get Curve. Then get Global Object. \n '
          'Select all animated objects and attach for timewarp. (Optional)\n '
          'Creates new attributes on Curve. Select Curve to bake.')

    tui1 = cmds.textFieldButtonGrp(ad2=1, ed=False, bl='      Curve      ',
                                   bc=lambda *x: cmds.textFieldButtonGrp(tui1, e=True,
                                                                         tx=cmds.ls(sl=True)[0] if cmds.ls(
                                                                             sl=True) else ''))
    tui2 = cmds.textFieldButtonGrp(ad2=1, ed=False, bl='Global Object',
                                   bc=lambda *x: cmds.textFieldButtonGrp(tui2, e=True,
                                                                         tx=cmds.ls(sl=True)[0] if cmds.ls(
                                                                             sl=True) else ''))
    cui1 = cmds.checkBox(l='Smart Bake')
    cui2 = cmds.checkBox(l='Bake To World', vis=False)
    row([cui1, cui2])

    bui1 = cmds.button(l='ATTACH',
                       bgc=[0, .5, 1],
                       c=lambda *x: cyclePath(globalObject=cmds.textFieldButtonGrp(tui2,
                                                                                   q=True,
                                                                                   tx=True),
                                              curve=cmds.textFieldButtonGrp(tui1,
                                                                            q=True,
                                                                            tx=True)
                                              )
                       )

    bui2 = cmds.button(l='BAKE',
                       bgc=[.25, 1, 1],
                       c=lambda *x: bakeCyclePath(smart=bool(cmds.checkBox(cui1,
                                                                           q=True,
                                                                           v=True)),
                                                  bakeWorld=bool(cmds.checkBox(cui2,
                                                                               q=True,
                                                                               v=True))))
    row([bui1, bui2])
    cmds.setParent('..')


def motionTrailToCurve(selected, *args):
    if cmds.objectType(selected, isType='motionTrailShape'):
        pts = cmds.getAttr('{}.pts'.format(selected))
        ptList = [[p[0], p[1], p[2]] for p in pts]
        cmds.curve(d=3, p=ptList)
    return


def menuUI(*args):
    cmds.menuBarLayout()
    cmds.menu(l='Extras')
    cmds.menuItem(l='Rebuild Curve', c= lambda *x: mel.eval('RebuildCurveOptions;'))
    cmds.menuItem(l='Curve from Motion Trail', c= lambda *x: motionTrailToCurve(getSelected()[0]))
    cmds.setParent('..')
    return


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


def ui(*args):
    winName = 'bltwUI'

    if cmds.window(winName, q=True, ex=True, w=100, h=100):
        cmds.deleteUI(winName)

    cmds.window(winName, t='JT Sticky Feet')

    cmds.frameLayout(lv=False, mw=2, mh=2)
    menuUI()

    cmds.columnLayout(adj=True)

    pathToolUI()
    cmds.separator(st='none', h=10, ebg=False)

    cmds.frameLayout(l='Bake To World', bgs=True, mw=10, mh=10, bgc=[0, 0, 0])
    cmds.columnLayout(adj=True)
    cmds.text(l='First get Global Object, then select all objects to bake.')
    cmds.separator(st='none', h=10, ebg=False)
    tui1 = cmds.textFieldButtonGrp(ad2=1, ed=False, bl='Global Object',
                                   bc=lambda *x: cmds.textFieldButtonGrp(tui1, e=True,
                                                                         tx=cmds.ls(sl=True)[0] if cmds.ls(
                                                                             sl=True) else ''))
    cmds.separator(st='none', h=10, ebg=False)
    cui1 = cmds.checkBox(l='Smart Bake')
    cmds.separator(st='none', h=10, ebg=False)
    cmds.button(l='BAKE', bgc=[1, .25, .45],
                c=lambda *x: bakeToWorld(getSelected(), globalObject=cmds.textFieldButtonGrp(tui1, q=True, tx=True),
                                         smart=bool(cmds.checkBox(cui1, q=True, v=True))))
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.separator(st='none', h=10, ebg=False)

    cmds.frameLayout(l='Foot Plant', bgs=True, mw=10, mh=10, bgc=[0, 0, 0])
    cmds.columnLayout(adj=True)
    cmds.text(
        l="Select foot control, set start and end frame, then plant. \n "
          "Time slider selection works.\n "
          "Works in local and global space.")
    
    cmds.separator(st='none', h=10, ebg=False)
    r1 = cmds.rowLayout(nc=2)
    cmds.text(l='Start:\t')
    iui1 = intField(getTimeRange()[0])
    cmds.setParent('..')
    r2 = cmds.rowLayout(nc=2)
    cmds.text(l='End:\t')
    iui2 = intField(getTimeRange()[0])
    cmds.setParent('..')
    row([r1, r2])
    cmds.separator(st='none', h=10, ebg=False)
    cmds.button(l='PLANT', bgc=[.25, 1, .45], c=lambda *x: anchorTransform(cmds.ls(sl=True)[0],
                                                                           iui1.get() if not getFrameRangeFromTimeControl() else
                                                                           getFrameRangeFromTimeControl()[0],
                                                                           iui2.get() if not getFrameRangeFromTimeControl() else
                                                                           getFrameRangeFromTimeControl()[1]))

    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.showWindow(winName)
