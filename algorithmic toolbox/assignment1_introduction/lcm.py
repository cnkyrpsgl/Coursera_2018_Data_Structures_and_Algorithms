# Uses python3
import sys

def lcm_naive(a, b):
    a_first=a
    b_first=b
    while True:
        remainder=a%b
        if (remainder==0):
            gcd=b
            lcm=(a_first*b_first)//gcd
            return lcm
        else:
            a=b
            b=remainder

#    count_a=1
#    count_b=1
#    while True:
#        a_new=a*count_a
#        b_new=b*count_b
#        if (max(a_new,b_new)%min(a_new,b_new)==0):
#            return max(a_new,b_new)
#        if (a_new==b_new):
#            return a_new
#        if (a_new>b_new):
#            count_b+=1
#        if (b_new>a_new):
#            count_a+=1
#    for l in range(1, a*b + 1):
#        if l % a == 0 and l % b == 0:
#            return l

#    return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
