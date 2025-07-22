class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        # Declaring variables
        idx = 0
        res = ''

        # Getting the chars index
        for i in range(len(word)):
            if word[i] == ch:
                idx = i
                break

        # Building the reverse part of the result
        temp = idx + 1
        while idx >= 0:
            res += word[idx]
            idx -= 1

        
        # Building the remaining part
        while temp < len(word):
            res += word[temp]
            temp += 1

        # Returning the result
        return res
    
# Time - O(N)
# Space - O(N)