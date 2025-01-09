# This code is used to find the max and min values from a list

def max_min(nums):
    max_val = float('-inf')
    min_val = float('inf')
    for i in nums:
        if i > max_val:
            max_val = i
        elif i < min_val:
            min_val = i
    return max_val, min_val

nums = list(map(int, input('Enter space separated nums: ').split()))
print(max_min(nums))

# Time Complexity = O(n)
# Space Complexity = O(1)