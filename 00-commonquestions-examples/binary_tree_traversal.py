'''
Classes and functions for traversal of binary tree
'''

class TreeNode:
    '''
    Tree Node Class to represent Binary tree node
    Attributes:
        - value
        - left pointer
        - right pointer
    '''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def print_tree(self):
        '''
        Method to print binary tree node value
        '''
        print(self.val)


#### In-Order Traversal ####
def inorder_traversal(binary_tree_root):
    '''
    Function to traverse binary tree In-Order
    Input: binary_tree_root - (TreeNode object)
    Output: answer - (list) for in order traversal
    '''
    answer = []

    inorder_traversal_util(binary_tree_root, answer)
    return answer

def inorder_traversal_util(root_node, answer):
    '''
    Function for utility iterator to recursively traverse binary tree In-Order
    Input: 
        - root_node - (TreeNode object) root node to traverse from
        - answer - list() to store the order of In-Order traversal
    Output: None
    '''

    if root_node is None:
        return

    inorder_traversal_util(root_node.left, answer)
    answer.append(root_node.val)
    inorder_traversal_util(root_node.right, answer)
    return


#### Pre-order Traversal ####
def preorder_traversal(binary_tree_root):
    '''
    Function
    '''
    answer = []

    preorder_traversal_util(binary_tree_root, answer)
    return answer

def preorder_traversal_util(root_node, answer):
    '''
    Function
    '''
    if root_node is None:
        return

    answer.append(root_node.val)

    preorder_traversal_util(root_node.left, answer)

    preorder_traversal_util(root_node.right, answer)

    return

# PostOrder Traversal
def postorder_traversal(binary_tree_root):
    '''
    Function
    '''
    answer = []

    postorder_traversal_util(binary_tree_root, answer)
    return answer

def postorder_traversal_util(root_node, answer):
    '''
    Function
    '''
    if root_node is None:
        return

    postorder_traversal_util(root_node.left, answer)

    postorder_traversal_util(root_node.right, answer)

    answer.append(root_node.val)

    return


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)


    print(inorder_traversal(root))
    print(preorder_traversal(root))
    print(postorder_traversal(root))
