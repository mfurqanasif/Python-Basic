#list
# it is of dynamic data type and length 

countries = ['Pakistan','Japan','UK']

print(countries)

#you can access any data by its index 0 to len -1

print(countries[0])
# last index
print(countries[-1])
# second to last element
print(countries[1:])
#first 2 element
print(countries[:2])

#we can update any value is list

countries[-1] = "USA"
print(countries[-1])

#we can define list using list constructor

list1 = list(('item 1','item 2'))

