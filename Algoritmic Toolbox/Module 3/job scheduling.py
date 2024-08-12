def job_scheduling(deadline, profit):
    largest = max(deadline)
    workdone = 0
    all = sorted([[deadline[i], profit[i]]for i in range(len(profit))], key=lambda x:x[1], reverse=True)
    gains = 0
    for i in all:
        if workdone <= i[0] and workdone < largest:
            gains += i[1]
            workdone += 1
    return gains

def job_scheduling_nonoverlapping(start, end, profit):
    all = sorted([[start[i], end[i], profit[i]]for i in range(len(start))], key=lambda x:x[0])
    return all


if __name__ == "__main__":
    a = [1, 2, 3, 3]
    b = [3, 4, 5, 6]
    c = [50, 10, 40, 70]
    print(job_scheduling_nonoverlapping(a,b,c))