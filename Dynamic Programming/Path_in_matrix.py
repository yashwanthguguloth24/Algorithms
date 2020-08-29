'''
Given a N X N  matrix Matrix[N][N] of positive integers.  There are only three possible moves from a cell Matrix[r][c].

1. Matrix[r+1][c]

2. Matrix[r+1][c-1]

3. Matrix[r+1][c+1]

Starting from any column in row 0, return the largest sum of any of the paths up to row N-1.

Input:
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the order of matrix. Next line contains N*N integers denoting the elements of the matrix in row-major form.

Output:
Output the largest sum of any of the paths starting from any cell of row 0 to any cell of row N-1. Print the output of each test case in a new line.
'''

def Path(m):
    dp = [[0 for i in range(N)]for i in range(N)]
    for j in range(N):
        dp[0][j] = m[0][j]
    for i in range(1,N):
        for j in range(N):
            if j == 0:
                dp[i][j] = m[i][j]+max(dp[i-1][j],dp[i-1][j+1])
            elif j == N-1:
                dp[i][j] = m[i][j]+max(dp[i-1][j],dp[i-1][j-1])
            else:
                x = max(dp[i-1][j],dp[i-1][j+1])
                dp[i][j] = m[i][j] + max(x,dp[i-1][j-1])
    return max(dp[N-1])
    
for _ in range(int(input())):
    N = int(input())
    arr = [int(x) for x in input().split()]
    temp=[] 
    k=0
    for i in range(N):
        a=[]
        for j in range(N):
            a.append(arr[k])
            k+=1
        temp.append(a)
    print(Path(temp))
    
    
