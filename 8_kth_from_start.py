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

# Method to return kth node from the start
def kth_from_start(head, k):
    while head:
        k -= 1
        if k == 0:
            return head.data
        head = head.next
    return None

# Creating the nodes of a linked list 1
head = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(3)
e = ListNode(3)
f = ListNode(4)
g = ListNode(5)
h = ListNode(5)

# Linking the nodes of list1
head.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h

# Printing the list before
print_ll(head)

# Performing the operations
a = kth_from_start(head, 6)

# Printing the list after
print(a)