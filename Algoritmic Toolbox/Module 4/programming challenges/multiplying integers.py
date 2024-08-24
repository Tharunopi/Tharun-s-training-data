def poly(x, y):
    ans = [0] * (len(x) + len(y) - 1)
    for i in range(len(x)):
        for j in range(len(y)):
            ans[i+j] += x[i] * y[j]
    return ans

x = [7, 8, 2]
y = [8, 6, 5]
print(poly(x, y))