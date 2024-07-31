def fibo(max):
    if max == 0:
        return 0
    elif max == 1:
        return 1
    else:
        ans = []
        for i in range(max):
            if (i <= 1):
                ans.append(i)
            else:
                ans.append(ans[i - 1] + ans[i - 2])
        return ans[-1] + ans[-2]

def sums(x):
    li = []
    for i in range(x+1):
        li.append(fibo(i))
    return sum(li)

if __name__ == "__main__":
    a = int(input())
    print(sums(a))