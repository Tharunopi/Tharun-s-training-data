import heapq

class Heap:
    def __init__(self, val):
        self.val = val

    def sort(self, type=None):
        ans = []

        if type is None:
            heapq.heapify(self.val)
            for i in range(len(self.val)):
                min = heapq.heappop(self.val)
                ans.append(min)
            return print(ans)
        elif type == "max":
            self.val = [-i for i in self.val]
            heapq.heapify(self.val)
            for i in range(len(self.val)):
                max = heapq.heappop(self.val)
                ans.append(-max)
            return print(ans)

x = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
item = Heap(x)
item.sort("max")