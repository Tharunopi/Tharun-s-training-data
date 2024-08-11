def liner_search(x, find):
    for i in x:
        if i == find:
            return i, "Found"

def linear_recursive(x, l, r, find):
    if r < l:
        return "not found"
    if x[l] == find:
        return "found", l
    return linear_recursive(x, l+1, r, find)

print(linear_recursive(["tharun", "naveen", "joe", "harish", "Jindo", "pravenn"],1, 5, "Jndo"))