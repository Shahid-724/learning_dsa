class Solution:
    def countTriples(self, n: int) -> int:
        
        res = 0

        for i in range(1, n):
            for j in range(i + 1, n + 1):
                temp = (i ** 2 + j ** 2) ** 0.5
                if temp == int(temp) and temp <= n:
                    res += 2

        return res
    
# Time - O(N ^ 2)
# Space - O(1)