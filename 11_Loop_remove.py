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

# Method to detect and find the length of a loop
def loop_length(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    length = 1
    if slow == fast:
        while slow.next != fast:
            slow = slow.next
            length += 1
    return length

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
h.next = e

# Printing the list before
# print_ll(head)

# Performing the operations
a = loop_length(head)

# Printing the list after
print(a)