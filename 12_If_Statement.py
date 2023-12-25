# if , elif and else in python



def numberEqulitychecker(numb1,numb2):
    numb1=  int(numb1)
    numb2=  int(numb2)

    if(numb1 > numb2):
        print("{0} is greator then {1}".format(numb1,numb2))
    elif (numb1 < numb2):
        print("{0} is less then {1}".format(numb1,numb2))
    else:
        print("{0} is equal to {1}".format(numb1,numb2))

numberEqulitychecker(input("Enter number 1:"),input("Enter number 2:"))
