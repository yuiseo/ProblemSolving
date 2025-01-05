import sys
from collections import deque

input = sys.stdin.readline

v = int(input())
arr = [[] for _ in range(v+1)]

for _ in range(v):
    info = list(map(int,input().split()))
    info.pop()
    idx = info.pop(0)

    for i in range(0,len(info),2):
        arr[idx].append((info[i],info[i+1]))


distance = [0] * (v+1)
visit = [0] * (v+1)

def BFS(start):
    queue = deque()
    queue.append(start)
    visit[start] = 1

    while queue:
        now = queue.popleft()

        for target, dist in arr[now]:
            if not visit[target]:
                visit[target] = 1
                distance[target] = distance[now]+dist
                queue.append(target)

BFS(1)

max_node = 1
for i in range(2,v+1):
    if distance[max_node] < distance[i]:
        max_node = i

distance = [0] * (v+1)
visit = [0] * (v+1)

BFS(max_node)

print(max(distance))



