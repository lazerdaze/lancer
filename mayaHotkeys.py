import maya.cmds as cmds
import maya.mel as mel


def hotMove():
    moveQuery = cmds.manipMoveContext('Move', q=True, mode=True) + 2
    if moveQuery > 2:
        moveQuery = 0
    if moveQuery == 0:
        moveName = 'object'
    elif moveQuery == 2:
        moveName = 'world'
    cmds.manipMoveContext('Move', edit=True, mode=moveQuery)
    cmds.headsUpMessage('Move: ' + moveName)


def hotRotate():
    rotateQuery = cmds.manipRotateContext('Rotate', q=True, mode=True) + 1
    if rotateQuery > 1:
        rotateQuery = 0
    if rotateQuery == 0:
        rotateName = 'object'
    elif rotateQuery == 1:
        rotateName = 'world'
    cmds.manipRotateContext('Rotate', edit=True, mode=rotateQuery)
    cmds.headsUpMessage('Rotate: ' + rotateName)


def zeroOut():
    selected = cmds.ls(sl=True)
    if selected:
        for obj in selected:
            for axis in ['x', 'y', 'z']:
                for attr in ['t', 'r', ]:
                    try:
                        cmds.setAttr('{}.{}{}'.format(obj, attr, axis), 0)
                    except:
                        print 'Zero out {}.{}{}. Skipped.'.format(obj, attr, axis)


def keyframeSpecial():
    mel.eval('performSetKeyframeArgList 1 {"0", "animationList"}; keyframe -time `currentTime -q` -tds 1;')
