'''
A frog jumps either 1, 2 or 3 steps to go to top. In how many ways can it reach the top.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains one line of input N denoting the total number of steps.

Output:
For each testcase, in a new line, print the number of ways to reach the top.
'''

def count_hops(n):
    dp = [0]*(n+1)
    for i in range(1,n+1):
        dp[0] = 1
        if i <= 2:
            dp[i] = i
        elif i>2:
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]
    
for _ in range(int(input())):
    n = int(input())
    print(count_hops(n))
        
