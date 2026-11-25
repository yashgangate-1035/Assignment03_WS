#Find the data type of every value in a mixed list.

data = [10, 3.14, "hello", True, [1, 2], (3, 4), {"a": 1}, {1, 2}, None, 2 + 3j]
for item in data:
    print(item, "->", type(item).__name__)
