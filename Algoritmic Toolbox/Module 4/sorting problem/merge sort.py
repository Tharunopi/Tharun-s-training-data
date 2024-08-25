def merge_sort(x):
    n = len(x)

    if len(x) == 1:
        return x

    mid = n//2
    left = x[:mid]
    right = x[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    ans = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            ans.append(left[l])
            l+=1
        else:
            ans.append(right[r])
            r+=1
    ans.extend(left[l:])
    ans.extend(right[r:])
    return ans

x = [2, 4, 1, 3, 5]
print(merge_sort(x))