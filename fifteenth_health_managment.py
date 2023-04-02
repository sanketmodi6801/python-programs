# This is a Health managment program, which stores my diet and exercise details..!!
from typing import TextIO


def getdate():
    import datetime
    return datetime.datetime.now()


def logging_deit():
    with open("sanket_diet.txt", "a") as f:
        diet = input("Add some space before entering your diet : ")
        f.write(diet + " : " + str(getdate()))
        f.write("\n")


def logging_exercise():
    with open("sanket_exercise.txt", "a") as f:
        exer = input("Add some space before entering your exercise : ")
        f.write(exer + " : " + str(getdate()))
        f.write("\n")


def retrive_diet():
    with open("sanket_diet.txt") as f:
        for item in f:
            print(item, end="")


def retrive_exercise():
    with open("sanket_exercise.txt") as f:
        for item in f:
            print(item, end="")


# from here program starts..!!
while True:
    print("This is your health record file..!!")
    print("For logging details press [ 1.]\n "
          "For retriving details press [ 2.] \n "
          "For exit press [ 0.]")
    l = int(input())
    if l == 1:
        n = int(input("select 1 or 2 for logging details of :"
                      " \n\t\t 1.) diet \n\t\t 2.) exercise\n"))

        if n == 1:
            logging_deit()
        elif n == 2:
            logging_exercise()
        else:
            print("Enter valid value ..!! ")
        continue



    elif l == 2:
        n = int(input("select 1 or 2 for retriving details of :"
                      " \n\t\t 1.) diet \n\t\t 2.) exercise\n"))
        if n == 1:
            retrive_diet()
        elif n == 2:
            retrive_exercise()
        else:
            print("Enter valid value ..!! ")
        continue
    elif l == 0:
        break

print("Thank you..!!\n\t Have a nice day..!!")
