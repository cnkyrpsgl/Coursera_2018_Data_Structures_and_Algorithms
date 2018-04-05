# Uses python3
def edit_distance(a, b):
    #write your code here
    list_a=list()
    list_a.append(0)
    list_b=list()
    list_b.append(0)
    for x in a:
        list_a.append(x)
    for y in b:
        list_b.append(y)
    n=len(list_a)
    m=len(list_b)
    d=[[0 for x in range(m)] for y in range(n)]
    for i in range(n):
        d[i][0]=i
    for j in range(m):
        d[0][j]=j
    for j in range(1,m):
        for i in range(1,n):
            insertion=d[i][j-1]+1
            deletion=d[i-1][j]+1
            match=d[i-1][j-1]
            mismatch=d[i-1][j-1]+1
            if list_a[i]==list_b[j]:
                d[i][j]=min(insertion,deletion,match)
            else:
                d[i][j]=min(insertion,deletion,mismatch)
    return d[n-1][m-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
