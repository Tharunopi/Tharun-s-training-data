def navie_poly_multiplication(a, b):
    ans = [0] * (len(a) + len(b) -1)
    for i in range(len(a)):
        for j in range(len(b)):
            ans[i+j] += a[i] * b[j]
    return ans

a = [3, 2, 5]
b = [5, 1, 2]
print(navie_poly_multiplication(a, b))