'''
Example Input
Input 1:

 A = 18
Input 2:

 A = 8


Example Output
Output 1:

 1
Output 2:

 3


Example Explanation
Explanation 1:

 18 in binary is represented as: 10010, there is 1 trailing zero.
Explanation 2:

 8 in binary is represented as: 1000, there are 3 trailing zeroes.
 '''
 
 
 class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        c = 0
        while A > 0:
            if A & 1 == 0:
                c += 1
            else:
                return c
            A = A >> 1
        return c
        # naive sol
        # a = bin(A)[2:]
        # f = len(a)
        # c = 0
        # while f > 0:
        #     if a[f-1] == '0':
        #         c += 1
        #     else:
        #         return c
        #     f = f-1
                
        # return c
