# check if given number is even or odd

def numberChecker(number):
    number = int(number)
    if( number%2 == 0):
        return "even"
    else:
        return "odd"
    
print(numberChecker(input("Enter a number: ")))