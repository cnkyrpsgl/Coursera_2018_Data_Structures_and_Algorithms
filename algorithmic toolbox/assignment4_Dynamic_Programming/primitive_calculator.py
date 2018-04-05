# Uses python3
import sys
import math
def optimal_sequence(n):
    c=[0]*(n+1)
    if (n==1):
        return[0,[1]]
    for i in range(2,n+1):
        val1=c[i-1]+1
        val2=math.inf
        val3=math.inf
        if (i%2==0):
            val2=c[i//2]+1
        if (i%3==0):
            val3=c[i//3]+1
        sp=min(val1,val2,val3)
        if (sp==val1):
            c[i]=c[i-1]+1
        elif (sp==val2):
            c[i]=c[i//2]+1
        elif (sp==val3):
            c[i]=c[i//3]+1
    return [c[n],write_sequence(n,c)]

def write_sequence(n,c):
    j=n
    sequence=[n]
    while j>1:
        val1=c[j-1]+1
        val2=math.inf
        val3=math.inf
        if (j%2==0):
            val2=c[j//2]+1
        if (j%3==0):
            val3=c[j//3]+1
        fp=min(val1,val2,val3)
        if (fp==val1):
            sequence.append(j-1)
            j=j-1
        elif(fp==val2):
            sequence.append(j//2)
            j=j//2
        elif (fp==val3):
            sequence.append(j//3)
            j=j//3
    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
[num,sequence] = (optimal_sequence(n))
print(num)
for x in sequence:
    print(x, end=' ')
