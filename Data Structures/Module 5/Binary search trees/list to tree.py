class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def listree(x):
    x = [None if i is None else Tree(i) for i in x]

    for i in range(len(x)):
        if x[i] is not None:
            left = (2*i) + 1
            right = (2*i) + 2
            if left < len(x):
                x[i].left = x[left]
            if right < len(x):
                x[i].right = x[right]
    return x[0]

Copytree = listree([1, 2, 3, 4, None, 5, 6, 7])