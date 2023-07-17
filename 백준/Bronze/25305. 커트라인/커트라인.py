import sys
input = sys.stdin.readline

N,K = map(int,input().split(' '))
arr = list(map(int,input().split(' ')))

arr.sort(reverse=True)
arr = arr[:K]
print(min(arr))
