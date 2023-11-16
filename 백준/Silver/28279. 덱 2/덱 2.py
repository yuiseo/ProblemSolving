import sys
input = sys.stdin.readline

from collections import deque

queue = deque()


N=int(input())

for _ in range(N):
    command = input().rstrip()
    if len(command)>1:
        if command[0] == '1':
            queue.appendleft(command[2:])
        elif command[0] == '2':
            queue.append(command[2:])

    if command == '3':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    if command == '4':
        if len(queue) == 0:
            print(-1)

        else:
            print(queue.pop())

    if command=='5':
        print(len(queue))

    if command=='6':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    if command == '7':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])

    if command == '8':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])