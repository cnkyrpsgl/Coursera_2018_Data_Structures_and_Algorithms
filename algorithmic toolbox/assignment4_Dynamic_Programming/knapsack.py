# Uses python3
import sys
def optimal_weight(W, w):
    result = [[0 for x in range(W + 1)] for y in range(n + 1)]
    for total_item in range(1, n + 1):
        for weight in range(1, W + 1):
            result[total_item][weight] = result[total_item - 1][weight]
            if w[total_item - 1] <= weight:
                val = result[total_item - 1][weight - w[total_item - 1]] + w[total_item - 1]
                if val > result[total_item][weight]:
                    result[total_item][weight] = val
    return result[n][W]
if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))