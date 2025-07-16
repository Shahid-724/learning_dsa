class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        res = 0
        count = 0

        for i in s:
            if i == 'L':
                count += 1
            else:
                count -= 1

            if not count:
                res += 1

        return res
    
# Time - O(N)
# Space - O(1)