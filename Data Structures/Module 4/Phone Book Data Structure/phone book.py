class HashTable:

    def __init__(self, size=7):
        self.size = size
        self.table = [[] for i in range(self.size)]

    def hashing(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hashing(key)

        self.table[index].append([key, value])
        return print("Contact added")

    def every(self):
        for i in self.table:
            if i:
                print(i)

ht = HashTable()
ht.insert(9360496526, "Tharun")
ht.insert(9360496527, "Atithya")
ht.insert(9360496758, "Cris Evans")

ht.every()