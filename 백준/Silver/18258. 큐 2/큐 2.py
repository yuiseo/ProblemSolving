import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque()
for i in range(N):
    temp = list(map(str,input().split()))

    if temp[0] == 'push':
        queue.append(int(temp[1]))

    elif temp[0] == 'front':
        if len(queue) != 0:
            temp = queue.popleft()
            queue.appendleft(temp)
            print(temp)
        else:
            print(-1)

    elif temp[0] == 'back':
        if len(queue) !=0:
            temp = queue.pop()
            queue.append(temp)
            print(temp)
        else:
            print(-1)

    elif temp[0] == 'size':
        print(len(queue))

    elif temp[0] == 'empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)

    else:
        if len(queue)!=0:
            print(queue.popleft())
        else:
            print(-1)