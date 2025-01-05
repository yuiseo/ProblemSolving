import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[]for _ in range(n+1)]
visit = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

arrive = False
def dfs(now,level):
    visit[now] = True
    global arrive
    if level == 5:
        arrive = True
        return

    for a in arr[now]:
        if not visit[a]:
            dfs(a, level+1)
    visit[now] = False



for i in range(n):
    dfs(i,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)