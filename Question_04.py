#Check whether a number is a power of 2 using operators.

n = int(input("Enter a number: "))
if n > 0 and (n & (n - 1)) == 0:
    print("Power of 2")
else:
    print("Not a power of 2")
