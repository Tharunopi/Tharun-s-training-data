def sort(x):
    if len(x) <= 1:
        return x, 0
    mid = len(x)//2
    left, inv_left = sort(x[:mid])
    right, inv_right= sort(x[mid:])
    merged, inv_merged = merge(left, right)
    return merged, inv_left + inv_merged + inv_right

def merge(left, right):
    ans = []
    i, j = 0, 0
    inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
            inv_count += len(left)-i
    ans.extend(left[i:])
    ans.extend(right[j:])
    return ans, inv_count

def navie(x):
    count = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] > x[j] and i < j:
                print(x[i], x[j])

a = [2, 3, 9, 2, 9]
x = [2, 4, 1, 3, 5]
sorted_a, inv_count = sort(a)
print(f"Sorted list: {sorted_a}")
print(f"Inversion count: {inv_count}")
