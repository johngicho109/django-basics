from utils import Students
class Myclass:
    x=5

p1 = Myclass()
print(p1.x)

class Person():
    #pass - allows empty class
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Person2(Students):
    pass

person1 = Person("Joe",26)
print(person1.name)
print(person1.age)

p2 = Person2()
print(p2.name)
print(p2.age)
