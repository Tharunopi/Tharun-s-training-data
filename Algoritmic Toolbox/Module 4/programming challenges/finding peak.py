def peak(x):
    if len(x) == 2:
        return max(x)
    if len(x) == 1:
        return x[0]
    mid = len(x)//2
    if x[mid] > x[mid+1] and x[mid] > x[mid-1]:
        return x[mid]
    elif x[mid] < x[mid-1]:
        return peak(x[:mid])
    else:
        return peak(x[mid+1:])

a = [3, 4, 2, 12, 13, 5, 8, 5, 7, 6, 1, 10, 15, 17]
print(peak(a))