# This code is used to reverse an array
# Taking an array as input
nums = list(map(int, input('Enter space separated numbers: ').split()))

# Reversing the array
for i in range(len(nums) // 2):
    nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]

# Printing the output
print(nums)