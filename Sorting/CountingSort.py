# Given a string S consisting of lowercase Latin letters, arrange all its letters in lexicographical order using Counting Sort.

def countingSort(s,n):
    MAX_SIZE = 256
    H = {}
    for i in range(MAX_SIZE):
        H[i] = 0
    for k in s:
        H[ord(k)] = H.get(ord(k),0)+1
    sum = 0
    for i in H.keys():
        sum = sum + H.get(i)
        H[i] = sum
    sorted_list = [0]*n
    for i in range(n):
        temp = H[ord(s[i])]
        sorted_list[temp-1] = s[i]
        H[ord(s[i])] = H[ord(s[i])] - 1
    return "".join(sorted_list)  
    
for _ in range(int(input())) :
     n = int(input())
     s = str(input())
     print(countingSort(s,n))
