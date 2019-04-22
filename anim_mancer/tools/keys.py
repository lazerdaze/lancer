# LANCER.CHANNELBOX.KEYS
#
#
#
#
#

# Maya Modules
from maya import cmds


########################################################################################################################
#
#
#	Keyframe Class
#
#
########################################################################################################################

class Keyframe(object):
    def __init__(self, frame, value):
        self.frame = frame
        self.value = value

    def getFrame(self):
        return self.frame

    def getValue(self):
        return self.value


########################################################################################################################
#
#
#	Utilities
#
#
########################################################################################################################
def attributeHasAnimation(attribute):
    if cmds.connectionInfo(attribute, id=True):
        node = cmds.connectionInfo(attribute, sfd=True)
        if cmds.nodeType(node) in ['animCurveTL', 'animCurveTA', 'animCurveTT', 'animCurveTU', ]:
            return True
    return False


def attributeHasAnimLayer(attribute):
    return


def detectThreshold(value, prev, next, threshold):
    if prev < value < next or prev > value > next:
        if next > value <= prev + threshold:
            return True
        elif next < value >= prev - threshold:
            return True
        elif prev > value <= next + threshold:
            return True
        elif prev < value >= next - threshold:
            return True
        else:
            return False
    else:
        return False


def detectTrajectory(value, prev, next):
    if prev < value < next:
        midPoint = (next - prev) / 2 + prev
        if value == midPoint:
            return True
        else:
            return False
    elif prev > value > next:
        midPoint = (prev - next) / 2 - prev
        if value == midPoint:
            return True
        else:
            return False
    else:
        return False


def deleteKeysDecorator(function, *args, **kwargs):
    '''
    Delete Keys on selected objects based on function.
    Function must return bool (current, prev, next).
    :param function:
    :param args:
    :param kwargs:
    :return:
    '''

    def wrapper(*args, **kwargs):
        selected = cmds.ls(sl=True)

        if selected:
            for item in selected:
                for attr in cmds.listAttr(item, k=True):
                    attribute = '{}.{}'.format(item, attr)

                    if attributeHasAnimation(attribute):
                        frames = cmds.keyframe(item, q=1, at=attr)
                        values = cmds.keyframe(item, q=1, at=attr, vc=1)
                        classArray = []
                        crushKeys = []

                        i = 0
                        while i < len(frames):
                            classArray.append(Keyframe(frames[i], values[i]))
                            i += 1

                        i = 1
                        while i < (len(classArray) - 1):
                            keyA = classArray[i - 1].getValue()
                            keyB = classArray[i].getValue()
                            keyC = classArray[i + 1].getValue()

                            if function(keyB, keyA, keyC, *args, **kwargs):
                                crushKeys.append(classArray[i].getFrame())
                            i += 1

                        for frame in crushKeys:
                            cmds.cutKey(item, at=attr, cl=1, t=(frame, frame))
    return wrapper


########################################################################################################################
#
#
#	Delete Static Channels
#
#
########################################################################################################################

def deleteStaticAllChannels(*args, **kwargs):
    cmds.delete(all=True, staticChannels=True)
    return


########################################################################################################################
#
#
#	Delete Redundant
#
#
########################################################################################################################

# TODO: Add Trajectory
# TODO: Add Threshold
# TODO: Detect anim layers feature

@deleteKeysDecorator
def deleteRedundant(current, prev, next, *args, **kwargs):
    if current == prev and current == next:
        return True
    else:
        return False
