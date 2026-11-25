#Check whether a number is an Armstrong number.

n = int(input("Enter a number: "))
digits = str(n)
power = len(digits)
total = 0
for d in digits:
    total += int(d) ** power
if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
