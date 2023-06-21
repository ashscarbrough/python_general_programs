# '''
# Python program for conversion of binary tree to doubly linked list.
# '''

class Node:
    '''
    Node Class to represent Binary tree node
    Attributes:
        - data
        - left pointer
        - right pointer
    '''
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def print_tree(self):
        '''
        Method to print binary tree node value
        '''
        print(self.data)

previous = None  # Global variable to track previous Node

def binary_tree_to_dll(tree_root):
    '''
    Function to convert binary tree to doubly linked list
    '''

    # Base case
    if tree_root is None:
        return tree_root

    # Recursively convert left subtree
    head_node = binary_tree_to_dll(tree_root.left)

    global previous

    # If prev is empty, then this is the
    # first node of DLL
    if previous is None:
        head_node = tree_root

    else:
        tree_root.left = previous
        previous.right = tree_root

    # Update prev
    previous = tree_root

    # Recursively convert right subtree
    binary_tree_to_dll(tree_root.right)

    return head_node

def print_dll(head_node):
    '''
    Function to print nodes in given doubly linked list
    Input:
        - head_node - (Node object) the current node to analyze
    '''

    while head_node is not None:
        print(head_node.data, end=" ")
        head_node = head_node.right


# Driver program to test above functions
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    head = binary_tree_to_dll(root)

    # Print the converted list
    print_dll(head)
