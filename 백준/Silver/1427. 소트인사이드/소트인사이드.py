import sys
input = sys.stdin.readline

N = input()

arr = [a for a in N]
arr = arr[:-1]
arr.sort(reverse=True)

print(('').join(arr))