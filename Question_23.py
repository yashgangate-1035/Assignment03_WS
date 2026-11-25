#Write a function to find the second-largest number in a list.

def second_largest(numbers):
    unique = sorted(set(numbers), reverse=True)
    if len(unique) < 2:
        return None
    return unique[1]

nums = list(map(int, input("Enter numbers separated by space: ").split()))
result = second_largest(nums)
if result is None:
    print("Second largest number does not exist")
else:
    print("Second largest number:", result)
