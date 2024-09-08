from longest_substring_without_repeating_chars import Operation

class EditDistance(Operation):
    def __init__(self, text:str, str1:str, str2:str):
        super().__init__(
            text
        )
        self.str1 = str1
        self.str2 = str2

    def edit_distance(self):
        n = len(self.str1)
        m = len(self.str2)

        dp = [[0] *(m + 1) for i in range(n + 1)]

        for i in range(n+1):
            dp[i][0] = i
        for i in range(m+1):
            dp[0][i] = i

        for i in range(1, n+1):
            for j in range(1, m+1):
                if self.str1[i-1] == self.str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[n][m]

    def __repr__(self):
        return f"class initated success fully {self.str1} and {self.str2}"

op = EditDistance("nothing", "bread", "really")
print(op.edit_distance())