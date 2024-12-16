import hashlib

def substring_equality(s, a, b, l):
    s1 = hashlib.md5(s[a:a+l].encode()).hexdigest()
    s2 = hashlib.md5(s[b:b+l].encode()).hexdigest()
    if s1 == s2:
        return print("Yes")
    return print("No")

s = "trololo"
ls = [[0, 0, 7], [2, 4, 3], [3, 5, 1]]
substring_equality(s, 2, 4, 3)