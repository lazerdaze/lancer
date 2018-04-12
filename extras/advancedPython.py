# List Comprehension
selected = [x for x in cmds.ls(sl=True)]

# Decorators
def testB(func):
    def wrapper():
        for x in range(10):
            func(x)
    return wrapper
        
@testB
def testA(var):
    print var
