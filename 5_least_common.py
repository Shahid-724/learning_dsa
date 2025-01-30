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
def least_common(list1, list2):
    hashset = set()

    while list1:
        hashset.add(list1.data)
        list1 = list1.next

    least = float('inf')
    while list2:
        if list2.data in hashset and list2.data < least:
            least = list2.data
        list2 = list2.next

    return least

# Creating the nodes of a linked list 1
list1 = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

# Linking the nodes of list1
list1.next = b
b.next = c
c.next = d
d.next = e

# Creating the nodes of linked list 2
list2 = ListNode(4)
f = ListNode(5)
g = ListNode(6)
h = ListNode(7)
i = ListNode(8)

# Linking the nodes of list2
list2.next = f
f.next = g
g.next = h
h.next = i

# Printing the list before
print_ll(list1)
print_ll(list2)

# Performing the operations
a = least_common(list1, list2)

# Printing the list after
print(a)