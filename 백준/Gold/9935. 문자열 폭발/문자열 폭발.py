import sys
input = sys.stdin.readline

target = input().rstrip()
bomb = input().rstrip()

stack = []
bomb_len = len(bomb)

for i in range(len(target)):
    stack.append(target[i])

    ## stack 끝에서 bomb 길이만큼 잘라 비교 후 같으면 stack에서 제거
    if ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')