def align(x, y):
    n = len(x) #len is 8
    m = len(y) #len is 7

    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp

x = ['A', 'T', 'G', 'T', 'T', 'A', 'T', 'A']
y = ['A', 'T', 'C', 'G', 'T', 'C', 'C']
print(align(x, y))