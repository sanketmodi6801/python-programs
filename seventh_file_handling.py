# For handling file..!!

# to open  & read
        # s=open("xyz.txt")
        # a=s.read()
        # a = s.readline()
        # print(a)
        # for line in s :
        #     print(line)

# to write and append           , in this mode only writing is available no reading is possible....
        # s=open("xyz.txt","w")
        # f=s.write("sanket is the best..!!")
        # print(f)                # ahiya f no of characters show karshe...aakhi file read nai thai...!!
        # s.close()
        #
        # s=open("xyz.txt","a")
        # s.write("\nI am the best...!!")
        # s.close()

# to read and write at the same time...!!
        # s=open("xyz.txt","r+")
        # print(s.read())
        # s.write("\nyes I am the best..!!\n I am the winner..!!")
        # print(s.read())
        # s.close()