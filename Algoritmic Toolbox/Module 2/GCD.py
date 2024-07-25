def gcd(a, b):
    while b != 0:
            c = a % b
            a = b
            b = c
    if b == 0:
        return a

print(gcd(357, 234))