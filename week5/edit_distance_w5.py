import numpy as np

def Edit_distance(a,b):
    d = np.zeros([len(a)+1,len(b)+1])
    for i in range(0,len(b)+1):
        d[0,i] = i
    for j in range(0,len(a)+1):
        d[j,0] = j

    for j in range(1,len(b)+1):
        for i in range(1,len(a)+1):
            op_ins = d[i,j-1] + 1
            op_del = d[i-1,j] + 1
            op_match = d[i-1,j-1]
            op_mismatch = d[i-1,j-1] + 1

            if a[i-1] == b[j-1] :
                d[i,j] = min(op_ins,op_del,op_match)
            else:
                d[i, j] = min(op_ins, op_del, op_mismatch)

    return d[len(a),len(b)]


if __name__ == '__main__':
    a = list(input())
    b = list(input())
    print(int(Edit_distance(a,b)))



