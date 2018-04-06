# Uses python3
import sys
def lcm(a, b):
    a_first, b_first = a, b
    while True:
        remainder = a % b
        if (remainder == 0):
            gcd = b
            lcm = (a_first * b_first) // gcd
            return lcm
        else:
            a, b = b, remainder
if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
