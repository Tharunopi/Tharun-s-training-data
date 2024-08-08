def revenue(x, y):
    total = 0
    x = sorted(x, reverse=True)
    y = sorted(y, reverse=True)
    for i in range(len(x)):
        total += (x[i] * y[i])
    return total

if __name__ == "__main__":
    x = [2, 3, 9]
    y = [7, 4, 2]
    print(revenue(x, y))