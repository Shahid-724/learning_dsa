# This code is used to check is an array can be split to two subarrays with equal sum

def canSplit(nums):
    left_sum = nums[0]
    total = sum(nums)
    for i in range(1, len(nums)):
        right_sum = total - left_sum
        if right_sum == left_sum:
            return True
        left_sum += nums[i]
    return False

# Time Complexity: O(n)
# Space Complexity: O(1)