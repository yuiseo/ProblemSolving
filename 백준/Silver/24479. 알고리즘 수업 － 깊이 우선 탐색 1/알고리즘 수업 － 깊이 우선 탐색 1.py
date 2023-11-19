import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N,M,R = map(int,input().split())
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]

# 방문 순서
c = 1

# 깊이 우선 탐색
def dfs(graph, V, visited):
    global c
    # 방문 순서 체크
    visited[V] = c

    for i in graph[V]:
        # 방문 하지 않은 곳 찾기
        if visited[i] == 0:
            c+=1
            dfs(graph, i, visited)

# 양방향 graph 연결
for i in range(M):
    u,v = map(int, input().split())
    if 1<=u<= N and u<=v<=N:
        graph[u].append(v)
        graph[v].append(u)

# 정점을 오름차순으로 방문
for i in range(N+1):
    graph[i].sort()


dfs(graph, R, visited)

# 방문 순서 출력
for i in range(1,N+1):
    print(visited[i])