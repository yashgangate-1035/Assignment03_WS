#Find the Greatest Common Divisor (GCD) of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x, y = abs(a), abs(b)
while y != 0:
    x, y = y, x % y
print("GCD:", x)
