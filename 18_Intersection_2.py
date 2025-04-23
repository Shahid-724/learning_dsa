class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        # Declaring variables
        hashmap = dict()
        res = []

        # Putting the first list into the hashmap
        for i in nums1:
            hashmap[i] = 1 + hashmap.get(i, 0)

        # Checking the second list and building result
        for i in nums2:
            if i in hashmap:
                res.append(i)
                if hashmap[i] == 1:
                    del hashmap[i]
                else:
                    hashmap[i] -= 1    

        # Returning the result
        return res
    
# Time - O(M + N)
# Space - O(N)