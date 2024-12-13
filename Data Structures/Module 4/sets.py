class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(self.size)]

    def hashing(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hashing(key)

        if not self.table[index]:
            self.table[index].append([key, value])
            return print("Added")

        that_table = self.table[index]
        if that_table[0][0] == key:
            that_table[0][1] = value
            return print("Altered")

    def get(self, key):
        index = self.hashing(key)

        if self.table[index]:
            if self.table[index][0][0] == key:
                return print(self.table[index][0][1])

        raise KeyError(key)

    def remove(self, key):
        index = self.hashing(key)

        if self.table[index]:
            if self.table[index][0][0] == key:
                self.table[index][0][1] = None
                return print("Removed")
        raise KeyError(key)

    def every_value(self):
        for i in self.table:
            if i:
                print(f"key: {i[0][0]}, value: {i[0][1]}", end="||")

ht = HashTable(10)
ht.insert(3, "king")
ht.insert(36, "godzilla")
ht.insert(75, "ben tennison")
ht.insert(125, "king gidhorah")
ht.every_value()