import sys
input = sys.stdin.readline

A,B = map(int,input().split(' '))
A_arr = list(map(int,input().split(' ')))
B_arr = list(map(int,input().split(' ')))

arr = set(A_arr+B_arr)

print(A+B-(A+B-len(arr))*2)

