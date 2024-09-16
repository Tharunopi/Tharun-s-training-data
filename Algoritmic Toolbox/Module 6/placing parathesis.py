from flax.core.lift import switch


class MaximumValue:

    def __init__(self, x):
        self.x = x

    def navie_method(self):
        total_value = 0
        for i in range(1, 8, 2):
            match(self.x[i]):
                case '+':
                    total_value += self.x[i-1] + self.x[i+1]
                    break
                case '+':
                    total_value += self.x[i - 1] - self.x[i + 1]
                    break
                case '+':
                    total_value += self.x[i - 1] * self.x[i + 1]
                    break
                case '+':
                    total_value += self.x[i - 1] / self.x[i + 1]
                    break
        return total_value


item = MaximumValue([1, '+', 2, '-', 3, '*', 4, '-', 5])
print(item.navie_method())