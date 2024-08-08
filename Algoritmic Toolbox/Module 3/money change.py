def money_change(x):
    coins = sorted([1, 5, 10], reverse=True)
    total_coins = 0
    for i in coins:
        while x>= i:
            x -= i
            total_coins+=1
    return total_coins

if __name__ == "__main__":
    print(money_change(28))