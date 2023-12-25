#strings are plain text it is like a list of character arrray it can contain any charater 

# \n is called a escaping chareacter we use this type of character for special fucntionaliy 
# like her \n is use enter newline 
print("Hello \nMy name is Furqan\nHopefully you are having a good day")

#stirng concatenation 
# simply you add 2 string
string1 = "\nhello world,"
string2 =  "Welcome to the world of programming"

concatedString =  string1 + string2

print(concatedString)

#as string are list you can check the length of the string using len fucntion 
len  = len(concatedString)
print("lenght of concatedString is {0}".format(len))

#You can access any character in you string. first character is at 0 Index and last character is at Len of stirng -1 index

print(concatedString[2])

# you can check is string is lower or upper case
upper = "HELLO"
lower = "hello"
cap = "Hello World"

print(upper.isupper())
print(lower.islower())
print(cap.istitle())

#same we can change case of our string 

upper = "HELLO"
lower = "hello"
cap = "hello world"


print(upper.lower())
print(lower.upper())
print(cap.title())


#replace , you replace character in string

stringA = "I am a developer"

print(stringA.replace('a','A'))

# you can replace multiple characters too

print(stringA.replace('am','AM'))

# you can fing index of a character , it will returns very first occurance of the given character 

print(stringA.index('a'))

#using count fucntion you can find apperance of character in given string 
print(stringA.count('e'))