import sys
input = sys.stdin.readline

def dfs(first, now, cost,visited, depth=1):
    global min_cost
    # visited합 n이랑 같은 시점에 다시 처음으로 돌아갈 수 있는 경우
    if depth == n:
        if graph[now][first]:
            min_cost = min(cost+graph[now][first], min_cost)
        return

    # 최솟값보다 작을 때만 유의미
    if cost >= min_cost:
        return

    # 모든 도시 순회!
    for i in range(n):
        if not visited[i] and graph[now][i]:
            visited[i] = 1
            dfs(first, i, cost+graph[now][i], visited,depth+1)
            visited[i] = 0




# 도시의 수
n = int(input())
# 비용 graph
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int,input().split()))
min_cost = float('inf')

for i in range(n):
    visited=[0] * n
    first = i
    visited[first] = 1
    dfs(first,i, 0,visited)
    visited[first] = 0

print(min_cost)




