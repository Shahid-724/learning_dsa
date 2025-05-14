# The iterative code
class Solution:
    def reverseList(self, head):
        
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev
    
# Time - O(N)
# Space - O(1)


# The recursive code
class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        next_node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return next_node
    
# Time - O(N)
# Space - O(N)