import sys
from collections import deque
input = sys.stdin.readline
F,S,G,U,D = map(int,input().split())
# 건물높이, 강호, 타겟, 위, 아래


queue = deque()
queue.append((S,0)) # 강호의 위치, count
visit = [0]*(F+1) # 메모리 관리를 위한 visit 배열

flag = 0 # 목표층에 가는지 여부를 위한 flag
while queue:
    now,ncnt = queue.popleft()
    visit[now] = 1
    direct = [U,D*(-1)]

    if now == G:
        flag = 1 #도착
        print(ncnt)
        break

    for i in range(2):
        move = now+direct[i]

        if 1<=move<(F+1) and visit[move]==0:
            visit[move] = 1
            queue.append((move,ncnt+1))


if flag==0: #도착하지 못했다면
    print('use the stairs')




