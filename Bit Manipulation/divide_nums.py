'''
Divide two integers without using multiplication, division and mod operator.

Return the floor of the result of the division.

Example:

5 / 2 = 2
Also, consider if there can be overflow cases. For overflow case, return INT_MAX.

Note: INT_MAX = 2^31 - 1
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        if B == 1:
            return A
        if (A<0)^(B<0):
            sign = -1
        else:
            sign = 1
        # if A < -2147483647:
        #     A = 
            
        A = abs(A)
        B = abs(B)
        t = 0
        q = 0
        for i in reversed(range(33)):
            if (t+ B << i) <= A:
                t = t + B <<i
                q = q|(1 << i)
        if q > 2147483647 or q < -2147483647:
            return 2147483647
        
                
        if sign == -1:
            return -q
        else:
            return q
