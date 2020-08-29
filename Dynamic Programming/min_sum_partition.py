'''
Given an array, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.

Input:
The first line contains an integer 'T' denoting the total number of test cases. In each test cases, the first line contains an integer 'N' denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.


Output:
In each seperate line print minimum absolute difference.
'''


# def Subset_sum(arr,val):
#     dp = [[False for i in range(val+1)] for j in range(len(arr))]
    
#     for i in range(len(arr)):
#         dp[i][0] = True
    
#     for j in range(val+1):
#         if j == arr[0]:
#             dp[0][j] = True
            
    
#     for j in range(1,val+1):
#         for i in range(1,len(arr)):
#             if dp[i-1][j] :
#                 dp[i][j] = True
#             else:
#                 if j >= arr[i]:
#                     dp[i][j] = dp[i-1][j-arr[i]]
                    
#     return dp
    
def Partition(arr,n):
    s = sum(arr)//2
    #dp = Subset_sum(arr,s)
    dp = [[False for i in range(s+1)] for j in range(len(arr))]
    
    for i in range(len(arr)):
        dp[i][0] = True
    
    for j in range(s+1):
        if j == arr[0]:
            dp[0][j] = True
            
    
    for j in range(1,s+1):
        for i in range(1,len(arr)):
            if dp[i-1][j] :
                dp[i][j] = True
            else:
                if j >= arr[i]:
                    dp[i][j] = dp[i-1][j-arr[i]]
                    
    for j in reversed(range(s+1)):
        if dp[len(arr)-1][j]:
            first_sum = j
            break
        
    second_sum = sum(arr)-first_sum
    diff = abs(first_sum-second_sum)
    return diff



for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(Partition(arr,n))
            
 
