class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        # Declaring variables
        res = ''
        rev = True

        # Iterating over the string
        for i in range(0, len(s), k):
            temp = s[i:i + k]
            if rev:
                temp = temp[::-1]
            res += temp
            rev = not rev

        # Returning the result
        return res
    
# Time - O(N)
# Space - O(N)