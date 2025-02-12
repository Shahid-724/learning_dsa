# This code is used to reverse a linked list recursively
# Defining a class to create the nodes of a Linked list
class ListNode:

    # The instance variables
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Creating a few nodes to make a linked list
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)

# Connecting the nodes to form a linked list
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# Defining a function to print a linked list
def print_ll(head):
    while head:
        print(head.data, end=' --> ')
        head = head.next
    print('None')

# Defining a function to reverse a linked list recursively
def reverse_ll(head):

    # The base case
    if not head or not head.next:
        return head
    
    # The unit of work to be done
    p = reverse_ll(head.next)
    head.next.next = head
    head.next = None
    return p

# Printing the linked list before calling the function
print_ll(a)

# Calling the function and saving the result
r_head = reverse_ll(a)

# Printing the linked list after calling the function
print_ll(r_head)