class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
        ptr = 0
        hashset = set()

        while ptr < len(word):
            temp = ''
            while ptr < len(word) and word[ptr].isdigit():
                temp += word[ptr]
                ptr += 1

            if temp:
                hashset.add(int(temp))

            ptr += 1

        return len(hashset)
    
# Time - O(N)
# Space - O(N)