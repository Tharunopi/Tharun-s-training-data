def segment(a):
    a = sorted(a, key=lambda x:x[1])
    points = []
    last = 0
    for i in a:
        x, y = i[0], i[1]
        if last == 0 or last < x:
            points.append(y)
            last = y
    return points


if __name__ == "__main__":
    a = [[4, 7], [1, 3], [2, 5], [5, 6]]
    print(len(segment(a)))
    print(segment(a))