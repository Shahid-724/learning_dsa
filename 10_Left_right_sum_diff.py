class Solution:
    def leftRightDifference(self, nums):
        
        left = 0
        total = sum(nums)
        res = []

        for i in range(len(nums)):
            right = total - left - nums[i]
            res.append(abs(left - right))
            left += nums[i]

        return res

# Time - O(N)
# Space - O(N)