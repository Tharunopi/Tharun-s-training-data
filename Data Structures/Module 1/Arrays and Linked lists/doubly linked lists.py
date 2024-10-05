class Node:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self.val)

def printing_elements(head):
    cur = head
    while cur:
        print(cur, end="<->")
        cur = cur.next
    print("None")

def insert_begning(head, val):
    new_node = Node(val, next=head)
    head.prev = new_node
    return new_node

head = Node(1)
second = insert_begning(head, 4)
printing_elements(second)