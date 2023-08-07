import sys
input = sys.stdin.readline

K,P,N = map(int,input().split())

for i in range(N):
    K = (K*P)%1000000007
print(K)