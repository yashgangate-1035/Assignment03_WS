#Create a menu-driven calculator using if-elif.

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Power")
choice = input("Enter your choice: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if choice == "1":
    print("Result:", a + b)
elif choice == "2":
    print("Result:", a - b)
elif choice == "3":
    print("Result:", a * b)
elif choice == "4":
    if b == 0:
        print("Division by zero is not allowed")
    else:
        print("Result:", a / b)
elif choice == "5":
    if b == 0:
        print("Modulus by zero is not allowed")
    else:
        print("Result:", a % b)
elif choice == "6":
    print("Result:", a ** b)
else:
    print("Invalid choice")
