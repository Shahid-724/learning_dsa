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

# Method to return kth node from the end
def kth_from_end(head, k):
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
    
    cur = head
    for i in range(length - k):
        cur = cur.next
    return cur.data

# Creating the nodes of a linked list 1
head = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)
h = ListNode(8)

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
a = kth_from_end(head, 6)

# Printing the list after
print(a)