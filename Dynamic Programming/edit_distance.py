'''
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1′ into ‘str2′.

Insert
Remove
Replace
All of the above operations are of cost=1.
Both the strings are of lowercase.

Input:
The First line of the input contains an integer T denoting the number of test cases. Then T test cases follow. Each tese case consists of two lines. The first line of each test case consists of two space separated integers P and Q denoting the length of the strings str1 and str2 respectively. The second line of each test case coantains two space separated strings str1 and str2 in order.

Output:
Corresponding to each test case, pirnt in a new line, the minimum number of operations required.
'''

def edit_distance(s1,s2,n,m):
    # convert s1 to s2
    dp = [[0 for i in range(101)] for j in range(101)]
    for i in range(n+1):
        dp[0][i] = i
    for j in range(m+1):
        dp[j][0] = j
        
    for i in range(1,m+1):
        for j in range(1,n+1):
            replace = dp[i-1][j-1]
            delete = dp[i-1][j]
            insert = dp[i][j-1]
            if s1[j-1] == s2[i-1]:
                dp[i][j] = replace
            else:
                dp[i][j] = 1 + min(replace,delete,insert)
                
    return dp[m][n]

for _ in range(int(input())):
    n,m = map(int,input().split())
    s1 , s2 = input().split()
    print(edit_distance(s1,s2,n,m))
    
