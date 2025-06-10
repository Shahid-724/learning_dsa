class Solution:
    def isThree(self, n: int) -> bool:
        
        divs = 0
        for i in range(1, n + 1):
            if n % i == 0:
                divs += 1
        return divs == 3
    
# Time - O(N)
# Space - O(1)