#Copy only the even-numbered lines from one file to another.

source = input("Enter source file name: ")
target = input("Enter destination file name: ")
with open(source, "r") as src:
    lines = src.readlines()
with open(target, "w") as dst:
    for number, line in enumerate(lines, start=1):
        if number % 2 == 0:
            dst.write(line)
print("Even-numbered lines copied successfully")
