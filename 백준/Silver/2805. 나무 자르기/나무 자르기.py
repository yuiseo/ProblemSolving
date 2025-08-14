import sys
input = sys.stdin.readline

n,m = map(int,input().split())
trees = list(map(int,input().split()))

# 정렬
trees.sort()

# left, right
left, right = 0, trees[-1]
answer = 0

while left<=right:
    mid = (left+right)//2
    cut = 0

    # mid 값으로 나무를 자르기
    # 잘랐을 때 합이 m 보다 크면 right를 mid-1로 바꿔치기
    # 잘랐을 때 합이 m 보다 작으면 left를 mid+1로 바꿔치기

    for tree in trees:
        if tree - mid > 0:
            cut += (tree - mid)

    if cut >= m:
        left = mid+1
        answer = mid

    # 잘라진 나무와 목표m 같을 때
    # if cut == m:
    #     print(mid)
    #     break

    if cut < m:
        right = mid-1

print(answer)









