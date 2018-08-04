# LANCER.RIG.AUTO
#
#
#
#
#

# Lancer Modules
import parts
import naming
import skeleton
import bodyPart

reload(parts)
reload(naming)
reload(skeleton)
reload(bodyPart)

# Python Modules
import json

# Maya Modules
from maya import cmds, mel


#########################################################################################################################
#																														#
#																														#
#	Query    																								        #
#																														#
#																														#
#########################################################################################################################

def queryLabels(root):
	tree = {}
	children = skeleton.getAllJointChildren(root)

	for label in skeleton.MAYAJOINTLABELS + [naming.component.cog.capitalize()]:
		tree[label] = {
			naming.side.center: None,
			naming.side.left  : None,
			naming.side.right : None,
		}

	for child in sorted(children + [root]):
		label = skeleton.getJointLabel(child)
		side = label[0]
		typ = label[1]

		if typ.lower() not in [naming.rig.bind, naming.rig.rig]:
			if side and typ and typ in tree:
				key = tree[str(typ)][str(side)]
				if key is None:
					tree[str(typ)][str(side)] = str(child)
	return tree


#########################################################################################################################
#																														#
#																														#
#	Auto Rig Functions  																								        #
#																														#
#																														#
#########################################################################################################################


def rigFromTemplate(*args):
	root = parts.ROOT(root='CenterRoot')

	cog = parts.COG(cog='CenterCOG',
	                hip='CenterHip',
	                networkRoot=root.network,
	                )
	spine = parts.SPINE(objects=['CenterSpine0', 'CenterSpine1', 'CenterSpine2', ],
	                    networkRoot=root.network)

	neck = parts.NECK(objects=['CenterNeck0'], networkRoot=root.network)
	head = parts.HEAD(head='CenterHead', networkRoot=root.network)

	armL = parts.ARM(side=naming.side.left,
	                 collar='LeftArmCollar',
	                 shoulder='LeftArmShoulder',
	                 elbow='LeftArmElbow',
	                 hand='LeftArmHand',
	                 networkRoot=root.network,
	                 )
	armR = parts.ARM(side=naming.side.right,
	                 collar='RightArmCollar',
	                 shoulder='RightArmShoulder',
	                 elbow='RightArmElbow',
	                 hand='RightArmHand',
	                 networkRoot=root.network,
	                 )

	legL = parts.LEG(side='Left',
	                 hip='LeftLegHip',
	                 knee='LeftLegKnee',
	                 foot='LeftLegFoot',
	                 toe='LeftLegToe',
	                 networkRoot=root.network,
	                 )

	legR = parts.LEG(side='Right',
	                 hip='RightLegHip',
	                 knee='RightLegKnee',
	                 foot='RightLegFoot',
	                 toe='RightLegToe',
	                 networkRoot=root.network,
	                 )
	cmds.select(d=True)
	return


def rigFromLabels(root, *args):
	tree = queryLabels(root)

	centerRoot = None
	rootNode = None
	centerCog = None
	cogNode = None
	centerHip = None
	centerSpine = None
	centerNeck = None
	centerHead = None

	leftArm = None
	rightArm = None

	leftLeg = None
	rightLeg = None

	# print json.dumps(tree, indent=2)
	# Root
	try:
		centerRoot = tree[naming.component.root.capitalize()][naming.side.center]
		rootNode = bodyPart.ROOT(root=centerRoot).network
	except:
		rootNode = bodyPart.ROOT().network
		print 'Auto Rig: "Root" Skipped.'

	# Cog / Hip
	try:
		centerCog = tree[naming.component.cog.capitalize()][naming.side.center]
		centerHip = tree[naming.component.hip.capitalize()][naming.side.center]
		cogNode = bodyPart.COG(cog=centerCog, hip=centerHip, networkRoot=rootNode)
	except:
		print 'Auto Rig: "Cog" / "Hip" Skipped.'

	# Spine
	try:
		centerSpine = tree[naming.component.spine.capitalize()][naming.side.center]
		items = skeleton.getJointChainByLabel(centerSpine, naming.component.spine.capitalize())

		bodyPart.SPINE(objects=items, networkRoot=rootNode, attrControl=cogNode.fkControl[0])

	except:
		print 'Auto Rig: "Spine" Skipped.'

	# Neck
	try:
		centerNeck = tree[naming.component.neck.capitalize()][naming.side.center]
		items = skeleton.getJointChainByLabel(centerNeck, naming.component.neck.capitalize())

		bodyPart.NECK(objects=items, networkRoot=rootNode, attrControl=cogNode.fkControl[0])

	except:
		print 'Auto Rig: "Neck" Skipped.'

	# Head
	try:
		centerHead = tree[naming.component.head.capitalize()][naming.side.center]
		bodyPart.HEAD(head=centerHead, networkRoot=rootNode)
	except:
		print 'Auto Rig: "Head" Skipped.'

	# Arms
	for side in [naming.side.left, naming.side.right]:
		try:
			collar = tree[naming.component.collar.capitalize()][side]
			shoulder = tree[naming.component.shoulder.capitalize()][side]
			elbow = tree[naming.component.elbow.capitalize()][side]
			hand = tree[naming.component.hand.capitalize()][side]

			bodyPart.ARM(side=side, collar=collar, shoulder=shoulder, elbow=elbow, hand=hand, networkRoot=rootNode)
		except:
			print 'Auto Rig: "{} Arm" Skipped.'.format(side)

	# Legs
	for side in [naming.side.left, naming.side.right]:
		try:
			hip = tree[naming.component.hip.capitalize()][side]
			knee = tree[naming.component.knee.capitalize()][side]
			foot = tree[naming.component.foot.capitalize()][side]
			toe = tree[naming.component.toe.capitalize()][side]

			bodyPart.LEG(side=side, hip=hip, knee=knee, foot=foot, toe=toe, networkRoot=rootNode)
		except:
			print 'Auto Rig: "{} Leg" Skipped.'.format(side)

	cmds.select(d=True)

	return


#########################################################################################################################
#																														#
#																														#
#	Menu    																								        #
#																														#
#																														#
#########################################################################################################################


def menu():
	cmds.menuItem(l='Rig From Template', c=rigFromTemplate)
	return
