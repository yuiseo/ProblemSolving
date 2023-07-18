import sys
input = sys.stdin.readline

N = int(input())

number = 1
for i in range(1,N+1):
    number*=i

number=str(number)

answer=0
for n in range(len(number)-1,-1,-1):
    if number[n] != '0':
        print(answer)
        break
    answer+=1