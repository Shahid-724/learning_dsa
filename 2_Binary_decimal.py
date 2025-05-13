class Solution:
    def getDecimalValue(self, head) -> int:
        
        # Reversing the linked list
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        # Calculating the decimal value
        res = 0
        power = 1
        while prev:
            res += prev.val * power
            prev = prev.next
            power *= 2

        return res