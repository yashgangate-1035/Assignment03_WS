#Read a text file and count the number of lines, words, and characters.

name = input("Enter file name: ")
with open(name, "r") as file:
    text = file.read()
print("Lines:", len(text.splitlines()))
print("Words:", len(text.split()))
print("Characters:", len(text))
