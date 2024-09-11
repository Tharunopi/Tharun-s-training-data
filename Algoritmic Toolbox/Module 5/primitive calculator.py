class PrimitiveCalculator:
    history = []

    def __init__(self, x:int):
        assert x > 0, f"received value {x} must be greater than 0"
        self.__x = x
        PrimitiveCalculator.history.append(self)

    @property
    def value(self):
        return self.__x

    def __repr__(self):
        return f"Object initialized with {self.__x} for primitive calculator operation"

    def calculate(self):
        dp = [float("inf")] * (self.__x + 1)
        dp[1] = 0
        operation = [0] * (self.__x + 1)

        for i in range(2, self.__x+1):
            dp[i] = dp[i-1] + 1
            operation[i] = i - 1

            if i % 2 == 0 and dp[i] > dp[i//2] + 1:
                dp[i] = dp[i//2] + 1
                operation[i] = i // 2

            if i % 3 == 0 and dp[i] > dp[i//3] + 1:
                dp[i] = dp[i//3] + 1
                operation[i] = i // 3

        # Reconstruct the sequence
        sequence = [self.__x]
        while sequence[-1] != 1:
            sequence.append(operation[sequence[-1]])
        sequence.reverse()

        return dp[self.__x], sequence

mat = PrimitiveCalculator(34)
print(mat.value)
print(PrimitiveCalculator.history)
min_operations, sequence = mat.calculate()
print(min_operations)
print(' '.join(map(str, sequence)))