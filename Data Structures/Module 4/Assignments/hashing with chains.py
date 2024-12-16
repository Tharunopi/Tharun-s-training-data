import hashlib

class HashTable:

    def __init__(self, buckets):
        self.buckets = buckets
        self.table = []

    def md5(self, s):
        return hashlib.md5(s.encode()).hexdigest()

    def printing_hash(self, s):
        print(self.md5(s))

    def add_string(self, s):
        hash_value = self.md5(s)
        self.table = [hash_value] + self.table
        return print("String added")

    def del_string(self, s):
        hash_value = self.md5(s)
        if self.table:
            for i in self.table:
                if i == hash_value:
                    self.table.remove(hash_value)
                    return print("Removed")
        return print("Match not found!")

    def find_string(self, s):
        hash_value = self.md5(s)
        if self.table:
            for i in self.table:
                if i == hash_value:
                    return print("Yes")
        return print("No")

    def check(self, i):
        if len(self.table) < i:
            return print("Invalid length")
        return print(self.table[i])

ht = HashTable(10)
ht.add_string("world")
ht.add_string("hello")
ht.check(4)
ht.find_string("world")
ht.find_string("World")
ht.del_string("world")
ht.check(4)
ht.del_string("Hello")
ht.add_string("Good")
ht.check(2)
ht.del_string("good")
