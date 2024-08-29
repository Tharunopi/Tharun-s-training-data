def count(x, y):
    dict = {y:0}
    k = True
    i = 0
    while k:
        if y == x[i]:
            dict[y] += 1
        if x[i] > y:
            k = False
        i += 1
    return dict

x = [2 ,3, 3, 3, 7, 9]
y = 3
print(count(x, y))