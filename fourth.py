# this is an if elif else program

var1 = int(input("Enter any integer number : "))
var2 = int(input("Enter another integer number : "))

if var1 > var2:
    print(str(var1),"is greater than ",str(var2))

elif var1 == var2:
    print(str(var1),"is equal to ",str(var2))

else:
    print("{0} is smaller than {1}".format(str(var1), str(var2)))

list1= [5,10,15,20]
if 5 in list1:
        print("In the list")


