import sys
from collections import deque
input = sys.stdin.readline

N,M,V = map(int, input().split())

graph = [[0]*(N+1)for _ in range(N+1)]

for i in range(M):
    x,y = map(int,input().split())
    graph[y][x] = 1
    graph[x][y] = 1

visitedDFS = [0] * (N+1)
visitedBFS = [0] * (N+1)


def DFS(v):
    visitedDFS[v] = 1
    print(v, end=" ")

    for i in range(1,N+1):
        # 방문 기록 없고, 연결 되어 있을 때
        if not visitedDFS[i] and graph[v][i] ==1:
            DFS(i)

def BFS(v):
    queue = deque([v])
    visitedBFS[v] = 1

    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for i in range(1,N+1):
            # 방문 기록 없고, 연결 되어 있을 때
            if not visitedBFS[i] and graph[v][i] == 1:
                queue.append(i)
                visitedBFS[i] = 1

DFS(V)
print()
BFS(V)