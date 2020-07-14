import sys
import math
def Binary_seach(a,key):
    low = 0
    high = len(a)-1
    while low <= high:
        mid = math.floor(low +((high-low)/2))
        if key == a[mid]:
            return mid
        elif key < a[mid]:
            high = mid-1
        elif key > a[mid]:
            low = mid+1
    return -1


if __name__ == '__main__':
    list1 = [int(i) for i in input().split()]
    list2 = [int(i) for i in input().split()]
    if (len(list1) != (list1[0]+1)) and (len(list2) != (list2[0]+1)):
        sys.exit()
    a = list1[1:]
    index = list2[1:]
    for num in index:
        print(Binary_seach(a,num),end=' ')
















