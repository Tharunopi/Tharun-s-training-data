# using sorting method

# def splitting(x):
#     if len(x)<=1:
#         return x
#     mid = len(x)//2
#     left = splitting(x[:mid])
#     right = splitting(x[mid:])
#     return merge(left, right)
#
# def merge(left, right):
#     ans = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] > right[j]:
#             ans.append(left[i])
#             i += 1
#         else:
#             ans.append(right[j])
#             j += 1
#     ans.extend(left[i:])
#     ans.extend(right[j:])
#     return ans
#
# print(splitting([9, 8, 9, 6, 1]))

# using append and remove method

def salary(x):
    ans = []
    while len(x) != 0:
        max = 0
        for i in x:
            if i > max:
                max = i
        ans.append(max)
        x.remove(max)
    return ans

print(salary([9, 8, 9, 6, 100]))