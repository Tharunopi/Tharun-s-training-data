def sort(x):
    if len(x) <=1:
        return x
    mid = len(x)//2
    left = x[:mid]
    right = x[mid:]
    return merge(sort(left), sort(right))

def merge(left, right):
    ans = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ans.append(left[i])
            i+=1
        else:
            ans.append(right[j])
            j+=1
    ans.extend(left[i:])
    ans.extend(right[j:])
    return ans

print(sort([9, 3, 1, 7, 4]))