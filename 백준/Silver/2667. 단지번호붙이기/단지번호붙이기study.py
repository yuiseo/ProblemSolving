import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int,input().strip())) for _ in range(n)]

answer = []
cnt=0


def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    arr[y][x] = 0

    bfs_cnt = 0
    while queue:
        ny,nx = queue.popleft()

        directy = [-1,1,0,0]
        directx = [0,0,-1,1]

        for i in range(4):
            dy = directy[i] + ny
            dx = directx[i] + nx

            if 0<=dy<n and 0<=dx<n:
                if arr[dy][dx]==1:
                    arr[dy][dx] = 0
                    queue.append((dy,dx))
        bfs_cnt+=1
    answer.append(bfs_cnt)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bfs(i,j)
            cnt+=1

answer.sort()
print(cnt)
for a in answer:
    print(a)
