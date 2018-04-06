#Uses python3
import sys
def max_dot_product(a, b):
    revenue = 0
    for i in range(len(a)):
        revenue += max(a) * max(b)
        a.pop(a.index(max(a)))
        b.pop(b.index(max(b)))
    return revenue
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))