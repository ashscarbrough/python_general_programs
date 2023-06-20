class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

# In-Order Traversal

def inorderTraversal(root):
    answer = []

    inorderTraversalUtil(root, answer)
    return answer

def inorderTraversalUtil(root, answer):

    if root is None:
        return

    inorderTraversalUtil(root.left, answer)
    answer.append(root.val)
    inorderTraversalUtil(root.right, answer)
    return

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(inorderTraversal(root))

## Pre-order Traversal

def preorderTraversal(root):
    answer = []

    preorderTraversalUtil(root, answer)
    return answer

def preorderTraversalUtil(root, answer):

    if root is None:
        return 

    answer.append(root.val)

    preorderTraversalUtil(root.left, answer)

    preorderTraversalUtil(root.right, answer)

    return

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(preorderTraversal(root))


# PostOrder Traversal
def postorderTraversal(root):
    answer = []

    postorderTraversalUtil(root, answer)
    return answer

def postorderTraversalUtil(root, answer):

    if root is None:
        return

    postorderTraversalUtil(root.left, answer)

    postorderTraversalUtil(root.right, answer)

    answer.append(root.val)

    return

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(postorderTraversal(root))
