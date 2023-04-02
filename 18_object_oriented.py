#                                                  OBJECT ORIENTED PROGRAMMING


# This file will give understanding regarding object oriented programming in python

class First:
    cars = "bmw"
    age = 20

    # use of constructor by _init_ function
    def __init__(self, name, Age, love, success):
        self.age = Age
        self.name = name
        self.love = love
        self.success = success
        print(f"The name is {self.name} and his age is {self.age}, currently his love status is {self.love} "
              f"because his success status is {self.success} ")

# if i want to change class variables than i have to use class methods, so i can change class variables by object also!!

    @classmethod
    def changeMethod(cls, newcar):
        cls.cars = newcar

    @classmethod
    def additself(cls, string):
        return cls(*string.split(" "))

    # use of static method as a simple function..
    @staticmethod
    def randomfunction():
        print("This functoin is a static function and does not do anything great.. unless like class method LOL..!")


Sanket = First("sanket", 20, "False", "True")  # ahiya sanket ek object bani gayu  first naam na class nu..

Sanket.age = 20
Sanket.name = "Sanket"
Sanket.love = False
Sanket.success = True
print(First.age, Sanket.name, Sanket.love, Sanket.success)
Sanket.changeMethod("audi")
print(Sanket.cars)
Sanket.changeMethod("mercedes")
print(Sanket.cars)

zalak = First.additself("Zalak 24 false true")
First.randomfunction()
