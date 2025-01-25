# This code is used to sort the first half in ascending and
# Second half in descending order
# Taking input for an array
nums = list(map(int, input('Enter space separated numbers: ').split()))

# The array initially needs to be sorted
nums.sort()

# Getting the middle point in the array
mid = len(nums) // 2

# Sorting the first half in ascending order
first_half = sorted(nums[:mid])

# Sorting the second half in descending order
second_half = sorted(nums[mid:], reverse=True)

# Combining the two halves
result = first_half + second_half

# Printing the output
print(result)