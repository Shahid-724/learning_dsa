class Solution:
    def average(self, salary) -> float:
        
        # Sorting the input list
        salary.sort()

        # Calculating the average
        total = 0
        for i in range(1, len(salary) - 1):
            total += salary[i]

        # Returning the result
        return total / (len(salary) - 2)
    
# Time - O(N logN)
# Space - O(1)