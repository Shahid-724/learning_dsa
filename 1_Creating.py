# This code is about creating a linked list
# To do this create a node class

# Creating the node class
class Node:

    # The instance variables
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


# The linked list
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

# Creating the links
a.next = b
b.next = c
c.next = d

# Traversal of the linked list
def print_linked_list(head):
    cur = head
    while cur is not None:
        print(cur.val)
        cur = cur.next

# Printing the linked list using the function
print_linked_list(a)