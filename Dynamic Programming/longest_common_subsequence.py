# Dynamic Programming
'''
Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

Input:
First line of the input contains no of test cases  T,the T test cases follow.
Each test case consist of 2 space separated integers A and B denoting the size of string str1 and str2 respectively
The next two lines contains the 2 string str1 and str2 .

Output:
For each test case print the length of longest  common subsequence of the two strings .

Constraints:
1<=T<=200
1<=size(str1),size(str2)<=100

Example:
Input:
2
6 6
ABCDGH
AEDFHR
3 2
ABC
AC

Output:
3
2
'''

def longest_subsequence(s1,s2):
    dp = [[0 for i in range(101)] for j in range(101)]
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[len(s2)][len(s1)]
    
for _ in range(int(input())):
    a,b = input().split()
    s1 = input()
    s2 = input()
    print(longest_subsequence(s1,s2))
    
    
