import sys
input = sys.stdin.readline

N,M = map(int,input().split(' '))
S = [input()for _ in range(N)]
arr = [input()for _ in range(M)]

answer = 0
for a in arr:
    if a in S:
        answer+=1

print(answer)

