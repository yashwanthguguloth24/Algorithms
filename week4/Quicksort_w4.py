#divide and conquer

def Quick_sort(a,left,right):
    if left >= right:
        return
    m1,m2 = Partition(a,left,right)
    Quick_sort(a,left,m1-1)
    Quick_sort(a,m2+1,right)


def Partition(a,l,r):
    x = a[l]
    m1 = l
    m2 = l
    for i in range(l+1,r+1):
        if a[i] < x :
            a[i],a[m1] = a[m1],a[i]
            a[i],a[m2+1] = a[m2+1],a[i]
            m1 += 1
            m2 += 1

        elif a[i] == x :
            a[i], a[m2 + 1] = a[m2 + 1], a[i]
            m2 += 1

    return m1,m2


if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    Quick_sort(a,0,n-1)
    for x in a:
        print(x, end=' ')
