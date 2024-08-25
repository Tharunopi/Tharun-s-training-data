def lottery_navie(x, y):
    ans = {}
    for i in y:
        for j in x:
            if i not in ans:
                ans[i] = 0
            if i >= j[0] and i <= j[1]:
                    ans[i] += 1
    return ans

a = [[3, 2], [0, 5], [-3, 2], [7, 10]]
y = [1, 6]
print(lottery_navie(a, y))