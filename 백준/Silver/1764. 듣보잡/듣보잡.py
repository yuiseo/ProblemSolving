import sys
input = sys.stdin.readline

n,m = map(int,input().split())
never = dict()
# 듣도 못한
for _ in range(n):
    name = input().strip()
    never[name]=1

# 보도 못한
for _ in range(m):
    name = input().strip()
    if name not in never:
        never[name]=1
    else:
        never[name]=2
        
# 알파벳 순 정렬
sort_never=sorted(never.items())

# 출력
cnt = 0
answers = []
for key,value in sort_never:
    if value == 2:
        cnt+=1
        answers.append(key)
print(cnt)
for answer in answers:
    print(answer)