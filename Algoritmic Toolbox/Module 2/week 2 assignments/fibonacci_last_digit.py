def fibo(x):
    ans = []
    for i in range(x):
        if i <=1:
            ans.append(i)
        else:
            ans.append(ans[i-1] + ans[i-2])
    return (ans[-1] + ans[-2])%10

if __name__ == "__main__":
    print(fibo(int(input())))