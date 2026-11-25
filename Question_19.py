#Write a function to check if a string is a palindrome.

def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

text = input("Enter a string: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")
