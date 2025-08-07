# This code is used to rotate a linked list in clockwise direction by k nodes

# Creating a linked list
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Method to print a linked list
def print_ll(head):
    while head:
        print(head.data, end=' --> ')
        head = head.next
    print('None')

# Method to get the lowest common element of two linked lists
def delete_m_after_n(head, m, n):
    p1 = head
    p2 = head
    for i in range(m - 1):
        p1 = p1.next
    for i in range(m + n):
        p2 = p2.next
    p1.next = p2
    return head

# Creating the nodes of a linked list 1
head = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

# Linking the nodes of list1
head.next = b
b.next = c
c.next = d
d.next = e

# Printing the list before
print_ll(head)

# Performing the operations
a = delete_m_after_n(head, 2, 2)

# Printing the list after
print_ll(a)