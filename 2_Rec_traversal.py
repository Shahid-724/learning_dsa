# This code removes a node from a linked list
# The linked list is created using a node class

# The node class
class Node:

    # The instance variables
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

# Creating the nodes A --> B --> C --> D
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

# Creating the links
a.next = b
b.next = c
c.next = d

# A recursive function to traverse the linked list
def print_linked_list(head):
    if head is None:
        return
    print(head.val)
    print_linked_list(head.next)

# Printing the linked list nodes
print_linked_list(a)