class Solution:
    def middleNode(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

# Time - O(N)
# Space - O(1)