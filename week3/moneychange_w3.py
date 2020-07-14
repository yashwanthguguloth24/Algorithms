##coin change problem
#denominations of 1 5 10

def CoinChange(m):
    list = [10,5,1]
    sum = 0
    while m > 0:
        if m >= list[0]:
            sum += m // list[0]
            m = m % list[0]

        if m >= list[1]:
            sum += m // list[1]
            m = m % list[1]

        if m >= list[2]:
            sum += m // list[2]
            m = m % list[2]

    return sum

if __name__ == '__main__':
    n = int(input())
    print(CoinChange(n))
