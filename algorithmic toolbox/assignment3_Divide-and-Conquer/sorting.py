# Uses python3
import sys
import random
def partition3(a, l, r):
    x, j1, j2 = a[l], l + 1, l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j2 += 1
            a[i], a[j2] = a[j2], a[i]
            if a[j2] < x:
                a[j1], a[j2] = a[j2], a[j1]
                j1 += 1
    a[l], a[j1-1] = a[j1-1], a[l]
    return j1, j2
def randomized_quick_sort(a, l, r):
    if l >= r: return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1 , r)
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')