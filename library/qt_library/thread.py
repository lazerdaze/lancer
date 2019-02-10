# Python Modules
import os
import sys
import time
import traceback
from PySide2 import QtCore, QtGui, QtWidgets


class workerSignals(QtCore.QObject):
	'''
	Defines the signals available from a running worker thread.
	Supported signals are:

	finished: No data
	error: `tuple` (exctype, value, traceback.format_exc() )
	result: `object` data returned from processing, anything
	'''
	finished = QtCore.Signal()
	error = QtCore.Signal(tuple)
	result = QtCore.Signal(object)


class workerRunnable(QtCore.QRunnable):
	def __init__(self, func, *args, **kwargs):
		'''
		:param func: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
	    :param args: Arguments to make available to the run code
	    :param kwargs: Keywords arguments to make available to the run code
	    '''
		QtCore.QRunnable.__init__(self)
		self.func = func
		self.args = args
		self.kwargs = kwargs
		self.signals = workerSignals()
		self.kwargs['progress_callback'] = self.signals.progress

	def run(self):
		'''
        Initialise the runner function with passed args, kwargs.
        '''
		try:
			result = self.func(*self.args, **self.kwargs)
		except:
			traceback.print_exc()
			exctype, value = sys.exc_info()[:2]
			self.signals.error.emit((exctype, value, traceback.format_exc()))
		else:
			self.signals.result.emit(result)
		finally:
			self.signals.finished.emit()
		return


class workerThread(QtCore.QThread):
	def __init__(self):
		QtCore.QThread.__init__(self)


class threadPool(QtCore.QThreadPool):
	def __init__(self):
		QtCore.QThreadPool.__init__(self)


