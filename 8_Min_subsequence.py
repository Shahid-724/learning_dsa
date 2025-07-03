class Solution:
    def minSubsequence(self, nums):
        
        nums.sort(reverse=True)
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - nums[i] - left
            left += nums[i]
            if left > right:
                return nums[:i + 1]
            
# Time - O(N logN)
# Space - O(1)