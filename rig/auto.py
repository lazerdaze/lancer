# LANCER.RIG.AUTO
#
#
#
#
#

'''
TODO
- Left Right Control Color: Left Blue / Right Red
- HIK Skeleton on FK Controls
- Better Hand Controls (Fist / Spread)
'''

# Lancer Modules
from api import *

# Python Modules

# Maya Modules
from maya import cmds


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
	root = rig.parts.ROOT(root='CenterRoot')

	cog = rig.parts.COG(cog='CenterCOG',
	                    hip='CenterHip',
	                    networkRoot=root.network,
	                    )
	spine = rig.parts.SPINE(objects=['CenterSpine0', 'CenterSpine1', 'CenterSpine2', ],
	                        networkRoot=root.network)

	neck = rig.parts.NECK(objects=['CenterNeck0'], networkRoot=root.network)
	head = rig.parts.HEAD(head='CenterHead', networkRoot=root.network)

	armL = rig.parts.ARM(side=naming.side.left,
	                     collar='LeftArmCollar',
	                     shoulder='LeftArmShoulder',
	                     elbow='LeftArmElbow',
	                     hand='LeftArmHand',
	                     networkRoot=root.network,
	                     )
	armR = rig.parts.ARM(side=naming.side.right,
	                     collar='RightArmCollar',
	                     shoulder='RightArmShoulder',
	                     elbow='RightArmElbow',
	                     hand='RightArmHand',
	                     networkRoot=root.network,
	                     )

	legL = rig.parts.LEG(side='Left',
	                     hip='LeftLegHip',
	                     knee='LeftLegKnee',
	                     foot='LeftLegFoot',
	                     toe='LeftLegToe',
	                     networkRoot=root.network,
	                     )

	legR = rig.parts.LEG(side='Right',
	                     hip='RightLegHip',
	                     knee='RightLegKnee',
	                     foot='RightLegFoot',
	                     toe='RightLegToe',
	                     networkRoot=root.network,
	                     )
	cmds.select(d=True)
	return


def rigFromLabels(root):
	amount = 0
	step = 100.0 / 8.0

	cmds.progressWindow(title='Auto Rigging',
	                    progress=amount,
	                    status='Query',
	                    isInterruptable=True)
	while True:
		if cmds.progressWindow(query=True, isCancelled=True):
			break

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

		cmds.progressWindow(edit=True, status='Rigging Root', step=step)

		# Root
		try:
			centerRoot = tree[naming.component.root.capitalize()][naming.side.center]
			rootNode = bodyPart.ROOT(root=centerRoot).network
		except:
			rootNode = bodyPart.ROOT().network
			print 'Auto Rig: "Root" Skipped.'

		cmds.progressWindow(edit=True, status='Rigging Cog', step=step)

		# Cog / Hip
		try:
			centerCog = tree[naming.component.cog.capitalize()][naming.side.center]
			centerHip = tree[naming.component.hip.capitalize()][naming.side.center]
			cogNode = bodyPart.COG(cog=centerCog, hip=centerHip, networkRoot=rootNode)
		except:
			print 'Auto Rig: "Cog" / "Hip" Skipped.'

		cmds.progressWindow(edit=True, status='Rigging Spine', step=step)

		# Spine
		try:
			centerSpine = tree[naming.component.spine.capitalize()][naming.side.center]
			items = skeleton.getJointChainByLabel(centerSpine, naming.component.spine.capitalize())

			bodyPart.SPINE(objects=items, networkRoot=rootNode, attrControl=cogNode.fkControl[0])

		except:
			print 'Auto Rig: "Spine" Skipped.'

		cmds.progressWindow(edit=True, status='Rigging Neck', step=step)

		# Neck
		try:
			centerNeck = tree[naming.component.neck.capitalize()][naming.side.center]
			items = skeleton.getJointChainByLabel(centerNeck, naming.component.neck.capitalize())

			bodyPart.NECK(objects=items, networkRoot=rootNode, attrControl=cogNode.fkControl[0])

		except:
			print 'Auto Rig: "Neck" Skipped.'

		cmds.progressWindow(edit=True, status='Rigging Head', step=step)

		# Head
		try:
			centerHead = tree[naming.component.head.capitalize()][naming.side.center]
			bodyPart.HEAD(head=centerHead, networkRoot=rootNode)
		except:
			print 'Auto Rig: "Head" Skipped.'

		cmds.progressWindow(edit=True, status='Rigging Arms', step=step)

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

		cmds.progressWindow(edit=True, status='Rigging Legs', step=step)

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
		cmds.progressWindow(edit=True, status='Finishing', step=step)
		break

	cmds.progressWindow(endProgress=True)
	return


def rigFromLabelsFunction(*args):
	selected = rigging.getSelected()

	if selected:
		root = selected[0]

		if cmds.objectType(root) != 'joint':
			cmds.warning('Auto Rig: Must specify a root joint.')
			return
		else:
			rigFromLabels(root)
	return


#########################################################################################################################
#																														#
#																														#
#	Menu    																								        #
#																														#
#																														#
#########################################################################################################################


def menu():
	cmds.menuItem(l='Rig Using Joint Labels', c=rigFromLabelsFunction)
	return
