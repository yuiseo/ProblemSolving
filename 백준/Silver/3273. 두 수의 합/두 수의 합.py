import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
x = int(input())

arr.sort()

start, end = 0,n-1
count = 0

while start < end:
    if arr[start] + arr[end] == x:
        count+=1

    if arr[start] + arr[end] <= x:
        start +=1

    if arr[start] + arr[end] > x:
        end-=1

print(count)





