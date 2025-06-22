class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        
        piles.sort(reverse=True)
        res = 0

        for i in range(len(piles) - len(piles) // 3):
            if (i - 1) % 2 == 0:
                res += piles[i]

        return res
    
# Time - O(N logN)
# Space - O(1)