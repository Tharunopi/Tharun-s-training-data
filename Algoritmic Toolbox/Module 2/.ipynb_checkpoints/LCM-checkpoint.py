def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def lcm(a, b):
    return a * b/gcd(a, b)
print(gcd(10, 4))
print(lcm(10, 4))