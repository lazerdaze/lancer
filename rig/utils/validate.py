# Lancer Modules
from naming import *
from general import *
from node import *
from joint import *
from skeleton import *

# Python Logging
import sys
import logging
import collections

# Maya Modules
from maya import cmds

########################################################################################################################
#
#
#	Logger
#
#
########################################################################################################################

'''
Wrapper above built-in python logging module to help logging to Shell, Maya and Nuke
directly using timestamp and logging-level to keep the logs clean.
Also, both Maya and Nuke have specific handlers that allow application sepcific logging
using warning and popup messages that are native to those applications.
fatal and critical levels will pop a warning message in Nuke and Maya to make sure
user attention was grabbed when needed.
To use:
    log = getLogger( 'mylogger' )
    log.info( 'log something' )
    # Set level to debug
    log = getLogger( 'mylogger', level=DEBUG )
    # OR
    log = getLogger( 'mylogger' )
    log.setLevel( DEBUG )
    # Alart user:
    try:
        ... do something
    except Exception, error :
        log.fatal( 'pop up this message if we're in nuke or maya' )
        raise error # re raise the error after we message the user.
'''

MESSAGE_FORMAT = '# %(levelname)s: %(name)s: %(message)s #'
DATE_FORMAT = '%Y/%m/%d - %H:%M:%S'

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0


class Validator:
	def __init__(self,
	             name='Validator',
	             filepath=None,
	             level=DEBUG,
	             ):
		'''
		name(str) : logger name
		shell(bol): output to shell
		maya(bol) : output to maya editor
		file(str) : output to given filename
		level(int): logger level
		'''

		self.name = name
		self.filepath = filepath
		self.level = level

		self.logger = logging.getLogger(name)
		self.logger.setLevel(level)

		if self.logger.handlers:
			return
		else:
			# Format
			messageFormat = logging.Formatter(MESSAGE_FORMAT)

			# File:
			if self.filepath:
				handler = logging.FileHandler(filepath)
				handler.setFormatter(messageFormat)
				self.logger.addHandler(handler)

	def __repr__(self):
		return '{}({} Level:{})'.format(self.__class__, self.name, self.level)

	def __getattr__(self, attr):
		if hasattr(self.logger, attr):
			return getattr(self.logger, attr)
		else:
			raise AttributeError('No attribute "{}".'.format(attr))

	def debug(self, message):
		self.logger.debug(message)

	def info(self, message):
		self.logger.info(message)

	def warning(self, message):
		self.logger.warning(message)

	def fatal(self, message):
		self.logger.fatal(message)

	def critical(self, message):
		self.logger.critical(message)


########################################################################################################################
#
#
#	Validator
#
#
########################################################################################################################

def validateOnSelected(func):
	def wrapper(*args, **kwargs):
		root = getSelected()[0]
		func(root, **kwargs)

	return wrapper


def validateMesh():
	return


def validateHierarchy():
	return


def validateDuplicates():
	return


def validateName():
	return


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
	log = Validator('Skeleton Validator')
	log.setLevel(logging.DEBUG)

	if nodeType(root) != 'joint':
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

				joint = Joint(str(item))
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

					if joint.sideLabel == 'none':
						log.debug('{} : is missing Side Label'.format(joint))
						debug = True

					# Segment Scale
					if cmds.getAttr('{}.{}'.format(joint, MayaAttr.segmentScaleCompensate)):
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


def validateRig(root):
	return
