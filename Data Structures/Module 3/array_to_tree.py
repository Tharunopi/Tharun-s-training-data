from collections import deque

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def converter(li):
    if not li:
        return None

    nodes = [None if i is None else Tree(i) for i in li]

    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_index = (2*i) + 1
            right_index = (2*i) + 2
            if left_index < len(li) and left_index is not None:
                nodes[i].left = nodes[left_index]
            if right_index < len(li) and right_index is not None:
                nodes[i].right = nodes[right_index]

    return nodes[0]

def inorder_traversal(node):
    if node is None:
        return
    print(node.val)
    inorder_traversal(node.left)
    inorder_traversal(node.right)

def bfs(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

li = [3, 6, 4, 9, 12, 8, 7, 14, 15, 13, 18, 11, 9]
node = converter(li)
inorder_traversal(node)