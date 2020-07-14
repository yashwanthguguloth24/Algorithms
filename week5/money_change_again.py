#coin change using dynamic programming
#code by yashwanth

import numpy as np


def Dp_coinchange(money):
    coins = [1,3,4]     #given
    d = np.zeros([len(coins),money+1])
    for i in range(0,money+1):
        d[0,i] = i
    for i in range(1,len(coins)):
        for j in range(0,money+1):
            d[i,0] = 0
            if coins[i] > j:
                d[i,j] = d[i-1,j]
            else:
                d[i,j] = min(d[i-1,j],1+d[i,j-coins[i]])

    return d[len(coins)-1,money]


if __name__ == '__main__':
    n = int(input())
    print(int(Dp_coinchange(n)))


