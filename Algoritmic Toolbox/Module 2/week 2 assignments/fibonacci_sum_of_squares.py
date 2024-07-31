def fib(r):
    li = []
    k = []
    for i in range(r):
        if i <= 1:
            li.append(i)
        else:
            li.append(li[i-1] + li[i-2])
            k.append(li[i-1] + li[i-2])
    k = [x**2 for x in k]
    return sum(k)%10

if __name__ == "__main__":
    a = int(input())
    print(fib(a))
