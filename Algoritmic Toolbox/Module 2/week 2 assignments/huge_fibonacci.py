def fib(m, n):
    ans = []
    for i in range(n):
        if i <= 1:
            ans.append(i%m)
        else:
            ans.append((ans[-1] + ans[-2])%m)
    if len(ans) <= 1:
        return ((ans[-1]+1)%m)
    else:
        return int((ans[-1] + ans[-2])%m)

def pisano_period(m):
    previous, current = 0, 1
    for i in range(m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1
    return None

def huge(n, m):
    p = pisano_period(m)
    if p:
        n = n%p
    return fib(m, n)

if __name__ == "__main__":
    k = list(map(int, input().split()))
    print(huge(k[0], k[1]))