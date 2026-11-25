#Handle file-not-found errors while reading a file.

name = input("Enter file name: ")
try:
    with open(name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: The file", name, "was not found.")
