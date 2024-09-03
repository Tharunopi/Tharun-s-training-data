def selection_sort(x):
    for i in range(len(x)):
        step = x[i:]
        mii = minimum(step)
        idex = step.index(mii)
        if step[0] != mii:
            step[0], step[idex] = step[idex], step[0]
        x[i:] = step
    return x
def minimum(x):
    ans = x[0]
    for i in x:
        if i < ans:
            ans = i
    return ans

a = [2, 4, 8, 5, 2]
print(selection_sort(a))