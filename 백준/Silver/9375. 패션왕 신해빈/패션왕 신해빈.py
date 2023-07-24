import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n=int(input())
    clothes={}

    for _ in range(n):
        name,category=map(str,input().split(' '))
        # 카테고리가 이미 옷장에 있다면
        if category in clothes:
            clothes[category]+=1
        else:
            clothes[category] = 1

    result = 1
    for count in clothes.values():
        result *= count+1 #입지 않은것도 포함하기 위해 1을 더함

    print(result-1) # 모두 다 입지 않은 경우를 제하기 위해 1을 뺌


