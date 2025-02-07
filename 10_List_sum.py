# This code is used to get the sum of elements of a list using recursion

def list_sum(nums):
    if not nums:
        return 0
    return nums[0] + list_sum(nums[1:])

nums = list(map(int, input('Enter space separated nums: ').split()))
print(list_sum(nums))