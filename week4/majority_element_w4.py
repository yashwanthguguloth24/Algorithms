#divide and conquer method

def Majority_element(a,left,right):
    if left == right:
        return -1
    if left+1 == right:
        return a[left]

    left_num = Majority_element(a,left,(left+right-1)//2 +1)
    right_num = Majority_element(a,(left+right-1)//2 +1,right)

    left_count = 0
    for i in range(left,right):
        if a[i] == left_num:
            left_count += 1
    if left_count > (right-left)//2:
        return left_num

    right_count = 0
    for i in range(left, right):
        if a[i] == right_num:
            right_count += 1
    if right_count > (right - left) // 2:
        return right_num

    return -1

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    if Majority_element(a,0,n) == -1:
        print(0)
    else :
        print(1)



