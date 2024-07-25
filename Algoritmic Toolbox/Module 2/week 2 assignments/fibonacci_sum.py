def fibo(x):
    li = []
    li[0] = 0
    li[1] = 1
    ans = []
    for i in range(x):
        li.append(li[i-1] + li[i-2])
        ans.append(li[i-1] + li[i-2])
    return sum(ans)

if __name__ == "__main__":
    print(fibo(int(input())))