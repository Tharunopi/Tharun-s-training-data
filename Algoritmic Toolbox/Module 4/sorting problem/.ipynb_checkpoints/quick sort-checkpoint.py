def quick_sort(x):
    if len(x) <= 1:
        return x

    p = x[-1]
    l = [i for i in x[:-1] if i <= p]
    r = [i for i in x[:-1] if i > p]

    l = quick_sort(l)
    r = quick_sort(r)

    return l + [p] + r

a = [6, 4, 8, 2, 9, 3, 9, 4, 7, 6, 1]
print(quick_sort(a))