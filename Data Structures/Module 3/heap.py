import heapq

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def converter(x):
    nodes = [Tree(i) if i is not None else None for i in x]

    for i in range(len(nodes)):
        if i is not None:
            left = (2*i) + 1
            right = (2*i) + 2
            if left < len(nodes):
                nodes[i].left = nodes[left]
            if right < len(nodes):
                nodes[i].right = nodes[right]

    return nodes[0]

def inorder(x):
    if x is None:
        return

    inorder(x.left)
    print(x.val)
    inorder(x.right)

def heapsort(x):
    x = [-i for i in x]
    heapq.heapify(x)
    ans = []
    for i in range(len(x)):
        mn = heapq.heappop(x)
        ans.append(-mn)
    return ans

a = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

print(heapsort(a))