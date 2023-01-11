import sys
input = sys.stdin.readline

# n은 양수이며 11보다 작음
dp=[0]*11 # 각 갯수를 저장
dp[1]=1 # 1
dp[2]=2 # 1+1,2
dp[3]=4 # 1+1+1, 1+2, 2+1, 3

# dp[4] => dp[1]+3, dp[2]+2, dp[3]+1
for i in range(4,11):
    dp[i]=dp[i-3]+dp[i-2]+dp[i-1]

T = int(input())
for _ in range(T):
    n=int(input())
    print(dp[n])

