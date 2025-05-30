class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        res = 1
        dir = -1

        for i in range(1, time + 1):
            if res == 1 or res == n:
                dir *= -1
            res += dir

        return res
    
# Time - O(N)
# Space - O(1)