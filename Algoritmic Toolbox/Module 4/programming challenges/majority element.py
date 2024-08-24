from collections import Counter
def majority(x):
    freq = list(sorted(Counter(x).items(), key=lambda j:j[1]))
    if freq[-1][-1] > len(x)/2:
        return 1
    else:
        return 0

x = [1, 2, 3, 1]
print(majority(x))