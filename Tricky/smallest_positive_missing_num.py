'''
Given an array arr[] of size N, find the smallest positive number missing from the array.
 
Example 1:
Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 6
Explanation: Smallest positive missing
number is 6.
 
Example 2:
Input:
N = 5
arr[] = {0,-10,1,3,-20}
Output: 2
Time complexity -- O(n)
Space complexity -- O(1)
'''

def findMissing(arr, size): 
    
    # replace greater than and less than with ones such that our range deosnt go beyond
    contains_one = 0
    for i in range(size):
        if arr[i] == 1:
            contains_one = 1
        elif arr[i] < 0 or arr[i] > size:
            arr[i] = 1
            
    if contains_one == 0:
        return 1
            
    for i in range(size):
        ind = abs(arr[i])-1
        if arr[ind] > 0:
            arr[ind] *= -1
            
    k = 0
    while k < size:
        if arr[k] > 0:
            return k+1
        else:
            k += 1
            
    return k+1
    
    
