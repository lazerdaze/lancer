# LANCER.RIG
#
#
#
#
#

# Lancer
from utils import *

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


def jointMenuItems():
	cmds.menuItem(d=True, l='Create')
	cmds.menuItem(l='Create Joint', c=createJoint)
	cmds.menuItem(l='Create Bind Joint', c=createBindJoint)
	cmds.menuItem(l='Create Leaf Joint', c=createLeafJoint)
	cmds.menuItem(d=True, l='Select')
	cmds.menuItem(l='Select Joint Hierarchy', c=selectJointHierarchy)
	cmds.menuItem(d=True, l='Edit')
	cmds.menuItem(l='Freeze Transforms', c=freezeTransformSelected)
	cmds.menuItem(l='Zero Orients', c=zeroJointOrientSelected)
	cmds.menuItem(l='Aim At Selected', c=aimAtSelected)
	cmds.menuItem(l='Reposition To Middle', c=repositionMiddleJointSelected)
	cmds.menuItem(l='Remove Segment Scale', c=removeSegmentScaleSelected)
	cmds.menuItem(l='Mirror', c=mirrorJointSelected)
	return


# TODO: Select Joints By Side
# TODO: Mirror Selection
def skeletonMenuItems():
	cmds.menuItem(l='Select Skeleton Hierarchy', c=selectJointHierarchy)
	cmds.menuItem(l='Select Non-Bind Joints', c=lambda *x: getSkeletonBindJointsOnSelected('joint'))
	cmds.menuItem(l='Select Bind Joints', c=lambda *x: getSkeletonBindJointsOnSelected('bind'))
	cmds.menuItem(l='Select Leaf Joints', c=lambda *x: getSkeletonBindJointsOnSelected('leaf'))
	cmds.menuItem(d=True, l='Relationships')
	cmds.menuItem(l='Create Skeleton Network From Labels', c=createSkeletonNetwork)
	cmds.menuItem(d=True, l='Bind Pose')
	cmds.menuItem(l='Restore Bind Pose', c=restoreBindPosePrompt)
	cmds.menuItem(l='Create Bind Pose', c=createBindPosePrompt)
	cmds.menuItem(l='Template', d=True)
	cmds.menuItem(l='Validate Skeleton', c=validateSkeletonOnSelected)
	cmds.menuItem(l='Import Template', c=importTemplate)
	cmds.menuItem(l='Export Template', c=exportTemplate)
	# cmds.menuItem(d=True)
	# cmds.menuItem(l='Import Biped (Simple)', c=importTemplate)
	# cmds.menuItem(l='Import Biped (Advanced)', c=importTemplate, enable=False)
	# cmds.menuItem(l='Import Quadruped (Simple)', c=importTemplate)
	# cmds.menuItem(l='Import Quadruped (Advanced)', c=importTemplate, enable=False)
	cmds.menuItem(d=True, l='Template Only')
	cmds.menuItem(l='Mirror Skeleton Positions', c=mirrorSelectedSkeleton)
	cmds.menuItem(l='Force T-Pose', c=forceTPoseOnSelected)
	return


def skinMenuItems():
	cmds.menuItem(l='Import Skin Weights', c=importSkinWeights)
	cmds.menuItem(l='Export Skin Weights', c=exportSkinWeights)
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
