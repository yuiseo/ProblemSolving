import sys
input = sys.stdin.readline

N = int(input())
S = int(input())
arr = input()

P=(2*N)+1

search=''
for i in range(1,P+1):
    #짝수
    if i % 2 == 0:
        search+='O'
    #홀수
    else:
        search+='I'

answer=0
for i in range(0,S-P+1):
    # print(arr[i:i+P])
    if arr[i:i+P] == search:
        answer+=1

print(answer)