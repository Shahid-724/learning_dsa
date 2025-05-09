class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        
        # Declaring variables
        allowed_chars = set(allowed)
        res = 0

        # Iterating over the words
        for word in words:
            for char in word:
                if char not in allowed_chars:
                    break
            else:
                res += 1

        # Returning the result
        return res
    
# Time - O(M * N) total no. of chars
# Space - O(1) allowed chars is at max of length 26