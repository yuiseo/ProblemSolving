import sys
input = sys.stdin.readline

N,M=map(int,input().split())
tree = list(map(int,input().split()))
tree.sort()

l=0 #최소
r=tree[-1] #최대

while l<=r:
    mid=(l+r)//2
    total=0

    for target in tree:
        if target > mid:
            total += target-mid

    if total>=M:
        l=mid+1
    else:
        r=mid-1

print(r)
