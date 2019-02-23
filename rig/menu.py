# LANCER.RIG
#
#
#
#
#

# Lancer Modules
import utils
import auto

# Python Modules
from functools import partial

# Maya Modules
from maya import cmds

'''
* Rigging Goals *
- Real-time Speed
- Simple to Use
- Robust

* Rig Structure *

- Global
	- Mesh Group
	- Control Rig
		- Network
		- Skeleton Hierarchy
	- Control Set
	- Geo Cache Set


* Tools *
- Manuel Rig Builder
- Auto Rig Builder
- FKIK Switcher
- Pose Mirror
- Human IK / Mocap
- Retarget & Bake Animation
- Geo Cache Export / Alembic
- FBX Export??
'''


# TODO: Select Joints By Side
# TODO: Mirror Selection
# TODO: Skeleton Validator UI: If there's critical warnings then skeleton is invalid (missing body part).
# TODO: Retargeter UI
# FIXME: Mirror Skeleton Pose
# FIXME: Select non-bind joints

def jointMenuItems():
	cmds.menuItem(d=True, l='Create')
	cmds.menuItem(l='Create Joint', c=utils.createJoint)
	cmds.menuItem(l='Create Bind Joint', c=utils.createBindJoint)
	cmds.menuItem(l='Create Leaf Joint', c=utils.createLeafJoint)
	cmds.menuItem(d=True, l='Select')
	cmds.menuItem(l='Select Joint Hierarchy', c=utils.selectJointHierarchy)
	cmds.menuItem(d=True, l='Edit')
	cmds.menuItem(l='Freeze Transforms', c=utils.freezeTransformSelected)
	cmds.menuItem(l='Zero Orients', c=utils.zeroJointOrientSelected)
	cmds.menuItem(l='Aim At Selected', c=utils.aimAtSelected)
	cmds.menuItem(l='Reposition To Middle', c=utils.repositionMiddleJointSelected)
	cmds.menuItem(l='Remove Segment Scale', c=utils.removeSegmentScaleSelected)
	cmds.menuItem(l='Mirror', c=utils.mirrorJointSelected)
	return


def skeletonMenuItems():
	cmds.menuItem(d=True, l='Hierarchy Selection')
	cmds.menuItem(l='Select Joint Hierarchy', c=utils.selectJointHierarchy)
	# cmds.menuItem(l='Select Non-Bind Joints', c=partial(getSkeletonBindJointsOnSelected, 'joint'))
	cmds.menuItem(l='Select Bind Joints', c=partial(utils.getSkeletonBindJointsOnSelected, 'bind'))
	cmds.menuItem(l='Select Leaf Joints', c=partial(utils.getSkeletonBindJointsOnSelected, 'leaf'))

	cmds.menuItem(d=True, l='Immediate Selection')
	cmds.menuItem(l='Select Immediate Bind Joints', c=partial(utils.immediateBindJointsCallback, True, False))
	cmds.menuItem(l='Select Immediate Leaf Joints', c=partial(utils.immediateBindJointsCallback, False, True))
	cmds.menuItem(l='Select Bind + Leaf Joints', c=partial(utils.immediateBindJointsCallback, True, True))

	cmds.menuItem(d=True, l='Bind Pose')
	cmds.menuItem(l='Restore Bind Pose', c=utils.restoreBindPosePrompt)
	cmds.menuItem(l='Create Bind Pose', c=utils.createBindPosePrompt)

	cmds.menuItem(l='Template', d=True)
	# FIXME Update with new Template class
	cmds.menuItem(l='Validate Skeleton', c=utils.validateSkeletonOnSelected)
	cmds.menuItem(l='Create Template From Labels', c=utils.skeletonSetupCallback)
	cmds.menuItem(l='Import Template', c=utils.importSkeletonCallback)
	cmds.menuItem(l='Export Skeleton', c=utils.exportSkeletonCallback)

	# FIXME: Update. Does not work with current setup
	cmds.menuItem(d=True, l='Template Tools')
	cmds.menuItem(l='Mirror Skeleton Positions', c=utils.mirrorSelectedSkeleton)
	cmds.menuItem(l='Force T-Pose', c=utils.forceTPoseOnSelected)

	cmds.menuItem(d=True, l='Auto Rig')
	autoMenuItems()
	return


# TODO: Consider Using XML instead of json. Smaller file size / faster processing (Low Priority)
def skinMenuItems():
	cmds.menuItem(l='Import Skin Weights', c=utils.importSkinWeights)
	cmds.menuItem(l='Export Skin Weights', c=utils.exportSkinWeights)
	return


def autoMenuItems():
	cmds.menuItem(l='Rig From Labels')
	cmds.menuItem(l='Rig From Definitions', c=auto.autoRigDefinitionsCallback)
	return


def menuItems():
	cmds.menuItem(l='Joint', subMenu=True, to=True)
	jointMenuItems()
	cmds.setParent('..', menu=True)

	cmds.menuItem(l='Skeleton', subMenu=True, to=True)
	skeletonMenuItems()
	cmds.setParent('..', menu=True)

	cmds.menuItem(l='Skin', subMenu=True, to=True)
	skinMenuItems()
	cmds.setParent('..', menu=True)
	return
