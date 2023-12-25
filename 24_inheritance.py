# inheritance 


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


class student (Person):
    pass


p1 = student("furqan",25)
print(p1.name)

print(p1.age)