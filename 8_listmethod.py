#list menthods 

list1 = [1,2,3,4,5]

list2  = ['banana','apples','oranges']

list1.extend(list2)

print(list1)

list2.append(list1[1])

print(list2)

list2.insert(1,list1[-1])

print(list2)

print(list1.index('apples'))


# sort
# we can sort a list by using sort()

unOrderList = [9,7,1,5,4,2,3,6,8]
unOrderList.sort()
print(unOrderList)

#reverse 
unOrderList.reverse()
print(unOrderList)

#clean the list 
unOrderList.clear()
print(unOrderList)