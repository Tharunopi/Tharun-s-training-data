def binary_search(a,key,start=0):
    if len(a) == 0:
        return -1
    mid = len(a)//2
    if a[mid] == key:
        return start+mid
    elif key > a[mid]:
        return binary_search(a[mid+1:], key, start+mid+1)
    else:
        return binary_search(a[:mid], key, start)
a = sorted(["tharun", "harish", "aqeel", "berbin"])
print(a)
print(f"{'berbin'} found in index {binary_search(a, 'berbin')}")
print(20//2)