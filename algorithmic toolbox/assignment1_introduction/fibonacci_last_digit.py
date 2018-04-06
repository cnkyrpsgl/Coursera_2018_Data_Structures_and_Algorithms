# Uses python3
import sys
def get_fibonacci_last_digit(n):
    if n <= 1: return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        previous = previous % 10
        current = current % 10
    return current
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
