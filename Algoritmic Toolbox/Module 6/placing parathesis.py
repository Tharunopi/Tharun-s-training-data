from flax.core.lift import switch


class MaximumValue:

    def __init__(self, x:str):
        self.x = x

    def not_optimal_solution(self):
        min = float("inf")
        max = float("-inf")
        ans = []
        mid = self.x[len(self.x)//2]
        left = self.x[:len(self.x)//2]
        right = self.x[(len(self.x) // 2)+1:]
        ans.append(
            (
                eval('(5-8)+7'),
                eval('5-(8+7)')
            )
        )
        ans.append(
            (
                eval('(4-8)+9'),
                eval('4-(8+9)')
            )
        )
        for k in ans:
            print(k)
        return left,mid, right, ans


item = MaximumValue('5-8+7*4-8+9')
print(item.not_optimal_solution())