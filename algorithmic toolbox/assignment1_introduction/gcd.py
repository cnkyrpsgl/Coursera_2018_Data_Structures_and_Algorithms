# Uses python3
import sys
def gcd(a, b):
    while True:
        remainder = a % b
        if (remainder == 0):
            return b
        else:
            a, b = b, remainder
if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
