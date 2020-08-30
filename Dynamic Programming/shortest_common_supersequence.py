'''
Given two strings str1 and str2, find the length of the smallest string which has both, str1 and str2 as its sub-sequences.
Note: str1 and str2 can have both uppercase and lowercase letters.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains two space-separated strings.

Output:
For each testcase, in a new line, output the length of the required string.

Expected Time Complexity: O(Length(str1) * Length(str2)).
Expected Auxiliary Space: O(Length(str1) * Length(str2)).
'''

def short_superseq(s1,s2):
    N1 = len(s1)
    N2 = len(s2)
    dp = [[0 for i in range(N1+1)] for j in range(N2+1)]
    for i in range(N2+1):
        dp[i][0] = i
    for j in range(N1+1):
        dp[0][j] = j
        
    for i in range(1,N2+1):
        for j in range(1,N1+1):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1])
    return dp[N2][N1]

for _ in range(int(input())):
    s1,s2 = map(str,input().split())
    print(short_subseq(s1,s2))
    
    
