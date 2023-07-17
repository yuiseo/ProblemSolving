import sys
input = sys.stdin.readline

N,C = map(int,input().split(' '))
arr = [int(input())for _ in range(N)]
arr.sort()

# Gap 집과 집 사이의 최소, 최대 거리
start,end = 1, arr[N-1]-arr[0]
result = 0

if C==2:
    print(arr[N-1]-arr[0])
else:
    while start<end:
        mid = (start+end)//2  #Gap
        count=1
        # 공유기 위치
        wifi = arr[0]

        for i in range(N):
            if arr[i] - wifi >= mid:
                count+=1
                wifi = arr[i]

        # 설치 가능 - 거리 더 넓게 가능
        if count >= C:
            result = mid
            start = mid+1

        # 설치 불가능 - 거리 좁게 해야함
        elif count <C:
            end = mid
    print(result)
