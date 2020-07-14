#code by yashwanth

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,(a%b))

'''
LCM(a,b) = a*b/GCD(a,b)
'''

def Lcm(a,b):
    return int((a*b)/(gcd(a,b)))

if __name__ == '__main__':
    a , b  = input().split()
    print(Lcm(int(a),int(b)))
