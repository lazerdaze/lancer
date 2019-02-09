# LANCER.TESTING.VALIDATOR.VALIDATE
#
#
#
#
#

# Lancer Modules
from logger import Logger
from rig import utils

# Python Logging
import logging
import sys
import collections

# Maya Modules
from maya import cmds


########################################################################################################################
#
#
#	Utils
#
#
########################################################################################################################

def validateOnSelected(func):
	def wrapper(*args, **kwargs):
		root = utils.getSelected()[0]
		func(root, **kwargs)

	return wrapper


########################################################################################################################
#
#
#	Validate Skeleton
#
#
########################################################################################################################


@validateOnSelected
def validateSkeletonOnSelected(root, *args, **kwargs):
	return validateSkeleton(root)


# TODO: UI For Validator
# FIXME : Values lower than zero (-e)
def validateSkeleton(root, *args, **kwargs):
	'''
	Go through skeleton hierarchy and check for these things:
		- Joint Labels:
			- Side not set to None
			- Type not set to None
		- Joint Orient XYZ set to zero
		- Translate YX set to zero
		- Rotate XYZ set to zero
		- Segment Scale Compensate set to off
		- If Inverse Scale is disconnected
		- Has message attributes for metadata relationships
		- Duplicates

	:return:
	'''
	debugList = []

	print '\n\n'
	# Logger
	log = Logger('Skeleton Validator')
	log.setLevel(logging.DEBUG)

	if utils.nodeType(root) != 'joint':
		log.fatal('Must provide a root joint.')
		return

	else:
		children = cmds.listRelatives(root, ad=True, type='joint')
		if not children:
			log.fatal('Skeleton has no hierarchy.')
			return
		else:
			children.insert(0, root)
			log.info('Length of Skeleton: {}'.format(len(children)))
			print ''

			for item in sorted(children):

				joint = utils.Joint(str(item))
				debug = False

				if not joint.isValid():
					log.fatal('{} : does not exist in scene.'.format(joint))
				else:
					if item != root:
						if joint.otherType.lower() not in ['leaf', 'bind']:

							# Translate
							for axis in ['y', 'z']:
								attrName = 'translate{}'.format(axis.upper())
								value = getattr(joint, attrName)

								if value != 0:
									log.debug('{} : {} : {}'.format(joint, attrName, value))
									debug = True

							# Joint Orient
							value = joint.jointOrient
							zeroCount = 3 - value.count(0.0)

							if zeroCount >= 2:
								log.debug('{} : has {} of 3 Joint Orients'.format(joint, zeroCount))
								debug = True

					# Rotate / Scale
					for attr in ['rotate', 'scale']:
						for axis in ['x', 'y', 'z']:
							attrName = '{}{}'.format(attr, axis.upper())
							value = getattr(joint, attrName)

							if attr == 'rotate':
								if value != 0:
									log.debug('{} : {} : {}'.format(joint, attrName, value))
									debug = True
							else:
								if value != 1:
									log.debug('{} : {} : {}'.format(joint, attrName, value))
									debug = True

					# Labels
					if joint.type == 'none':
						log.debug('{} : is missing Type Label'.format(joint))
						debug = True

					elif joint.type == 'other':
						if not joint.otherType:
							log.debug('{} : is missing OtherType Label'.format(joint))
							debug = True

					if joint.side == 'none':
						log.debug('{} : is missing Side Label'.format(joint))
						debug = True

					# Segment Scale
					if cmds.getAttr('{}.{}'.format(joint, utils.MayaAttr.segmentScaleCompensate)):
						log.debug('{} : has Segment Scale'.format(joint))
						debug = True

				# Debug
				if debug:
					if joint not in debugList:
						debugList.append(joint)
						print ''

		cmds.select(debugList)
		print '\n\n# Skeleton Validator : Validator Finished. View Script Editor for details. #',
		return debugList
