#code by yashwanth

def Fib_lastdigit(n):
    if n <= 1:
        return n

    prev = 0
    curr = 1
    for i in range(0,n-1):
        prev , curr = curr%10 , (prev + curr)%10


    return curr

if __name__ == '__main__':
    n = int(input())
    print(Fib_lastdigit(n))