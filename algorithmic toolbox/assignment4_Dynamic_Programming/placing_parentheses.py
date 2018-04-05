# Uses python3
def MinAndMax(i,j,m,M,op):
    min_num=float("inf")
    max_num=float("-inf")
    for k in range(i,j):
            a=eval(str(str(M[i][k])+op[k]+str(M[k+1][j])))
            b=eval(str(str(M[i][k])+op[k]+str(m[k+1][j])))
            c=eval(str(str(m[i][k])+op[k]+str(M[k+1][j])))
            d=eval(str(str(m[i][k])+op[k]+str(m[k+1][j])))
            min_num=min(min_num,a,b,c,d)
            max_num=max(max_num,a,b,c,d)

    return [min_num,max_num]
def parentheses(dataset):
    #write your code here
    length=len(dataset)
    n=(length-1)//2
    n+=1
    m=[[0 for j in range(n+1)] for i in range(n+1)]
    M=[[0 for j in range(n+1)] for i in range(n+1)]
    op=[0]
    for num in range(1,length-1,2):
        op.append(dataset[num])
    i=1
    for num in range(0,length+1,2):
        m[i][i]=dataset[num]
        M[i][i]=dataset[num]
        i+=1
    for s in range(1,n):
        for i in range(1,n-s+1):
            j=i+s
            [m[i][j],M[i][j]]=MinAndMax(i,j,m,M,op)
    return M[1][n]


if __name__ == "__main__":
    print(parentheses(input()))
