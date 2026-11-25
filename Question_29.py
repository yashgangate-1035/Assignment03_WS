#Count the frequency of each element in a tuple.

data = tuple(input("Enter elements separated by space: ").split())
frequency = {}
for item in data:
    frequency[item] = frequency.get(item, 0) + 1
for key, value in frequency.items():
    print(key, ":", value)
