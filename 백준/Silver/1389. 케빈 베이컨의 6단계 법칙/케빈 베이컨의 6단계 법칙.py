import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graph=list([]for _ in range(n+1))

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 사람별로 최단 거리를 구해야 함!
# visited 함수 매번 초기화 필요
# 베이컨 배열 필요
bacon = [9999999e2] * (n+1)

def bfs(graph,start):
    queue = deque()
    visited = [start]
    count = [0] * (n+1)
    queue.append(start)

    while queue:
        a = queue.popleft()

        for i in graph[a]:
            if i not in visited:
                count[i] = count[a] +1
                visited.append(i)
                queue.append(i)

    return sum(count)


for i in range(1,n+1):
    bacon[i] = bfs(graph,i)

print(bacon.index(min(bacon)))
