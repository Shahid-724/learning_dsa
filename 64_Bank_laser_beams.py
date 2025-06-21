class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        
        res = 0
        prev = 0

        for row in bank:
            ones = 0
            for col in row:
                if col == '1':
                    ones += 1
            
            if ones:
                res += prev * ones
                prev = ones

        return res
    
# Time - O(N * M)
# Space - O(1)