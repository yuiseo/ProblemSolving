import sys
input = sys.stdin.readline

N=int(input())
arr=list(map(int,input().split(' ')))
answer = [0 for _ in range(N)]

stack = []

for i in range(N):
    while stack:
        # 현재 높이 > 스택
        if arr[i] > stack[-1][0]:
            stack.pop()
        else:
            answer[i] = stack[-1][1]+1
            break

    stack.append((arr[i],i))

# stack = []
# idx = 0
# stack.append(arr[0])
# for i in range(1,N):
#     if stack[-1] < arr[i]:
#         print('i',i+1)
#         answer[i]=0
#         stack.pop()
#         idx = i+1
#         stack.append(arr[i])
#     else:
#         answer[i] = idx
print(*answer)

