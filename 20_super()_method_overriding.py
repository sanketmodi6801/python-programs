# using super() function and method overriding

class A:
    var1 = "This is var 1 of class A"
    def __init__(self):
        self.var2 = "This is var 2.. lol"

    @staticmethod
    def printany():
        print("This going to be a mess,, yeah man!!!")


class B(A):
    var1 = "This is var1 of class B"

    def __init__(self):
        self.var2 = "yeah, again var2 from class B... hahahaha"
        super().__init__()


    @staticmethod
    def printany():
        print("This going to be a mess, class B , yeah man!!!")


b = B()
print(b.var2)
b.printany()

# super is not applicable on methods...!!

""" super ni upar lakhelu badhu j override thai jai che, ena pachi nu j account ma 
 leva ma aave che. super ek important function na jem kaam kare che, jyare be karta 
   vadhare class sathe deal karvanu hoy. """
