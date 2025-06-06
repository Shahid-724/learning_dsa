class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        
        n = len(grid)
        res = 0

        for i in range(n):
            temp_row_max = float('-inf')
            temp_col_max = float('-inf')

            for j in range(n):
                temp_row_max = max(temp_row_max, grid[i][j])
                temp_col_max = max(temp_col_max, grid[j][i])
                if grid[i][j]:
                    res += 1

            res += temp_row_max + temp_col_max

        return res
    
# Time - O(N ^ 2)
# Space - O(1)