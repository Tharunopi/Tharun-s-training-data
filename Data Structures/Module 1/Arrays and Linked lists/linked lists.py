class Node:

    def __init__(self, head, next=None):
        self.head = head
        self.next = next

    def __repr__(self):
        return str(self.head)

def printing_elements(Head):
    cur = Head
    while cur:
        print(cur, end="->")
        cur = cur.next
    print("None")

def search(head, val):
    cur = head
    while cur:
        if cur.val == val:
            return "Found"
        cur = cur.next
    return "Not found"

def push_front(head, val):
    new_node = Node(val, next=head)
    return new_node

def top_front(head):
    return head

def pop_front(head):
    if head is None:
        return None
    new_value = head.next
    return new_value

def push_back(head, val):
    new_value = Node(val)
    if head is None:
        return new_value

    cur = head
    while cur.next:
        cur = cur.next
    cur.next = new_value

    return head

def top_back(head):
    cur = head
    while cur.next:
        cur = cur.next
    return cur

def pop_back(head):
    cur = head
    while head:
        if cur.next is None:
            return

Head = Node(5)
A = Node(6)
B = Node(7)
C = Node(8)

Head.next = A
A.next = B
B.next = C

print(top_back(Head))
