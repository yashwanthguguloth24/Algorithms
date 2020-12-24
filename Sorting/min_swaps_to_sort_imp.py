'''
9. Minimum Swaps to Sort 
Medium Accuracy: 50.0% Submissions: 35324 Points: 4
Given an array of size N. Find the minimum number of swaps required to sort the array in non-decreasing order.


Example 1:

Input: 
N = 5
arr = {1 5 4 3 2}
Output: 2
Explaination: swap 2 with 5 and 3 with 4.
 

Example 2:

Input: 
N = 4
arr[] = {8 9 16 15}
Output: 1
Explaination: swap 16 and 15.

Your Task:
You do not need to read input or print anything. Your task is to complete the function minSwaps() which takes the array arr[] and its size N as input parameters and returns an integer denoting the minimum number of swaps required to sort the array. If the array is already sorted, return 0. 


Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)

 

Constraints:
1 <= N <= 105
1 <= A[] <= 106
'''


# code 

def minSwaps(arr, N):
    pos_arr = [*enumerate(arr)]
    count = 0
    
    pos_arr.sort(key = lambda x:x[1])
    
    visited = {j:False for j in range(N)}
    
    for i in range(N):
        if visited[i] or pos_arr[i][0] == i:
            continue
        j = i
        temp_count = 0
        while not visited[j]:
            visited[j] = True
            temp_count += 1
            j = pos_arr[j][0]
        
        if temp_count > 0:
            count += temp_count-1
            
    return count
            

