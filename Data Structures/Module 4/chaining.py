class Node:
    def __init__(self, head, next=None):
        self.head = head
        self.next = next

def push(head, val):
    new_val = Node(val, next=None)

    if head is None:
        return new_val

    cur = head
    while cur.next:
        cur = cur.next
    cur.next = new_val

    return head

def front(head, val):
    new_val = Node(val, head)
    return new_val

def pp(head):
    cur = head
    while cur:
        print(cur.head, end="->")
        cur = cur.next
    print("None")

one = Node(5)
push(one, val=7)
push(one, val=9)
push(one, val=11)
push(one, val=13)
pp(front(one, 3))


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

a = Tree(5)
b = Tree(3)
c = Tree(7)
d = Tree(6)

a.left = b
a.right = c
c.left = d

inorder(a)