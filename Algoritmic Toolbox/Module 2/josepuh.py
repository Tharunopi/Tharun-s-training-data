def joesup(n, k):
    if n == 1:
        return 0
    else:
        return (joesup(n-1, k)+k)%n



if __name__ == "__main__":
    print(joesup(7, 3))