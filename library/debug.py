# PRISM.LIBRARY.DEBUG
#
#
#
#
#

# Python Modules
import os
import sys
import collections
import time


def processTime(func, *args):
	def wrapper(*args):
		t1 = time.time()
		output = func(*args)
		print'Function: "{}" completed successfully in {} seconds.'.format(func, time.time() - t1)
		return output
	return wrapper

