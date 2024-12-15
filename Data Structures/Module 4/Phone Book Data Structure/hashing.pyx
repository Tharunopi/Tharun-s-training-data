class HashTableNames:

    def __init__(self, size=120):
        self.size = size
        self.table = [[] for i in range(self.size)]

    def hashing(self, value):
        return hash(value) % self.size

    def insert(self, key, value):
        index = self.hashing(value)
        self.table[index].append([key, value])
        return print("Added")

    def every(self):
        for i in self.table:
            if i:
                print(i)

ht = HashTableNames()
ht.insert(9360496526, "Tharun")
ht.insert(9360496527, "Atithya")
ht.insert(9360496758, "Cris Evans")

ht.every()