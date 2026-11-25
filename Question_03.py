#Remove all duplicate values from a mixed list while preserving the original order.

data = [1, "a", 2, "a", 1, 3.5, 2, 3.5, "b", (1, 2), (1, 2)]
result = []
for item in data:
    if item not in result:
        result.append(item)
print(result)
