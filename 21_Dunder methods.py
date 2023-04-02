# This file is about Dunder methods or special functions

class A:

    def __init__(self, name, salary):
        self.name = name
        self.sal = salary

    def __add__(self, a):
        return self.sal + a.sal

    def __mul__(self, other):
        return self.sal * other.sal


a = A("sanket", 50000)
b = A("xyz", 10000)
c = A("yeah", 5000)
print(a + c)
print(a * c)

# and a lot more...!! to discover
# you can simply add up like this also...yeah but though there might be some use of dunder method

print(a.sal+b.sal)