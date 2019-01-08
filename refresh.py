import sys
import inspect
from os.path import dirname


def refreshModules(userPath=None):
	if userPath is None:
		userPath = dirname(__file__)
	userPath = userPath.lower()

	toDelete = []
	for key, module in sys.modules.iteritems():

		try:
			moduleFilePath = inspect.getfile(module).lower()

			if moduleFilePath == __file__.lower():
				continue

			if moduleFilePath.startswith(userPath):
				print "Removing %s" % key
				toDelete.append(key)
		except:
			pass

	for module in toDelete:
		del (sys.modules[module])


if __name__ == "__main__":
	refreshModules()
