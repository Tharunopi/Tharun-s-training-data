class Array:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f'Array has been initilazed {self.x}'

x = [1, 2, 3, 4, 5]
item = Array(x)
print(item)