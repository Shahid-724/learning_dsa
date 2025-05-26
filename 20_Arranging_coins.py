class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        low = 1
        high = n

        while low <= high:

            mid = (low + high) // 2
            val = mid * (mid + 1) // 2

            if val == n:
                return mid

            elif val < n:
                low = mid + 1

            else:
                high = mid - 1

        return high
    
# Time - O(logN)
# Space - O(1)