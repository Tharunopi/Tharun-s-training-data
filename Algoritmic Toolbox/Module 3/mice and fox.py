def hiding_mice(m ,n):
    return sorted(m), sorted(n)

if __name__ == "__main__":
    m = [4, -4, 2]
    h = [4, 0, 5]
    print(hiding_mice(m, h))