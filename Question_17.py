#Reverse a number and check if it is a palindrome.

n = int(input("Enter a number: "))
temp = n
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reversed number:", rev)
if rev == n:
    print("Palindrome")
else:
    print("Not a palindrome")
