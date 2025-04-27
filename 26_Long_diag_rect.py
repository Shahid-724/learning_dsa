class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        
        res = 0
        diag = 0

        for l, b in dimensions:
            temp = (l ** 2 + b ** 2) ** 0.5
            if temp > diag:
                diag = temp
                res = l * b
            elif temp == diag:
                res = max(res, l * b)

        return res
    
# Time - O(N)
# Space - O(1)