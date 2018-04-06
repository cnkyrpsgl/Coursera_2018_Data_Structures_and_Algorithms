# Uses python3
import sys
def inversions_count(a):
    [inversions_num, sorted_result] = mergesort(a)
    return inversions_num
def mergesort(a):
    if len(a) == 1:
        return [0, a]
    mid = len(a) // 2
    left = mergesort(a[0:mid])
    right = mergesort(a[mid:])
    return merge(left, right)
def merge(left, right):
    inversions_num = left[0] + right[0]
    left_array = left[1]
    right_array = right[1]
    result = []
    while len(left_array) > 0 and len(right_array) > 0:
        if left_array[0] > right_array[0]:
            result.append(left_array[0])
            inversions_num += len(right_array)
            del(left_array[0])
        else:
            result.append(right_array[0])
            del(right_array[0])
    result = result + left_array
    result = result + right_array
    return [inversions_num, result]
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(inversions_count(a))