def fibo(y, x):
    if x <=1:
        return x
    p, c = 0, 1
    for i in range(x-1):
        p, c = c, c+p
    return c%y

print(fibo(1000, 115))