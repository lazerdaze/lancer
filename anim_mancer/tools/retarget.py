'''
Reusing code from AXEL
'''


from maya import cmds, mel

ANIMCURVES = ['animCurveTL',
              'animCurveTA',
              'animCurveTT',
              'animCurveTU',
              ]

ANIMLAYERS = ['animBlendNodeAdditive']


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################



def doesAttributeExist(attribute, node=None):
    if '.' in attribute:
        node = attribute.split('.')[0]
        attribute = attribute.split('.')[1]
        return True if cmds.attributeQuery(attribute, node=node, ex=True) else False
    elif node:
        return True if cmds.attributeQuery(attribute, node=node, ex=True) else False
    else:
        return False


def isAnimCurve(node):
    return True if cmds.nodeType(node) in ANIMCURVES else False


def isAnimLayer(node):
    return True if cmds.nodeType(node) in ANIMLAYERS else False


def isAttributeConnected(attribute, node=None):
    if '.' in attribute:
        attrLN = attribute
    else:
        attrLN = '{}.{}'.format(node, attribute)

    if cmds.connectionInfo(attrLN, id=True):
        return cmds.connectionInfo(attrLN, sfd=True)
    else:
        return False


def hasAnimation(attribute, node=None):
    connection = isAttributeConnected(attribute, node)

    if connection:
        connection = connection.split('.')[0]
        if isAnimCurve(connection) or isAnimLayer(connection):
            return connection
    return False


def retarget(namespace):
    controls = []

    for obj in cmds.ls(sl=True):
        target = '{}:{}'.format(namespace, obj.split(':')[-1])
        if cmds.objExists(target):
            controls.append(target)

            for attr in cmds.listAttr(obj, k=True):
                connect = hasAnimation(attr, obj)

                if connect:
                    node = cmds.duplicate(connect)[0]

                    try:
                        cmds.connectAttr('{}.output'.format(node), '{}.{}'.format(target, attr), f=True)
                    except:
                        cmds.delete(node)
        else:
            print '''Target: "{}" does not exist'''.format(target)
    return controls
