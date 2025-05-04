# Using Two pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        p1 = 0
        p2 = 0

        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1

        return p1 == len(s)
    
# Time - O(N)
# Space - O(1)

# Recursion approach
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # There are 2 base cases
        if not s:
            return True
        if not t:
            return False

        # There are 2 recursive calls
        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        return self.isSubsequence(s, t[1:])
    
# Time - O(2 ^ (M + N))
# Space - O(N)