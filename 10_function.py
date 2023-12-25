#functions

# this is simple function
def myFucntion():
    print('this is a fucntion')

myFucntion()


# we can pass data to our fucntion by passing parameters
# we can pass N number of parameters 

def myFucntionWithParameters(name):
    print("welcome "+name+" to the world of python")

myFucntionWithParameters('Asif')

# we can pass N number of argument with just parameters
# your parameter can be any name but use have to add a prefix * to specify that it is a lsit of argument 
def argsFucntion(*args):
    print(args)

argsFucntion('furqan','asif','muhammad')

