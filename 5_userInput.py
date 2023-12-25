#user input 
# we take input from user in console by just using input fucntion 

name =  input("Enter your name: ")

print("your name is: {0}".format(name))

#the user input is of type stirng

print("user input take in name variable is of type {0}".format(type(name)))

# so if you to take any number type input then you must cast you data into of your desired type

age = int(input("Enter your age: "))

print("user input take in age variable is of type {0} after type  casting".format(type(age)))

