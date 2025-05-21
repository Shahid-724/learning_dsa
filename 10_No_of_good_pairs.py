class Solution:
    def numIdenticalPairs(self, nums) -> int:
        
        hashmap = dict()
        res = 0

        for i in nums:
            if i in hashmap:
                res += hashmap[i]
            hashmap[i] = 1 + hashmap.get(i, 0)

        return res

# Time - O(N)
# Space - O(N)