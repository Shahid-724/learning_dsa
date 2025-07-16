class Solution:
    def maxPower(self, s: str) -> int:
        result = 0
        count = 1
        cur = s[0]
        for i in range(1, len(s)):
            if s[i] == cur:
                count += 1
            else:
                cur = s[i]
                result = max(result, count)
                count = 1
        result = max(result, count)
        return result
    
# Time - O(N)
# Space - O(1)