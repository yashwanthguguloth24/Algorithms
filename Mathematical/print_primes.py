# Print all the prime nums less than n
# using sieve of Eratosthenes
# O(n*log(log(n)))
'''
Create a list of consecutive integers from 2 to n: (2, 3, 4, …, n).
Initially, let p equal 2, the first prime number.
Starting from p2, count up in increments of p and mark each of these numbers greater than or equal to p2 itself in the list. These numbers will be p(p+1), p(p+2), p(p+3), etc..
Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this number (which is the next prime), and repeat from step 3.
'''

def Primes(n):
    
    sieve = [True for i in range(n+1)]
    p = 2
    
    while (n>=p*p):
        if sieve[p]:
            for i in range(p*p,n+1,p):
                sieve[i] = False
        p += 1
        
    for j in range(2,n+1):
        if sieve[j]:
            print(j,end = " ")
            
for _ in range(int(input())):
    n = int(input())
    Primes(n)
    print()
