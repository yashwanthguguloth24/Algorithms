'''
@author yashguguloth24

Given an integer N denoting the Length of a line segment. you need to cut the line segment in such a way that the cut length of a line segment each time is integer either x , y or z. and after performing all cutting operation the total number of cutted segments must be maximum. 


Input
First line of input contains of an integer 'T' denoting number of test cases. First line of each testcase contains N . Second line of each testcase contains 3 space separated integers x , y and z.

Output
For each test case print in a new line an integer corresponding to the answer .
'''

import sys
def Max_cutseg(n,x,y,z):
    
    # base case
    mini = min(x,y,z)
    if mini!=0 and n%mini == 0:
        return n//mini
        
    dp = [-sys.maxsize]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        if (i >= x) and (dp[i] < 1+dp[i-x]):
            dp[i] = 1+dp[i-x]
        if (i >= y) and (dp[i] < 1+dp[i-y]):
            dp[i] = 1+dp[i-y]
 
        if (i >= z) and (dp[i] < 1+dp[i-z]):
            dp[i] = 1+dp[i-z]
            
    return dp[n]
    
for _ in range(int(input())):
    n = int(input())
    x,y,z = map(int,input().split())
    print(Max_cutseg(n,x,y,z))
    
