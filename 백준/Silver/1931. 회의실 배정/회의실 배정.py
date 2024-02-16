n = int(input())

meeting=[list(map(int,input().split())) for _ in range(n)]
meeting.sort(key=lambda x:x[0])
meeting.sort(key=lambda x:x[1])

cnt=0
time=0
for j in range(n):
    if time<=meeting[j][0]:
        time = meeting[j][1]
        cnt+=1
print(cnt)