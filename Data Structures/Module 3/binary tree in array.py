def converter(x):
    #check the principles of binary tree
    for i in range(len(x)):
        left = (2*i) + 1
        right = (2*i) + 2

        if left < len(x):
            if x[i] < x[left]:
                x[i], x[left] = x[left], x[i]
        if right < len(x):
            if x[i] > x[right]:
                x[i], x[right] = x[right], x[i]

        for j in range(i, -1, -1):
            parent = (j-1) // 2
            if parent >= 0:
                left_child = 2 * parent + 1
                right_child = 2 * parent + 2
                if left_child < len(x) and x[parent] < x[left_child]:
                    x[parent], x[left_child] = x[left_child], x[parent]
                if right_child < len(x) and x[parent] > x[right_child]:
                    x[parent], x[right_child] = x[right_child], x[parent]

    return x

x = [3, 6, 4, 9, 12, 8, 7]
print(converter(x))