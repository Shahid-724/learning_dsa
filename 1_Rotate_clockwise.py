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

# Method to rotate the list clockwise by k
def rotate_clockwise(head, k):
    if not head:
        return head

    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    k = k % length
    if not k:
        return head

    cur = head
    for i in range(length - k - 1):
        cur = cur.next

    new_head = cur.next
    cur.next = None
    tail.next = head
    return new_head

# Creating the nodes of a linked list
a = ListNode(12)
b = ListNode(99)
c = ListNode(37)
d = ListNode(8)
e = ListNode(18)

# Linking the nodes
a.next = b
b.next = c
c.next = d
d.next = e

# Printing the list before
print_ll(a)

# Performing the operations
a = rotate_clockwise(a, 2)

# Printing the list after
print_ll(a)