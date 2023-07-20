import sys
input = sys.stdin.readline

X = int(input())
N = int(input())

money=0
for _ in range(N):
    a,b = map(int,input().split(' '))
    money+=a*b

if money == X:
    print('Yes')
else:
    print('No')
