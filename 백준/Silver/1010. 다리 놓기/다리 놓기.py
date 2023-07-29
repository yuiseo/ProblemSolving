import sys

input = sys.stdin.readline

def factorial(x):
    if x>1:
        return x * factorial(x-1)
    else:
        return 1

T=int(input())
for _ in range(T):
    N,M = map(int,input().split())
    print(factorial(M)//(factorial(M-N)*factorial(N)))
