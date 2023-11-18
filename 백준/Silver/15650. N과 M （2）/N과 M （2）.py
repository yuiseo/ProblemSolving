import sys
input = sys.stdin.readline

N,M = map(int,input().split())

arr = []
def dfs(start):
    if len(arr) == M:
        print(' '.join(map(str,arr)))

    for i in range(start,N+1):
        if i not in arr:
            arr.append(i)
            # 중복 제거를 위함
            dfs(i+1)
            arr.pop()

# 1부터 시작
dfs(1)