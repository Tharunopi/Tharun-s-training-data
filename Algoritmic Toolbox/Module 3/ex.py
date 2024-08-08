a = [1, 2, 3, 4]
count = 0
b = []
for j in range(len(a)):
        mul = 1
        for i in range(len(a)):
            if i == count:
                continue
            else:
                mul *= a[i]
        print(mul)
        count += 1