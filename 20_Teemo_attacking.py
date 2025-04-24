class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        
        res = 0

        for i in range(len(timeSeries) - 1):
            res += min(duration, timeSeries[i + 1] - timeSeries[i])

        return res + duration
    
# Time - O(N)
# Space - O(1)