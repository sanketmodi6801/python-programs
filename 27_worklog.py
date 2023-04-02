import os
print(os.getcwd())
path = r"C:\Users\welcome\Documents\workLog.txt"

press = input(" Press 1.) For Logging the Work Log\n\t   2.) For retriving the Work Log \n")

if press == "1":
    with open(path, "a") as s:
        log = input("Enter your work here :")
        s.write(log + "\n")
        s.close()

elif press == "2":
    with open(r"C:\Users\welcome\Documents\workLog.txt") as s:
        for items in s:
            print(items)
    s.close()

print("Happy Logging")

