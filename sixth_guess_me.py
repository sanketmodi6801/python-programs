print("Guess Me...!! \n \t I Am A Number..!!")
print("Rules : identify me within 9 chances..!! :) ")

i: int=0
def count():
    print("You ",9-i," chances left..!!")

while(i<=8):
    n=int(input("\tGuess a number between 1 to 50 : "))
    i = i + 1
    if 1 <= n <= 10 :
        print("\tEnter a big number...!!")
        count()
        continue
    elif 11 <= n <= 20:
        print("\tyou are quite close.!!")
        count()
        continue
    elif 21 <= n <= 22:
        print("\tjust a little bigger number...!!")
        count()
        continue
    elif n == 23:
        print("Boom\n\t you made it correct!!")
        print("\tYou did it within ",i," chances..!!")
        break
    elif 24 <= n <= 30:
        print("\tjust a little smaller number...!!")
        count()
        continue
    if 31 <= n <= 40:
        print("\tYou are quite close...!!")
        count()
        continue
    if 41 <= n :
        print("\tEnter a smaller number...!!")
        count()
        continue


if i >= 9 :
    print("Game over..!!\n\t Try again...")
