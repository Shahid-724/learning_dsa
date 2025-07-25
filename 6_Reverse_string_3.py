class Solution:
    def reverseWords(self, s: str) -> str:
        
        # Declaring variables
        res = ''
        l = 0
        r = 0

        # Iterating over s
        while l < len(s):
            while l < len(s) and s[l] != ' ':
                l += 1
            r = l - 1
            while r >= 0 and s[r] != ' ':
                res += s[r]
                r -= 1
            res += ' '
            l += 1

        return res.strip()
    
# Time - O(N)
# Space - O(N)