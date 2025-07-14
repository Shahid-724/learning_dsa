class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        
        s1 = ''
        ptr = 0

        for word in word1:
            for char in word:
                s1 += char

        for word in word2:
            for char in word:
                if ptr >= len(s1) or char != s1[ptr]:
                    return False
                ptr += 1

        return ptr == len(s1)
    
# Time - O(M + N)
# Space - O(N)