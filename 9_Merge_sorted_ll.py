# This code is used to merge two sorted linked lists together
# Defining a class to create the nodes of a linked list
class ListNode:

    # The instance variables
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Creating a few nodes to make two linked lists
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)
h = ListNode(8)
i = ListNode(9)
j = ListNode(10)

# Connection the linked lists
a.next = c
b.next = d
c.next = e
d.next = f
e.next = g
f.next = h
g.next = i
h.next = j

# Defining a function to print the elements of the linked list
def print_ll(head):
    while head:
        print(head.data, end=' --> ')
        head = head.next
    print('None')

# Defining a function to merge the two sorted linked lists
def merge_sorted_ll(head1, head2):

    # These are the two base cases
    if not head1:
        return head2
    if not head2:
        return head1
    
    # The recursive calls
    if head1.data < head2.data:
        head1.next = merge_sorted_ll(head1.next, head2)
        return head1
    else:
        head2.next = merge_sorted_ll(head1, head2.next)
        return head2
    
# Printing the two linked lists before merging
print_ll(a)
print_ll(b)

# Merging the two linked list using the function
result = merge_sorted_ll(a, b)

# Printing the linked lists after merging
print_ll(result)