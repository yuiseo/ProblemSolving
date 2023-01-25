import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]

queue = deque()
visit[0][0] = 1
queue.append((0,0))

while queue:
    ny,nx = queue.popleft()
    arr[ny][nx] = 0

    if ny == n and nx == m:
        break

    directy = [-1,1,0,0]
    directx = [0,0,-1,1]

    for i in range(4):
        dy = directy[i] + ny
        dx = directx[i] + nx

        if 0<=dy<n and 0<=dx<m:
            if arr[dy][dx] == 1 and visit[dy][dx] == 0:
                visit[dy][dx]=visit[ny][nx]+1
                queue.append((dy,dx))

print(visit[-1][-1])