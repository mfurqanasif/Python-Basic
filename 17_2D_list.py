#2d list
#list in side a list 

myList = [
    [0,2,4,6,8],
    [1,3,5,7,9]
]

for i in myList:
    print(i)

for i in myList:
    for j in i:
        print(j)