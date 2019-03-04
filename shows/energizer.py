# Maya Modules
from maya import cmds

# Globals
WHITE_LIST = ['joint',
              'transform',
              'locator'
              ]

ENERGIZER_HANDLER = {'C_mouth_BONES': 'head1_head',
                     'R_strap_BONES': 'spine1_hiResSpine4',
                     'L_strap_BONES': 'spine1_hiResSpine4',
                     'L_sandalStrap_BONES': 'leftLeg1_HiResFoot',
                     'R_sandalStrap_BONES': 'rightLeg1_HiResFoot',
                     'L_brow_BONES': 'head1_head',
                     'R_brow_BONES': 'head1_head',
                     'battery_GRP': 'R_knee_02_JNT',
                     }

ENERGIZER_WHITE_LIST = ['C_mouth_BONES',
                        'R_strap_BONES',
                        'L_strap_BONES',
                        'L_sandalStrap_BONES',
                        'R_sandalStrap_BONES',
                        'L_brow_BONES',
                        'R_brow_BONES',
                        'battery_GRP',
                        ]


# Utilities
def getNodeType(node, *args, **kwargs):
    return cmds.nodeType(node)


def nodeExists(node):
    return cmds.objExists(node)


def getAllJointsFromRoot(root, *args, **kwargs):
    return cmds.listRelatives(root, ad=True, type='joint')


def getAllDecendantsFromRoot(root, *args, **kwargs):
    return cmds.listRelatives(root, ad=True)


def getAllDecendantsFromWhiteList(root, *args, **kwargs):
    return [node for node in getAllDecendantsFromRoot(root) if getNodeType(node) in WHITE_LIST]


def bakeAnimation(nodes, startFrame, endFrame, *args, **kwargs):
    cmds.bakeResults(
        nodes,
        simulation=True,
        t=(startFrame, endFrame),
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
    return


def bakeRig(rootJoint='TSMGWorldJoint',
            rootModel='model_GRP',
            blackList=None,
            whiteList=None,
            *args,
            **kwargs
            ):
    blackListDefaults = ['TSMG_Cruft', 'TSMG_root']

    if blackList:
        if isinstance(blackList, str):
            blackList = [blackList] + blackListDefaults

        elif isinstance(blackList, list):
            blackList = blackList + blackListDefaults
    else:
        blackList = blackListDefaults

    # Edge Cases
    for node in [rootJoint, rootModel]:
        if not nodeExists(rootJoint):
            raise RuntimeError('Node "{}" does not exist.'.format(node))

    # Time Range
    startFrame = cmds.playbackOptions(q=True, minTime=True)
    endFrame = cmds.playbackOptions(q=True, maxTime=True)

    # Bake Animation
    bakeList = []

    if whiteList:
        if isinstance(whiteList, str):
            whiteList = [rootJoint, whiteList]

        elif isinstance(whiteList, list):
            whiteList = [rootJoint] + whiteList

        elif isinstance(whiteList, (tuple, dict)):
            whiteList = [rootJoint]

            for item in whiteList:
                whiteList.append(item)
    else:
        whiteList = [rootJoint]

    for node in whiteList:
        children = getAllDecendantsFromWhiteList(node)

        if children:
            for child in children:
                if children not in bakeList:
                    print child
                    bakeList.append(child)

    # bakeAnimation(bakeList, startFrame, endFrame)

    ## Reparent Hierarchy
    # for node in [rootJoint, rootModel]:
    #     cmds.parent(node, world=True)
    #
    # # Delete Hierarchy
    # allDescendants = getAllDecendantsFromRoot(rootJoint)
    #
    # for node in allDescendants:
    #     if nodeExists(node):
    #         if getNodeType(node) not in WHITE_LIST:
    #             cmds.delete(node)
    #
    # if blackList:
    #     for node in blackList:
    #         if nodeExists(node):
    #             cmds.delete(node)
    return


def handleRig(handler, *args, **kwargs):
    if not isinstance(handler, dict):
        raise TypeError('Handler must be dict.')

    for item in handler:
        parent = handler[item]
        try:
            cmds.parent(item, parent)
        except RuntimeError:
            print 'Unable to "{}" to "{}".'.format(item, parent)

    return


# bakeRig(whiteList=ENERGIZER_HANDLER)
# handleRig(ENERGIZER_HANDLER)

def unrealConstraint(root='TSMGWorldJoint', prefix='unreal'):
    for parent in [root] + getAllJointsFromRoot(root):
        child = '{}_{}'.format(prefix, parent)

        if nodeExists(child):
            cmds.parentConstraint(parent, child, mo=True)
            cmds.scaleConstraint(parent, child, mo=True)
        else:
            print 'Node "{}" does not exists. Skipped.'.format(child)
    return


def unrealBake(root='unreal_TSMGWorldJoint'):
    # Time Range
    startFrame = cmds.playbackOptions(q=True, minTime=True)
    endFrame = cmds.playbackOptions(q=True, maxTime=True)

    # Bake Animation
    bakeList = [root] + getAllJointsFromRoot(root)
    bakeAnimation(bakeList, startFrame, endFrame)

    # Delete Hierarchy
    allDescendants = getAllDecendantsFromRoot(root)

    for node in allDescendants:
        if nodeExists(node):
            if getNodeType(node) != 'joint':
                cmds.delete(node)
    return
