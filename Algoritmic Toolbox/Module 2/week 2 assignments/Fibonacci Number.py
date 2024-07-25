def fib(max):
    ans = []
    for i in range(max):
        if(i<=1):
            ans.append(i)
        else:
            ans.append(ans[i-1] + ans[i-2])
    return ans[-1] + ans[-2]

if __name__ == "__main__":
    a = int(input())
    print(fib(2816213588))