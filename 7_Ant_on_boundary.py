class Solution:
    def returnToBoundaryCount(self, nums) -> int:
        
        res = 0
        pos = 0

        for i in nums:
            pos += i
            if not pos:
                res += 1

        return res
    
# Time - O(N)
# Space - O(1)