def gcd(a, b):
    while(b != 0):
        c = a%b
        a = b
        b = c
    return a

if __name__ == "__main__":
    k = list(map(int, input().split()))
    print(gcd(k[0], k[1]))