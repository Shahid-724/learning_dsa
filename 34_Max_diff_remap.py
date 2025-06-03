class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        # Finding the first non nine number and first non zero
        first_non_zero = str(num)[0]
        first_non_nine = ' '
        for i in str(num):
            if i != '9':
                first_non_nine = i
                break

        # Remapping the digits
        min_number = str(num).replace(first_non_zero, '0')
        max_number = str(num).replace(first_non_nine, '9')

        # Returning the result
        return int(max_number) - int(min_number)
    
# Time - O(logN)
# Space - O(logN)