def binary_search(x, y, start=0):
    if len(x) == 0:
        return -1
    mid = len(x)//2
    if x[mid] == y:
        return start+mid
    elif y > x[mid]:
        return binary_search(x[mid+1:], y, start+mid+1)
    else:
        return binary_search(x[:mid], y, start)

x = [1, 2, 4, 6]
print(binary_search(x, 4))