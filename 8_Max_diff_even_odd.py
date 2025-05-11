class Solution:
    def maxDifference(self, s: str) -> int:
        
        # Declaring variables
        hashmap = dict()
        odd_max = float('-inf')
        even_min = float('inf')

        # Putting the chars in the hashmap
        for i in s:
            hashmap[i] = 1 + hashmap.get(i, 0)

        # Iterating the hashmap to get min and max vals
        for i in hashmap:
            if hashmap[i] % 2:
                odd_max = max(odd_max, hashmap[i])
            else:
                even_min = min(even_min, hashmap[i])

        # Returning the result
        return odd_max - even_min
    
# Time - O(N)
# Space - O(1)

# The space is constant because the hashmap may contain at most 26 chars of english.