class Solution:
    def totalMoney(self, n: int) -> int:
        
        # Declaring variables
        res = 0
        count = 1
        start = 1
        week = 1

        # Iterating through the range
        for i in range(n):
            res += start
            count += 1
            start += 1
            if count > 7:
                week += 1
                start = week
                count = 1

        # Returning the result
        return res
    
# Time - O(N)
# Space - O(1)

# Most optimized code
class Solution:
    def totalMoney(self, n: int) -> int:
        k = n // 7
        F = 28
        L = 28 + (k - 1) * 7
        arithmetic_sum = k * (F + L) // 2
        
        monday = 1 + k
        final_week = 0
        for day in range(n % 7):
            final_week += monday + day
        
        return arithmetic_sum + final_week
    
# Time - O(1)
# Space - O(1)