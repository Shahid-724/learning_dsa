class Solution:
    def constructRectangle(self, n: int) -> list[int]:
        
        res = [1, 1]

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                res = [n // i, i]

        return res
    
# Time - O(Sqrt(N))
# Space - O(1)