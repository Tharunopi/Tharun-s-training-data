import random
import numpy as np
def product(lists):
    sec = -1
    max = -1
    for i in lists:
        if i > max:
            sec = max
            max = i
        elif sec < i and sec != max:
            sec = i
    print(sec , max)
    print(sec * max)

if __name__ == "__main__":
    # a = int(input())
    # b = list(map(int, input().split()))
    # using random testcases
    c = 0
    while(c != 100):
        v = random.randint(1, 90)
        m = []
        for i in range(v):
            m.append(random.randint(1, 10))
        product(m)
        c +=1
    # product(b)