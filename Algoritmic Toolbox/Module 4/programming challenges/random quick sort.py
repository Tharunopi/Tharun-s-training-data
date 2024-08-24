def quick_sort(x):
    if len(x) <= 1:
        return x
    p = x[-1]
    l = [i for i in x[:-1] if i <= p]
    r = [i for i in x[:-1] if i > p]

    l = quick_sort(l)
    r = quick_sort(r)

    return l + [p] + r

x = [2, 3, 9, 2, 2]
print(quick_sort(x))