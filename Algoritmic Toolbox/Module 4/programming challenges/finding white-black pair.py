def pair(x):
    if len(x) <= 2:
        return x

    mid = len(x)//2
    if x[mid] == "W":
        return  pair(x[mid:])
    else:
        print(x[:mid+1])
        return pair(x[:mid+1])

a = "WWWWWBBBBB"
print(pair(a))
