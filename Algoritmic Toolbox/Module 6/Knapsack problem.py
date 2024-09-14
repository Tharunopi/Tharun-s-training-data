from sympy.printing.maple import known_functions
from torchgen.api.ufunc import kernel_name


class KnapSack:
    history = []

    def __init__(self, weight:int, items, cost):
        self.weight = weight
        self.items = items
        self.cost = cost
        KnapSack.history.append(self)

    def navie_fractional_knapsack(self):
        info = [[(self.items[i] / self.cost[i]), self.items[i], self.cost[i]] for i in range(len(self.cost)) ]
        info = sorted(info, key=lambda x:x[0], reverse=True)
        ans = []
        total_value = 0
        i = 0
        while(i < len(info)):
            if self.weight - info[i][1] > 0:
                ans.append([info[i][1], info[i][0]])
                total_value += info[i][2]
                self.weight -= info[i][1]
            else:
                fraction = self.weight / info[i][1]
                total_value += info[i][2] * fraction
                ans.append([info[i][1]*fraction, info[i][0]])
            i += 1
        print(info)
        return ans, total_value

    def optimal_without_repeative_knapsack(self):
        n = len(self.items)
        dp = [[0] * (self.weight + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, self.weight + 1):
                if self.items[i - 1] <= j:
                    dp[i][j] = max(self.cost[i - 1] + dp[i - 1][j - self.items[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][self.weight]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.weight}, {self.items}, {self.cost})"

items = [6, 3, 4, 2]
cost = [30, 14, 16, 9]
weight = 10

problem = KnapSack(weight, items, cost)
print(problem.optimal_without_repeative_knapsack())