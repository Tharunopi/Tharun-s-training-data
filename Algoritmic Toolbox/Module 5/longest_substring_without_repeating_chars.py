class Operation:
    def __init__(self, text:str):
        self.text = text

    def longest_substring(self):
        n = []
        for i in self.text:
            if i not in n:
                n.append(i)
            else:
                n.pop(0)
                n.append(i)
        return n

# operation = Operation("abcae")
# print(operation.longest_substring())