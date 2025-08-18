import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]

if n == 1:
    print(wine[0])
elif n == 2:
    print(wine[0] + wine[1])
else:
    memo = [0] * n
    memo[0] = wine[0]
    memo[1] = wine[0] + wine[1]
    memo[2] = max(wine[2] + wine[1], wine[2] + wine[0], memo[1])
    
    for i in range(3, n):
        memo[i] = max(
            wine[i] + wine[i-1] + memo[i-3],
            wine[i] + memo[i-2],
            memo[i-1]
        )
    print(memo[n-1])
