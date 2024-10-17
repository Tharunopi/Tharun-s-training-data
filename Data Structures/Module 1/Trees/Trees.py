from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'

def pre_order_traversal(node):
    if not node:
        return
    print(node.val)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

def in_order_traversal(node):
    if not node: return
    in_order_traversal(node.left)
    print(node.val)
    in_order_traversal(node.right)

def bfs(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
        

a = Node(2)
b = Node(1)
c = Node(3)

a.left = b
a.right = c

bfs(a)