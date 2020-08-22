def merge(arr, l, m, r): 
    
    new_arr = [0]*(r-l+1)
    i = l
    j = m+1
    k = 0
    while(i <= m and j <= r):
        if arr[i]<= arr[j]:
            new_arr[k] = arr[i]
            i += 1
        else:
            new_arr[k] = arr[j]
            j += 1
        k += 1
        
    while(i<=m):
        new_arr[k] = arr[i]
        k += 1
        i += 1
        
    while(j<=r):
        new_arr[k] = arr[j]
        k += 1
        j += 1        
    
    for i in range(l,r+1):
        arr[i] = new_arr[i-l]
        
    return arr
		
def mergeSort (arr, l, r):
    if l < r:
        m = l + (r - l)/2
        
        mergeSort (arr, l, m)
        mergeSort (arr, m+1, r)
        merge (arr, l, m, r)
				
if __name__ == "__main__":
	for i in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        mergeSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end = " ")
        print()
