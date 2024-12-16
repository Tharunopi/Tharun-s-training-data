import hashlib

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class HashTable:
    def __init__(self):
        self.table = []

    def md5(self, s):
        return hashlib.md5(s.encode()).hexdigest()

    def add_string(self, s, node=None):
        hash_value = self.md5(s)
        new_node = Node(hash_value)
        if not node:
            return new_node
        new_node.next = node
        return new_node

    def del_string(self, s, node):
        hash_value = self.md5(s)
        cur = node
        while cur:
            if cur.val == hash_value:
                cur.next = cur.next.next
                return node
            cur = cur.next
        return node

    def find_string(self, s, node):
        hash_value = self.md5(s)
        cur = node
        while cur:
            if cur.val == hash_value:
                return print("yes")
            cur = cur.next
        return print("No")

    def check(self, i, node):
        cur = node
        itera = 0
        while cur and (i > itera):
            print(cur.val, end=" ")
            itera += 1
            cur = cur.next

ht = HashTable()
n1 = ht.add_string("world")
n2 = ht.add_string("hello", n1)
ht.find_string("hello5", n2)