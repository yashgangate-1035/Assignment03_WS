#Rotate a list to the left by k positions.

nums = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter k: "))
if nums:
    k = k % len(nums)
    nums = nums[k:] + nums[:k]
print(nums)
