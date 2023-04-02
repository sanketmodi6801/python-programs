# i = 0
# while (True):
#     if i == 5:
#         i=i+1
#         continue
#
#     print(i)
#     i = i + 1
#
#
#     if i == 45:
#         break
#         i=i+1


# s=10
# while(s>=10):
#     print(s)
#     if(s>=100):
#         break
#
#     s = s + 1


i: int = 0


def count():
    print("Only ", 9 - i, " rounds remaining..!!")


while (i <= 8):
    i = i + 1
    print("Enter a number : ")
    n: int = int(input())

    if 100 <= n:
        print("Enter a smaller number..!!")
        count()
        continue
    elif 50 <= n <= 54:
        print("you are very close...!!")
        count()
        continue
    elif 56 <= n <= 60:
        print("you are very close...!!")
        count()
        continue
    elif (n == 55):
        print("Boom...!! \n you have entered correct number...!!")
        break
    elif 40 <= n <= 49:
        print("you are very close...!!")
        count()
        continue
    else:
        print("Try again...with some good number..!!")
        count()
        continue

if 9 < i:
    print("Game over...!!\n\t try again.")
