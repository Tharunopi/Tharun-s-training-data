def fibo(x, y):
    ans = []
    real = []
    for i in range(y+1):
        if i <= 1:
           ans.append(i)
        else:
            ans.append(ans[i-1] + ans[i-2])
    for i in range(x, y+1):
        real.append(ans[i-1] + ans[i-2])
    return sum(real)%10

if __name__ == "__main__":
    k = list(map(int, input().split()))
    print(fibo(k[0], k[1]))