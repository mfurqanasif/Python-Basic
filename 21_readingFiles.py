# reading file in python 
# for reading a file , we have to pass a file path for that

filepath = "D:\w+ program\Python\\templte.txt"

file  = open(filepath, 'r')

print(file.read())

file.close()
data = ""
with open(filepath, 'r') as file:
    data = file.readlines()

print(data)
