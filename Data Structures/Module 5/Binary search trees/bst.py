class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

def list_to_bst(x):
    nodes = [Tree(i) for i in x]
