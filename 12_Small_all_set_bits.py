class Solution:
    def smallestNumber(self, n: int) -> int:
        
        res = 0
        power = 1

        while n:
            res += power
            power *= 2
            n //= 2

        return res
    
# Time - O(logN)
# Space - O(1)