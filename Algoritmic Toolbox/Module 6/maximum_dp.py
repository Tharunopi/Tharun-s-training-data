class MaximumDP:
    history = []

    def __init__(self, x:int):
        self.x = x
        MaximumDP.history.append(self)

    def __repr__(self):
        return f"object initalized with {self.x}"

    def maxi(self):
        n = len(self.x)
        dp = [0] * n
        dp[0] = self.x[0]
        for i in range(1, n):
            dp[i] = max(self.x[i], dp[i-1] + self.x[i])
        return dp

x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
item = MaximumDP(x)
print(item.maxi())