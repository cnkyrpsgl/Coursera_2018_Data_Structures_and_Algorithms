# Uses python3
import sys

def fibonacci_partial_sum_naive(m, n):
    last1=0
    last2=1
    f=[0,1]
    if (n>=60):
        for _ in range(2,61):
            last3=(last1+last2)%10
            f.append(last3)
            last1=last2%10
            last2=last3%10
    if (n<60):
        for _ in range(2,n+1):
            last3=(last1+last2)%10
            f.append(last3)
            last1=last2%10
            last2=last3%10

    sum = 0
    for i in range(m%60,(n+1)%60):
        i_remainder=i%60
        sum+=f[i_remainder]%10
        sum=sum%10

    return sum


if __name__ == '__main__':
    input = sys.stdin.read();
    m, n = map(int, input.split())
    print(fibonacci_partial_sum_naive(m, n))
