n,t = map(int,input().split())

coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

cnt=0
for j in range(n):
    if coin[j] <= t:
        cnt+=t//coin[j]
        t=t%coin[j]

print(cnt)