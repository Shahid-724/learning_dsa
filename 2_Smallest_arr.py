# This code is used to find the smallest element in an array

def smallest(nums):
    min_val = float('inf')
    for i in nums:
        if i < min_val:
            min_val = i
    return min_val

nums = list(map(int, input('Enter space separated nums: ').split()))
print(smallest(nums))