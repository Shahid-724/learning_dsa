class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        # Declaring variables
        hashmap = dict()
        res = -1

        # Iterating over the input
        for i in range(len(s)):
            if s[i] in hashmap:
                res = max(res, i - hashmap[s[i]] - 1)
            else:
                hashmap[s[i]] = i

        # Returning the result
        return res
    
# Time - O(N)
# Space - O(1)