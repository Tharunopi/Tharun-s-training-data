import math

def closest_point(x):
    for i in x:
        p, q = i[0], i[1]
        result = math.sqrt(((p-0)**2) + ((q-0)**2))
        print(result)



x = [(3, 3), (2, 2), (4, 4), (1, 1)]
print(closest_point(x))