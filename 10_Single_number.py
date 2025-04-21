class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        # Declaring variables
        res = 0

        # Finding the single number using xor
        for i in nums:
            res ^= i

        # Returning the result
        return res
    
# Time - O(N)
# Space - O(1)