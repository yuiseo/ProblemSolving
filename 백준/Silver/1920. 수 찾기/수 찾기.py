import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split(' ')))
A.sort()
M = int(input())
B = list(map(int,input().split(' ')))

for i in range(M):
    target = B[i]
    left = 0
    right = N-1

    while left<=right:
        mid = (left+right)//2
        
        if A[mid] == target:
            print(1)
            break

        elif A[mid] > target:
            right = mid-1

        else:
            left = mid+1
    else:
        print(0)

