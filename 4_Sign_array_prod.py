class Solution:
    def arraySign(self, nums) -> int:
        
        sign = 1

        for i in nums:

            if i == 0:
                return 0

            elif i < 0:
                sign *= -1

        return sign
    
# Time - O(N)
# Space - O(1)