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

# Generators
def generate(var):
    for x in range(var):
        yield x
    

for x in generate(100):
    print 
    
    
