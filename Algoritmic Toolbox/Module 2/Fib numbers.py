#fibbonacci algorithm

def navie_algorithm(rangef):
    n = 0
    fib = []
    for i in range(rangef):
        if n <= 1:
            fib.append(n)
            n += 1
        else:
            fib.append((fib[i-1] + fib[i-2]))
    return fib[rangef-1]

if __name__ == "__main__":
    mm = navie_algorithm(3)
    print(mm)