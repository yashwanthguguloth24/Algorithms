'''
Given two numbers 'N' and 'S' , find the largest number that can be formed with 'N' digits and whose sum of digits should be equals to 'S'.

Example 1:

Input: N = 2, S = 9
Output: 90
Explaination: It is the biggest number 
with sum of digits equals to 9.
Example 2:

Input: N = 3, S = 20
Output: 992
Explaination: It is the biggest number 
with sum of digits equals to 20.
'''

class Solution:
    def findLargest(self, N, S):
        if S == 0 and N == 1:
            return '0'
        if S == 0 and N > 1:
            return '-1'
            
        res = ''
        for i in range(N):
            if S > 9:
                res += '9'
                S -= 9
            elif S == 0:
                res += '0'
            else:
                res += str(S)
                S -= S
        
        if S > 0:
            return '-1'
        else:
            return res
