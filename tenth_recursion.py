# This shows the recursive approach for finding factorial of any number...!!
def recur(n):
    if n == 1:
        return 1
    else:
        return n * recur(n - 1)


print("Enter any number for the factorial : ")
n = int(input())

print(recur(n))

# Now iterative approach using FOR loop...!!
def iterat(n):
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac


print("Enter any number for the factorial : ")
n = int(input())
print(iterat(n))
