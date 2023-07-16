import sys
input = sys.stdin.readline

N = int(input())
cards = set(map(int,input().split(' ')))

M = int(input())
arr = list(map(int,input().split(' ')))

answer = [0 for _ in range(M)]

for i in range(len(arr)):
    if arr[i] in cards:
        answer[i] +=1

print(*answer)