# LANCER.RIG.AUTO
#
#
#
#
#

# Lancer Modules
import parts
import naming
reload(parts)
reload(naming)

# Maya Modules
from maya import cmds, mel


def rigFromTemplate(*args):

	root = parts.ROOT(root='CenterRoot')

	cog = parts.COG(cog='CenterCOG',
	                hip='CenterHip',
	                networkRoot=root.network,
	                )
	spine = parts.SPINE(objects=['CenterSpine0', 'CenterSpine1', 'CenterSpine2', ],
	                    networkRoot=root.network)

	#neck = parts.NECK(objects=['CenterNeck0'], networkRoot=root.network)
	#head = parts.HEAD(head='CenterHead', networkRoot=root.network)

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
	                 networkRoot=root.network,
	                 )

	legR = parts.LEG(side='Right',
	                 hip='RightLegHip',
	                 knee='RightLegKnee',
	                 foot='RightLegFoot',
	                 networkRoot=root.network,
	                 )
	'''
	armList = ['LeftArmShoulder', 'LeftArmElbow', 'LeftArmHand']
	upperList = ['LeftArmShoulderBind0', 'LeftArmShoulderBind1']
	lowerList = ['LeftArmElbowBind1', 'LeftArmElbowBind2']
	midObject = 'LeftArmElbowBind0'

	parts.RIBBONLIMB(start=armList[0],
	                 mid=armList[1],
	                 end=armList[2],
	                 upperObjects=upperList,
	                 lowerObjects=lowerList,
	                 midObject=midObject,
	                 )
	'''
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
