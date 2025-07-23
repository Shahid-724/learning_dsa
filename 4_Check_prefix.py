class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        # Declaring variables
        res = 0
        i = 0

        # Iterating over the sentence
        while i < len(sentence):
            if i == 0 or sentence[i - 1] == ' ':
                res += 1
                for j in searchWord:
                    if i >= len(sentence) or sentence[i] != j:
                        break
                    i += 1
                else:
                    return res
            i += 1

        # Returning the result
        return -1
    
# Time - O(N * M)
# space - O(1)