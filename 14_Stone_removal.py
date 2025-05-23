class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        Alice = True
        stones = 10

        while n >= 0:
            n -= stones
            Alice = not Alice
            stones -= 1

        return Alice
    
# Time - O(N)
# Space - O(1)