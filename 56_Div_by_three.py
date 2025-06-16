class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        
        res = 0

        for i in nums:
            if i % 3:
                res += 1

        return res
    
# Time - O(N)
# Space - O(1)