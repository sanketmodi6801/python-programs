#  This file is about INHERITANCE and it's types...!!

#                               single inheritance
class First:
    @staticmethod
    def printdetails():
        print("This is parent class...!!")


class Second(First):
    @staticmethod
    def printextra():
        print("This is child class..!!")


# i can use all properties of class first in class second by inheritance
object1 = Second()
object1.printdetails()
object1.printextra()


#                               Multiple inheritance

class computer:
    def __init__(self, name, price, effeci):
        self.price = price
        self.effe = effeci
        self.name = name

    # def properties(self):
    #     print("powerful and works on ac supply")


class laptop:
    def properties(self):
        print("more compact and works on battery as well as ac source")


class mobile(computer, laptop):
    pass


hp = computer("hp pavilion", 45000, "powerful and works on ac supply")
iphone = mobile("iphone 12 pro", 95000, "Most powerful phone ever...!!")
print(iphone.name)
iphone.properties()

""" Here i have not written anything in class mobile but still just by passing arguments
 in constructor, i am able to use all the properties of class computer as well as laptop  """


#                               Multilevel inheritance !!

class grandfather:
    basketball =True
    cricket = False
    football=True


class father(grandfather):
    basketball = False
    cricket = True


class son(father):
    football = False

sanket=son()
vipul=father()

print(sanket.basketball)
print(vipul.football)
print(sanket.football)

""" This shows that the multilevel inheritance also works in the order of class given 
     here class son has access in both class grandfather and father."""