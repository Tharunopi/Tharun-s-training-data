class Stack:
    def __init__(self, value=None):
        if value is not None:
            self.value = value
        else:
            self.value = []

    def push(self, val):
        self.value.append(val)

    def pop(self):
        self.value.pop(-1)

    def max(self):
        return print(max(self.value))

item = Stack()
item.push(2)
item.push(1)
item.max()
item.pop()
item.max()