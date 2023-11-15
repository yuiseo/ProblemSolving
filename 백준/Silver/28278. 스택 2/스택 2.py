import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    command = input().rstrip()
    if len(command)>1:
        stack.append(int(command[2:]))

    if command == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    if command == '3':
        print(len(stack))

    if command == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    if command == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


