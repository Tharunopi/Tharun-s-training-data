from longest_substring_without_repeating_chars import Operation
import numpy as np

class Operation3(Operation):
    def __init__(self, text:str, text2:str, text3:str):
        super().__init__(
            text
        )
        self.text2 = text2
        self.text3 = text3

    def longest_substring_3strings(self):
        n = len(self.text)
        m = len(self.text2)
        o = len(self.text3)

        dp = np.zeros((n+1, m+1, o+1), dtype=int)

        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(1, o+1):
                    if self.text[i-1] == self.text2[j-1] == self.text3[k-1]:
                        dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
        return dp[n][m][o]

x = "83217"
y = "82138107"
z = "68314"
op = Operation3(x, y, z)
print(op.longest_substring_3strings())