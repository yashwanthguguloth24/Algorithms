'''
Given a set of numbers, check whether it can be partitioned into two subsets such that the sum of elements in both subsets is same or not.

Input:
The first line contains an integer 'T' denoting the total number of test cases. Each test case constitutes of two lines. First line contains 'N', representing the number of elements in the set and the second line contains the elements of the set.

Output:
Print YES if the given set can be partioned into two subsets such that the sum of elements in both subsets is equal, else print NO.
'''

def subset_sum(arr):
    N = len(arr)
    s = sum(arr)//2
    dp = [[False for i in range(s+1)] for j in range(N)]
    for i in range(N):
        dp[i][0] = True
        
    for j in range(s+1):
        if j == arr[0]:
            dp[0][j] = True
            
    for j in range(1,s+1):
        for i in range(1,N):
            if dp[i-1][j] :
                dp[i][j] = True
            elif j >= arr[i]:
                dp[i][j] = dp[i-1][j-arr[i]]
    
    flag = False                
    for j in reversed(range(s+1)):
        if dp[N-1][j]:
            first_sum = j
            break
    sec_sum = sum(arr)-first_sum
    if first_sum == sec_sum:
        flag = True

    
    if flag == True:
        print("YES")
    else:
        print("NO")
    
        
for _ in range(int(input())):
    N = int(input())
    arr = [int(x) for x in input().split()]
    subset_sum(arr)
