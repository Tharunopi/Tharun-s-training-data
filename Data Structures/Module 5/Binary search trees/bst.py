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

def list_bst(x):
    def helper(left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        root = Tree(x[mid])
        root.left = helper(left, mid-1)
        root.right = helper(mid+1, right)

        return root
    return helper(0, len(x)-1)

