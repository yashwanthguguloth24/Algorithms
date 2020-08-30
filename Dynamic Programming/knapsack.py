'''
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of four lines.
The first line consists of N the number of items.
The second line consists of W, the maximum capacity of the knapsack.
In the next line are N space separated positive integers denoting the values of the N items,
and in the fourth line are N space separated positive integers denoting the weights of the corresponding items.

Output:
For each testcase, in a new line, print the maximum possible value you can get with the given conditions that you can obtain for each test case in a new line.
'''

def knapsack(v,w,target,N):
    if target < min(w):
        return 0
    dp = [[0 for i in range(target+1)] for j in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,target+1):
            if i == 0 or j ==0:
                dp[i][j] = 0
            elif w[i-1] <= j:
                dp[i][j] = max(dp[i-1][j],(v[i-1]+dp[i-1][j-w[i-1]]))
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][target]
    
for _ in range(int(input())):
    N = int(input())
    target = int(input())
    v = [int(x) for x in input().split()]
    w = [int(x) for x in input().split()]
    print(knapsack(v,w,target,N))
    
    
