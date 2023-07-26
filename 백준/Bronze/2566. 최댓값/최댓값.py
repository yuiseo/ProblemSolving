import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    temp = list(map(int,input().split(' ')))
    arr.append(temp)

max_V=0
max_x,max_y=0,0
for i in range(9):
    if max_V < max(arr[i]):
        max_V = max(arr[i])
        max_y=i


for j in range(9):
    if arr[max_y][j] == max_V:
        max_x = j

print(max_V)
print(max_y+1,max_x+1)