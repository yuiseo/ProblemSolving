N,M=map(int,input().split())
tree = list(map(int,input().split()))
tree.sort()

l=1
r=tree[-1]

while l<=r:
    mid=(l+r)//2
    total=[target-mid if target>mid else 0 for target in tree]
    result = sum(total)

    if result>=M:
        l=mid+1
    else:
        r=mid-1

print(r)