class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        # Declaring variables
        res = 0
        
        # Simulating the process
        while n > 1:
            matches = n // 2
            rem = n % 2
            res += matches
            n = matches + rem

        # Returning the result
        return res
    
# Time - O(logN)
# Space - O(1)