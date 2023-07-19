import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

res = 0
IOI = 0 # IOI의 인덱스 (1부터 시작 기준)

for s in S:
    # IOI에서 O는 짝수 (이전 인덱스)
    if s == 'O' and IOI%2==1:
        IOI+=1
    # IOI에서 I는 홀수
    elif s == 'I' and IOI%2==0:
        IOI+=1

    # IOI 체크 다시 시작
    elif s== 'I':
        IOI = 1

    else:
        IOI = 0


    if IOI>=2*N+1 and IOI%2==1:
        res+=1

print(res)
