from math import *
import maya.cmds as cmds


def listCheck(var):
    if type(var) is str or type(var) is unicode:
        var = [str(var)]
    return var


def snap(par, child, t=False, r=False):
    parPosition = cmds.xform(par, q=True, ws=True, rp=True)
    parRotation = cmds.xform(par, q=True, ws=True, ro=True)
    if t:
        cmds.xform(child, t=parPosition, ws=True)
    if r:
        cmds.xform(child, ro=parRotation, ws=True)
    return


def getSelected():
    selected = cmds.ls(sl=True)
    if not selected:
        cmds.warning('Nothing selected.')
        return None
    return selected


def freezeTransform(obj, t=True, r=True, s=True):
    if t:
        cmds.makeIdentity(obj, apply=True, t=True)
    if r:
        cmds.makeIdentity(obj, apply=True, r=True)
    if s:
        cmds.makeIdentity(obj, apply=True, s=True)
    return


def createJointChain(selected=[], name='bind'):
    selected = listCheck(selected)
    jntList = []
    if not selected:
        return None
    else:
        cmds.select(d=True)
        for obj in selected:
            jntName = '{}_{}_joint#'.format(obj, name)
            jnt = cmds.joint(n=jntName)
            # cmds.setAttr('{}.drawStyle'.format(jnt), 2)
            snap(obj, jnt, t=True, r=True)
            jntList.append(jnt)
            cmds.select(d=True)

        for jnt in jntList:
            i = jntList.index(jnt)
            freezeTransform(jnt)
            if i != 0:
                cmds.parent(jnt, jntList[i - 1])
        return jntList


def createCurve(objects, n='curve_#', d=1):
    # 1 == Linear / 3 == Curve
    pointList = []
    for obj in objects:
        if type(obj) == str or type(obj) == unicode:
            var = cmds.xform(obj, q=True, ws=True, rp=True)
        elif type(obj) == list:
            var = obj
        pointList.append(var)
    curve = cmds.curve(n=n, d=d, p=pointList)
    shape = cmds.listRelatives(curve, shapes=True)
    cmds.rename(shape, '{}Shape'.format(curve))
    return curve

def createSplineIK():
    pass


def getDistance(start, end):
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
