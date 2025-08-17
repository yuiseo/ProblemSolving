import sys
from collections import Counter, defaultdict

input = sys.stdin.readline

n, k = map(int,input().split())
arr = list(map(int,input().split()))

start,end = 0,0
max_len = 0
count = defaultdict(int)

while end < n:
    count[arr[end]] +=1

    while count[arr[end]] > k:
        count[arr[start]]-=1
        start+=1
    
    # 조건이 만족할 때 갱신
    max_len = max(max_len, end-start+1)
    end+=1

print(max_len)

# 시간 복잡도
# start->n, end->n ==> 2n =>O(n)

# 공간 복잡도
# O(n)
