def range_sum(x, l, r):
    return sum(x[l:r+1])

if __name__ == "__main__":
    print(range_sum([1, 3, 4, 8, 6, 1, 4, 2], 1, 4))