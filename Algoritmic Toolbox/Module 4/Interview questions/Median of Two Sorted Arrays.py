def median(x, y):
    x = x + y
    mid = len(x) // 2
    if len(x) % 2 == 0:
        return x[mid-1], x[mid]
    else:
        return x[mid]

x = [1]
y = [3, 4]
print(median(x, y))