class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        res = 0

        for i in range(len(s) - 2):
            if not (s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i + 2] == s[i]):
                res += 1
            
        return res
    
# Time - O(N)
# Space - O(1)