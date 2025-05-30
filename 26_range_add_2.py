class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        
        if not ops:
            return m * n

        row = float('inf')
        col = float('inf')

        for r, c in ops:
            row = min(row, r)
            col = min(col, c)

        return row * col
    
# Time - O(ops)
# Space - O(1)