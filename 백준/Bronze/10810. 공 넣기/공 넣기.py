import sys
input = sys.stdin.readline

N,M = map(int,input().split(' '))

basket = [0]*N

for _ in range(M):
    i,j,k = map(int,input().split(' '))

    for r in range(i,j+1):
        basket[r-1]=k

print(*basket)