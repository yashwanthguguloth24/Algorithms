
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        # naive approach
        # c = 0
        # f = bin(A)[2:]
        # for i in range(len(f)):
        #     if f[i] == '1':
        #         c += 1
        # return c
        
        # mathematical approach
        c = 0
        while A > 0:
            A &= A-1
            c += 1
        return c
