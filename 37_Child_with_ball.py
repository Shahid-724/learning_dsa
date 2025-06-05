class Solution:
    def numberOfChild(self, n: int, k: int) -> int:

        n -= 1
        
        full_rounds = k // (n)
        rem_rounds = k % (n)

        if full_rounds % 2 == 0:
            return rem_rounds
        return n - rem_rounds
    
# Time - O(1)
# Space - O(1)