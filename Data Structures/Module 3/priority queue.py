
class Priority:
    def __init__(self):
        self.ans = []

    def insert(self, val, pri):
        self.ans.append([val, pri])
        self.ans = sorted(self.ans, key= lambda x:x[1], reverse=True)

    def extract(self):
        return print(self.ans[0])

    def remove(self, val):
        elements = [i[0] for i in self.ans]
        value = elements.index(val)
        self.ans.pop(value)
        return print(self.ans)

    def change_priority(self,val, new_pri):
        elements = [i[0] for i in self.ans]
        value = elements.index(val)
        self.ans[value][1] = new_pri

    def display(self):
        return print(self.ans)

item = Priority()
item.insert(10, 2)
item.insert(18, 10)
item.insert(2, 12)
item.extract()
item.change_priority(2, 11)
item.display()