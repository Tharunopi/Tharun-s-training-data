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
        if nodes[i] is not None:
            left = ( 2 * i ) + 1
            right = ( 2 * i ) + 2

            if left < len(nodes):
                nodes[i].left = nodes[left]
            if right < len(nodes):
                nodes[i].right = nodes[right]

    return nodes[0]

def inorder(x):
    if x is None:
        return

    inorder(x.left)
    print(x.val)
    inorder(x.right)

def get_max(x):
    if x is None:
        return 0
    return max(x.val, get_max(x.left), get_max(x.right))

def two_node(x):
    if x.left is None or x.right is None:
        return

    values = sorted([x.val, x.left.val, x.right.val])
    x.val, x.left.val, x.right.val = values[1], values[0], values[2]

    two_node(x.left)
    two_node(x.right)
    return x

def insert(x, val):
    if x is None:
        return Tree(val)

    if val < x.val:
        x.left = insert(x.left, val)
    elif val > x.val:
        x.right = insert(x.right, val)
    return x

def left(x):
    if x is None:
        return

    left(x.left)
    print(x.val)

x = [3, 6, 4, 9, 12, 8, 7]
root = converter(x)
left(root)