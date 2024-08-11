def binary_search(x, l, r, find):
    if l > r:
        return l -1

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(sorted(a), 7))