class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        cur = self.head
        while cur:
            print(cur, end="->")
            cur = cur.next
        print("None")

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

    def find(self, key):
        cur = self.head
        while cur:
            if cur.val == key:
                return print(f'Found {key}')
            cur = cur.next
        return print(f'Not found {key}')

    def erase(self, val):
        cur = self.head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next

    def empty(self):
        return print(self.head is None)

    def add_before(self, key, val):
        cur = self.head
        while cur.next:
            if cur.next.val == key:
                new_node = Node(val)
                new_node.next = cur.next
                cur.next = new_node
                return
            cur = cur.next

    def add_after(self, key, val):
        cur = self.head
        while cur.next:
            if cur.val == key:
                new_node = Node(val)
                new_node.next = cur.next
                cur.next = new_node
                return
            cur = cur.next

item = LinkedList()
item.push_front(10)
item.push_back(100)
item.add_after(10, 12)
item.display()