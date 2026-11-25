#Convert a nested list into a tuple of tuples.

nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
result = tuple(tuple(inner) for inner in nested)
print(result)
