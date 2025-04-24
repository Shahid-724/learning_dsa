class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        
        nums.sort() 
        res = 0

        for i in range(0, len(nums), 2):
            res += nums[i]

        return res
    
# Time - O(N logN)
# Space - O(1)