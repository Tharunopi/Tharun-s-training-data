def gcd(a, b):
    while(b != 0):
        c = a%b
        a = b
        b = c
    return a

if __name__ == "__main__":
    print(gcd(28851538, 1183019))