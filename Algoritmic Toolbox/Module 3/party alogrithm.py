def sorting(x):
    if len(x)<=1:
        return x
    mid = len(x)//2
    left = x[:mid]
    right = x[mid:]
    return merge(sorting(left), sorting(right))

def merge(left, right):
    ans = []
    i, j =0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ans.append(left[i])
            i+=1
        else:
            ans.append(right[j])
            j += 1
    ans.extend(left[i:])
    ans.extend(right[j:])
    return ans

def party(x):
    x = sorting(x)
    mid = len(x)//2
    left = x[mid:]
    right = (x[:mid])
    for i in left:
        for j in right:
            if i -j >1 and i-j <=2:
                print(i, j)
                left.remove(i)
                right.remove(j)

print(party([9, 18, 29, 35, 7, 14, 25, 30]))