# python3
import sys
n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank, parent, ans = [1] * n, list(range(0, n)), max(lines)
def getParent(table):
    if table != parent[table]: parent[table] = getParent(parent[table])
    return parent[table]
def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)
    if realDestination == realSource: return False
    global ans
    if rank[realDestination] <= rank[realSource]:
        realDestination, realSource = realSource, realDestination
        if rank[realDestination] == rank[realSource]: rank[realDestination] += 1
    parent[realSource] = realDestination
    lines[realDestination] += lines[realSource]
    lines[realSource] = 0
    ans = max(ans, lines[realDestination])
    return True
for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)