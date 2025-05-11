class Solution:
    def frequencySort(self, nums):

        # A function for sorting
        def my_sort(n):
            return [hashmap[n], -n]
        
        # Declaring variables
        hashmap = dict()

        # Putting all the elements in a hashmap
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)

        # Using a custom sort 
        nums.sort(key=my_sort)

        # Returning the result
        return nums
    
# Time - O(N logN)
# Space - O(N)