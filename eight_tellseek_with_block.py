with open("xyz.txt") as f:

    print(f.readline())
    print(f.tell())
    f.seek(0)
    print(f.readline())
    print(f.tell())