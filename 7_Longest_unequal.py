class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        
        res = [words[0]]
        prev = groups[0]

        for i in range(1, len(groups)):
            if groups[i] != prev:
                res.append(words[i])
                prev = groups[i]

        return res
    
# Time - O(N)
# Space - O(N)