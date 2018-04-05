# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    n_remainder=n%60
    if (n_remainder==0) or (n_remainder==1):
        return n_remainder
    for _ in range(n_remainder-1):
        previous, current = (current%10), (previous%10) + (current%10)
        sum += current%10
        sum=sum%10

    return sum

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
