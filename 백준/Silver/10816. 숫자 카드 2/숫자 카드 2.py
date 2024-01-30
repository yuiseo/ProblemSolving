import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))


cards = {}
for a in A:
    if a not in cards:
        cards[a] = 1

    else:
        cards[a] +=1

for b in B:
    if b not in cards:
        print(0, end=" ")
    else:
        print(cards[b], end=" ")