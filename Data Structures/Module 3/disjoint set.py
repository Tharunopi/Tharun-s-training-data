class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        print(self.parent)
        print(self.rank)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return

        if self.rank[px] < self.rank[py]:
            self.rank[px] = py
        elif self.rank[px] > self.rank[py]:
            self.rank[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

ds = DisjointSet(5)
ds.union(0, 2)
ds.union(1, 3)

print(ds.find(3))
print(ds.find(2))

print(ds.find(0) == ds.find(2))
print(ds.find(0) == ds.find(1))