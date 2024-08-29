def missing_element(x):
    ans = []
    y = [i for i in range(x[0], x[-1])]
    y.append(x[-1])
    count = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            ans.append(y[count])
            count += 1
        count += 1
    return ans, y, x

x = [1, 2, 3, 5, 7, 10]
print(missing_element(x))