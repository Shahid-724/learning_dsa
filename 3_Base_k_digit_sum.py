class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        res = 0

        while n:
            res += (n % k)
            n //= k

        return res
    
# Time - O(logN base K)
# Space - O(1)