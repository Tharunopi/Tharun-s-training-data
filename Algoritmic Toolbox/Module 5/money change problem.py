def change(x):
    value = []
    denominations = [4, 3, 1]

    for i in denominations:
        while x >= i:
            x -= i
            value.append(i)

    return (value)

x = 34
print(change(x))
