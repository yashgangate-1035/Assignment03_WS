#Check whether three sides can form a triangle.

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("The sides can form a triangle")
else:
    print("The sides cannot form a triangle")
