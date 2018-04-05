# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    last1=0
    last2=1
    length_count=0
    f=[0,1]
    for _ in range(2,(m*m)+1):
        last3=(last1+last2)%m
        f.append(last3)
        last1=last2
        last2=last3
        length_count+=1
        if (last3==1) and (last1==0):
            break
    f_remainder=n%length_count
    return f[f_remainder]





if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
