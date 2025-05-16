class ListNode:
    ...

# The iterative Code
class Solution:
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return dummy.next
    
# Time - O(M + N)
# Space - O(1)


# The recursive code
class Solution:
    def mergeTwoLists(self, list1, list2) :
        
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
# Time - O(M + N)
# Space - O(M + N)