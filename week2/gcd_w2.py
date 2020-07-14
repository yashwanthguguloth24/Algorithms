#code by yashwanth

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,(a%b))

if __name__ == '__main__':
    a , b  = input().split()
    print(gcd(int(a),int(b)))