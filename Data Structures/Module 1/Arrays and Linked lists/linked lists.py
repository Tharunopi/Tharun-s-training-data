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
    if head is None or head.next is None:
        return None
    cur = head
    while cur.next.next:
        cur = cur.next
    cur.next = None
    return head

def erase(head, val):
    if head is None:
        return None
    if head.head == val:
        return head.next

    cur = head
    while cur.next:
        if cur.next.head == val:
            cur.next = cur.next.next
            return head
        cur = cur.next
    return head

def empty(head):
    if head is None:
        return True
    else:
        return False

def add_before(head, key, val):
    if head is None:
        return Node(val)

    cur = head
    while cur.next:
        if cur.next.head == key:
            new_node1 = Node(val)
            new_node1.next = cur.next
            cur.next = new_node1
            return head
        cur = cur.next
    return head

def add_after(head, key, val):
    if head is None:
        return Node(val)

    cur = head
    while cur.next:
        if cur.head == key:
            new_node = Node(val)
            new_node.next = cur.next
            cur.next = new_node
            return head
        cur = cur.next
    return head

Head = Node(5)
A = Node(6)
B = Node(7)
C = Node(8)

Head.next = A
A.next = B
B.next = C

c = add_after(Head, 6, 0)
printing_elements(c)
