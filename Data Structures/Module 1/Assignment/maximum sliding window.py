def max_sliding_window(x, y):

    bo = True
    max_val = len(x)
    i, j = 0, y

    li = []

    while bo:
        k = x[i:j]
        print(k)
        li.append(max(x[i:j]))
        i += 1
        j += 1
        if j >= max_val+1 or len(k) < y:
            bo = False
    return li

x = [2, 7, 3, 1, 5, 2, 6, 2]
y = 4
print(max_sliding_window(x, y))