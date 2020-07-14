#
# def pairwise(x):
#     n = len(x)
#     product = 0
#     for i in range(0,n):
#         for j in range(i+1,n):
#             product = max(product,x[i]*x[j])
#
#     return product
#
# if __name__ == '__main__':
#     input_n = int(input())
#     input_numbers = [int(x) for x in input().split()]
#     print(pairwise(input_numbers))
# def MaxPairwiseProduct(n,a,c):
#     for i in range(0,n):
#         for j in range (1,n):
#             if a[i] != a[j]:
#                 m = a[i]*a[j]
#                 c.append(m)
#
#             else:
#                 continue
#
#     Product = max(c)
#     return Product
#
# n = int(input())
# a = [int(x) for x in input().split()]
# c = list()
# print(MaxPairwiseProduct(n,a,c))

'''
Max pair wise by sorting method
'''
def pairwise(arr):
    l = len(arr)
    arr = sorted(arr)
    max = (arr[l-1])*(arr[l-2])
    return max

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(pairwise(input_numbers))