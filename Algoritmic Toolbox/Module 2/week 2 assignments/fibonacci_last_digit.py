def fib_last(num):
    ans = []
    for i in range(num):
        if i <=1:
            ans.append(i)
        else:
            ans.append(ans[-1] + ans[-2])
    return  (ans[-1] + ans[-2])%10
if __name__ == "__main__":
    print(fib_last(91239))
