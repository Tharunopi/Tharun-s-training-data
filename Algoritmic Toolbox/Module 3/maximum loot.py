def knapsnack(x, y, limit):
    avail = [[x[i]/y[i], x[i], y[i]]for i in range(len(x))]
    ans = []
    value = 0
    avail = sorted(avail, key=lambda x:x[0], reverse=True)
    for i in avail:
        if limit == 0:
            break
        if i[2] <= limit:
            limit -= i[2]
            ans.append(i[2])
            value += i[2]*i[0]
        elif limit <= i[2]:
            ans.append(limit)
            value += limit*i[0]
            limit -= limit

    return value, avail

if __name__ == "__main__":
    k = list(map(int, input("enter number and limit").split()))
    a = []
    b = []
    c = k[1]
    for i in range(k[0]):
        m = list(map(int, input("enter weight and price").split()))
        a.append(m[0]), b.append(m[1])
    print(knapsnack(a, b, c))