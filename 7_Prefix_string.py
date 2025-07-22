class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        
        i = 0
        j = 0

        while i < len(s) and j < len(words):
            length = len(words[j])

            if s[i:i + length] != words[j]:
                return False

            i += length
            j += 1

        return i == len(s)
    
# Time - O(N)
# Space - O(1)