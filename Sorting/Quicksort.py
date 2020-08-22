#Quick sort

def partition(arr,low,high):
    pIndex = low
    pivot = arr[high]
    for i in range(low,high):
        if arr[i] <= pivot:
            arr[i],arr[pIndex] = arr[pIndex],arr[i]
            pIndex += 1
    arr[pIndex],arr[high] = arr[high],arr[pIndex]
    return pIndex
    
def QuickSort(arr,low,high):
    if low < high:
        

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        QuickSort(arr, low, pi-1)
        QuickSort(arr, pi+1, high)
    
 if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        quicksort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end = " ")
        print()

