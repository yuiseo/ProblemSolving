import sys
from collections import deque

input = sys.stdin.readline
n,m,v = map(int,input().split())
arr = [[] for _ in range(n+1)]

dfs_visit = [0] * (n+1)
bfs_visit = [0] * (n+1)

dfs_result = []
bfs_result = []

for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(n+1):
    arr[i].sort()

def dfs(now):
    dfs_visit[now] = 1
    dfs_result.append(now)

    for a in arr[now]:
        if not dfs_visit[a]:
            dfs(a)


def bfs(now):
    queue = deque()
    queue.append(now)
    bfs_visit[now] = 1

    while queue:
        start = queue.popleft()
        bfs_result.append(start)

        for a in arr[start]:
            if not bfs_visit[a]:
                bfs_visit[a] = True
                queue.append(a)

dfs(v)
bfs(v)
print(*dfs_result)
print(*bfs_result)
