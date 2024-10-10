class Ini_Stack:
    def __init__(self, val=None):
        if val:
            self.val = val
        else:
            self.val = []

    def push(self, val):
        self.val.append(val)

    def display(self):
        return print(self.val)

    def top(self):
        return print(self.val[-1])

    def remove(self):
        if self.val:
            return print(self.val.pop(-1))
        return print(f'Unable to remove element!!')

    def empty(self):
        if self.val:
            return print("False")
        return print("True")

item = Ini_Stack()
item.push(5)
item.push(5)
item.display()
item.empty()