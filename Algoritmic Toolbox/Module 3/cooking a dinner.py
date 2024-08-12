def cooking(x, y):
    fresh = sorted([[x[i], y[i]]for i in range(len(x))])
    ans = []
    for i in fresh:
        cook, time = i[0], i[1]
        if len(ans) == 0:
            ans.append([f"cooking takes {cook} minutes to complete and fresh for {time} minutes"]+i)
        elif cook >= ans[-1][2]:
            ans.append(f"food takes {cook} minutes exceeds previous fresh time {ans[-1][2]}")
        else:
            ans.append(f"food is fresh")
    return ans

x = [1, 2, 3]
y = [5, 7, 10]

print(cooking(x, y))