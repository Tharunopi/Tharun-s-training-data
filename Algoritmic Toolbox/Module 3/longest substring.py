def substring(x):
    i, j = 0, 0
    ans = []
    for p in x:
        if x[i:j] not in ans:
            ans.append(x[i:j])

s = "abcabca"
print(substring(s))