class NumGoldBar:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def naive_method(self):
        weight = self.x
        ans = 0
        bars = sorted(self.y, reverse=True)
        for i in bars:
            if i <= weight:
                ans += i
                weight -= i
        return ans

    def optimal_method(self):
        dp = [[0] * (self.x+1) for i in range(len(y)+1)]

        for i in range(1, len(self.y)+1):
            for j in range(1, self.x+1):
                if self.y[i-1] <= j:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-self.y[i-1]] + self.y[i-1])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(self.y)][self.x]

x = 10
y = [1, 4, 8]
item = NumGoldBar(x, y)
print(item.optimal_method())