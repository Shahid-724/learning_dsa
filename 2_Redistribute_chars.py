class Solution:
    def makeEqual(self, words) -> bool:
        
        # Declaring variables
        hashmap = dict()

        # Getting all the chars into the hashmap
        for word in words:
            for char in word:
                hashmap[char] = 1 + hashmap.get(char, 0)

        # Counting the chars to get the result
        n = len(words)
        for i in hashmap:
            if hashmap[i] % n:
                return False
        return True
    
# Time - O(M * N)
# Space - O(26)