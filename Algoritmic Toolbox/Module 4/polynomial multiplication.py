def poly_mul(x, y):
    ans = [0] * (len(a)+len(b)-1)
    for i in range(len(x)):
        for j in range(len(y)):
            ans[i+j] += x[i] * y[j]
    return ans

a = [4, 3, 2, 1]
b = [1, 2, 3, 4]
print(poly_mul(a, b))

