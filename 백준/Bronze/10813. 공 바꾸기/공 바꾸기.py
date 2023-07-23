import sys
input = sys.stdin.readline

N,M = map(int,input().split(' '))

basket = [0]
for i in range(1,N+1):
    basket.append(i)

for _ in range(M):
    i,j = map(int,input().split(' '))
    temp_i,temp_j = basket[i], basket[j]
    basket[j]=temp_i
    basket[i]=temp_j


print(*basket[1::])


