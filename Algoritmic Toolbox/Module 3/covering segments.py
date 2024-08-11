def segment(a):
    a = sorted(a, key=lambda x:x[1])
    seg = []
    last = None
    for i in a:
        x, y = i[0], i[1]
        print(x, y)
        if last is None or last < x:
            seg.append(y)
            last = y
    return seg

if __name__ == "__main__":
    a = [[1, 3], [2, 5], [3, 6]]
    # print(len(segment(a)))
    print(segment(a))