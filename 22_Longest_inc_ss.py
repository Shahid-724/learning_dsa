class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        
        res = 1
        temp = 1

        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                res = max(res, temp)
                temp = 1
            else:
                temp += 1

        res = max(res, temp)

        return res
    
# Time - O(N)
# Space - O(1)