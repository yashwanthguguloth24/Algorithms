'''
There are two parallel roads, each containing N and M buckets, respectively. Each bucket may contain some balls. The buckets on both roads are kept in such a way that they are sorted according to the number of balls in them. Geek starts from the end of the road which has the bucket with a lower number of balls(i.e. if buckets are sorted in increasing order, then geek will start from the left side of the road).
The geek can change the road only at the point of intersection(which means, buckets with the same number of balls on two roads). Now you need to help Geek to collect the maximum number of balls.

Input:
The first line of input contains T denoting the number of test cases. The first line of each test case contains two integers N and M, denoting the number of buckets on road1 and road2 respectively. 2nd line of each test case contains N integers, number of balls in buckets on the first road. 3rd line of each test case contains M integers, number of balls in buckets on the second road.

Output:
For each test case output a single line containing the maximum possible balls that Geek can collect.

Constraints:
1<= T <= 1000
1<= N <= 10^3
1<= M <=10^3
0<= A[i],B[i]<=10^6

Example:
Input:
1
5 5
1 4 5 6 8
2 3 4 6 9

Output:
29

Explanation:

The path with maximum sum is (2,3,4)[5,6](9). Integers in [] are the buckets of first road and in () are the buckets of second road. So, max balls geek can collect is 29.
'''

# Merge sort approach

def MaxBalls(r1,r2,n,m):
    res = 0
    first = 0
    second = 0
    i = 0
    j = 0
    while i < n and j < m:
        if r1[i] < r2[j]:
            first += r1[i]
            i += 1
        elif r2[j] < r1[i]:
            second += r2[j]
            j += 1
        else:
            res += max(first,second)+r1[i]
            first = 0
            second = 0
            temp = r1[i]
            i += 1
            j += 1
            
            # for duplicates of common element 
            while i < n and r1[i] == temp:
                res += r1[i]
                i += 1
            while j < m and r2[j] == temp:
                res += r2[j]
                j += 1
            
            
    while i < n:
        first += r1[i]
        i += 1
        
    while j < m:
        second += r2[j]
        j += 1
        
    res += max(first,second)
    return res
    
for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    r1 = [int(x) for x in input().split()]
    r2 = [int(y) for y in input().split()]
    print(MaxBalls(r1,r2,n,m))



