class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def converter(x):
    if x is None:
        return None

    nodes = [Tree(i) if i is not None else None for i in x]
    for i in range(len(nodes)):
        if nodes[i] is not None:  # Add this check
            left_index = (2*i) + 1
            right_index = (2*i) + 2
            if left_index < len(x):
                nodes[i].left = nodes[left_index]
            if right_index < len(x):
                nodes[i].right = nodes[right_index]

    return nodes[0]

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val, )
    inorder(node.right)

def node_counter(node):
    if node is None:
        return 0
    return 1 + max(node_counter(node.left), node_counter(node.right))

x = [3, 6, 4, 9, 12, 8, 7]
root = converter(x)
# inorder(root)
print(len(x))
print(node_counter(root))