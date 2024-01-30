import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split(' ')))

sorted_arr = sorted(set(arr))

target = {}
for i in range(len(sorted_arr)):
    target[sorted_arr[i]] = i

for a in arr:
    print(target[a], end=' ')