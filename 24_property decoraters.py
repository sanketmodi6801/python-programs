#  Getters and setters are useful for changing or updating value of object in run time..!!

class Athlete:

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        # self.fullname = f"{self.fname} {self.lname}"

    def printdetails(self):
        return f"The name is {self.fname} {self.lname} and the age is {self.age} years !!"

    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"

    @fullname.setter
    def fullname(self, string):
        names = string.split(" ")
        self.fname = names[0]
        self.lname = names[1]


Cricketer = Athlete("virat", "kohli", 35)
print(Cricketer.printdetails())
Cricketer.fname = "sachin"
print(Cricketer.printdetails())
Cricketer.lname = "Tendulkar"
print(Cricketer.printdetails())
print(Cricketer.fullname)

Cricketer.fullname = "MS Dhoni"
print(Cricketer.lname)
