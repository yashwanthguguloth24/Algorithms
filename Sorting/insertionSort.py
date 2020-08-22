def insert(arr):
    for i in range(1,len(arr)):
        value = arr[i]
        hole = i
        while(hole > 0 and arr[hole-1]>value):
            arr[hole] = arr[hole-1]
            hole = hole - 1 
        arr[hole] = value
    return arr
    
if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        insert(arr)
        for i in range(n):
            print(arr[i],end = " ")
        print()
