def fuel_limit(d, m, stops):
    stops.append(d)
    miles_traveled = m
    refuel = 0
    count = 0
    for i in (stops):
        if stops[count] -stops[count-1] > m:
            return -1
        if i > miles_traveled :
            refuel+=1
            miles_traveled += m
        count+=1
    return refuel

if __name__ == "__main__":
    d = 10#int(input("Enter integer d"))           #distance between cities
    m = 3#int(input("Enter integer m"))           #mielage of car
    n = 4#int(input("Enter integer n"))           #number of stops
    stops = [1, 2, 5, 8]#list(map(int, input().split()))     #km that has stops
    print(fuel_limit(d, m, stops))

