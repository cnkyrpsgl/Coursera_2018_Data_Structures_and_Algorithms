# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    if table!=parent[table]:
        parent[table]=getParent(parent[table])
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False
    global ans
    if rank[realDestination]<=rank[realSource]:
        realDestination, realSource = realSource, realDestination
        if rank[realDestination] == rank[realSource]: rank[realDestination] += 1
    parent[realSource]=realDestination
    lines[realDestination] += lines[realSource]
    lines[realSource] = 0
    ans = max(ans, lines[realDestination])

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    
    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)
    
