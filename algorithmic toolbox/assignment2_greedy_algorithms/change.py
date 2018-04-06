# Uses python3
import sys
def get_change(m):
    coins = 0
    tens = m // 10
    fives = (m - 10 * tens) // 5
    ones = (m - 10 * tens - 5 * fives) // 1
    coins = tens + fives + ones
    return coins
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
