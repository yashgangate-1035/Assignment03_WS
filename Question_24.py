#Merge two lists without duplicates.

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
merged = []
for item in list1 + list2:
    if item not in merged:
        merged.append(item)
print(merged)
