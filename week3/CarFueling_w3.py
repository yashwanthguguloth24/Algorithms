#Greedy Algorithm
#Car Fueling problem
#code by yashwanth G
import sys

def MinRefills(distance,full_tank,n,stops):
    stops.insert(0,0)
    stops.append(distance)
    numRefill = 0
    currRefill = 0
    while currRefill <= n:
        lastRefill = currRefill
        while (currRefill<=n and (stops[currRefill+1]-stops[lastRefill]<=full_tank)):
            currRefill += 1
        if currRefill == lastRefill:
            return -1
        if currRefill <= n:
            numRefill += 1

    return numRefill


if __name__ == '__main__':
    distance = int(input())
    full_tank = int(input())
    n = int(input())
    list = [int(i) for i in input().split()]
    if n != len(list):
        sys.exit()
    print(MinRefills(distance,full_tank,n,list))
