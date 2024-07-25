def lcm(a, b):
    value = a*b
    while(b != 0):
        c = a%b
        a = b
        b = c
    return int(value/a)

if __name__ == "__main__":
    k = list(map(int, input().split()))
    print(lcm(k[0], k[1]))