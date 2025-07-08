class Solution:
    def sortSentence(self, s: str) -> str:
        
        words = s.split()
        hashmap = dict()

        for i in range(len(words)):
            hashmap[int(words[i][-1])] = words[i][:-1]

        res = ''
        for i in sorted(hashmap):
            res += hashmap[i] + ' '

        return res.rstrip()
    
# Time - O(N)
# Space - O(N)