n=int(input())
arr = []
for i in range(n):
    arr.append(input().split())

stack = []
for i in range(n):
    if arr[i][0] == 'push':
        stack.append(arr[i][1])

    elif arr[i][0] == 'size':
        print(len(stack))

    elif arr[i][0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif arr[i][0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(len(stack)-1))

    elif arr[i][0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])