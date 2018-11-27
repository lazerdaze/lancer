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
    return False


########################################################################################################################
#
#
#	Delete Redundant
#
#
########################################################################################################################


def deleteRedundant(item, attribute, threshold=None, *args):
    # TODO: Add Threshold
    # TODO: Detect anim layers feature

    if attributeHasAnimation('{}.{}'.format(item, attribute)):
        frames = cmds.keyframe(item, q=1, at=attribute)
        values = cmds.keyframe(item, q=1, at=attribute, vc=1)
        classArray = []
        crushKeys = []

        i = 0
        while i < len(frames):
            newKey = Keyframe(frames[i], values[i])
            classArray.append(newKey)
            i += 1

        i = 1

        while i < (len(classArray) - 1):
            keyA = classArray[i - 1].getValue()
            keyB = classArray[i].getValue()
            keyC = classArray[i + 1].getValue()
            if keyB == keyA and keyB == keyC:
                crushKeys.append(classArray[i].getFrame())
            # else:
            #     if threshold:
            #         if detectThreshold(value=float(keyB),
            #                            prev=float(keyA),
            #                            next=float(keyC),
            #                            threshold=float(threshold)
            #                            ):
            #             crushKeys.append(classArray[i].getFrame())
            i += 1

        for frame in crushKeys:
            cmds.cutKey(item, at=attribute, cl=1, t=(frame, frame))
    return


def deleteAllRedundant(*args):
    selected = cmds.ls(sl=True)

    if selected:
        amount = 0
        maxAmount = len(selected)

        cmds.progressWindow(title='Delete Redundant Keys',
                            progress=amount,
                            max=maxAmount,
                            status='Deleting Keys',
                            isInterruptable=True)

        for item in selected:
            amount += 1
            cmds.progressWindow(edit=True, progress=amount, status='Deleting Keys on: {}'.format(item))

            if cmds.progressWindow(query=True, isCancelled=True):
                break
            else:
                for attr in cmds.listAttr(item, k=True):
                    deleteRedundant(item, attr, 0.001)

        cmds.progressWindow(endProgress=True)
    return
