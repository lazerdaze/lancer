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
from rig.templates import Templates
from utils import *
import parts

# Maya Modules
from maya import cmds


########################################################################################################################
#
#
#	Query
#
#
########################################################################################################################

def queryLabels(root):
	tree = {}
	children = getAllJointChildren(root)

	for label in MAYAJOINTLABELS + [Part.cog.capitalize()]:
		tree[label] = {
			Position.center: None,
			Position.left  : None,
			Position.right : None,
		}

	for child in sorted(children + [root]):
		label = getJointLabel(child)
		side = label[0]
		typ = label[1]

		if typ.lower() not in [Component.bind, Component.rig]:
			if side and typ and typ in tree:
				key = tree[str(typ)][str(side)]
				if key is None:
					tree[str(typ)][str(side)] = str(child)
	return tree


########################################################################################################################
#
#
#	Auto Rig Functions
#
#
########################################################################################################################

def rigFromTemplate(*args):
	root = ROOT(root='CenterRoot')

	cog = COG(cog='CenterCOG',
	          hip='CenterHip',
	          networkRoot=root.network,
	          )
	spine = SPINE(objects=['CenterSpine0', 'CenterSpine1', 'CenterSpine2', ],
	              networkRoot=root.network)

	neck = NECK(objects=['CenterNeck0'], networkRoot=root.network)
	head = HEAD(head='CenterHead', networkRoot=root.network)

	armL = ARM(side=Position.left,
	           collar='LeftArmCollar',
	           shoulder='LeftArmShoulder',
	           elbow='LeftArmElbow',
	           hand='LeftArmHand',
	           networkRoot=root.network,
	           )
	armR = ARM(side=Position.right,
	           collar='RightArmCollar',
	           shoulder='RightArmShoulder',
	           elbow='RightArmElbow',
	           hand='RightArmHand',
	           networkRoot=root.network,
	           )

	legL = LEG(side=Position.left,
	           hip='LeftLegHip',
	           knee='LeftLegKnee',
	           foot='LeftLegFoot',
	           toe='LeftLegToe',
	           networkRoot=root.network,
	           )

	legR = LEG(side=Position.right,
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
			centerRoot = tree[Part.root.capitalize()][Position.center]
			rootNode = ROOT(root=centerRoot).network
		except:
			rootNode = ROOT().network
			print 'Auto Rig: "Root" Skipped.'

		cmds.progressWindow(edit=True, status='Rigging Cog', step=step)

		# Cog / Hip
		try:
			centerCog = tree[Part.cog.capitalize()][Position.center]
			centerHip = tree[Part.hip.capitalize()][Position.center]
			cogNode = COG(cog=centerCog, hip=centerHip, networkRoot=rootNode)
		except:
			print 'Auto Rig: "Cog" / "Hip" Skipped.'

		cmds.progressWindow(edit=True, status='Rigging Spine', step=step)

		# Spine
		try:
			centerSpine = tree[Part.spine.capitalize()][Position.center]
			items = getJointChainByLabel(centerSpine, Part.spine.capitalize())

			SPINE(objects=items, networkRoot=rootNode, attrControl=cogNode.fkControl[0])

		except:
			print 'Auto Rig: "Spine" Skipped.'

		cmds.progressWindow(edit=True, status='Rigging Neck', step=step)

		# Neck
		try:
			centerNeck = tree[Part.neck.capitalize()][Position.center]
			items = getJointChainByLabel(centerNeck, Part.neck.capitalize())

			NECK(objects=items, networkRoot=rootNode, attrControl=cogNode.fkControl[0])

		except:
			print 'Auto Rig: "Neck" Skipped.'

		cmds.progressWindow(edit=True, status='Rigging Head', step=step)

		# Head
		try:
			centerHead = tree[Part.head.capitalize()][Position.center]
			HEAD(head=centerHead, networkRoot=rootNode)
		except:
			print 'Auto Rig: "Head" Skipped.'

		cmds.progressWindow(edit=True, status='Rigging Arms', step=step)

		# Arms
		for side in [Position.left, Position.right]:
			try:
				collar = tree[Part.collar.capitalize()][side]
				shoulder = tree[Part.shoulder.capitalize()][side]
				elbow = tree[Part.elbow.capitalize()][side]
				hand = tree[Part.hand.capitalize()][side]

				ARM(side=side, collar=collar, shoulder=shoulder, elbow=elbow, hand=hand, networkRoot=rootNode)
			except:
				print 'Auto Rig: "{} Arm" Skipped.'.format(side)

		cmds.progressWindow(edit=True, status='Rigging Legs', step=step)

		# Legs
		for side in [Position.left, Position.right]:
			try:
				hip = tree[Part.hip.capitalize()][side]
				knee = tree[Part.knee.capitalize()][side]
				foot = tree[Part.foot.capitalize()][side]
				toe = tree[Part.toe.capitalize()][side]

				LEG(side=side, hip=hip, knee=knee, foot=foot, toe=toe, networkRoot=rootNode)
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


########################################################################################################################
#
#
#	Auto Class
#
#
########################################################################################################################

class Auto(object):
	def __init__(self, root):
		self.root = root
		self.rootRig = None
		self.template = None
		self.skeleton = None

		self._handler = {}
		self._exceptions = []
		self.templateDatabase = Templates()

		self.validate()
		self.createRootRig()

	@property
	def handler(self):
		return self._handler

	@handler.setter
	def handler(self, handler):
		if not isinstance(handler, dict):
			raise TypeError('Must provide a dict.')
		self._handler = handler
		return

	@property
	def exceptions(self):
		return self._exceptions

	@exceptions.setter
	def exceptions(self, exceptions):
		if not isinstance(exceptions, (list, dict, tuple)):
			raise TypeError('Must provide a iter type: list, dict, tuple.')
		self._exceptions = exceptions
		return

	def validate(self):
		if nodeType(self.root) != 'joint':
			raise TypeError('Must select a joint.')

		if not attributeExist(self.root, 'kind'):
			raise AttributeExistsError('Skeleton is invalid. Joint is missing "kind" attribute.')
		else:
			if not getAttribute(self.root, 'kind'):
				raise ValueError('Skeleton is invalid. No Skeleton kind specified.')
			else:
				if getAttribute(self.root, 'kind') != 'skeleton':
					raise ValueError('Skeleton is invalid. Joints kind is not skeleton.')

		if not attributeExist(self.root, 'skeletonTemplate'):
			raise AttributeExistsError('Skeleton is invalid. Missing "skeletonTemplate" attribute.')
		else:
			if not getAttribute(self.root, 'skeletonTemplate'):
				raise ValueError('Skeleton is invalid. No "skeletonTemplate" specified.')

		query = getAttribute(self.root, 'skeletonTemplate')

		if not self.templateDatabase.templateExists(query):
			raise KeyError('{} is not a valid definition.'.format(self.template))
		else:
			self.template = query
		return

	def createRootRig(self):
		self.rootRig = parts.ROOT(root=self.root)
		self.rootRig.create()
		return

	def rigFromDefinitions(self, debug=False):
		template = self.templateDatabase.getTemplate(self.template)

		for component in template:
			componentName = component.tag

			# Get Part Class
			if hasattr(parts, componentName):
				rig = getattr(parts, componentName)
				rig = rig()

				attributes = component.attrib

				# Set Class Arguments
				for attr in attributes:
					definition = attributes[attr]
					items = getConnectedNode(self.root, definition)

					if attr == 'objects':
						if not isinstance(items, (list, dict, tuple)):
							items = [items]

					setattr(rig, attr, items)
					if debug:
						print component, attr, definition, items, rig

				# Setup Network
				rig.networkRoot = self.rootRig.network

				# Create Rig
				rig.create()
		return

	def rigFromLabels(self):
		return

	def rigFromFile(self):
		return


def autoRigLabelsCallback(*args, **kwargs):
	return


def autoRigDefinitionsCallback(*args, **kwargs):
	rig = Auto(root=getSingleSelected())
	rig.rigFromDefinitions()
	return
