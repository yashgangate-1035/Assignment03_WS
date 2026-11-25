#Create a dictionary from two lists (keys and values).

keys = input("Enter keys separated by space: ").split()
values = input("Enter values separated by space: ").split()
result = dict(zip(keys, values))
print(result)
