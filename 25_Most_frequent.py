class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        
        hashmap = dict()   
        count = 0
        res = float('inf')

        for i in nums:
            if i % 2 == 0:
                hashmap[i] = 1 + hashmap.get(i, 0)
                count = max(count, hashmap[i])

        for i in hashmap:
            if hashmap[i] == count:
                res = min(res, i)

        if res == float('-inf')or not count:
            return -1
        return res
    
# Time - O(N)
# Space - O(N)