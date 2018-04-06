# Uses python3
import sys
def fibonacci_sum(n):
    if n <= 1: return n
    previous, current, sum, n_remainder = 0, 1, 1, n % 60
    if (n_remainder == 0) or (n_remainder == 1): return n_remainder
    for _ in range(n_remainder - 1):
        previous, current = current % 10, previous % 10 + current % 10
        sum = (sum + current % 10) % 10
    return sum
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
