'''
Given an array of distinct elements of size N, find the number of pairs in the array with their sum greater than 0.

Input:
First line of input contains number of testcases T. For each testcase, there will be two lines, first of which will contain N. Second line contains N space separated integers. 

Output:
Print number of valid pairs whose sum is greater that 0.

Your Task:
Complete the function ValidPair() that takes array and N as input and returns an integer.

Constraints: 
1 <= T <= 100
1 <= N <= 105
-104 <= A[i] <= 104

Example:
Sample Input:
2
3
3 -2 1
4
-1 -1 -1 0

Sample Output:
2
0

Explanation:
Testcase 1 : There are two pairs of elements in the array whose sum is positive. They are:
{3, -2} = 1
{3, 1} = 4
'''
from bisect import bisect_left as lower_bound 

def findNumOfPair(array, n): 
    array = sorted(array)
    count = 0
    for i in range(n):
        if array[i] <= 0:
            continue
        j = lower_bound(array,-array[i]+1)
        count += i-j
        
    return count
        
