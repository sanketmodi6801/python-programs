Sanket = "my name is sanket"
"""print(Sanket)
print(len(Sanket))
print(Sanket.endswith("ket"))
print(Sanket.capitalize())
print(Sanket.replace("sanket", "hero"))
print(Sanket.upper())
print(Sanket.islower())

print(Sanket[3:])
print(Sanket[: 5])
print(Sanket[0::2])"""

# this is a single line comment
"""this is a 
multi-line 
comment
"""
list1 = [1, 2, 5, 8, 9]

print(list1)
print(list1[0::2])

print(list1[::-1])  # A simple way to reverse any list from character to character
list1.reverse()
print(list1)

# A simple way to swap numbers in python
a=10
b=5
c=40
print(a,b,c)      #gives 10 5 40
a,b,c=b,c,a
print(a,b,c)      #gives 5 40 10
list1.sort()
print(list1)

tup1=(1,'sanket',8.8)
print(tup1)