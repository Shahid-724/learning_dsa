# This code is used to find the largest element in an array

def largest(nums):
    max_val = float('-inf')
    for i in nums:
        if i > max_val:
            max_val = i
    return max_val

nums = list(map(int, input('Enter space separated nums: ').split()))
print(largest(nums))