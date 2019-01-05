# LANCER.API.UTILS.NAMING
#
#
#
#
#


def longName(*args):
	var = ''
	for arg in args:
		if arg is not None:
			if not isinstance(arg, (list, dict)):
				if var:
					var += '_{}'.format(arg)
				else:
					var += str(arg)
			else:
				for item in arg:
					if var:
						var += '_{}'.format(longName(item))
					else:
						var += longName(item)
	return var


def attributeName(*args):
	var = ''
	for arg in args:
		if type(arg) is str:
			if arg[0] in '0123456789':
				raise TypeError('Argument must start with a letter.')
			else:

				if var:
					var += '.{}'.format(arg)
				else:
					var = arg
		else:
			raise TypeError('Argument must be str.')
	return var
