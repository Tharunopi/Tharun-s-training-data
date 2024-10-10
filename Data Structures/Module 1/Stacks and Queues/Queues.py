class Queues:
    def __init__(self, queue=None):
        if queue:
            self.queue = queue
        else:
            self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def display(self):
        return print(self.queue)

    def dequeue(self):
        if self.queue:
            self.queue.pop(0)

    def empty(self):
        if self.queue:
            return print("False")
        return print("True")

item = Queues([2, 3])
item.enqueue(1)
item.enqueue(2)
item.enqueue(3)
item.enqueue(4)
item.enqueue(5)
item.dequeue()
item.display()