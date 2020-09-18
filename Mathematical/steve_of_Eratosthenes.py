import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        primes = [1]*(A+1)
        primes[0] = 0
        primes[1] = 0
        a = []
        for i in range(2,int(math.sqrt(A))+1):
            if primes[i] == 1:
                j = i
                while j*i <= A:
                    primes[i*j] = 0
                    j += 1
                    
        for i in range(len(primes)):
            if primes[i] == 1:
                a.append(i)
                
                
                
        return a
