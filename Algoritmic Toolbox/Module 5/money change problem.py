from collections import Counter

def change(user_amt, actual_price):
    x = user_amt - actual_price
    value = []
    denominations = {5: 100000, 2: 2, 1: 10}

    for i, j in denominations.items():
        while x >= i and denominations[i] > 0:
            x -= i
            value.append(i)
            denominations[i] -= 1

    return Counter(value)

x = 3000
y = 2212
print(change(x, y))
