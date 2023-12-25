# write to file


# this file already exists , learn about differnt mode of reading a file 
data = "i am added by python code in txt file"
filepath = "D:\w+ program\Python\\templte.txt"


file  = open(filepath,'a')
file.write(data)

file.close()

# in this it will first creat a file 
file1  = open('myfile.txt','a')

file1.write("i am just created")

file1.close()