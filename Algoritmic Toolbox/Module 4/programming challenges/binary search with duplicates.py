from collections import Counter
def binary_search(x, key, start=0):
    if len(x) == 0:
        return -1
    mid = len(x)//2
    if x[mid] == key:
        return mid + start
    elif key > x[mid]:
        return binary_search(x[mid+1:], key, start+mid+1)
    else:
        return binary_search(x[:mid], key, start)

x = [1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8, 8, 9, 10]
count = Counter(x)
key = 3
m = binary_search(x, key)
if key in count and count[key] > 1:
    print(m - (count[key]-1))
else:
    print(m)