# Uses python3
import sys

def gcd_naive(a, b):
    #current_gcd = 1
    while True:
        remainder=a%b
        if (remainder==0):
            return b
        else:
            a=b
            b=remainder
    #for d in range(2, min(a, b) + 1):
    #    if a % d == 0 and b % d == 0:
    #        if d > current_gcd:
    #            current_gcd = d

    #return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
