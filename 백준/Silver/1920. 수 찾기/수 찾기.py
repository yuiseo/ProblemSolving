import sys
input = sys.stdin.readline

n = int(input())
n_arr = list(map(int,input().split()))
m= int(input())
m_arr = list(map(int,input().split()))

n_arr.sort()

def binarySearch(num):
    left = 0
    right = n-1

    while left<=right:
        mid = (left+right)//2

        if n_arr[mid] == num:
            return True

        elif n_arr[mid] > num:
            right = mid-1

        else:
            left = mid+1
    return False


for a in m_arr:
    result = binarySearch(a)

    if result:
        print(1)
    else:
        print(0)
