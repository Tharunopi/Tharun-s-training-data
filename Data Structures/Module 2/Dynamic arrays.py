# There is no static arrays in python

class Arrays:
    def __init__(self, val=None):
        if val is not None:
            self.val = val
        else:
            self.val = []

    def get(self, x):
        if x > len(self.val) or x < 0:
            return print("Error: Index out of bounds")
        return print(self.val[int(x)])

    def set(self, pos, val):
        if pos > len(self.val) or pos < 0:
            return print("Error: Index out of bounds")
        self.val[pos] = val

    def pushback(self, val):
        self.val.append(val)

    def size(self):
        return print(len(self.val))

    def remove(self, pos):
        self.val.pop(pos)

item = Arrays([1, 2, 3, 4])
item.remove(0)
item.size()