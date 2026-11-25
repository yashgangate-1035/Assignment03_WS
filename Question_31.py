#Check whether one set is a subset of another.

set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))
if set1.issubset(set2):
    print("First set is a subset of the second set")
else:
    print("First set is not a subset of the second set")
