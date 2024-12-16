x = [1, 2, 3, 5]
for i in range(len(x)-1):
    if x[i] > x[i+1]:
        print(f"{x[i]} left{x[i+1]}")
    else:
        print(f"{x[i]} right{x[i+1]}")