import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(v):
    visit[v] = 1

    for a in arr[v]:
        if not visit[a]:
            dfs(a)


count = 0
for i in range(1, n+1):
    if visit[i] == 0:
        count+=1
        dfs(i)

print(count)