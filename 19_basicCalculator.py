# creating a basic calculator 

def operations():
    menu = """Basic Calculator\n
    1. Addition +\n
    2. Substraction -\n
    3. Multiply *\n
    4. Divide /\n
    5. Modulus %\n"""

    print(menu)
    operator = input("Enter the operation you want to perform: ")

    return operator

def calculator(ops, oprand1, oprand2):
    if ops == '+':
        return oprand1 + oprand2
    elif ops == '-':
        return oprand1 - oprand2
    elif ops == '*':
        return oprand1 * oprand2
    elif ops == '/':
        return oprand1 / oprand2
    elif ops == '%':
        return oprand1 % oprand2

isTrue = True
while (isTrue):

    ops =  operations()

    op1 = int(input("Enter oprand 1: "))
    op2 = int(input("Enter oprand 2: "))

    print(calculator(ops,op1,op2))

    isTrue = True if input("You want to perform another operation (y/n)").lower() == 'y' else False 





