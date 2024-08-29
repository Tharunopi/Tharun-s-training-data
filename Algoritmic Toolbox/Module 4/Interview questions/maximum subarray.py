def maximum(x):
    current_sum = 0
    max_sum = -10

    for i in x:
        current_sum += i
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum

x = [-7, 3, -2, 0, 7, -5, 4]
print(maximum(x))