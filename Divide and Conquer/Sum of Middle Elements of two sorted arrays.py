'''
Given 2 sorted arrays A and B of size N each. Print sum of middle elements of the array obtained after merging the given arrays.

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases.
Each case begins with a single positive integer N denoting the size of array. The second line contains the N space separated positive integers denoting the elements of array A. The third line contains N space separated positive integers denoting the elements of array B.

Output:
For each testcase, print the sum of middle elements of two sorted arrays. The number of the elements in the merged array are even so there will be 2 numbers in the center n/2 and n/2 +1. You have to print their sum.

Constraints:
1 <= T <= 50
1 <= N <= 103
1 <= A[i] <= 106
1 <= B[i] <= 106

Example:
Input :
1
5
1 2 4 6 10
4 5 6 9 12

Output : 
11

Explanation:
Testcase 1: After merging two arrays, sum of middle elements is 11 (5 + 6).

'''


def SumMiddle(A,B,N):
    arr = []
    i = 0
    j = 0
    while i < N and j < N:
        if A[i] < B[j]:
            arr.append(A[i])
            i += 1
        else:
            arr.append(B[j])
            j += 1
    
    while i < N:
        arr.append(A[i])
        i += 1
        
    while j < N:
        arr.append(B[j])
        j += 1

    
    s = arr[((2*N)//2)-1]+arr[(2*N)//2]   
    return s
    
for _ in range(int(input())):
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    print(SumMiddle(A,B,N))
    
    
