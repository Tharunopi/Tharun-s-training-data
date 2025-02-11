from Tools.scripts.stable_abi import itemclasses


class Node:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self.val)

class DoublyLinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        cur = self.head
        while cur:
            print(cur, end="<->")
            cur = cur.next
        print("None")

    def push_front(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def top_front(self):
        print(self.head)

    def pop_front(self):
        self.head = self.head.next

    def push_back(self, val):
        new_node = Node(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def top_back(self):
        cur = self.head
        while cur.next:
            cur = cur.next
        print(cur)

    def pop_back(self):
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None

    def find(self, val):
        cur = self.head
        while cur:
            if cur.val == val:
                return print(f'Found {val}')
            cur = cur.next
        return print(f'Not found {val}')

    def erase(self, val):
        cur = self.head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next

    def empty(self):
        return self.head is None

    def add_before(self, key, val):
        cur = self.head
        while cur.next:
            if cur.next.val == key:
                new_ = Node(val)
                new_ = cur.next
                cur.next = new_
            cur = cur.next

item = DoublyLinkedLists()
item.push_front(1)
item.push_front(3)
item.push_back(5)
item.push_back(6)
item.push_back(7)
item.add_before(6, 99)
item.display()