#numbers
#in programing numbers is of mainly 2 types integers(1,2,3,....) and flaoting point (1.1,2.2,....)

varInt = 1
varflaot = 1.1 

print("variable name 'varInt' conatins value of type '{0}'".format(type(varInt)))
print("variable name 'varFlaot' conatins value of type '{0}'".format(type(varflaot)))

#you can perform all the arthmetic fucntion these varaiable 

print("addition {0} + {1} = {2}".format(2,2,2+2))

print("substract {0} - {1} = {2}".format(2,2,2-2))

print("multiply {0} * {1} = {2}".format(2,2,2*2))

print("divide {0} / {1} = {2}".format(2,2,2/2))

print("modulus {0} % {1} = {2}".format(5,2,5%2))

print("power {0} ^ {1} = {2}".format(2,2,2**2))

# can perform these operation on can kind of number 
# varable must be of int or float or any number type 
# other wise it will not treated correctly
#like "23" is stirng not an int type of number 


print("max of {0} , {1} is {2}".format(4,2,max(4,2)))

print("min {0} , {1} is {2}".format(4,2,min(4,2)))

print("abs of {0} is {1}".format(-2,abs(-2)))


print("round of {0} is {1}".format(3.5,round(3.5)))
print("round of {0} is {1}".format(4.5,round(4.5)))
print("round of {0} is {1}".format(3.4, round(3.4)))
print("round of  {0} is {1}".format(3.6,round(3.6)))


#we can import any other python module in our own program by using this line

from  math import *

print(sqrt(100))