class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        
        res = len(prices)
        l = 0
        r = 1

        while r < len(prices):
            if prices[r - 1] - prices[r] == 1:
                res += r - l
            else:
                l = r
            r += 1

        return res
    
# Time - O(N)
# Space - O(1)