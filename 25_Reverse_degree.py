class Solution:
    def reverseDegree(self, s: str) -> int:
        
        res = 0

        for i in range(len(s)):

            temp = 26 - (ord(s[i]) - 97)
            res += temp * (i + 1)

        return res
    
# Time - O(N)
# Space - O(1)