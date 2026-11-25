#Find whether a number is divisible by both 4 and 6 using logical operators.

n = int(input("Enter a number: "))
if n % 4 == 0 and n % 6 == 0:
    print("Divisible by both 4 and 6")
else:
    print("Not divisible by both 4 and 6")
