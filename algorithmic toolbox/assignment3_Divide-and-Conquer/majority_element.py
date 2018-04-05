# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    a.sort()
    if right%2==0:
        major=int((n/2)+1)
    if right%2!=0:
        major=int(((n+1)/2))
    for i in range((n//2)+(n%2)):
        if a[i]==a[i+major-1]:
            return 1
    #write your code here
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    get_majority_element(a,0,n)
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
