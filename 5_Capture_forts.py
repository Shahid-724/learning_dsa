class Solution:
    def captureForts(self, forts: list[int]) -> int:
        
        # Declaring variables
        res = 0
        last_fort = 0

        # Iterating over forts
        for i in range(len(forts)):
            if forts[i]:
                if forts[last_fort] == -forts[i]:
                    res = max(res, i - last_fort - 1)
                last_fort = i

        # Returning the result
        return res
    
# Time - O(N)
# Space - O(1)