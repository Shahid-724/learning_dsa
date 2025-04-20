class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        
        # Declaring variables
        l = m + n - 1

        # Using while loop
        while m and n:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[l] = nums1[m - 1]
                m -= 1
            else:
                nums1[l] = nums2[n - 1]
                n -= 1
            l -= 1

        # The remaining elements of nums2
        while n:
            nums1[l] = nums2[n - 1]
            n -= 1
            l -= 1

# Time - O(M + N)
# Space - O(1)