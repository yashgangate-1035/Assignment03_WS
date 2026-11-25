#Create a simple ATM menu (Withdraw, Deposit, Balance).

balance = 10000.0
while True:
    print("\n1. Withdraw")
    print("2. Deposit")
    print("3. Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print("Please collect your cash. Remaining balance:", balance)
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount")
        else:
            balance += amount
            print("Deposit successful. Current balance:", balance)
    elif choice == "3":
        print("Current balance:", balance)
    elif choice == "4":
        print("Thank you for using the ATM")
        break
    else:
        print("Invalid choice")
