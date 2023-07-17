import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(5)]

arr.sort()
print(int(sum(arr)/5))
print(arr[2])