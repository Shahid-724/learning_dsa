class Solution:
    def findValidPair(self, s: str) -> str:
        
        # Declaring variables
        hashmap = dict()

        # Putting the chars into a hashmap
        for i in s:
            hashmap[i] = 1 + hashmap.get(i, 0)

        # Checking for valid pairs
        for i in range(len(s) - 1):
            if s[i] != s[i + 1] and hashmap[str(s[i])] == int(s[i]) and hashmap[str(s[i + 1])] == int(s[i + 1]):
                return s[i] + s[i + 1]

        return ''
    
# Time - O(N)
# Space - O(1)