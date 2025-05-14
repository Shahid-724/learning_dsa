class Solution:
    def isPalindrome(self, head) -> bool:
        
        # Finding the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the second half
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Comparing the two halves
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
    
# Time - O(N)
# Space - O(1)