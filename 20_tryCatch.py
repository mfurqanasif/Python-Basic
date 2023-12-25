# try catch 

a = 0 
b  =1 

try:
    print(b/a)
except Exception:
    print("some thing went wrong")
else:
    print("All good")
finally:
    print("i will run every time at end ")