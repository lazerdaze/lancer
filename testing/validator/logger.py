# LANCER.TESTING.VALIDATOR.LOGGER
#
#
#
#
#

# Python Logging
import logging

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


class Logger:
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