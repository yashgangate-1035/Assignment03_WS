#Find the second-largest and second-smallest elements.

nums = list(map(int, input("Enter numbers separated by space: ").split()))
unique = sorted(set(nums))
if len(unique) < 2:
    print("Not enough distinct elements")
else:
    print("Second largest:", unique[-2])
    print("Second smallest:", unique[1])
