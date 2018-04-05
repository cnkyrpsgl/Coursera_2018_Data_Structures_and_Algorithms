# Uses python3
import sys
#from sympy import Eq, Symbol, solve
def optimal_summands(n):
    summands = []
    pile=0
    #write your code here
    if(n<=2):
        summands.append(n)
        return summands
    #s=Symbol("s")
    #ind=solve(n^2-n-2*s,s)
    #print(ind)
    for i in range(1,n):
        pile=pile+i
        if(n<pile):
            summands[i-2]=n-pile+2*i-1
            return summands
        summands.append(i)
        i+=1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
