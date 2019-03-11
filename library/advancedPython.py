# List Comprehension
def listComprehend():
	get = cmds.ls(sl=True)
	selected = [x for x in get] if get else None


# Decorators
def testB(func):
	def wrapper():
		for x in range(10):
			func(x)

	return wrapper


@testB
def testA(var):
	print var


# Generators
def generate(var):
	for x in range(var):
		yield x


# Kwargs
def test(**kwargs):
	kwargs['side'] = 'left'
	print kwargs
	return


test()
