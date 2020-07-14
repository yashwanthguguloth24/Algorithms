#Primivite calculator
import sys

#create dynamic array
def Dynamic_array(n):
    d_array = []
    #array with n+1 zeros
    for i in range(0,n+1):
        d_array.append(0)

    for i in range(2,n+1):
        temp1 = d_array[i-1]
        temp2 = sys.maxsize
        temp3 = sys.maxsize

        if i%2 == 0:
            temp2 = d_array[int(i/2)]

        if i%3 == 0:
            temp3 = d_array[int(i/3)]

        minimum = min(temp1,temp2,temp3)

        d_array[i] =  minimum + 1

    return d_array

#Backtracking
def Construct_list(n,list):
    sequence = []
    while n > 0:
        sequence.append(n)

        if n%2 != 0 and n%3 != 0:
            n = n -1
        elif n%2 == 0 and n%3 == 0:
            n = n//3
        elif n%2 == 0:
            if list[n-1] < list[n//2]:
                n = n - 1
            else:
                n = n // 2
        elif n % 3 == 0:
            if list[n - 1] < list[n // 3]:
                n = n - 1
            else:
                n = n // 3

    return reversed(sequence)

def Optimal_sequence(n):
    if n == 1:
        return [1]
    out = Dynamic_array(n)
    return Construct_list(n,out)

if __name__ == '__main__':
    n = int(input())
    sequence = list(Optimal_sequence(n))
    print(len(sequence)-1)
    for x in sequence:
        print(x,end = ' ')





