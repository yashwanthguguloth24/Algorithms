import numpy as np
def fibonacci(n):
    if n == 0:
        return 0
    fib = np.zeros(n+1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]

    return int(fib[n])



if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))