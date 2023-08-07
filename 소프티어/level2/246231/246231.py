import sys
input = sys.stdin.readline

N, K = map(int,input().split())
arr = list(map(int,input().split()))

for _ in range(K):
    a,b = map(int,input().split())
    n = b-a+1

    answer = sum(arr[a-1:b])/n
    print('%0.2f'%answer)