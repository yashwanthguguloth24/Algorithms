'''
So to compute, say F2019 mod 5, we’ll find the remainder of 2019 when divided by 20 (Pisano Period of 5 is 20)
. 2019 mod 20 is 19. Therefore, F2019 mod 5 = F19 mod 5 = 1
'''




def PisanoPeriod(n):
    prev , curr = 0 , 1
    for i in range(0,n*n):
        prev , curr = curr,  (prev + curr) % n

        if (prev == 0 and curr == 1):
            return i+1


def fibonacciModulo(n, m):
    # Getting the period
    pisano_period = PisanoPeriod(m)

    # Taking mod of N with
    # period length
    n = n % pisano_period

    previous, current = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(0,n - 1):
        previous, current = current, previous + current

    return (current % m)


# Driver Code
if __name__ == '__main__':
    n , m = input().split()
    print(fibonacciModulo(int(n),int(m)))




