from collections import Counter
def non_comparison(x):
    freq = [[i, j] for i, j in Counter(x).items()]

    return sorted(freq, key=lambda x:x[1])

a = [2, 3, 2, 1, 3, 2, 2, 3, 2, 2, 2, 1]
print(non_comparison(a))